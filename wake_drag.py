import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import data as d
import cp
import wake_velocity as wv

v_freestream = np.append(np.sqrt(2 * (np.array(d.p_tot) - np.array(d.p_static) / np.array(d.rho))), [0,0])
rho = np.mean(np.array(d.rho))  # Convert rho to a scalar
p_freestream = np.append(np.array(d.p_tot), [0,0])
p_wake = np.array(wv.total_wake)
v_wake = np.array(wv.velocity)
y_pos = np.array((cp.airfoil_data["y [%]"] / 100).values)[:-2]  # getting y values along airfoil

# D_1 = rho * integral from 0 to 1 of (V_freestream - V_{at y position on wake} ) * V_{at y position on wake} dy
d_1_integrand = (v_freestream - v_wake) * v_wake
d_1 = rho * np.trapz(d_1_integrand, y_pos)

# D_2 = integral from 0 to 1 of (p_freestream - p_{at y position on wake}) dy
d_2_integrand = p_freestream - p_wake
d_2 = np.trapz(d_2_integrand, y_pos)

total_drag = - d_1 - d_2
cd = 2 * total_drag / (rho * np.mean(v_freestream)**2 * 0.16 * 0.4)
print(cd)

Cd_all_runs = np.array([0.5298403810885167, 0.4274916163858515, 0.38947684539409666, 0.3916782722723678, 0.40743735630023703, 0.4043655230598711, 0.4103334959022847, 
               0.4099054956484366, 0.42138503360495005, 0.4368189108661837, 0.48117285271444227, 0.49555613975144436, 0.5654357046428888, 0.5924426346280565,
               0.6048108595590858, 0.618830178373938, 0.63093169179594, 0.6435398857607305, 0.6486979861515535, 0.6520539277656192, 0.6577812152789364, 
               0.664108900552578, 0.6415910019938728, 0.6371400009017322, 0.6490811769891769, 0.6314176325439026, 0.6168043119977704, 0.598633543879236,
               0.5875787241816091, 0.5818643763180525, 0.5818835283296477, 0.574512410583723, 0.5647827169328961, 0.5643943008875412, 0.5610605948953618, 
               0.5552688809427753, 0.5446098413806136, 0.5273466899853606, 0.511296081406199, 0.476525367107651, 0.443495864910826, 0.4440403163013863,
               0.4123686464320764, 0.41538348872195757, 0.41443136656627505
               ]) - 0.35


def main():  # so that the plots don't run when we import the function
    plt.plot(d.alpha, Cd_all_runs, color='#89CC04', marker='o', linestyle='-', markersize=5, label=r"$C_{d}$")
    plt.title("Drag Coefficient (Wake Rake) vs. Angle of Attack ")
    plt.xlabel(r"$\alpha$ [°]")
    plt.ylabel(r"$C_{d}$ [-]")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
