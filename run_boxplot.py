import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

seed = 1234
rng = np.random.default_rng(seed)
sensor_a = rng.normal(loc=25, scale=3, size=200)
sensor_b = rng.normal(loc=27, scale=4.5, size=200)

plt.figure(figsize=(6,6))
plt.boxplot([sensor_a, sensor_b], labels=['Sensor A','Sensor B'], patch_artist=True)
plt.ylabel('Temperature (°C)')
plt.title('Box plot of sensor temperatures')
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig(r'C:\Users\bpber\OneDrive\Desktop\ECE105-lab3-plots\sensor_boxplot.png')
plt.close()

print('Saved: sensor_boxplot.png')
