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

## Notes

