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

# Helper plotting functions

def plot_scatter(ax, sensor_a, sensor_b, timestamps=None):
    """Plot sensor scatter data onto an existing Axes in-place.

    This function modifies the provided Axes by plotting two scatter
    series. If ``timestamps`` is provided, it plots each sensor against
    time; otherwise it plots Sensor A versus Sensor B.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw onto. Modified in-place; nothing is
        returned.
    sensor_a : array_like
        1-D array of shape (n,) containing Sensor A temperature values
        in degrees Celsius.
    sensor_b : array_like
        1-D array of shape (n,) containing Sensor B temperature values
        in degrees Celsius.
    timestamps : array_like, optional
        1-D array of shape (n,) containing timestamps (seconds). If
        provided, both sensors are plotted versus time. If ``None``, a
        scatter of ``sensor_a`` vs ``sensor_b`` is drawn.

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


def plot_histogram(ax, sensor_a, sensor_b, bins=20, alpha=0.6):
    """Plot overlapping histograms of two sensor arrays onto an Axes.

    The function draws two semi-transparent histograms on the given
    Axes to compare the distributions of Sensor A and Sensor B.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to draw onto. Modified in-place.
    sensor_a : array_like
        1-D array of shape (n,) containing Sensor A temperature values (°C).
    sensor_b : array_like
        1-D array of shape (n,) containing Sensor B temperature values (°C).
    bins : int or sequence, optional
        Number of histogram bins or bin edges to use (default 20).
    alpha : float, optional
        Transparency level for histogram patches (default 0.6).

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=bins, alpha=alpha, label='Sensor A')
    ax.hist(sensor_b, bins=bins, alpha=alpha, label='Sensor B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of sensor temperatures')
    ax.legend()
    ax.grid(False)


def plot_boxplot(ax, sensor_a, sensor_b):
    """Plot side-by-side boxplots of two sensor arrays onto an Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to draw onto. Modified in-place.
    sensor_a : array_like
        1-D array of shape (n,) containing Sensor A temperature values (°C).
    sensor_b : array_like
        1-D array of shape (n,) containing Sensor B temperature values (°C).

    Returns
    -------
    None
    """
    # Create the boxplot using patch_artist to allow colored boxes if desired
    bp = ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'], patch_artist=True)

    # Optional: style the boxes for better publication-quality appearance
    try:
        colors = ['#AAD3DF', '#F6C1C1']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.8)
    except Exception:
        # If matplotlib version doesn't support patch styling in this context, ignore
        pass

    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Box plot of sensor temperatures')
    ax.grid(True, axis='y')
    return None


def main(seed=1234):
    """Generate data and save all plots to disk.

    Parameters
    ----------
    seed : int, optional
        Seed for the random number generator to make results
        reproducible. Defaults to 1234.

    Returns
    -------
    None
        The function saves PNG files to the working directory and
        returns nothing.
    """
    # Generate data
    sensor_a, sensor_b, timestamps = generate_data(seed=seed)

    # Scatter: sensors vs time
    fig, ax = plt.subplots(figsize=(8, 4))
    plot_scatter(ax, sensor_a, sensor_b, timestamps=timestamps)
    fig.tight_layout()
    fig.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_scatter_time.png')
    plt.close(fig)

    # Scatter: Sensor A vs Sensor B
    fig, ax = plt.subplots(figsize=(6, 6))
    plot_scatter(ax, sensor_a, sensor_b, timestamps=None)
    fig.tight_layout()
    fig.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_scatter_compare.png')
    plt.close(fig)

    # Histogram
    fig, ax = plt.subplots(figsize=(8, 4))
    plot_histogram(ax, sensor_a, sensor_b)
    fig.tight_layout()
    fig.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_histogram.png')
    plt.close(fig)

    # Box plot
    fig, ax = plt.subplots(figsize=(6, 6))
    plot_boxplot(ax, sensor_a, sensor_b)
    fig.tight_layout()
    fig.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_boxplot.png')
    plt.close(fig)

    print('Saved: sensor_scatter_time.png, sensor_scatter_compare.png, sensor_histogram.png, sensor_boxplot.png')


if __name__ == '__main__':
    main()
