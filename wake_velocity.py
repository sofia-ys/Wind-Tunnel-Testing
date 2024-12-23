import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import data as d
import cp

static_wake = []
total_wake = []
for i in range(12):
    static_wake.append(d.run_data[cp.run][i+97])

for j in range(47):
    total_wake.append(d.run_data[cp.run][j+49])

tot_wake_position = (cp.airfoil_data["total wake rake probe locations [mm]"]).values[:-2]  # getting wake rake positions
stat_wake_position = (cp.airfoil_data["static wake rake probe locations [mm]"]).values[:12]  # getting wake rake positions

velocity = []
for m in range(6):
    velocity.append(np.sqrt(2 * (total_wake[m] - d.p_static[cp.run] / d.rho[cp.run])))

for n in range(6, 42):
    total_probe_pos = tot_wake_position[n]
    
    # Find the closest static probe
    closest_static_probe_idx = min(
        range(len(stat_wake_position)),
        key=lambda s: abs(total_probe_pos - stat_wake_position[s])
    )
    
    # Calculate velocity using the closest static probe
    velocity.append(np.sqrt(2 * (total_wake[n] - static_wake[closest_static_probe_idx] / d.rho[cp.run])))

for p in range(5):
    velocity.append(np.sqrt(2 * (total_wake[(p + 42)] - d.p_static[cp.run] / d.rho[cp.run])))


def main():  # so that the plots don't run when we import the function
    plt.plot(velocity, tot_wake_position, color='#89CC04', marker='o', linestyle='-', markersize=5)
    plt.title("Wake Rake Velocity Profile")
    plt.ylabel(r"Wake Rake Probe Position [mm]")
    plt.xlabel(r"Flow Velocity [mm]")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

# Function to calculate velocity for a given run
def calculate_velocity(cp_run):
    static_wake = []
    total_wake = []

    # Collect static and total wake values for the given cp.run
    for i in range(12):
        static_wake.append(d.run_data[cp_run][i+97])

    for j in range(47):
        total_wake.append(d.run_data[cp_run][j+49])

    # Get wake rake probe positions
    tot_wake_position = (cp.airfoil_data["total wake rake probe locations [mm]"]).values[:-2]  # getting wake rake positions
    stat_wake_position = (cp.airfoil_data["static wake rake probe locations [mm]"]).values[:12]  # getting wake rake positions

    # Calculate velocity for total wake probes
    velocity = []

    # First 6 probes use static pressure directly
    for m in range(6):
        velocity.append(np.sqrt(2 * (total_wake[m] - d.p_static[cp_run] / d.rho[cp_run])))

    # Probes 7 to 42 use closest static pressure probe
    for n in range(6, 42):
        total_probe_pos = tot_wake_position[n]
        
        # Find the closest static probe
        closest_static_probe_idx = min(
            range(len(stat_wake_position)),
            key=lambda s: abs(total_probe_pos - stat_wake_position[s])
        )
        
        # Calculate velocity using the closest static probe
        velocity.append(np.sqrt(2 * (total_wake[n] - static_wake[closest_static_probe_idx] / d.rho[cp_run])))

    # Last 5 probes use static pressure directly
    for p in range(5):
        velocity.append(np.sqrt(2 * (total_wake[(p + 42)] - d.p_static[cp_run] / d.rho[cp_run])))

    return velocity, tot_wake_position

# Function to plot velocity profiles for all runs
def plot_velocity_profiles():
    # Create a new figure
    plt.figure()

    # Loop through all the cp.run values and plot velocity profiles
    for cp_run in range(len(d.run_data)):  # Adjust the range based on how many cp.run values you have
        if cp_run > 21 or cp_run in [6, 8, 10, 12, 13, 14, 16, 17, 18, 19, 20]:
            continue
        else:
            velocity, tot_wake_position = calculate_velocity(cp_run)
            
            # Plot the velocity profile for this run
            plt.plot(velocity, tot_wake_position, label=f'α {d.alpha[cp_run]}', marker='o', linestyle='-', markersize=5)

    # Adding labels and title
    plt.title("Wake Rake Velocity Profile at All Angles of Attack")
    plt.ylabel(r"Wake Rake Probe Position [mm]")
    plt.xlabel(r"Flow Velocity [m/s]")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

# Main function to call the plot function
def main():
    plot_velocity_profiles()

# Run the main function
if __name__ == "__main__":
    main()
