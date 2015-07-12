# Kalman filter example demo in Python

# A Python implementation of the example given in pages 11-15 of "An
# Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
# University of North Carolina at Chapel Hill, Department of Computer
# Science, TR 95-041,
# http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html

# by Andrew D. Straw

import numpy
import pylab
import pylab as pl
from pykalman import KalmanFilter

# intial parameters
n_iter = 50
sz = (n_iter,) # size of array
x = -0.37727 # truth value (typo in example at top of p. 13 calls this z)
observations = numpy.random.normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)

Q = 1e-5 # process variance

kf = KalmanFilter()
kf = kf.em(X=observations, n_iter=n_iter)

# estimate state with filtering and smoothing
filtered_state_estimates = kf.filter(observations)[0]
smoothed_state_estimates = kf.smooth(observations)[0]

# draw estimates
pylab.figure()

# lines_true = pl.plot(states, color='b')
pylab.plot(observations,color='m',label='noisy measurements')
pylab.axhline(x,color='g',label='truth value')
pylab.plot(filtered_state_estimates, color='r', label='filt')
pylab.plot(smoothed_state_estimates, color='b', label='smoth')
pylab.legend()
pylab.show()

# # allocate space for arrays
# xhat=numpy.zeros(sz)      # a posteri estimate of x
# P=numpy.zeros(sz)         # a posteri error estimate
# xhatminus=numpy.zeros(sz) # a priori estimate of x
# Pminus=numpy.zeros(sz)    # a priori error estimate
# K=numpy.zeros(sz)         # gain or blending factor
#
# R = 0.1**2 # estimate of measurement variance, change to see effect
#
# # intial guesses
# xhat[0] = 0.0
# P[0] = 1.0
#
# for k in range(1,n_iter):
#     # time update
#     xhatminus[k] = xhat[k-1]
#     Pminus[k] = P[k-1]+Q
#
#     # measurement update
#     K[k] = Pminus[k]/( Pminus[k]+R )
#     xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
#     P[k] = (1-K[k])*Pminus[k]
#
# pylab.figure()
# pylab.plot(z,'k+',label='noisy measurements')
# pylab.plot(xhat,'b-',label='a posteri estimate')
# pylab.axhline(x,color='g',label='truth value')
# pylab.legend()
# pylab.xlabel('Iteration')
# pylab.ylabel('Voltage')
#
# pylab.figure()
# valid_iter = range(1,n_iter) # Pminus not valid at step 0
# pylab.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
# pylab.xlabel('Iteration')
# pylab.ylabel('$(Voltage)^2$')
# pylab.setp(pylab.gca(),'ylim',[0,.01])
# pylab.show()
