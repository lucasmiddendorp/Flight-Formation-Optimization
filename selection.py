import random

def select_parents(population, fitness_scores, tournament_size):


    parents = []
    
    # Get the list of individuals from the Population object
    individuals = population.get_agents()
    
    for _ in range(2):  # Select two parents
        # Pair individuals with their fitness scores
        tournament_pool = list(zip(individuals, fitness_scores))
        
        # Select a random sample for the tournament
        tournament = random.sample(tournament_pool, tournament_size)
        
        # Sort the tournament participants by fitness (assuming higher fitness is better)
        tournament.sort(key=lambda x: x[1][1], reverse=True)
        
        # The best individual from the tournament is selected as a parent
        parents.append(tournament[0][0])
    
    return parents[0], parents[1]
