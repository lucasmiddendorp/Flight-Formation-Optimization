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
destination = [100, 0]
destination_threshold = 3.0
max_waypoints = 30
drafting_threshold = 3.0

draft_benefit = 0.9
# Define leader paths
leader_path1 = [[0, 15], [100, 15]]
# leader_path2 = [[0, 5], [100, 5]]
leader_paths = [leader_path1]

# Define population sizes to test
population_sizes = [10, 100, 1000, 10000]
num_generations = 20
mutation_rate = 0.01
tournament_size = 10

# Initialize the environment
env = FlightEnv(leader_paths, distance_between_waypoints)

# Variables to store results
best_fitnesses = []
total_times = []

# Loop through each population size
for pop_size in population_sizes:
    print(f"Testing population size: {pop_size}")
    
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

    # Store the best fitness and total time for this population size
    best_fitnesses.append(best_fitness)
    total_times.append(run_duration)

    print(f"Population size {pop_size}: Best fitness = {best_fitness}, Time taken = {run_duration:.2f} seconds")

# Plotting population size vs best fitness
plt.figure(figsize=(10, 6))
plt.plot(population_sizes, best_fitnesses, marker='o', linestyle='-', color='blue')
plt.xscale('log')
plt.yscale('symlog')
plt.xlabel('Population Size')
plt.ylabel('Best Fitness')
plt.title('Population Size vs Best Fitness')
plt.grid(True)
plt.show()

# Plotting population size vs total time
plt.figure(figsize=(10, 6))
plt.plot(population_sizes, total_times, marker='o', linestyle='-', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Population Size')
plt.ylabel('Total Time (seconds)')
plt.title('Population Size vs Total Time')
plt.grid(True)
plt.show()
