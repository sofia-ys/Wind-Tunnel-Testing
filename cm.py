import numpy as np
import matplotlib.pyplot as plt
import aero_forces as af
import data as d

Cm_all_runs = []
for alpha in range(len(d.run_nr)):
    # calculate cp for the upper and lower surfaces for the current run
    Cp_upper = []  # upper surface cp values for this run
    for j in range(24):
        Cp_upper.append((float(d.run_data[alpha][j]) - d.p_tot[alpha]) / d.q_infy[alpha])

    Cp_lower = []  # lower surface cp values for this run
    for k in range(24):
        Cp_lower.append((float(d.run_data[alpha][k+24]) - d.p_tot[alpha]) / d.q_infy[alpha])

    # calculate the difference between Cp_lower and Cp_upper
    Cp_difference = []  # difference in cp necessary for cn and cm plots
    for m in range(len(Cp_upper)):
        Cp_difference.append(Cp_lower[m] - Cp_upper[m])

    Cm_integrand = []
    for p in range(len(Cp_upper)):
        Cm_integrand.append(Cp_difference[p] * af.xc_avg[p])

    Cm = np.trapz(Cm_integrand, x=af.xc_avg)
    
    # Store Cm for this run
    Cm_all_runs.append(Cm)


'''centre of pressure is when cm = 0 which is between cm[1] and cm[2]'''
Cm_slope = (af.xc_avg[2] - af.xc_avg[1])/(Cm_all_runs[2] - Cm_all_runs[1])
centre_p = (Cm_slope * (0 - Cm_all_runs[1]) + af.xc_avg[1]) * 100

print(centre_p)

def main():  # so that the plots don't run when we import the function
    plt.plot(d.alpha, Cm_all_runs, color='#89CC04', marker='o', linestyle='-', markersize=5, label=r"$C_{m}$")
    plt.title("Pitching Moment Coefficient vs. Angle of Attack ")
    plt.xlabel(r"$\alpha$ [°]")
    plt.ylabel(r"$C_{m}$ [-]")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()