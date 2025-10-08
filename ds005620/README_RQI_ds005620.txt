RQI-Lite v1.1 Reproduction Bundle
---------------------------------
Script: rqi_lite_fixed_v2.py (see RQI_Lite_v1.1_script.txt)
Dataset: OpenNeuro ds005620 — “A repeated awakening study exploring the capacity of complexity measures to capture dreaming during propofol sedation” (Bajwa et al., 2023)
DOI: 10.18112/openneuro.ds005620.v1.0.0
URL: https://openneuro.org/datasets/ds005620
Subjects: sub-1010, sub-1016, sub-1017, sub-1022, sub-1024
Conditions: Awake vs. Sedated (propofol)
Files:
 - /Awake: .vhdr, .eeg, .vmrk
 - /Sedated: .vhdr, .eeg, .vmrk
 - rqi_out_*/: PNG histogram and CSV score per subject
Parameters:
  sfreq=250, bandpass=1–40 Hz, notch=60 Hz,
  epoch-sec=2, step-sec=1, max-ch=16, max-triads=50–100
Goal:
  Establish RQI-Lite’s sensitivity to consciousness-state changes (Awake↔Sedation)
Next Planned Dataset:
  ds004902 — Sleep Deprivation EEG (Awake vs. Sleep-deprived)
Contact:
  Ben (Principal Investigator, Human Witness)
Notes:
  This bundle includes all code, subject outputs, and raw EEG data for reproducibility.
  Raw EEG may be omitted in public archives if dataset already accessible via OpenNeuro.
