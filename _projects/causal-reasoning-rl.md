---
title: Causal Reasoning in RL
area: model-free-rl
description: Learning and using causal knowledge, such as whether the agent has causal influence on its environment, to make RL algorithms more robust and sample efficient.
status: current
---

Reinforcement learning is fundamentally a causal endeavor. The agent intervenes in the environment through actions and observes their effects; learning through credit assignment involves the counterfactual question whether another action would have resulted in a better outcome. *Causal Reasoning for RL* is about learning and using causal knowledge *to improve RL algorithms*. We are interested in using tools from causality to make RL algorithms more robust and sample efficient.

In a first project, we showed how learning a causal model of agent-object interactions allows to infer whether the agent has causal influence on its environment. We then demonstrated how this information can be integrated into RL algorithms to steer the exploration process and improve sample-efficiency of off-policy training. Experiments on robotic manipulation benchmarks show a clear improvement over state-of-the-art.
