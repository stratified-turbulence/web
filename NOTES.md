# Project Notes

## Overview
Jekyll-based GitHub Pages site for the STRATA research group (stratified turbulence).
Published at: https://stratified-turbulence.github.io/web

## Site Structure
- `_pages/` — static pages (About, CV, etc.)
- `_posts/` — blog/news posts
- `_publications/` — publication entries
- `_portfolio/` — portfolio items
- `_talks/` — talk entries
- `_teaching/` — teaching entries
- `_data/` — YAML data files (navigation, etc.)
- `assets/` — CSS, JS, images
- `files/` — downloadable files (PDFs, etc.)

## Local Preview

Run the site locally with:

```bash
bundle exec jekyll serve
```

Then open http://localhost:4000/web in a browser. The `/web` suffix matches the `baseurl` set in `_config.yml`.

To rebuild automatically when files change, add `--livereload`:

```bash
bundle exec jekyll serve --livereload
```

Requires Ruby and Bundler. Run `bundle install` first if dependencies aren't installed yet.

## Reordering Gallery Sections

Sections appear in the order their blocks are written in `_pages/gallery.html`.
To reorder:

1. In `gallery.html`, cut and paste the `<div class="project-section" id="...">...</div>` blocks into the desired order.
2. Update the `<nav class="gallery-sidenav">` links at the top of the file to match — the `<a>` tags must be in the same order as the section blocks or the sidebar will be out of sync.

The nav links and section blocks are the only two things to keep in sync.

## Customizing the Publications Page

Each publication is a file in `_publications/` with YAML front matter. The page at `_pages/publications.html` iterates over these files automatically.

### Adding a new publication
Create a new `.md` file in `_publications/` (e.g. `2025_Smith_JFM.md`) with this structure:

```yaml
---
title: "Paper title"
collection: publications
category: manuscripts        # manuscripts | conferences | books | archive
link: https://doi.org/...
authors: Smith, J., and de Bruyn Kops, S.M.
journal: Journal of Fluid Mechanics
volume: 999, A1              # optional
year: 2025
image: /web/images/publications/2025_Smith_JFM.jpg   # optional
dataset: Forced              # optional — shown as a tag linking to /Datasets/
---
```

Drop the image into `images/publications/` using the same filename convention.

### Changing a dataset tag
Edit the `dataset:` field in the relevant `_publications/` file. Current values in use: `Forced`, `Sheared`, `Taylor-Green`. Leave blank to show no tag.

### Changing card appearance
Edit the `<style>` block at the top of `_pages/publications.html`:
- Card image size: `.pub-image` width and `.pub-image img` height
- Font sizes: `.pub-title`, `.pub-authors`, `.pub-venue`
- Tag style: `.pub-dataset`

### Publication categories
Categories are defined in `_config.yml` under `publication_category`. The order there controls the order of sections on the page.

## Notes

