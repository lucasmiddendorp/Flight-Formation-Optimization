import numpy as np
from performance import calculate_fuel_cost

def fitness_function(population, waypoints, env, max_waypoints, drafting_threshold, destination, draft_benefit):
    fitness_scores = []
    
    for idx, individual in enumerate(population.get_agents()):
        fitness = calculate_fitness(individual, individual.waypoints, env, max_waypoints, drafting_threshold, destination, draft_benefit)
        fitness_scores.append((idx, fitness))
    
    return fitness_scores

def calculate_fitness(individual, waypoints, env, max_waypoints, drafting_threshold, destination, draft_benefit):
    penalty = 0.0

    aircraft_path = np.array(waypoints)
    distance_between_waypoints = np.linalg.norm(waypoints[0] - waypoints[1])

    # Calculate the total fuel used
    total_fuel_used = calculate_fuel_cost(aircraft_path, env.get_leader_paths(), drafting_threshold, distance_between_waypoints, draft_benefit)

    # Penalty for the distance from the final position to the destination
    final_position = aircraft_path[-1]
    distance_to_destination = np.linalg.norm(final_position - destination)
    penalty += distance_to_destination * 10

    opt_fitness = np.linalg.norm(destination) 

    fitness = opt_fitness - total_fuel_used - penalty
    return fitness
