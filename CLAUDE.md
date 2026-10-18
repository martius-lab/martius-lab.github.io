# Autonomous Learning Group website

Jekyll site based on [greenelab/lab-website-template](https://github.com/greenelab/lab-website-template), served at https://martius-lab.github.io/ via GitHub Pages (`gh-pages` branch, built by GitHub Actions).
Teaching and open positions stay on the university TYPO3 site; `teaching/` and `open-positions/` only redirect there.

## Where content lives

| What | Where | Notes |
|---|---|---|
| Publications | `_data/publications.bib` | Single source of truth. Never edit `_data/citations.yaml` (generated). |
| Paper images | `images/papers/<bibkey>.webp` | Characters other than `a-zA-Z0-9_-` in the key become `-` (e.g. `paulus2026:DiffMJX` → `paulus2026-DiffMJX.webp`). Picked up automatically. |
| Research areas | `_data/research-areas.yaml` | Ordered list; `key` is referenced by projects. |
| Projects | `_projects/<slug>.md` | Rendered at `/research/<slug>/`, listed on `/research/` by `area`. |
| Project images | `images/projects/<slug>/` | `teaser.webp` is the card image. |
| Team | `_members/<slug>.md` | `role`: principal-investigator, admin, postdoc, researcher, phd, student, alumni. |
| Team photos | `images/team/<slug>.webp` | ~600px max. |
| News | `_posts/YYYY-MM-DD-title.md` | Shown on `/blog/` and the last year's posts on the home page. |
| Group photos | `images/group/` + `_data/group-photos.yaml` | Slider on home and team page, newest first. |
| Logos | `images/logo.png` (white, header), `images/icon.png` (favicon), `images/logo-full.png`, `images/funders/` | Sources in `content/Logo/`. |

`content/` holds raw source material (old project figures, the original bib, a report PDF). It is gitignored and not published.

## Publications (BibTeX)

`_cite/plugins/bibtex.py` turns every entry of `_data/publications.bib` into a citation (no Manubot lookups).
Besides the standard fields, these optional fields are understood:

- `projects = {icem, policy-extraction}` — project slugs; the paper is listed on those project pages and inherits the first project's teaser image if it has no own image.
- `selected = {true}` — shown under "Selected" on the publications page.
- `image = {images/papers/foo.webp}` — explicit image (path or URL), overrides the naming convention.
- `description = {One-line summary, Markdown allowed}`
- `code`, `website`, `video`, `pdf` — URLs, rendered as buttons. arXiv and DOI buttons are derived from `eprint`/`url`/`doi`.
- `tags = {robotics, haptics}`

Group members (name or any of their `aliases` in `_members/*.md`) are shown in bold.
The plugin fails loudly if an entry can't be parsed; fix the bib syntax rather than working around it.

## Workflow

- Make changes on a branch and open a PR. The `on-pull-request` workflow regenerates citations and deploys a preview to `https://martius-lab.github.io/preview/pr-<n>/`.
- Merging to `main` rebuilds citations and the site.
- Keep text faithful to the source; don't invent claims, results, or affiliations.
- Images: convert to `.webp`, max 1600px on the long side (team photos 600px). Don't commit PDFs, svgz, xcf, or tiff.

## Local build

```sh
# citations (Python venv in .venv, see _cite/requirements.txt)
uv venv .venv && uv pip install --python .venv/bin/python -r _cite/requirements.txt
.venv/bin/python _cite/cite.py

# site: local gems use .bundle/local/Gemfile (Jekyll 4.4 for Ruby 3.3); CI uses Gemfile/Gemfile.lock with Ruby 3.1
export PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH"
bundle exec jekyll serve   # http://localhost:4000
```

## Third-party assets

Fonts (Barlow, Roboto Mono), Font Awesome, and the template's JS libraries are served from `assets/vendor/` so pages make no requests to external servers (GDPR).
To update them, edit versions in `_vendor/fetch.py` and run `python3 _vendor/fetch.py`.
Don't add CDN links or embeds that load from other servers without asking.

## Template conventions

- Components live in `_includes/` (`figure.html`, `card.html`, `citation.html`, `portrait.html`, `list.html`, ...); the template docs are at https://greene-lab.gitbook.io/lab-website-template-docs.
- `list.html` takes a `filter` that is evaluated as Ruby against each item's fields, e.g. `filter="role == 'phd'"`.
- Project pages use `_layouts/project.html`, which appends the papers whose bib entry lists the project slug in `projects`.
