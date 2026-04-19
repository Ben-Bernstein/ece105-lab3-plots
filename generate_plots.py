"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

 def generate_data(seed=1234, n=200): """Generate synthetic sensor temperature readings and timestamps.

   Parameters
   ----------
   seed : int
       Seed for the NumPy random number generator used to produce
       reproducible synthetic data.
   n : int
       Number of samples to generate for each sensor and for the
       timestamps array.

   Returns
   -------
   sensor_a : numpy.ndarray
       Array of shape (n,) containing Sensor A temperature readings (°C).
   sensor_b : numpy.ndarray
       Array of shape (n,) containing Sensor B temperature readings (°C).
   timestamps : numpy.ndarray
       Array of shape (n,) containing timestamps (seconds) uniformly
       sampled from 0 to 10.
   """
   rng = np.random.default_rng(seed)
   sensor_a = rng.normal(loc=25, scale=3, size=n)
   sensor_b = rng.normal(loc=27, scale=4.5, size=n)
   timestamps = rng.uniform(low=0, high=10, size=n)
   return sensor_a, sensor_b, timestamps


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Generate synthetic sensor data
seed = 1234
rng = np.random.default_rng(seed)
sensor_a = rng.normal(loc=25, scale=3, size=200)
sensor_b = rng.normal(loc=27, scale=4.5, size=200)
timestamps = rng.uniform(low=0, high=10, size=200)

# Scatter: sensors vs time
plt.figure(figsize=(8, 4))
plt.scatter(timestamps, sensor_a, s=20, alpha=0.7, label='Sensor A')
plt.scatter(timestamps, sensor_b, s=20, alpha=0.7, label='Sensor B')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Sensor readings vs time (scatter)')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_scatter_time.png')
plt.close()

# Scatter: Sensor A vs Sensor B
plt.figure(figsize=(6, 6))
plt.scatter(sensor_a, sensor_b, s=20, alpha=0.7)
plt.xlabel('Sensor A (°C)')
plt.ylabel('Sensor B (°C)')
plt.title('Sensor A vs Sensor B (scatter)')
plt.grid(True)
plt.tight_layout()
plt.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_scatter_compare.png')
plt.close()

# Histogram
plt.figure(figsize=(8, 4))
plt.hist(sensor_a, bins=20, alpha=0.6, label='Sensor A')
plt.hist(sensor_b, bins=20, alpha=0.6, label='Sensor B')
plt.xlabel('Temperature (°C)')
plt.ylabel('Count')
plt.title('Histogram of sensor temperatures')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_histogram.png')
plt.close()

# Box plot
plt.figure(figsize=(6, 6))
plt.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'], patch_artist=True)
plt.ylabel('Temperature (°C)')
plt.title('Box plot of sensor temperatures')
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_boxplot.png')
plt.close()

print('Saved: sensor_scatter_time.png, sensor_scatter_compare.png, sensor_histogram.png, sensor_boxplot.png')

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(ax, sensor_a, sensor_b, timestamps=None):
      """Plot a scatter plot of sensor data.

      Parameters:
          ax: The axes on which to plot.
          sensor_a: Data for sensor A.
          sensor_b: Data for sensor B.
          timestamps: Optional timestamps for data points.

      Returns:
          None
      """
      ax.scatter(sensor_a, sensor_b)
  ```

● def plot_scatter(ax, sensor_a, sensor_b, timestamps=None): """Plot sensor scatter data onto an existing Axes
  in-place.

   Parameters
   ----------
   ax : matplotlib.axes.Axes
       The Axes object to draw onto. Modified in-place.
   sensor_a : array_like
       1-D array of shape (n,) containing Sensor A temperature values (°C).
   sensor_b : array_like
       1-D array of shape (n,) containing Sensor B temperature values (°C).
   timestamps : array_like, optional
       1-D array of shape (n,) containing timestamps (seconds). If
       provided, both sensors are plotted versus time; if None, a
       scatter of sensor_a vs sensor_b is drawn.

   Returns
   -------
   None
   """
   if timestamps is not None:
       ax.scatter(timestamps, sensor_a, s=20, alpha=0.7, label='Sensor A')
       ax.scatter(timestamps, sensor_b, s=20, alpha=0.7, label='Sensor B')
       ax.set_xlabel('Time (s)')
       ax.set_ylabel('Temperature (°C)')
       ax.set_title('Sensor readings vs time (scatter)')
       ax.legend()
   else:
       ax.scatter(sensor_a, sensor_b, s=20, alpha=0.7)
       ax.set_xlabel('Sensor A (°C)')
       ax.set_ylabel('Sensor B (°C)')
       ax.set_title('Sensor A vs Sensor B (scatter)')
       ax.grid(True)