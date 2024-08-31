import numpy as np

class FlightEnv:
    def __init__(self, leader_paths, distance_between_waypoints):
        """
        Initialize the flight environment.

        :param leader_paths: List of tuples containing the start and end points for each leader path.
                             Each tuple should have (start_position, end_position).
        :param distance_between_waypoints: Distance between waypoints for the leader path.
        """
        self.leader_paths = [
            self.create_leader_path(start_position, end_position, distance_between_waypoints)
            for start_position, end_position in leader_paths
        ]

    def create_leader_path(self, start_position, end_position, distance_between_waypoints):
        """
        Create a straight-line leader path between start and end positions.
        
        :param start_position: The starting coordinates of the leader path.
        :param end_position: The ending coordinates of the leader path.
        :param distance_between_waypoints: The distance between each waypoint.
        :return: A numpy array representing the leader path.
        """
        total_distance = np.linalg.norm(np.array(end_position) - np.array(start_position))
        num_waypoints = int(total_distance // distance_between_waypoints) + 1

        x_coords = np.linspace(start_position[0], end_position[0], num_waypoints)
        y_coords = np.linspace(start_position[1], end_position[1], num_waypoints)
        
        return np.column_stack((x_coords, y_coords))

    def get_leader_paths(self):
        """
        Return the flight paths of the leaders.
        
        :return: A list of numpy arrays representing the leader paths.
        """
        return self.leader_paths
