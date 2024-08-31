import numpy as np
import random
from fit_function import fitness_function
from environment import FlightEnv
from waypoints import generate_waypoints

def test_fitness_function():
    # Initialize environment
    env = FlightEnv()
    
    # Example starting conditions
    start_position = np.array([0, 0])
    initial_heading = 0  # Facing East (0 degrees)
    destination = np.array([100, 0])  # Example destination
    distance_between_waypoints = 20  # 20 km between waypoints

    # Create a population of 3 individuals with random decisions
    decision_space = [-10, -5, 0, 5, 10]
    population = []

    for _ in range(3):  # Create 3 individuals
        decisions = [random.choice(decision_space) for _ in range(5)]  # Assuming 5 waypoints for this example
        individual = {"decisions": decisions}
        population.append(individual)
    
    # Generate a set of waypoints based on one of the individual's decisions
    waypoints = generate_waypoints(start_position, initial_heading, population[0]['decisions'], distance_between_waypoints, destination)

    # Run the fitness function
    fitness_scores = fitness_function(population, waypoints, env)

    # Assertions for the test, check the length of the fitness_scores matches the population
    assert len(fitness_scores) == len(population), \
        f"Expected {len(population)} fitness scores, got {len(fitness_scores)}"
    
    # Additional checks could include verifying the fitness scores are within expected ranges
    for idx, fitness in fitness_scores:
        assert isinstance(fitness, float), f"Fitness score should be a float, got {type(fitness)}"
        assert fitness <= 0, f"Fitness score should be negative (penalty + fuel cost), got {fitness}"

    print("All fitness function tests passed.")

if __name__ == "__main__":
    test_fitness_function()
