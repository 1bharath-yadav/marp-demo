---
marp: true
title: Product Documentation
author: Your Name
theme: custom
paginate: true
math: true
---

<style>
@theme custom {
	/* Base colors and font */
	--bg-1: #0f172a; /* slate-900 */
	--bg-2: #0b1220; /* darker */
	--fg: #e6eef8;   /* light text */

	section {
		background: linear-gradient(135deg, var(--bg-1), var(--bg-2));
		color: var(--fg);
		font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
	}

	h1 { color: #ffffff; font-size: 3.2rem; }
	h2 { color: #cbd5e1; }
	p { color: #dbeafe; }

	/* Style the built-in pagination */
	.marp-pagination {
		color: rgba(230,238,248,0.85);
		font-weight: 600;
		background: transparent;
	}
}

/* Improve contrast when a slide has a background image */
section[data-background-image]::before {
	content: "";
	position: absolute;
	inset: 0;
	background: rgba(2,6,23,0.45);
	pointer-events: none;
}
</style>

# Product Documentation

Your product one-liner goes here.

Contact: 24f1001694@ds.study.iitm.ac.in

---

## Overview

- Purpose
- Key features
- Maintained in Git for easy conversion (Marp -> HTML/PDF)

---

<!--
backgroundImage: url('https://picsum.photos/1600/900')
backgroundSize: cover
-->
## Visual Tour

This slide uses a background image (fetched from a placeholder service) to demonstrate background styling and contrast overlays.

---

## Architecture (Quick)
<!-- Background image -->

![bg](arch.jpg)
High-level components:

1. Frontend — SPA
2. Backend — API + Worker queue
3. Data store — SQL + object store

---

## Algorithmic Complexity

Consider a divide-and-conquer algorithm with recurrence:

$$T(n) = 2T\left(\frac{n}{2}\right) + n$$

By the Master Theorem this gives:

$$T(n) = \Theta(n \log n)$$

Use this slide to document performance guarantees and reasoning.

---

## Styling & Export Notes

- Theme defined inside this Markdown via Marp's `@theme` rule.
- Math is enabled with `math: true` in front-matter (KaTeX rendering).
- Page numbers are enabled with `paginate: true`.
- Background-image slide demonstrates slide-level directives.

---

## Contact & Next Steps

Email: 24f1001694@ds.study.iitm.ac.in

Thank you.


