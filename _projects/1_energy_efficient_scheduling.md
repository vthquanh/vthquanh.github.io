---
layout: page
title: Energy-efficient scheduling
description: Lexicographic tardiness–energy scheduling in semiconductor assembly and test hybrid flow shops (M.Eng. thesis)
img: assets/img/projects/hfs_layout.jpg
importance: 1
category: scheduling
---

Semiconductor assembly and test facilities run long, energy-intensive operations such as burn-in and electrical testing. Schedulers have to meet customer due dates while consuming as little energy as possible. Delivery performance usually matters more, so I treat the problem **lexicographically**: first minimize tardiness, then minimize energy without giving any of it back.

{% include figure.liquid loading="eager" path="assets/img/projects/hfs_layout.jpg" title="Four-stage semiconductor assembly and test hybrid flow shop" class="img-fluid rounded z-depth-1" %}
<div class="caption">The four-stage hybrid flow shop: assembly, packaging, burn-in (batch stress test) and functional test, with buffers between stages.</div>

**What I did**

- Formulated a **four-stage MILP** that integrates job sequencing, machine assignment, burn-in batching and tester speed selection.
- Developed an **Extended Teachers' Teaching-Learning-Based Optimization (E-TTLBO)** algorithm with a feasibility-preserving batch-packing decoder.
- Achieved at least 80% lexicographic win rates in 17/18 configurations against a lexicographic GA and 16/18 against simulated annealing, **reducing energy consumption by 8.8–21.7% without increasing tardiness**.

{% include figure.liquid loading="lazy" path="assets/img/projects/hfs_winrate.jpg" title="E-TTLBO lexicographic win rate" class="img-fluid rounded z-depth-1" %}
<div class="caption">Lexicographic win rate of E-TTLBO against Lex-GA and simulated annealing across all 18 problem configurations (n jobs × due-date tightness τ).</div>

**Collaboration.** Part of this work was carried out during my TEEP research internship (Jun–Jul 2026) with Asst. Prof. Nguyen Thi My Hanh at the Global Logistics and Innovative Optimization Lab, Department of Industrial Engineering and Management, Yuan Ze University, Taiwan. A follow-up study extends the model to **burn-in batching and multi-site testing** and is under review at _The International Journal of Advanced Manufacturing Technology_.

Code and benchmark instances: [github.com/vthquanh/lexicographic-energy-efficient-hfs-scheduling](https://github.com/vthquanh/lexicographic-energy-efficient-hfs-scheduling)

#### Publications

<div class="publications">{% bibliography --query @*[key=quanh2026lexicographic || key=quanh2026hfsburnin] %}</div>
