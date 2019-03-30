import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#x = np.linspace(0, 2000, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show() 
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)

z = np.sqrt(xs ** 2 + ys ** 2)
plt.show(z)
#plt.colorbar()
