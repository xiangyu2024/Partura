#!/bin/bash
# End-to-end smoke test of the Partura pipeline on a synthetic cube (no real data
# needed). Proves the wiring -- decompose -> evaluate -> metrics -> diagnostics ->
# report -- not the alpha: a synthetic cube has no signal, so every IC here is noise.
set -eu
PY=${PY:-$HOME/.venvs/alphacube/bin/python}
AC=${ALPHACUBE_ROOT:-$HOME/Desktop/AlphaCube-steering}
WORK=${WORK:-/tmp/partura_smoke}
CFG=${CFG:-configs/F001_dwgated_covamtlow.yaml}
mkdir -p "$WORK"

if [ ! -d "$WORK/cube" ]; then
  PYTHONPATH="$AC/src" "$PY" -m alphacube.cli synth --out "$WORK/cube" \
      --symbols 60 --days 1200 --minutes 30 --seed 7 --plant 1
fi

# the synthetic calendar starts in 2020, so override the production splits
sed -e 's/^factor_id: .*/factor_id: SMOKE/' "$CFG" > "$WORK/smoke.yaml"
cat >> "$WORK/smoke.yaml" <<'YML'

splits:
  train:   ["20200102", "20211231"]
  valid:   ["20220101", "20230630"]
  holdout: ["20230701", "20241231"]
  full:    ["20200102", "20241231"]
YML

"$PY" -m partura.cli decompose --config "$CFG" | head -20
for st in S1_components S2_scale S3_gate S4_memory S5_fields S6_distil; do
  "$PY" -m partura.cli run "$WORK/smoke.yaml" --store "$WORK/cube" --stages "$st" \
        --device cpu --out-root "$WORK/runs"
done
"$PY" -m partura.cli report "$WORK/smoke.yaml" --out-root "$WORK/runs"
echo "smoke OK -> research/alpha_distillation/SMOKE.md"
