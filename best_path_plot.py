


import numpy as np
import matplotlib.pyplot as plt

def plot_best_path(env, best_path, destination, drafting_threshold):
    """
    Plot the best path taken by the best agent, show the destination, and highlight the drafting areas around each leader's path.
    
    :param env: The environment containing the leader's paths.
    :param best_path: List of (x, y) tuples representing the best agent's path.
    :param destination: (x, y) tuple representing the destination.
    :param drafting_threshold: Distance threshold to highlight the drafting area around the leader's paths.
    """
    plt.figure(figsize=(10, 6))
    
    # Iterate over each leader's path in the environment
    for leader_path in env.leader_paths:
        leader_x = leader_path[:, 0]
        leader_y = leader_path[:, 1]

        # Plot the drafting area around the leader's path
        plt.fill_between(leader_x, leader_y - drafting_threshold, leader_y + drafting_threshold, 
                         color='lightgreen', alpha=0.5, label='Drafting Area')

        # Plot the leader's path
        plt.plot(leader_x, leader_y, linestyle='--', color='black', label='Leader Path')

    # Plot the best agent's path
    best_path = np.array(best_path)
    plt.plot(best_path[:, 0], best_path[:, 1], marker='', linestyle='-', color='blue', label='Best Agent Path')

    # Plot the destination
    plt.scatter(destination[0], destination[1], color='red', label='Destination', s=100, marker='X')

    plt.title('Best Path to Destination')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.xlim(-10, 120)
    plt.ylim(-70, 70)
    plt.grid(True)
    plt.pause(60)  # Show the plot, this time without clearing it immediately
    plt.clf()

