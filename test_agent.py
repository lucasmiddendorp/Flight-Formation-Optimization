import numpy as np
import matplotlib.pyplot as plt
from agent import Agent
from waypoints import check_if_reached

def test_agent_navigation():
    # Test setup
    start_position = np.array([0, 0])
    destination = np.array([100, 0])
    initial_heading = 0  # Facing east
    angle_options = [-10,-5,0,5,10]  # Force the agent to always go straight for simplicity

    agent = Agent(start_position, destination, initial_heading, angle_options)
    path = agent.navigate()

    # Ensure the path is not empty and the agent reached the destination within the threshold
    assert len(path) > 0, "Path is empty."

    
    final_position = agent.current_position

    # Plot the path taken by the agent
    plot_path(path, destination)

    assert check_if_reached(final_position, destination), \
        f"Agent did not reach the destination. Final position: {final_position}"

    print("All tests passed.")

def plot_path(path, destination):
    """
    Plot the path taken by the agent and show the destination.
    
    :param path: List of (x, y) tuples representing the agent's path.
    :param destination: (x, y) tuple representing the destination.
    """
    path = np.array(path)
    
    plt.figure(figsize=(10, 6))
    plt.plot(path[:, 0], path[:, 1], marker='o', linestyle='-', color='blue', label='Agent Path')
    plt.scatter(destination[0], destination[1], color='red', label='Destination', s=100, marker='X')

    plt.title('Agent Path to Destination')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_agent_navigation()
