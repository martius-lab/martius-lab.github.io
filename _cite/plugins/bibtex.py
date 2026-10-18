import re
from pathlib import Path
import bibtexparser
from bibtexparser.bparser import BibTexParser
from pylatexenc.latex2text import LatexNodes2Text
from util import *


# image extensions to look for in images/papers/<key>.<ext>
image_extensions = ["webp", "png", "jpg", "jpeg", "gif", "svg"]

# map bibtex entry type to citation type (icon), see _data/types.yaml
entry_types = {
    "article": "journal",
    "inproceedings": "paper",
    "conference": "paper",
    "incollection": "book",
    "inbook": "book",
    "book": "book",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
    "techreport": "preprint",
    "unpublished": "unpublished",
    "misc": "preprint",
}

months = {
    m: i + 1
    for i, m in enumerate(
        ["jan", "feb", "mar", "apr", "may", "jun"]
        + ["jul", "aug", "sep", "oct", "nov", "dec"]
    )
}

latex = LatexNodes2Text(math_mode="verbatim")


def main(entry):
    """
    receives single list entry from bibtex data file, e.g. { file: publications.bib }
    returns list of sources (one per bib entry) with full citation details,
    so manubot is not needed
    """

    path = Path("_data") / get_safe(entry, "file", "")
    if not path.is_file():
        raise Exception(f"Can't find bib file {path}")

    # non-breaking spaces (e.g. from copy-pasted entries) break the parser
    text = path.read_text(encoding="utf8").replace("\u00a0", " ")

    parser = BibTexParser(common_strings=True, ignore_nonstandard_types=False)
    bib = bibtexparser.loads(text, parser=parser)

    # bibtexparser silently skips malformed entries, so check that none got lost
    keys = re.findall(r"^\s*@(?!string|comment|preamble)\w+\s*[{(]\s*([^,\s]+)", text, re.M | re.I)
    parsed = {bib_entry["ID"] for bib_entry in bib.entries}
    lost = [key for key in keys if key not in parsed]
    if lost:
        raise Exception(f"Could not parse bib entries (check their syntax): {', '.join(lost)}")

    members = load_member_names()
    project_images = load_project_images()

    sources = []
    for bib_entry in bib.entries:
        source = convert(bib_entry, members, project_images)
        # fields from data file entry (e.g. type) apply to all sources
        for key, value in entry.items():
            if key != "file":
                source.setdefault(key, value)
        sources.append(source)

    return sources


def clean(value):
    """
    convert latex to plain unicode text
    """
    text = latex.latex_to_text(value or "")
    return re.sub(r"\s+", " ", text).strip()


def split_list(value):
    """
    split comma separated bib field into list
    """
    return [item.strip() for item in (value or "").split(",") if item.strip()]


def format_author(name):
    """
    convert "Last, First" to "First Last"
    """
    name = clean(name)
    if "," in name:
        last, first = name.split(",", 1)
        name = f"{first.strip()} {last.strip()}"
    return name


def load_front_matter(folder):
    """
    get front matter of all markdown files in folder, by file name
    """
    front_matter = {}
    for file in Path(folder).glob("*.md"):
        text = file.read_text(encoding="utf8")
        match = re.match(r"---\n(.*?)\n---", text, re.S)
        if match:
            front_matter[file.stem] = yaml.load(match.group(1), Loader=SafeLoader) or {}
    return front_matter


def load_member_names():
    """
    get names and aliases of lab members, to highlight them in author lists
    """
    names = set()
    for data in load_front_matter("_members").values():
        names.add(get_safe(data, "name", ""))
        names.update(get_safe(data, "aliases", []) or [])
    return {name.strip() for name in names if name and name.strip()}


def load_project_images():
    """
    get teaser image of each project, as fallback image for its papers
    """
    return {
        slug: get_safe(data, "image", "")
        for slug, data in load_front_matter("_projects").items()
    }


def get_date(bib_entry):
    """
    get date (YYYY-MM-DD) from year and month fields
    """
    year = re.sub(r"\D", "", bib_entry.get("year", ""))[:4]
    if not year:
        return ""
    month = bib_entry.get("month_numeric") or bib_entry.get("month") or "1"
    month = month.strip().lower()
    month = int(month) if month.isdigit() else months.get(month[:3], 1)
    return format_date(f"{year}-{month:02d}-01")


def get_arxiv(bib_entry):
    """
    get arxiv id from eprint or url fields
    """
    for field in ["eprint", "arxiv", "url", "note"]:
        match = re.search(r"(\d{4}\.\d{4,5})", bib_entry.get(field, ""))
        if match and (field in ["eprint", "arxiv"] or "arxiv" in bib_entry[field]):
            return match.group(1)
    return ""


def get_image(key, bib_entry, project_images):
    """
    get image from bib field, or from images/papers/<key>.<ext>,
    or else the teaser image of the paper's first project
    """
    if bib_entry.get("image"):
        return bib_entry["image"].strip()
    name = image_name(key)
    for ext in image_extensions:
        image = Path("images/papers") / f"{name}.{ext}"
        if image.is_file():
            return image.as_posix()
    for project in split_list(bib_entry.get("projects")):
        if project_images.get(project):
            return project_images[project]
    return ""


def image_name(key):
    """
    filesystem-safe version of bib key
    """
    return re.sub(r"[^a-zA-Z0-9_-]", "-", key)


def convert(bib_entry, members, project_images):
    """
    convert bibtexparser entry to citation source
    """
    key = bib_entry["ID"]
    entry_type = bib_entry["ENTRYTYPE"].lower()

    authors = [
        format_author(author)
        for author in re.split(r"\s+and\s+", bib_entry.get("author", ""), flags=re.I)
        if author.strip()
    ]
    authors = [f"**{a}**" if a in members else a for a in authors]

    doi = bib_entry.get("doi", "").strip()
    arxiv = get_arxiv(bib_entry)
    url = bib_entry.get("url", "").strip()
    pdf = bib_entry.get("pdf", "").strip()

    publisher = clean(
        bib_entry.get("journal")
        or bib_entry.get("booktitle")
        or bib_entry.get("school")
        or bib_entry.get("howpublished")
        or bib_entry.get("publisher")
    )
    if not publisher and arxiv:
        publisher = "arXiv preprint"

    link = url or (doi and f"https://doi.org/{doi}") or (arxiv and f"https://arxiv.org/abs/{arxiv}") or pdf

    buttons = []
    if pdf:
        buttons.append({"type": "pdf", "link": pdf})
    if arxiv:
        buttons.append({"type": "arxiv", "link": f"https://arxiv.org/abs/{arxiv}"})
    if doi and not link.startswith("https://doi.org"):
        buttons.append({"type": "doi", "link": f"https://doi.org/{doi}"})
    for field, button_type in [("code", "source"), ("website", "website"), ("video", "video")]:
        if bib_entry.get(field):
            buttons.append({"type": button_type, "link": bib_entry[field].strip()})

    source = {
        "id": key,
        "title": clean(bib_entry.get("title")),
        "authors": authors,
        "publisher": publisher,
        "date": get_date(bib_entry),
        "link": link,
        "type": entry_types.get(entry_type, "paper"),
        "image": get_image(key, bib_entry, project_images),
        "description": bib_entry.get("description", "").strip(),
        "buttons": buttons,
        "tags": split_list(bib_entry.get("tags")),
        "projects": split_list(bib_entry.get("projects")),
        "selected": bib_entry.get("selected", "").strip().lower() in ["true", "yes", "1"],
    }

    # drop empty fields to keep citations.yaml tidy
    return {k: v for k, v in source.items() if v not in ["", [], False, None]}
