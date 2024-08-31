import numpy as np
from waypoints import generate_waypoints, check_if_reached

class Agent:
    def __init__(self, start, destination, initial_heading, angle_options):

        self.position = start
        self.destination = destination
        self.initial_heading = initial_heading
        self.angle_options = angle_options
        self.current_position = start
        self.current_heading = initial_heading
        self.path = [start]  # Record the path taken by the agent
        self.decisions = []

    def choose_action(self):

        # Example logic for choosing an angle
        return np.random.choice(self.angle_options)

    def move(self, angle, distance):

        rad_angle = np.radians(angle)
        new_x = self.current_position[0] + distance * np.cos(rad_angle)
        new_y = self.current_position[1] + distance * np.sin(rad_angle)
        self.current_position = np.array([new_x, new_y])
        self.path.append(self.current_position)

    def navigate(self, distance_between_waypoints, threshold, max_waypoint):

        decisions = []
        while not check_if_reached(self.current_position, self.destination, threshold) and len(decisions)<max_waypoint:
            # Choose a heading decision
            decision = self.choose_action()
            decisions.append(decision)
            self.decisions = decisions
            # Generate the next waypoint based on the current heading and decision
            waypoints = generate_waypoints(self.current_position, self.current_heading, [decision], distance_between_waypoints, self.destination, threshold)
            
            # Move the agent to the next waypoint
            next_position = waypoints[-1]
            distance = np.linalg.norm(next_position - self.current_position)
            self.move(decision, distance)
            
            # Update the current heading after the move
            self.current_heading += decision
            
        return self.path

