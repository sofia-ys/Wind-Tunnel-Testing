import numpy as np
import matplotlib.pyplot as plt
import aero_forces as af
import data as d

Cd_all_runs = []
Cl_all_runs = []
for i in range(len(d.run_nr)):
    # calculate cp for the upper and lower surfaces for the current run
    Cp_upper = []  # upper surface cp values for this run
    for j in range(24):
        Cp_upper.append((float(d.run_data[i][j]) - d.p_tot[i]) / d.q_infy[i])

    Cp_lower = []  # lower surface cp values for this run
    for k in range(24):
        Cp_lower.append((float(d.run_data[i][k+24]) - d.p_tot[i]) / d.q_infy[i])

    # calculate the difference between Cp_lower and Cp_upper
    Cp_difference = []  # difference in cp necessary for cn and cm plots
    for m in range(len(Cp_upper)):
        Cp_difference.append(Cp_lower[m] - Cp_upper[m])

    Cn = np.trapz(Cp_difference, x=af.xc_avg)

    Cd = Cn * np.sin(np.radians(d.alpha[i]))
    Cl = Cn * np.cos(np.radians(d.alpha[i]))
    
    # store cl and cd for this run
    Cd_all_runs.append(Cd)
    Cl_all_runs.append(Cl)


def main():  # so that the plots don't run when we import the function
    plt.plot(d.alpha, Cd_all_runs, color='#89CC04', marker='o', linestyle='-', markersize=5, label=r"$C_{d}$")
    plt.title("Drag Coefficient vs. Angle of Attack ")
    plt.xlabel(r"$\alpha$ [°]")
    plt.ylabel(r"$C_{d}$ [-]")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.plot(Cd_all_runs, Cl_all_runs, color='#89CC04', marker='o', linestyle='-', markersize=5)
    plt.title("Lift Coefficient vs. Drag Coefficient ")
    plt.xlabel(r"$C_{d}$ [-]")
    plt.ylabel(r"$C_{l}$ [-]")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()