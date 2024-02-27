import random

# Constants
time_required = [45, 60, 15, 45, 15]  # Time required for each category of work
probability = [0.40, 0.15, 0.15, 0.10, 0.20]  # Probability for each category of work
random_numbers = [40, 82, 11, 34, 25, 66, 17, 79]  # Random numbers for simulation
total_simulated_time = 4 * 60  # Total simulation time in minutes (4 hours)

# Step 1: Establishing Probability Distribution
cumulative_probability = [sum(probability[:i + 1]) for i in range(len(probability))]

# Step 2: Cumulative Probability Distribution
def get_category(random_number):
    for i in range(len(cumulative_probability)):
        if random_number <= cumulative_probability[i]:
            return i

# Simulation
total_waiting_time = 0
total_patients = 0
total_idle_time = 0

current_time = 8 * 60  # Start time at 8:00 AM in minutes
while current_time < (8 * 60) + total_simulated_time:
    random_index = random.choice(random_numbers)
    category_index = get_category(random_index / 100)
    work_time = time_required[category_index]

    # Check if the patient has to wait
    if current_time > 8 * 60:
        waiting_time = current_time - (8 * 60)
        total_waiting_time += waiting_time
        total_patients += 1

    current_time += work_time

    # Calculate idle time of the doctor
    arrival_time = current_time
    service_start_time = max(arrival_time, current_time)
    idle_time = max(0, arrival_time - current_time)
    total_idle_time += idle_time
    
    service_end_time = service_start_time + work_time

        # Update current time
    current_time = service_end_time

# Calculate average waiting time
average_waiting_time = total_waiting_time / total_patients if total_patients != 0 else 0
average_idle_time = total_idle_time / total_patients if total_patients != 0 else 0

# Output
print("Simulation Results:")
print("Total number of patients: ", total_patients)
print("Average waiting time for patients: {:.2f} minutes".format(average_waiting_time))
print("Average idle time of the doctor: {:.3f} minutes".format(average_idle_time))
 