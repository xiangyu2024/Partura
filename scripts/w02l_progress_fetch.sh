#!/bin/bash
# PROD W02L, laptop side: write the run's progress snapshot (scripts/w02l_progress.py on the server) to <out>.json, for the
# progress dashboard (claude.ai artifact "W02L 进度看板"; its four datasets read this one JSON file through loaders).
#   bash scripts/w02l_progress_fetch.sh <out.json>
# Then: upload <out.json> as an asset of the dashboard, point datasets stages / tail / history / summary at the new /_blob/<id>
# (update source.url, updated, edit), and delete the previous asset.
OUT=${1:?out.json}
ssh -o ConnectTimeout=20 root@100.111.77.69 'cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura && python3 scripts/w02l_progress.py' > "$OUT.part" \
  && python3 -c "import json,sys; d=json.load(open(sys.argv[1])); assert all(k in d for k in ('stages','tail','history','summary'))" "$OUT.part" \
  && mv "$OUT.part" "$OUT" && echo "wrote $OUT ($(wc -c < "$OUT") bytes)"
