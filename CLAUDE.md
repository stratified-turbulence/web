# CLAUDE.md — Project Instructions

This is a Jekyll-based GitHub Pages site for the STRATA research group.
Published at: https://stratified-turbulence.github.io/web

## Key Facts
- Theme: academicpages (based on Minimal Mistakes)
- Config: `_config.yml`
- `NOTES.md` and `CLAUDE.md` are excluded from the Jekyll build (won't appear on the site)

## Content Files
- Pages live in `_pages/` with YAML front matter
- Publications in `_publications/`, talks in `_talks/`, etc.
- Navigation is configured in `_data/navigation.yml`

## Do Not
- Add front matter (`---`) to `NOTES.md` or `CLAUDE.md` — Jekyll would try to process them
- Commit generated `_site/` output (it's built by GitHub Actions)
