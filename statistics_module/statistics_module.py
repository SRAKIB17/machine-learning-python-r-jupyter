from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from scipy import optimize



chips_15s = np.array([44.000, 46.400, 43.600, 35.000, 35.000, 32.600, 28.900, 27.700, 25.500, 20.375, 12.500, 37.000, 37.500, 36.500, 36.200, 33.000, 43.000, 46.000, 29.000, 31.700, 31.000, 28.750, 23.500, 32.400, 31.000, 29.500, 22.500,
                     20.600, 35.000, 33.100, 31.500, 28.800, 21.300, 37.800, 37.000, 37.100, 36.200, 31.400, 30.200, 31.300, 26.100, 25.200, 23.660, 22.250, 17.500, 15.500, 14.750, 15.000, 14.000, 18.500, 27.700, 26.000, 21.700, 12.500, 12.500],  dtype=float)
temp_celsius = np.array([26.944, 25.833, 25.556, 23.056, 21.389, 20.000, 18.889, 18.333, 16.389, 13.889, 12.778, 24.583, 23.333, 23.333, 22.500, 18.889, 25.278, 25.833, 20.278, 20.278, 20.000, 18.889, 15.000, 21.111, 20.556, 19.444, 16.250,
                        14.722, 22.222, 21.667, 20.556, 19.167, 15.556, 23.889, 22.917, 22.500, 21.111, 19.722, 18.889, 20.556, 17.222, 17.222, 16.111, 16.667, 13.611, 12.778, 11.111, 11.667, 10.000, 11.111, 18.333, 17.222, 15.000, 10.417, 9.5833],  dtype=float)


X = chips_15s
y = temp_celsius

plt.scatter(X, y, color='red')
plt.title('Cricket relation with Temperature')
plt.xlabel('Chrips')
plt.ylabel('Temperature')
plt.legend(['Chrips', 'Temperature'])

slope, intercept, r, p, std_err = stats.linregress(X, y)


def my_model(slope, intercept):
    return slope*X + intercept


plt.plot(X, my_model(slope=slope, intercept=intercept))

plt.grid()
plt.show()
