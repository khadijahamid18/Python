import random

# Constants
time_required = [45, 60, 15, 45, 15]  # Time required for each category of work
probability = [0.40, 0.15, 0.15, 0.10, 0.20]  # Probability for each category of work
random_numbers = [40, 82, 11, 34, 25, 66, 17, 79]  # Random numbers for simulation
total_simulated_time = 4 * 60  # Total simulation time in minutes (4 hours)

# Step 1: Establishing Probability Distribution
cumulative_probability = [sum(probability[:i + 1]) for i in range(len(probability))]

# Simulation
total_waiting_time = 0
total_idle_time = 0
total_patients = 0

current_time = 8 * 60  # Start time at 8:00 AM in minutes
while current_time < (8 * 60) + total_simulated_time:
    random_index = random.choice(random_numbers)
    category_index = None

    # Step 2: Cumulative Probability Distribution
    for i in range(len(cumulative_probability)):
        if random_index <= cumulative_probability[i] * 100:  # Multiply by 100 to match random number scale
            category_index = i
            break

    if category_index is not None:
        work_time = time_required[category_index]
        arrival_time = current_time
        service_start_time = max(arrival_time, current_time)
        service_end_time = service_start_time + work_time

        # Calculate waiting time for the patient
        waiting_time = max(0, service_start_time - arrival_time)
        total_waiting_time += waiting_time
        total_patients += 1

        # Calculate idle time of the doctor
        idle_time = max(0, arrival_time - current_time)
        total_idle_time += idle_time

        # Update current time
        current_time = service_end_time

# Calculate average waiting time and average idle time
average_waiting_time = total_waiting_time / total_patients if total_patients != 0 else 0
average_idle_time = total_idle_time / total_patients if total_patients != 0 else 0

# Output
print("Simulation Results:")
print("Total number of patients: ", total_patients)
print("Average waiting time for patients: {:.3f} minutes".format(average_waiting_time))
print("Average idle time of the doctor: {:.3f} minutes".format(average_idle_time))
