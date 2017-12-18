#Exercise 10

from matplotlib import pyplot as py
import numphy as np 

x = np.linspace(0,2)
s = np.sin(x-2)
eneg = -x*np.exp(2)
e = np.exp(eneg)

py.plot(x, s*e)
py.xlim(xmin=0, xmax=2)
py.show()