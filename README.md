 ECE105 Lab 3 — Sensor Plots

  Overview

  This repository generates synthetic temperature sensor data and produces publication-quality visualizations
  (scatter, histogram, and box plot) saved as PNG files.

  Requirements

   - Conda environment named ece105 (recommended)
   - Python
    3.x
   - NumPy
   - Matplotlib

  Installation

  Activate the environment and install dependencies:

   conda activate ece105
   # Using conda
   conda install -n ece105 numpy matplotlib
   # Or, using mamba (faster)
   mamba install -n ece105 numpy matplotlib

  If you prefer pip or don't use conda:

   pip install numpy matplotlib

  Usage

  Run the standalone script to generate the plots:

   python generate_plots.py

  The script is deterministic by default (seed = 1234). To control randomness, edit the seed argument in main()
  or call generate_data(seed) from another script.

  Output files

  The script saves the following PNG files to the repository root:

   - sensor_scatter_time.png — Sensor A and Sensor B vs time (scatter)
   - sensor_scatter_compare.png — Sensor A vs Sensor B (scatter)
   - sensor_histogram.png — Overlapping histograms comparing distributions
   - sensor_boxplot.png — Side-by-side box plots comparing distributions

  Files of interest

   - generate_plots.py — Standalone script: data generation (generate_data), plotting helpers (plot_scatter,
  plot_histogram, plot_boxplot), and main() to produce PNGs.
   - lab3_sensor_plots.ipynb — Original notebook with exploratory code and inline plotting cells.

  AI tools used and disclosure

  [Placeholder] Describe any AI tools used to assist in writing code, editing files, or generating
  documentation. Include details you wish to disclose.

  License

  (If applicable) Add license information here.

  Contact

  For questions, contact the author or maintainer.