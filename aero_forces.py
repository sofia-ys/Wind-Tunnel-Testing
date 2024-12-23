import numpy as np
import matplotlib.pyplot as plt
import data as d
import cp

xc_upper = np.array(cp.x_over_c[:25])  # separating the lower and upper surfaces
xc_lower = np.array(cp.x_over_c[25:])
xc_norm = np.linspace(0, 1, 100)

Cp_upper = []  # getting the values for the upper surface cp
for j in range(24):
    Cp_upper.append((float(d.run_data[cp.run][j]) - d.p_tot[cp.run]) / d.delta_Pb[cp.run])

Cp_lower = []
for k in range(24):
    Cp_lower.append((float(d.run_data[cp.run][k+24]) - d.p_tot[cp.run]) / d.delta_Pb[cp.run])

Cp_difference = []  # difference in cp necessary for cn and cm plots
for m in range(len(Cp_upper)):
    Cp_difference.append(Cp_lower[m] - Cp_upper[m])

xc_avg = []  # getting an average x/c position, not perfect but good enough for the numerical integration
for n in range(len(Cp_upper)):
    xc_avg.append((xc_upper[n] + xc_lower[n])/2)

Cn = np.trapz(Cp_difference, x=xc_avg)

Cm_integrand = []
for p in range(len(Cp_upper)):
    Cm_integrand.append(Cp_difference[p] * xc_avg[p])

Cm = np.trapz(Cm_integrand, x=xc_avg)
