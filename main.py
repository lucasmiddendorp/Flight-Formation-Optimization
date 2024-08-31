from selection import select_parents
from variation import crossover, mutate
from fit_function import fitness_function
from init_population import Population
from environment import FlightEnv
from waypoints import generate_waypoints
from agent import Agent
from evolution import run_evolution
from plot_paths import plot_all_paths
from performance import is_in_formation
import numpy as np
global start_position, initial_heading
from best_path_plot import plot_best_path

# Inputs for all the scripts
start_position = [0,0]
initial_heading = 0
decisions = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
distance_between_waypoints = 5
destination = [100, 0]
destination_threshold = 3.0
max_waypoints = 30
drafting_threshold = 1.0

draft_benefit = 0.9
# Define leader paths
leader_path1 = [[3.5, 3.4], [96, 0]]
# leader_path2 = [[0, -10], [100, 10]]
leader_paths = [leader_path1]

pop_size = 2000
num_generations = 20
mutation_rate = 0.01
tournament_size = 10

# Initialize the environment
env = FlightEnv(leader_paths, distance_between_waypoints)

# Initialize population
population = Population(size=pop_size)
population.initialize_population(start_position, destination, initial_heading, decisions, distance_between_waypoints, destination_threshold, max_waypoints)


# Generate and print paths for each individual
paths = []
for i, individual in enumerate(population.get_agents()):
    agent = Agent(start_position, destination, initial_heading, angle_options=decisions)
    path = agent.navigate(distance_between_waypoints, destination_threshold, max_waypoints)
    individual.waypoints = path
    # print(f"Individual {i} path: {path}")
    # print("lenght path = ",len(path))
    paths.append(path)
    

        

# Run the evolutionary algorithm to find the best flight path
best_path, best_fitness = run_evolution(env, population, pop_size, num_generations, mutation_rate, tournament_size, max_waypoints, drafting_threshold, distance_between_waypoints, destination_threshold, destination, draft_benefit)

# Print the best path found by the evolutionary algorithm
print("Best flight path found by evolution:", best_path.decisions)


# Generate the best path using these decisions
agent = Agent(start_position, destination, initial_heading, angle_options=decisions)
best_decisions = best_path.decisions
best_path_coordinates = generate_waypoints(start_position, initial_heading, best_decisions, distance_between_waypoints, destination, destination_threshold)

# Now plot the best path using the coordinates
plot_best_path(env, best_path_coordinates, destination, drafting_threshold)