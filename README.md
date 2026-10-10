# BME Computing & Data Analysis Foundations

A structured repository documenting self-directed computational training, numerical array modeling, and data pipelines oriented towards biomedical engineering and translational research workflows.

## Current Progress
* **Core Python:** Algorithm design, list/dictionary comprehensions, genomic sequencing parsing (GC-content, classification, nucleotide frequency mapping, among others), sensor telemetry indexing.
* **Numerical Computing (NumPy):** Multi-dimensional array operations, vectorized mathematical calculations, broadcasting rules, array reshaping, joining, and aggregated statistical reductions.
* **Tabular Data Processing (Pandas - Active):** Series and DataFrame construction, label-based indexing, conditional masking/filtering, missing value imputation ('dropna', 'fillna'), and vectorized data transformations ('apply', 'map').
* **Tooling:** Jupyter Notebooks, Git/GitHub, macOS Terminal environment.

---

## Repository Structure

* `core_syntax_and_indexing/`: Applied exercises covering string manipulation on FASTA-style biological sequences and multi-slice sensor telemetry arrays.
* `02_numpy_computational_arrays/`: Vectorized array operations and multi-variable numerical processing notebooks.
* *(Upcoming)* `03_pandas_biochemical_curation/`: Data ingestion and cleaning pipelines tailored to multi-well plate reader outputs and chromatography fractions.

---

## Research Application & Trajectory

This computational foundation supports quantitative modeling in cancer metabolism, enzyme kinetics, and biotransport, including:
1. Automated peak detection, baseline correction, and integration for FPLC UV absorbance chromatograms.

   ## Pipeline
   | Stage | Status |
   |---|---|
   | 1. Load and inspect the trace | done |
   | 2. Baseline estimation and subtraction | done |
   | 3. Peak detection | not started |
   | 4. Peak boundary assignment | not started |
   | 5. Trapezoidal integration  | not started |
   | 6. Validation against known areas | not started |

   ## Data

   * ´run_001.csv´ - 1200 points over 60 minutes: six Gaussian elution peaks on a drifting baseline with detector noise.
   * It includes an injection artifact, a partially resolved peak pair, and a peak close to the noise floor.
   * The data is simulated. The generator was written separately and is not included here, so the analysis cannot see the true peak areas.
   * **Recovered values can be scored against time afterward.**

   ## Approach used so far

   * The baseline is estimated by splitting the run into equal windows, taking a low percentile of each, and interpolating in a linear fashion between those anchor points.
   * **Assumption:** The elution peaks only add absorbance, so the lowest values in a window are the least peak-contaminated. This holds for well-behaved UV traces, but fails whenever the signal can dip below the baseline, which can occur through a refractive index mismatch at gradient transitions, air bubbles present in the column, or changes in the buffer absorbance. Those regions would need separate handling.
   * **Edge Clamping:** ´np.interp´ holds values flat outside the range of the first and last anchor times ($t=1.98$ and $t=58.02$). The baseline does not track drift in the first and last two minutes of the run, and those regions should be flagged as unreliable.
   * **Window Size:** 1200 points over 60 min is 0.05 min/point, so ´window_size = 80´ is a 4-minute window against peaks 1-2 min wide. There were two constraints that set this:
     a. Wider than the widest peak - otherwise a window falls inside a peak and the method subtacts the peak from itself.
     b. Narrower than the scale of baseline curvature - otherwise the interpolation cannot track the drift.
   * The big question! **Why not AsLS?** As known, asymmetric least squares, SNIP, and rolling-ball are the standard approaches and would likely perform better. Windowed percentile was picked because its failure modes are tractable, meaning that the bias below is predictable in closed form than dependent on a tuned smoothing parameter.
   
    
   ## Running it

   * Open 'FPLC_peak_integration.ipynb' and run all cells. Requires NumPy and matplotlib.
  
    ---
2.  Non-linear parameter estimation for allosteric enzyme kinetics (Michaelis-Menten / Hill formulations).
