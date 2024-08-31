import random
from agent import Agent
import numpy as np

def crossover(parent1, parent2):

    # Access the decisions (or actions) list from the parent objects
    parent1_decisions = parent1.decisions
    parent2_decisions = parent2.decisions

# Ensure both parents have the same number of decisions
    num_decisions = np.min([len(parent1.decisions), len(parent2.decisions)])
    
    # Perform crossover at a random point within the range of decisions
    if num_decisions > 1:  # Ensure there is more than one decision
        crossover_point = random.randint(1, num_decisions - 1)
    else:
        crossover_point = 1  # If only one decision, crossover point is at the start
    
    child1_decisions = parent1_decisions[:crossover_point] + parent2_decisions[crossover_point:]
    child2_decisions = parent2_decisions[:crossover_point] + parent1_decisions[crossover_point:]
    
    # Create new Agent objects for the children, ensuring proper initialization
    child1 = Agent(start=parent1.position, destination=parent1.destination, initial_heading=parent1.initial_heading, angle_options=parent1.angle_options)
    child2 = Agent(start=parent2.position, destination=parent2.destination, initial_heading=parent2.initial_heading, angle_options=parent2.angle_options)
    
    # Assign the crossover-generated decisions to the children
    child1.decisions = child1_decisions
    child2.decisions = child2_decisions
    
    return child1, child2


def mutate(agent, mutation_rate):
    """
    Mutates an agent by randomly changing its decisions.
    
    Args:
        agent (Agent): The agent to mutate.
        mutation_rate (float): The probability of each decision being mutated.
        
    Returns:
        Agent: The mutated agent.
    """
    # Access the decisions list from the agent object
    decisions = agent.decisions
    
    for i in range(len(decisions)):
        if random.random() < mutation_rate:
            # Assuming the decisions are chosen from angle_options
            decisions[i] = random.choice(agent.angle_options)
    
    # Update the agent's decisions
    agent.decisions = decisions
    
    return agent
