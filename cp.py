import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import data as d

# getting the airfoil tap positions
airfoil_data = pd.read_excel("SLT practical coordinates.xlsx")

x_over_c = (airfoil_data["x [%]"] / 100).values  # getting x over c values along airfoil (chord length is 100)

run = int(input("which run number ? ")) - 1  # generating Cps for different runs

Cp = []
for i in range(49):  # since only 49 taps are for the surface pressure measurements
    if i == 24:  # making sure we don't plot that line going from 100 to 0 as it switches from upper to lower surface
        Cp.append(np.nan)
    else:
        Cp.append((float(d.run_data[run][i]) - d.p_static[run]) / d.q_infy[run])  # cp = p - p_infty / q

def main():  # so that the plots don't run when we import the function
    # plt.plot(x_over_c[:25], Cp_upper, color='#89CC04', marker='o', linestyle='-', markersize=5, label=r"$C_{p}$ Upper")
    # plt.plot(x_over_c[25:], Cp_lower, color='black', marker='o', linestyle='-', markersize=5, label=r"$C_{p}$ Lower")
    plt.plot(x_over_c, Cp, color='#89CC04', marker='o', linestyle='-', markersize=5, label=r"$C_{p}$ Data")
    plt.gca().invert_yaxis()  # flipping y axis for Cp plot style
    plt.title("Pressure Coefficient vs. Chordwise Position for " + str(d.alpha[run]) + "° Angle of Attack ")
    plt.xlabel(r"$x/c$ [-]")
    plt.ylabel(r"$C_{p}$ [-]")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()