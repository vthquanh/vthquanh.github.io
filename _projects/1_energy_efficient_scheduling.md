---
layout: page
title: Energy-efficient scheduling
description: Lexicographic tardiness–energy scheduling in semiconductor assembly and test hybrid flow shops (M.Eng. thesis)
importance: 1
category: scheduling
---

Semiconductor assembly and test facilities run long, energy-intensive operations such as burn-in and electrical testing. Schedulers have to meet customer due dates while consuming as little energy as possible. Delivery performance usually matters more, so I treat the problem **lexicographically**: first minimize tardiness, then minimize energy without giving any of it back.

**What I did**

- Formulated a **four-stage MILP** that integrates job sequencing, machine assignment, burn-in batching and tester speed selection.
- Developed an **Extended Teachers' Teaching-Learning-Based Optimization (E-TTLBO)** algorithm with a feasibility-preserving batch-packing decoder.
- Achieved at least 80% lexicographic win rates in 17/18 configurations against a lexicographic GA and 16/18 against simulated annealing, **reducing energy consumption by 8.8–21.7% without increasing tardiness**.

**Collaboration.** Part of this work was carried out during my TEEP research internship (Jun–Jul 2026) at the Global Logistics and Innovative Optimization Lab, Department of Industrial Engineering and Management, Yuan Ze University, Taiwan. A follow-up study extends the model to **burn-in batching and multi-site testing** and is under review at _The International Journal of Advanced Manufacturing Technology_.

Code and benchmark instances: [github.com/vthquanh/lexicographic-energy-efficient-hfs-scheduling](https://github.com/vthquanh/lexicographic-energy-efficient-hfs-scheduling)

#### Publications

<div class="publications">{% bibliography --query @*[key=quanh2026lexicographic || key=quanh2026hfsburnin] %}</div>
