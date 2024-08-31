import numpy as np
import matplotlib.pyplot as plt
from waypoints import generate_waypoints
from agent import Agent

def test_waypoints():
    # Define the test parameters
    start_position = np.array([0, 0])
    initial_heading = 0  
    decisions = [0, 15, -10, 5, 0]  
    distance_between_waypoints = 20  
    destination = np.array([100, 0])  
    
    # Generate the waypoints
    waypoints = generate_waypoints(start_position, initial_heading, decisions, distance_between_waypoints, destination)

    # straight_path = navigate_to_destination(agent, destination, threshold=5.0)
    # Plot the path
    path_x, path_y = zip(*waypoints)
    plt.plot(path_x, path_y, marker='o', color='blue', label='Path')
    plt.plot(destination[0], destination[1], 'ro', label='Destination')
    plt.xlabel('X Position (km)')
    plt.ylabel('Y Position (km)')
    plt.title('Agent Path to Destination')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test_waypoints()

