from selection import select_parents
from variation import crossover, mutate
from fit_function import fitness_function
from init_population import Population
from environment import FlightEnv
from waypoints import generate_waypoints
from agent import Agent
from evolution import run_evolution
import numpy as np
import matplotlib.pyplot as plt
import time

# Inputs for all the scripts
start_position = [0, 0]
initial_heading = 0
decisions = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
distance_between_waypoints = 5
destination = [100, 25]
destination_threshold = 3.0
max_waypoints = 30
drafting_threshold = 3.0

# Define leader paths
leader_path1 = [[0, 10], [100, 10]]
leader_path2 = [[0,20], [100, 20]]
leader_paths = [leader_path1, leader_path2]

# Define the parameters for the evolutionary algorithm
pop_size = 2000
num_generations = 20
mutation_rate = 0.01
tournament_size = 10

# Initialize the environment
env = FlightEnv(leader_paths, distance_between_waypoints)

# Variables to store results
best_fitnesses = []
total_times = []
all_best_paths = []

# Drafting benefit values to test
draft_benefit_lst = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Loop through each drafting benefit value
for draft_benefit in draft_benefit_lst:
    print(f"--------------------------------- Testing drafting benefit: {draft_benefit}")
    
    start_time = time.time()

    # Initialize population
    population = Population(size=pop_size)
    population.initialize_population(start_position, destination, initial_heading, decisions, distance_between_waypoints, destination_threshold, max_waypoints)

    # Generate and print paths for each individual
    paths = []
    for i, individual in enumerate(population.get_agents()):
        agent = Agent(start_position, destination, initial_heading, angle_options=decisions)
        path = agent.navigate(distance_between_waypoints, destination_threshold, max_waypoints)
        individual.waypoints = path
        paths.append(path)

    # Run the evolutionary algorithm to find the best flight path
    best_path, best_fitness = run_evolution(env, population, pop_size, num_generations, mutation_rate, tournament_size, max_waypoints, drafting_threshold, distance_between_waypoints, destination_threshold, destination, draft_benefit)

    end_time = time.time()
    run_duration = end_time - start_time

    # Store the best fitness, best path, and total time for this draft benefit
    best_fitnesses.append(best_fitness)
    total_times.append(run_duration)
    all_best_paths.append(best_path.waypoints)  # Store the waypoints of the best path

    print(f"Draft benefit {draft_benefit}: Best fitness = {best_fitness}")

# Plotting draft benefit vs best fitness
plt.figure(figsize=(10, 6))
plt.plot(draft_benefit_lst, best_fitnesses, marker='', linestyle='-', color='blue')
plt.xlabel('Fuel usage during draft')
plt.ylabel('Best Fitness')
plt.title('Draft Benefit vs Best Fitness')
plt.grid(True)
plt.show()

# Plotting all the best paths from each draft benefit

plt.figure(figsize=(10, 6))
for i, path in enumerate(all_best_paths):
    path = np.array(path)
    draft_percentage = 100*(1-draft_benefit_lst[i])
    plt.plot(path[:, 0], path[:, 1], marker='', linestyle='-', label=f'Draft Benefit {draft_percentage}%')

# Highlight the drafting areas and leader paths
for leader_path in env.leader_paths:
    leader_x = np.array([point[0] for point in leader_path])
    leader_y = np.array([point[1] for point in leader_path])
    plt.fill_between(leader_x, leader_y - drafting_threshold, leader_y + drafting_threshold, color='lightgreen', alpha=0.5)
    plt.plot(leader_x, leader_y, linestyle='--', color='black', label='Leader Path')

# Plot the destination
plt.scatter(destination[0], destination[1], color='red', label='Destination', s=100, marker='X')

plt.title('Best Paths for Different Draft Benefits')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.xlim(-10, 120)
plt.ylim(-70, 70)
plt.grid(True)
plt.show()
