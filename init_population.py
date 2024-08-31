import random
import numpy as np
from agent import Agent

class Population:
    def __init__(self, size):
        self.size = size
        self.agents = []

    def initialize_population(self, start_position, destination, initial_heading, angle_options, distance_between_waypoints, threshold, max_waypoint):
        """Initialize the population with Agents."""
        for _ in range(self.size):
            # Create an Agent instance
            agent = Agent(start=start_position, destination=destination, initial_heading=initial_heading, angle_options=angle_options)
            
            # Have the agent navigate to generate its path and decisions
            agent.navigate(distance_between_waypoints, threshold, max_waypoint)
            
            # Add the agent to the population
            self.agents.append(agent)

    def get_agents(self):
        """Return the list of agents in the population."""
        return self.agents
    
    def add_agent(self, agent):
        """Add an agent to the population."""
        if len(self.agents) < self.size:
            self.agents.append(agent)
    
    def get_best_agent(self, fitness_scores):
        """Return the best agent based on fitness scores."""
        best_index = max(fitness_scores, key=lambda x: x[1])[0]
        return self.agents[best_index]