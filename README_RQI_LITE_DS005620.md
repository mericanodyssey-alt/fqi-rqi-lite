# RQI-Lite (v1.1) — Propofol Pilot (OpenNeuro ds005620)

## Purpose
Minimal, reproducible proof-of-concept showing that RQI-Lite separates **Awake** vs **Propofol Sedation** within subjects using EEG.

## Data Provenance
- Source: OpenNeuro
- Accession: **ds005620** — “A repeated awakening study exploring the capacity of complexity measures to capture dreaming during propofol sedation” (Bajwa et al.)
- DOI: 10.18112/openneuro.ds005620.v1.0.0
- URL: https://openneuro.org/datasets/ds005620
- Subjects analyzed: **sub-1010, sub-1016, sub-1017, sub-1022, sub-1024**
- Files used: BrainVision **.vhdr/.eeg/.vmrk**
  - Awake: `task-awake_acq-EC` or `task-awake_acq-EO`
  - Sedation: `task-sed2_acq-rest_run-1`

## Code / Version
- Script: `rqi_lite_fixed_v2.py` (included in this bundle)
- Hash: see `SCRIPT_SHA256.txt` (SHA-256 of the script file)
- Notes: line `mne.set_config("MNE_USE_IIR_FILTERS", "true")` is placed immediately after `import mne`.

## Environment (conda/pip essentials)
python 3.10–3.13
numpy scipy pandas scikit-learn matplotlib mne networkx tigramite

markdown
Copy code

## Parameters (applied to all 5 subjects)
- Resample: `--sfreq 250`
- Filters: `--bandpass 1 40`, `--notch 60` (IIR filters via MNE config)
- Epoching: `--epoch-sec 2`, `--step-sec 1`
- Channels: `--max-ch 16` (first 16 EEG channels after MNE picking)
- Synergy: `--max-triads 50` (Gaussian O-information over random triads)
- Causal graph: PCMCI (ParCorr, `tau_max=1`)
- RQI-Lite = `z(Φ_proxy) + z(Syn_Gauss)`

## Exact Commands Used (per subject)
(Adjust base path if needed, keep unique `--outdir` to avoid overwriting.)

:: SUBJECT 1010
python rqi_lite_fixed_v2.py --data-path "C:\Users\meric\Desktop\New folder (6)\sub-1010" --pattern "*.vhdr" --cond-a "awake" --cond-b "sed2" --sfreq 250 --bandpass 1 40 --epoch-sec 2 --step-sec 1 --max-ch 16 --max-triads 50 --notch 60 --outdir "rqi_out_1010"

:: SUBJECT 1016
python rqi_lite_fixed_v2.py --data-path "C:\Users\meric\Desktop\New folder (6)\sub-1016" --pattern "*.vhdr" --cond-a "awake" --cond-b "sed2" --sfreq 250 --bandpass 1 40 --epoch-sec 2 --step-sec 1 --max-ch 16 --max-triads 50 --notch 60 --outdir "rqi_out_1016"

:: SUBJECT 1017
python rqi_lite_fixed_v2.py --data-path "C:\Users\meric\Desktop\New folder (6)\sub-1017" --pattern "*.vhdr" --cond-a "awake" --cond-b "sed2" --sfreq 250 --bandpass 1 40 --epoch-sec 2 --step-sec 1 --max-ch 16 --max-triads 50 --notch 60 --outdir "rqi_out_1017"

:: SUBJECT 1022
python rqi_lite_fixed_v2.py --data-path "C:\Users\meric\Desktop\New folder (6)\sub-1022" --pattern "*.vhdr" --cond-a "awake" --cond-b "sed2" --sfreq 250 --bandpass 1 40 --epoch-sec 2 --step-sec 1 --max-ch 16 --max-triads 50 --notch 60 --outdir "rqi_out_1022"

:: SUBJECT 1024
python rqi_lite_fixed_v2.py --data-path "C:\Users\meric\Desktop\New folder (6)\sub-1024" --pattern "*.vhdr" --cond-a "awake" --cond-b "sed2" --sfreq 250 --bandpass 1 40 --epoch-sec 2 --step-sec 1 --max-ch 16 --max-triads 50 --notch 60 --outdir "rqi_out_1024"

markdown
Copy code

## Outputs to Save
From each `--outdir`:
- `rqi_lite_hist.png` (per-subject histogram)
- `rqi_lite_scores.csv` (per-epoch metrics and RQI)

Optional: combine all CSVs into one table for group summaries.

## Results Summary (console d/p you observed)
- 1010: RQI d ≈ +1.09 (p ≈ 4.4e-09)
- 1016: RQI d ≈ +1.00 (p ≈ 4.6e-07)
- 1017: RQI d ≈ −0.65 (p ≈ 4.5e-04)
- 1022: RQI d ≈ +0.83 (p ≈ 8.9e-06)
- 1024: RQI d ≈ −0.96 (p ≈ 7.7e-13)

## Known Limitations / Notes
- Two inversions (1017, 1024) likely reflect Φ-proxy variability and/or subject-specific factors.
- No artifact rejection beyond filtering; future: epoch-level amplitude rejection or ICA.
- Φ-proxy uses PCMCI val-matrix → symmetrize → 0.8 quantile threshold → global efficiency; try graph density or lower threshold for robustness.

## License / Sharing
- Analysis code & this README: CC-BY 4.0 (attribution to Ben + “Collaborative Reflections”).
