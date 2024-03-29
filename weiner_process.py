import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import yfinance as yf


def weiner_process(dt=0.1,x0=0,n=1000):
    W = np.zeros(n+1)
    t = np.linspace(x0,n,n+1)
    W[1:n+1] = np.cumsum(np.random.normal(0,np.sqrt(dt),n))
    print(t)
    print(W)
    return t,W

def plot_process(t,W):
    plt.plot(t,W)
    plt.show()


time,data = weiner_process()
plot_process(time,data)