# itinitalisng lists
run_nr = [] 
alpha = []
delta_Pb = []
p_bar = []
T = []
rpm = []
rho = []
run_data = [] 
q_infy = []
# this is a list of lists with all the taps, where list 0 contains all the run 1 values for each tap, list 1 contains the values of run 2 etc, 
# you can index a value by doing p_taps[4] will give you the data for tap P005
p_taps = [[] for _ in range(113)]  # empty list with 113 spaces we can rewrite

# reading the file to process data
with open("2Draw_testG24.txt") as file:
    for line in file.readlines()[2:]:  # skipping first two lines
        row = line.strip().split("\t")  # getting rid of blank spaces, splitting all data points at the tab and then adding to data list
        
        # general data
        run_nr.append(float(row[0]))
        alpha.append(float(row[2]))
        delta_Pb.append(float(row[3]))
        p_bar.append(float(row[4]))
        T.append(float(row[5]))
        rpm.append(float(row[6]))
        rho.append(float(row[7]))

        # pressure tap data
        for i, value in enumerate(row[8:]):
            p_taps[i].append(float(value))
        
        run_data.append([float(value) for value in row[8:]])

for j in range(len(run_nr)):  # getting the dynamic pressure
    q_infy.append(0.211804 + 1.928442 * delta_Pb[j] + 1.879374 * 10**(-4) * delta_Pb[j]**2)

p_tot = p_taps[96]  # tap with total pressure is P097
p_static = p_taps[109]  # tap with static pressure is P110