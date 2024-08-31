import numpy as np

def generate_waypoints(start_position, initial_heading, decisions, distance_between_waypoints, destination, threshold=2.0):


    # print("Generating waypoints...")
    waypoints = [start_position]
    current_position = start_position
    current_heading = initial_heading
    
    for decision in decisions:
        # Update the heading based on the decision
        current_heading += decision
        
        # Convert the heading to radians
        rad_heading = np.radians(current_heading)
        
        # Calculate the next waypoint position
        delta_x = distance_between_waypoints * np.cos(rad_heading)
        delta_y = distance_between_waypoints * np.sin(rad_heading)
        next_position = current_position + np.array([delta_x, delta_y])
        
        # Append the new waypoint to the list
        waypoints.append(next_position)
        
        # Update the current position
        current_position = next_position
        
        # Check if the aircraft is within the threshold distance from the destination
        if np.linalg.norm(current_position - destination) <= threshold:
            # print(f"Reached close proximity to the destination: {current_position}")
            break
    
    return waypoints

def check_if_reached(current_position, destination, threshold):
    """
    Check if the aircraft has reached a waypoint within a certain threshold distance.
    
    :param current_position: Current position of the aircraft (numpy array)
    :param destination: Target destination (numpy array)
    :param threshold: Distance threshold to consider as 'reached'
    :return: True if the destination is reached, otherwise False
    """
        # Convert current_position and destination to numpy arrays if they aren't already
    current_position = np.array(current_position)
    destination = np.array(destination)
    
    distance = np.linalg.norm(current_position - destination)
    return distance <= threshold
