"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_data(seed=1234, n=200):
    """Generate synthetic sensor temperature readings and timestamps.

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


# Generate synthetic sensor data
seed = 1234
sensor_a, sensor_b, timestamps = generate_data(seed=seed)

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
