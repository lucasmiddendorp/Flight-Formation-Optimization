import numpy as np
import matplotlib.pyplot as plt

def plot_all_paths(env, paths, destination, drafting_threshold, gen_number):
    """
    Plot all paths taken by agents, show the destination, and highlight the drafting areas around each leader's path.
    
    :param env: The environment containing the leader's paths.
    :param paths: List of paths, where each path is a list of (x, y) tuples representing an agent's path.
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

    # Plot each agent's path
    for i, path in enumerate(paths):
        path = np.array(path)
        plt.plot(path[:, 0], path[:, 1], marker='', linestyle='-')
    
    # Plot the destination
    plt.scatter(destination[0], destination[1], color='red', label='Destination', s=100, marker='X')

    plt.title(f'Paths of All Agents to Destination, Generation {gen_number} ')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.xlim(-10, 120)
    plt.ylim(-70, 70)
    plt.grid(True)
    plt.pause(0.1)
    plt.clf()
