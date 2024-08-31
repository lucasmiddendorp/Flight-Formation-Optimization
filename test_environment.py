import matplotlib.pyplot as plt
import numpy as np
from environment import FlightEnv
from waypoints import generate_waypoints

def plot_flight_paths(follower_path, leader_path, box_size):
    # Plot the flight paths
    plt.plot(follower_path[:, 0], follower_path[:, 1], label="Follower Path", color='blue', linestyle='--')
    plt.plot(leader_path[:, 0], leader_path[:, 1], label="Leader Path", color='green', linestyle='-')
    
    # Set plot limits based on the bounding box size
    plt.xlim(box_size[0] - 10, box_size[2] + 10)
    plt.ylim(box_size[1] - 10, box_size[3] + 10)
    
    # Adding labels and title
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Flight Paths of Leader and Follower")
    
    # Adding a legend to distinguish between the paths
    plt.legend()
    
    # Display the plot
    plt.show()

# Initialize the environment
env = FlightEnv()

# Retrieve the leader's flight path and bounding box size
leader_path = env.get_leader_path()
box_size = env.box_size

# Define follower's decisions for each waypoint
decisions = np.random.choice([-10, -5, 0, 5, 10], size=10)  # Random decisions for simplicity

# Generate the follower's path using the waypoints script
start_position = env.departure_place()  # Start at the follower's departure place
initial_heading = 0  # Assume an initial heading of 0 degrees
distance_between_waypoints = 10  # Distance between waypoints
destination = env.arrival_place()  # Follower's destination

follower_path = generate_waypoints(start_position, initial_heading, decisions, distance_between_waypoints, destination)

# Convert follower_path to a numpy array for consistent plotting
follower_path = np.array(follower_path)

# Plot the flight paths
plot_flight_paths(follower_path, leader_path, box_size)
