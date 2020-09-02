#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:53:36 2020

@author: Lauría Juan

Módulo principal.
Procesamiento digital de señales.
19/08 - 1er clase (uso de generador de señales)
26/08 - 2da clase (uso de transformada discreta)

"""

import matplotlib.pyplot as plt
import numpy as npy
import scipy as spy

import senoidalTest as fxSen
import funcDFT as fxDFT

vmax = 1
dc = 0
fs = 1000
N = 1000
ph = npy.pi * 0

f = 1
  
tt,xx = fxSen.mi_func_sen(vmax,dc,f,ph,N,fs)  


xx_dft = fxDFT.mi_func_DFT (xx,N)
xx_fft = spy.fft(xx)


plt.figure(1)
plt.title('Señal original')
plt.plot(tt,xx)
plt.grid()

plt.figure(2)
plt.plot(tt,npy.abs(xx_dft))
plt.title('Función DFT')
plt.grid()

plt.figure(3)
plt.plot(tt,npy.abs(xx_fft))
plt.title('Función FFT')
plt.grid()

plt.show()
