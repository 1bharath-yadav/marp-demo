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

## Themes & Built-ins

Marp ships with several built-in themes. Switch by changing the `theme:` front-matter (example shown below).

```yaml
---
marp: true
title: Example
theme: gaia   # or: default, uncover
paginate: true
math: true
---
```

This deck uses a `custom` theme defined via `@theme` above, but you can swap to `gaia` or `default` for different looks.

---

## Image sizing examples

- Regular image:

![](arch.jpg)

- Set width:

![width:320px](arch.jpg)

- Set height:

![height:180px](arch.jpg)

- Both width & height:

![w:320 h:180](arch.jpg)

---

## Background image variants

<!-- Background image -->

![bg](arch.jpg)

![bg fit](arch.jpg)

![bg cover](arch.jpg)

<!-- Multiple backgrounds -->

![bg left](arch.jpg)
![bg right](arch.jpg)

---

<!-- _header: **Docs — Product** -->
<!-- _footer: _Draft — Internal_ -->

## Directives & Slide Metadata

You can control slides with HTML comments (Marp directives). Examples above include background instructions and header/footer.

<!-- _backgroundColor: #123456 -->

This slide shows how to set a custom background color for a slide.

<!-- _color: red -->

This text would become red using a `_color` directive on the slide.

---

## Code highlighting

```python
def hello(name: str) -> None:
		print(f"Hello, {name}!")

hello("Marp")
```

```javascript
console.log('Hello, Marp');
```

---

## Math examples

Inline math: $E = mc^2$

Block math:

$$
\frac{d}{dx}e^x = e^x
$$

And the algorithmic slide above shows:

$$T(n) = 2T\left(\frac{n}{2}\right) + n = \Theta(n \log n)$$

---

## Tables and Lists

| Item | Cost |
| ---- | ---- |
| A    | $1   |
| B    | $2   |

- Bullet point
	- Sub-point
		- Sub-sub-point

1. Numbered list
2. Second item

---

## Exporting & Build Notes

Export to common formats with the Marp CLI:

```bash
# HTML
marp demo.md -o demo.html

# PDF
marp demo.md --pdf

# PowerPoint
marp demo.md --pptx
```

If you're using the VS Code Marp extension, use the Command Palette to export or start watch mode.

---


## Contact & Next Steps

Email: 24f1001694@ds.study.iitm.ac.in

Thank you.


