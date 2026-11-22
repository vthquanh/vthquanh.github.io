---
layout: page
title: TEEP research internship in Taiwan
description: Energy-efficient semiconductor scheduling at Yuan Ze University (Jun–Jul 2026)
img: assets/img/projects/yzu_campus.jpg
importance: 2
category: scheduling
---

{% include figure.liquid loading="eager" path="assets/img/projects/yzu_campus.jpg" title="Yuan Ze University campus" class="img-fluid rounded z-depth-1" %}
<div class="caption">At Yuan Ze University, Taoyuan, Taiwan (summer 2026).</div>

In June–July 2026 I was a fully funded research intern under the **Taiwan Experience Education Programme (TEEP)**, a Taiwan Ministry of Education initiative. I worked with **Asst. Prof. Nguyen Thi My Hanh** at the **Global Logistics and Innovative Optimization Lab**, Department of Industrial Engineering and Management, Yuan Ze University.

**Project: Hierarchical energy-efficient scheduling in semiconductor assembly and test hybrid flow shops**

The project asked how a semiconductor back-end plant can schedule jobs through several processing stages while controlling energy use. In make-to-order production, late deliveries are costly, so the model treats **delivery performance as the first priority** and reduces energy only among schedules that do not worsen tardiness. Exact optimization was used on small instances to check model behaviour, and a metaheuristic was used for larger instances.

The main finding is that energy can be reduced **without sacrificing delivery performance**. It also explains why a hierarchical (lexicographic) objective suits make-to-order production better than an equal-weight trade-off, which can "save" energy by allowing more delay.

**My contributions**

- Reviewed literature on hybrid flow shop scheduling, semiconductor manufacturing and energy-aware production planning, and organized the research gap.
- Reviewed the model structure and computational results, checking that the method matched the research problem.
- Revised the manuscript for academic clarity, from the introduction and literature review to the method, results and conclusion, and prepared it for journal submission.

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid loading="lazy" path="assets/img/projects/yzu_iem.jpg" title="Department of Industrial Engineering and Management, Yuan Ze University" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Department of Industrial Engineering and Management, Yuan Ze University.</div>

This work fed into my M.Eng. thesis, the paper in [_Computers, Materials &amp; Continua_](https://doi.org/10.32604/cmc.2026.088630), and a follow-up manuscript under review. See [Energy-efficient scheduling]({{ '/projects/1_energy_efficient_scheduling/' | relative_url }}).
