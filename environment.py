import numpy as np

class FlightEnv:
    def __init__(self, leader_paths, distance_between_waypoints):

        self.leader_paths = [
            self.create_leader_path(start_position, end_position, distance_between_waypoints)
            for start_position, end_position in leader_paths
        ]

    def create_leader_path(self, start_position, end_position, distance_between_waypoints):

        total_distance = np.linalg.norm(np.array(end_position) - np.array(start_position))
        num_waypoints = int(total_distance // distance_between_waypoints) + 1

        x_coords = np.linspace(start_position[0], end_position[0], num_waypoints)
        y_coords = np.linspace(start_position[1], end_position[1], num_waypoints)
        
        return np.column_stack((x_coords, y_coords))

    def get_leader_paths(self):

        return self.leader_paths
