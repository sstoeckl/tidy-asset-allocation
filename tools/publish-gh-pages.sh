#!/usr/bin/env bash
# Publish the rendered book (D:/tmp/tidyaa_book) to the gh-pages branch of
# origin, from a persistent clone outside the synced project tree.
#
# `quarto publish gh-pages` renders by default and, with --no-render and
# --no-prompt, refuses to initialize the branch; with the output directory
# outside the project it also inherits the theme-link quirk. This script does
# the plain thing: fix the theme links, mirror the output into a clone of the
# gh-pages branch, commit, push. Run from the project root after a render:
#
#     bash tools/publish-gh-pages.sh
#
# The site is served at https://sstoeckl.github.io/tidy-asset-allocation/ and,
# through the Netlify proxy rule in the old book's publish branch, at
# https://www.tidy-pm.com/dev/.
set -euo pipefail

SITE="D:/tmp/tidyaa_book"
CLONE="D:/tmp/tidyaa_ghpages"
REMOTE="$(git remote get-url origin)"

python tools/fix-theme-links.py "$SITE"

# Slide decks render standalone next to their source (CLAUDE.md, "Slides");
# they ride into the site here, under slides/, where the chapter banner links.
if ls slides/*.html >/dev/null 2>&1; then
  mkdir -p "$SITE/slides" && cp slides/*.html "$SITE/slides/"
fi

if [ ! -d "$CLONE/.git" ]; then
  if git ls-remote --exit-code --heads "$REMOTE" gh-pages >/dev/null 2>&1; then
    git clone -q --branch gh-pages --single-branch "$REMOTE" "$CLONE"
  else
    mkdir -p "$CLONE" && git -C "$CLONE" init -q -b gh-pages
    git -C "$CLONE" remote add origin "$REMOTE"
  fi
fi

# Mirror: everything in the clone except .git is replaced by the site.
find "$CLONE" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -r "$SITE"/. "$CLONE"/
touch "$CLONE/.nojekyll"
rm -rf "$CLONE/.quarto"

cd "$CLONE"
git add -A
if git diff --cached --quiet; then
  echo "gh-pages: nothing changed"
else
  git -c core.safecrlf=false commit -q -m "Publish the book, rendered $(date +%Y-%m-%d\ %H:%M)"
  git push -q origin gh-pages
  echo "gh-pages: pushed $(git rev-parse --short HEAD), $(git ls-files | wc -l) files"
fi
