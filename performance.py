import numpy as np

def calculate_fuel_cost(path, formation_paths, drafting_threshold, distance_between_waypoints, draft_benefit):
    """
    Calculate the fuel cost for the given path.

    :param path: The list of coordinates representing the path taken by the agent.
    :param formation_paths: The list of coordinates representing the optimal formation paths.
    :param drafting_threshold: The threshold distance within which drafting occurs.
    :param draft_benefit: The fractional fuel saving during drafting (e.g., 0.9 for 10% savings).
    :return: The fuel cost for the path.
    """
    fuel_cost = 0

    for i in range(1, len(path)):
        # Calculate the actual distance between consecutive points
        segment_distance = np.linalg.norm(np.array(path[i]) - np.array(path[i-1]))

        # Check if the segment is in formation (close to any formation path)
        if is_in_formation(path[i], formation_paths, drafting_threshold):
            fuel_cost += segment_distance * draft_benefit

        else:
            fuel_cost += segment_distance

    return fuel_cost


def is_in_formation(point, formation_paths, drafting_threshold):
    """
    Check if the point is close enough to any formation path to benefit from drafting.

    :param point: A tuple representing the point (x, y).
    :param formation_paths: A list of paths, where each path is a list of tuples representing coordinates.
    :param drafting_threshold: The threshold distance for drafting.
    :return: True if the point is in formation, False otherwise.
    """
    for formation_path in formation_paths:
        for formation_point in formation_path:
            if np.linalg.norm(np.array(point) - np.array(formation_point)) < drafting_threshold:
                return True
    return False
