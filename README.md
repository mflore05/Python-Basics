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

   * The baseline is estimated by splitting the run into equal windows, taking the lowest value in each, and interpolating between those anchor points.
   * This proves the fact that peaks only ever push the signal up, so the low values in any windows are the least contaminated.
   * **Known limitation:** The minimum of a noisy window sits below the true baseline, giving an offset value of ~0.012 AU.
       * Because integration error scales with peak *width* rather than height, this alters small peaks disproportionately.
       * The next step is a low percentile instead of the minimum.
    
   ## Running it

   * Open 'FPLC_peak_integration.ipynb' and run all cells. Requires NumPy and matplotlib.
  
    ---
3.  Non-linear parameter estimation for allosteric enzyme kinetics (Michaelis-Menten / Hill formulations).
4. 1D/2D finite-difference modeling of interstitial fluid pressure (IFP) and convective transport gradients in solid tumors.

