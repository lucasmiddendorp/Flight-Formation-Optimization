from selection import select_parents
from variation import crossover, mutate
from fit_function import fitness_function
from init_population import Population
from environment import FlightEnv
from waypoints import generate_waypoints
from agent import Agent
import numpy as np
from plot_paths import plot_all_paths

def run_evolution(env, population, pop_size, num_generations, mutation_rate, tournament_size, max_waypoints, drafting_threshold, distance_between_waypoints, destination_threshold, destination, draft_benefit):

    best_fitness = None
    best_individual = None
    
    for generation in range(num_generations):
        
        print(" ------------------- Generation", generation, ' -------------------')
        
        # Calculate fitness scores for the current population
        fitness_scores = fitness_function(population, [ind.waypoints for ind in population.get_agents()], env, max_waypoints, drafting_threshold, destination, draft_benefit)
        print('Average fitness:', np.average([score[1] for score in fitness_scores]))

        # Identify the best fitness in the current population
        best_fitness_in_gen = np.max([score[1] for score in fitness_scores])
        best_individual_in_gen = population.get_agents()[np.argmax([score[1] for score in fitness_scores])]
        print(f"Best fitness in Generation {generation}: {best_fitness_in_gen}")
        
        # Update the best fitness and individual if the current generation is better
        if best_fitness is None or best_fitness_in_gen > best_fitness:
            best_fitness = best_fitness_in_gen
            best_individual = best_individual_in_gen
        
        # Initialize the new population for the next generation
        new_population = Population(size=pop_size)

        paths = []

        # Generate the new population via crossover and mutation
        while len(new_population.get_agents()) < pop_size:
            parent1, parent2 = select_parents(population, fitness_scores, tournament_size)

            child1, child2 = crossover(parent1, parent2)
            
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            
            # Generate and assign waypoints for the children
            child1.start_position = [0, 0]
            child2.start_position = [0, 0]
            child1.initial_heading = 0
            child2.initial_heading = 0
            child1.destination = destination
            child2.destination = destination

            child1.waypoints = generate_waypoints(child1.start_position, child1.initial_heading, child1.decisions, distance_between_waypoints, child1.destination, destination_threshold)
            child2.waypoints = generate_waypoints(child2.start_position, child2.initial_heading, child2.decisions, distance_between_waypoints, child2.destination, destination_threshold)
            
            new_population.add_agent(child1)
            new_population.add_agent(child2)

            paths.append(child1.waypoints)
            paths.append(child2.waypoints)

        plot_all_paths(env, paths, destination, drafting_threshold, generation)
        # Set the current population to the new one for the next generation
        population = new_population
        
        # print(f"Generation {generation} completed with best fitness: {best_fitness_in_gen}")

    
    return best_individual, best_fitness
