"""Write ONE synthetic cube to disk, with the baseline tree's own writer.

Both sides then open this same directory, so no part of the comparison depends on
the two trees agreeing about how to GENERATE data -- only on how they read and
compute over it. Run under the baseline PYTHONPATH.
"""
import sys
from pathlib import Path

from alphacube.synthetic import write_synthetic_store

out = Path(sys.argv[1])
st = write_synthetic_store(out, n_symbols=16, n_days=90, n_minutes=24, seed=8,
                           suspended_frac=0.05, unlisted_days=6, plant_beta=1.0)
print(f"cube at {st.directory}: {st.n_symbols} symbols x {st.n_days} days x {st.n_minutes} minutes")
print("fields:", ", ".join(st.fields))
print("contract_hash:", getattr(st, "contract_hash", "<n/a>"))
