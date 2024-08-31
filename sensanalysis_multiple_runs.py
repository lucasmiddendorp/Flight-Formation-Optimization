from selection import select_parents
from variation import crossover, mutate
from fit_function import fitness_function
from init_population import Population
from environment import FlightEnv
from waypoints import generate_waypoints
from agent import Agent
from evolution import run_evolution
from performance import is_in_formation
import numpy as np
import matplotlib.pyplot as plt

global start_position, initial_heading
# from best_path_plot import plot_best_path

# Inputs for all the scripts
start_position = [0, 0]
initial_heading = 0
decisions = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
distance_between_waypoints = 5
destination = [100, 0]
destination_threshold = 3.0
max_waypoints = 30
drafting_threshold = 3.0

draft_benefit = 0.9

# Define leader paths
leader_path1 = [[0, 10], [100, 10]]
# leader_path2 = [[0, 50], [100, 50]]
leader_paths = [leader_path1]

pop_size = 2000
num_generations = 20
mutation_rate = 0.01
tournament_size = 10

# Initialize the environment
env = FlightEnv(leader_paths, distance_between_waypoints)

# Variables to store results across runs
all_best_paths = []
fitness_values = []

# Run the simulation multiple times
num_runs = 10

for run in range(num_runs):
    print(f"Run {run + 1}/{num_runs}")

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

    # Print the best path found by the evolutionary algorithm
    print("Best flight path found by evolution:", best_path.decisions)

    # Generate the best path using these decisions
    best_decisions = best_path.decisions
    best_path_coordinates = generate_waypoints(start_position, initial_heading, best_decisions, distance_between_waypoints, destination, destination_threshold)

    # Store the best path and fitness
    all_best_paths.append(best_path_coordinates)
    fitness_values.append(best_fitness)  

# Calculate and print the average fitness across runs
average_fitness = np.mean(fitness_values)
best_fitness = np.min(fitness_values)  # Best fitness across all runs

print(f"Average fitness across {num_runs} runs: {average_fitness}")
print(f"Best fitness across {num_runs} runs: {best_fitness}")

# Plot all best paths from all runs on a single graph
plt.figure(figsize=(10, 6))
for i, path in enumerate(all_best_paths):
    path = np.array(path)
    plt.plot(path[:, 0], path[:, 1], marker='', linestyle='-', label=f'Run {i + 1} Best Path')

# Highlight the drafting areas and leader paths
for leader_path in env.leader_paths:
    leader_x = np.array([point[0] for point in leader_path])
    leader_y = np.array([point[1] for point in leader_path])
    plt.fill_between(leader_x, leader_y - drafting_threshold, leader_y + drafting_threshold, color='lightgreen', alpha=0.5)
    plt.plot(leader_x, leader_y, linestyle='--', color='black', label='Leader Path')

# Plot the destination
plt.scatter(destination[0], destination[1], color='red', label='Destination', s=100, marker='X')

plt.title('Best Paths of All Runs')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.xlim(-10, 120)
plt.ylim(-70, 70)
plt.grid(True)
plt.show()

# Plot a bar chart of fitness scores from each run
plt.figure(figsize=(10, 6))
plt.bar(range(1, num_runs + 1), fitness_values, color='blue', alpha=0.7, width=0.5)
plt.title('Fitness Scores of Best Paths Across Runs')
plt.xlabel('Run Number')
plt.ylabel('Fitness Score')
plt.grid(True)
plt.show()
