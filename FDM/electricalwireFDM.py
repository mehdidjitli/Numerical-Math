#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:12:52 2023

@author: mehdidjitli
"""

import numpy as np
import matplotlib.pyplot as plt

#Initialisation des constantes

R1=0.3 # cm
R2=0.4 # cm
T_inf=25
h_inf=10
ka=400
kb=0.1
nr=101
q=200
dr=R2/(nr-1)
nf=int(R1/R2*nr)

#Initialisation des variables
r=np.linspace(0,R2,nr)
A=np.zeros((nr,nr))
b=np.zeros(nr)

#Noeud 0 
A[0,0]=-1
A[0,1]=1
b[0]=0

#Noeud interne cuivre

for i in range(1,nf):
    A[i,i-1]=-1/(r[i]*2*dr)+1/dr**2
    A[i,i]=-2/dr**2
    A[i,i+1]=1/(r[i]*2*dr)+1/dr**2
    b[i]=-q/ka

#Noeud frontière cuivre-plastique

A[nf,nf-1]=-ka
A[nf,nf]=ka+kb
A[nf,nf+1]=-kb
b[nf]=0

#Noeud interne plastique 

for i in range(nf+1,len(r)-1):
    A[i,i-1]=-1/(r[i]*2*dr)+1/dr**2
    A[i,i]=-2/dr**2
    A[i,i+1]=1/(r[i]*2*dr)+1/dr**2
    b[i]=0

#Noeud frontière air-plastique

A[-1,-2]=kb/dr
A[-1,-1]=-kb/dr-h_inf
b[-1]=-h_inf*T_inf

# Résoudre et tracer graphique

T=np.linalg.solve(A,b)
plt.plot(r,T)
plt.xlabel("r (m)")
plt.ylabel("Température (degré C)")
plt.title("Température dans un fil électrique")
theta = np.linspace(0, 2.*np.pi, 100)
r, theta = np.meshgrid(r, theta)
T2D = np.tile(T, (len(theta), 1))
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
c = ax.pcolormesh(theta, r, T2D,cmap='bwr')
fig.colorbar(c, ax=ax)
plt.title('Vue de coupe de la température dans le fil électrique (degré Celcius)')
plt.show()

