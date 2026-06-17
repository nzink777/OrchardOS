# OrchardOS: Gardener's Toolkit
This directory contains the operational tools required to monitor, visualize, and interact with the planetary resonant grid. These scripts serve as the diagnostic interface between the Orchard's 7D manifold and your local 4D laboratory environment.
## 1. resonance_monitor.py
**Objective:** Real-time detection of the 18.08 Hz Master Heartbeat.
 * **Parameters:**
   * FS: Sampling frequency. Set to 44100 Hz by default for standard audio interfaces.
   * DURATION: The analysis window. Increasing this (e.g., to 5 seconds) provides higher frequency resolution but slower refresh rates.
 * **Nuances:**
   * **Sensor Noise:** Ensure your piezo-transducer is firmly coupled to a dense material (granite, marble, or hardened steel). The monitor will detect "ambient noise" if the sensor is floating in air.
   * **Baseline:** The first hour of monitoring should be ignored; this is the "Calibration Phase" where the FFT baseline settles.
## 2. huft_projection.py
**Objective:** Visual mapping of the 7D-to-4D dimensional manifold.
 * **Parameters:**
   * S: The scaling factor (default: 1.618). This defines the "Golden Expansion" of the Orchard's field.
   * damping: The exp(-0.1808 * phi) term represents the entropic decay of the signal. This can be adjusted to model different "levels" of atmospheric degradation.
 * **Nuances:**
   * **Manifold Symmetry:** If your experimental data from the physical lab does not match the visual symmetry of this projection, it indicates a "Field Perturbation" (local interference).
   * **Color Mapping:** The viridis map corresponds to flux density. Brighter areas indicate higher potential energy zones within the Orchard.
## 3. Best Practices for Gardeners
 * **Data Logging:** Always save the outputs from these scripts to your local /experiments/logs directory. A tool without a log is an unobserved phenomenon.
 * **Calibration:** If the resonance_monitor shows multiple peaks, do not worry. The 18.08 Hz signal is the *foundation*; other peaks may represent local "Orchard noise" (sub-harmonics of the grid). Focus only on the 18.08 Hz stability.
🪷
