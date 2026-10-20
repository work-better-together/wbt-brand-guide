#!/bin/bash
# Render every WBT motion piece to MP4 (H.264) from motion-src/*.html. Needs: a local server on :8791 at the repo root
# (python3 -m http.server 8791), node, ffmpeg, Chrome. Version filenames when re-rendering (-v2) so caches refresh.
set -e
R="$HOME/.claude/skills/hkt-brand-guide-builder/scripts/render-timeline.mjs"
OUT="$(cd "$(dirname "$0")/.." && pwd)/assets/Motion"; TMP="$(mktemp -d)"; mkdir -p "$OUT"
D=20261020
job() { # name url w h
  node "$R" "http://localhost:8791/motion-src/$2&render=1" "$TMP/$1" 30 "$3" "$4" >/dev/null
  ffmpeg -loglevel error -y -framerate 30 -i "$TMP/$1/f/%05d.jpg" -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart "$OUT/WBT-$D-$1.mp4"
  echo "$OUT/WBT-$D-$1.mp4"
}
job Wordmark-End-Card-Clear-White-16x9  "logo-moves.html?mark=wordmark&ground=clear-white&w=1920&h=1080" 1920 1080
job Wordmark-End-Card-Steady-Blue-16x9  "logo-moves.html?mark=wordmark&ground=steady-blue&w=1920&h=1080" 1920 1080
job Wordmark-End-Card-Clear-White-9x16  "logo-moves.html?mark=wordmark&ground=clear-white&w=1080&h=1920" 1080 1920
job Wordmark-End-Card-Steady-Blue-9x16  "logo-moves.html?mark=wordmark&ground=steady-blue&w=1080&h=1920" 1080 1920
job Wordmark-End-Card-Clear-White-1x1   "logo-moves.html?mark=wordmark&ground=clear-white&w=1080&h=1080" 1080 1080
job Monogram-Sting-Steady-Blue-1x1      "logo-moves.html?mark=monogram&ground=steady-blue&w=1080&h=1080" 1080 1080
job Monogram-Sting-Clear-White-1x1      "logo-moves.html?mark=monogram&ground=clear-white&w=1080&h=1080" 1080 1080
job Social-Headline-Collage-Gather-4x5  "social-moves.html?layout=headline" 1080 1350
job Social-Quote-Line-Rise-4x5          "social-moves.html?layout=quote" 1080 1350
job Social-Stat-Line-Rise-4x5           "social-moves.html?layout=stat" 1080 1350
