#!/usr/bin/env python

'''
compute the propagator of the harmonic oscillator

current problem: dealing with end points to get a sensical integral since

\int_{\omega}d^{n}x f(x) \approx \vol{\omeag}\frac{1}{N}\sum_{n=1}^{N}f(x)

i.e. the \vol{\omega} term is bothersome

'''
import random
import numpy as np

#number of simulations
n=100000

#constants
m=1
a=0.5
N=8
x0=0
xN=x0

#the action
def S(x):
	action=0.0
	N=len(x)
	for i in range(0,N):
		action=action+m/(2*a)*(x[j+1]-x[j])**2+a*V(x[j])
	return action

# the potential
def V(x):
	return x**2/2.0

x=np.zeros(N)

#enforce boundary conditions
x[0]=x0
x[N-1]=xN

int_sum=0.0
for num_trials in range(0,n):
	for j in range(1,N-1):
		x[j]=random.uniform(-5,5)

	int_sum=int_sum+np.exp(-S(x))
#	print 'action=', np.exp(-S(x))
#	print 'totals=',int_sum


print int_sum/n
