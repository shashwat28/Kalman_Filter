"""
Created on Fri Mar  8 18:43:17 2019

@author: Shashwat
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
class kalman_filter:
    def __init__(self):
        datafile=pd.read_csv("ParadeToHomeLabelled.csv",header=0)
        index=datafile['index']
        speed=datafile['speed (m/s)']
        init_estimate=np.mean(speed)
        init_estimate_error=0.5
        init_measured_error=0.75
        new_estimate=list()
        self.kalmanfilter(new_estimate,speed,init_estimate,init_estimate_error,init_measured_error)
        plt.plot(index,speed,'g')
        plt.plot(index,new_estimate,'b')
        plt.show()
    def kalmanfilter(self,new_estimate,speed,init_estimate,init_estimate_error,init_measured_error):
        for i in range(len(speed)):
            kalman_gain=init_estimate_error/(init_estimate_error+init_measured_error)
            init_estimate=init_estimate+(kalman_gain*(speed[i]-init_estimate))
            new_estimate.append(init_estimate)
            init_estimate_error=(1-kalman_gain)*init_estimate_error
kf=kalman_filter()

