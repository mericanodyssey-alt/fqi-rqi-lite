RQI-Lite v1.2 Reproduction Bundle — Sleep Deprivation Study
-----------------------------------------------------------
Script: rqi_lite_fixed_v2.py  (see RQI_Lite_v1.1_script.txt for code reference)
Dataset: OpenNeuro ds004902 — “A Resting-State EEG Dataset for Sleep Deprivation”
Citation: Xiang et al., 2023
DOI: 10.18112/openneuro.ds004902.v1.0.0
URL: https://openneuro.org/datasets/ds004902

Subjects: (to fill in after runs, e.g. sub-01 … sub-05)
Conditions:
  • Normal Sleep (baseline)
  • Sleep-Deprived Condition (24 h deprivation)

Files per subject:
  /Normal/    → raw BrainVision .vhdr / .eeg / .vmrk
  /Deprived/  → raw BrainVision .vhdr / .eeg / .vmrk
  /rqi_out_*/ → PNG histogram + CSV score (one folder per subject)

Processing parameters:
  sfreq = 250 Hz  
  bandpass = 1–40 Hz  
  notch = 60 Hz  
  epoch-sec = 2  
  step-sec = 1  
  max-ch = 16  
  max-triads = 100  

Goal:
  Evaluate whether RQI-Lite detects reductions in neural integration (Φ_MS) and synergy (Syn)
  after sleep deprivation.  Expect Syn↓ and RQI↓ in the deprived condition, mirroring reduced
  experiential richness.

Command example:
  python rqi_lite_fixed_v2.py ^
    --data-path "C:\Users\<user>\Desktop\ds004902\sub-####" ^
    --pattern "*.vhdr" ^
    --cond-a "normal" ^
    --cond-b "deprived" ^
    --sfreq 250 --bandpass 1 40 --epoch-sec 2 --step-sec 1 ^
    --max-ch 16 --max-triads 100 --notch 60 ^
    --outdir "rqi_out_<subject>"

Expected output:
  • rqi_out_<subject>/rqi_lite_hist.png
  • rqi_out_<subject>/rqi_lite_scores.csv
  • console readout with Cohen’s d and p-value

Reproducibility notes:
  – Use the same script version as ds005620 runs.  
  – Save all per-subject output folders.  
  – Record dataset accession (ds004902) instead of including raw EEG files if already public.  

Next steps:
  Compare RQI-Lite effects between Propofol Sedation (ds005620) and Sleep Deprivation (ds004902).
  Compute group-level mean |d| across subjects and conditions.
  Archive bundle as RQI_ds004902.zip and link both studies in the RQI v1.2 methods preprint.

Results:
Subject sub-01 — Normal > Deprived
Φ = 0.831, Syn = 0.534, RQI = 0.914, t = 11.18, p = 2.56e-26
Interpretation: clear loss of integration and synergy after sleep deprivation.
Subject: sub-01 (Normal vs. Deprived, ds004902 Sleep Deprivation)
Output files: rqi_out_01/rqi_lite_hist_sub01.png, rqi_out_01/rqi_lite_scores_sub01.csv
Parameters: 1–40 Hz bandpass, 2 s epochs, 1 s step, 16 channels, 100 triads, 60 Hz notch.

EEG data not included due to size.
Download ds004902 dataset from OpenNeuro:
https://openneuro.org/datasets/ds004902
Place the .set/.fdt files in /data/ds004902/ before running scripts.
