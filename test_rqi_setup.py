# Quick sanity check for RQI-Lite setup
import numpy, scipy, pandas, networkx, matplotlib, mne, statsmodels
import importlib.util, sys, os

print("✅ Basic imports successful.")

# Check for your main script
expected_script = "rqi_lite_fixed_v2.py"
if os.path.exists(expected_script):
    print(f"✅ Found {expected_script}")
else:
    print(f"⚠️ {expected_script} not found in current directory.")

# Check tigramite availability
spec = importlib.util.find_spec("tigramite")
if spec is not None:
    print("✅ Tigramite is installed.")
else:
    print("⚠️ Tigramite not found. Install with: pip install tigramite")

print("All setup checks complete.")
