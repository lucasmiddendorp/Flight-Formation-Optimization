import matplotlib.pyplot as plt
import numpy as np
from performance import calculate_fuel_cost, is_in_formation

def plot_paths(agent_path, formation_path, in_formation_flags):

    agent_path = np.array(agent_path)
    formation_path = np.array(formation_path)
    
    # Plot formation path
    plt.plot(formation_path[:, 0], formation_path[:, 1], 'b--', label='Formation Path')
    
    # Plot agent path
    for i in range(1, len(agent_path)):
        if in_formation_flags[i-1]:
            plt.plot(agent_path[i-1:i+1, 0], agent_path[i-1:i+1, 1], 'g', label='In Formation' if i == 1 else "")
        else:
            plt.plot(agent_path[i-1:i+1, 0], agent_path[i-1:i+1, 1], 'r', label='Not in Formation' if i == 1 else "")
    
    # Highlight start and end points
    plt.scatter(agent_path[0, 0], agent_path[0, 1], color='green', marker='o', label='Start')
    plt.scatter(agent_path[-1, 0], agent_path[-1, 1], color='red', marker='x', label='End')
    
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.title('Flight Paths')
    plt.legend()
    plt.grid(True)
    plt.show()

def test_calculate_fuel_cost():
    # Define a basic path for the agent
    agent_path = [
        (0, 0), (10, 0), (20, 0), (30, 0), (40, 0), (50, 0)
    ]
    
    # Define an optimal formation path (close to the agent's path)
    formation_path = [
        (0, 0), (10, 1), (20, 0.5), (30, 1), (40, 0), (50, 0)
    ]

    # Test with the agent always in formation (within threshold)
    some_threshold = 2.0  # Setting a threshold distance for formation benefits
    in_formation_flags = []
    fuel_cost = calculate_fuel_cost(agent_path, formation_path, some_threshold)
    expected_fuel_cost = 50 * 0.9  # All segments are within formation, so 10% savings on all

    for i in range(1, len(agent_path)):
        in_formation_flags.append(is_in_formation(agent_path[i], formation_path, some_threshold))
    
    assert np.isclose(fuel_cost, expected_fuel_cost), \
        f"Fuel cost calculation error. Expected: {expected_fuel_cost}, Got: {fuel_cost}"

    print("Test passed: Agent always in formation.")

    # Plot the paths
    plot_paths(agent_path, formation_path, in_formation_flags)

    # Test with the agent never in formation (out of threshold)
    some_threshold = 0.5  # Reduce threshold so almost no point qualifies for formation
    in_formation_flags = []
    fuel_cost = calculate_fuel_cost(agent_path, formation_path, some_threshold)
    expected_fuel_cost = 48  # No formation benefit, so full distance cost

    for i in range(1, len(agent_path)):
        in_formation_flags.append(is_in_formation(agent_path[i], formation_path, some_threshold))

    assert np.isclose(fuel_cost, expected_fuel_cost), \
        f"Fuel cost calculation error. Expected: {expected_fuel_cost}, Got: {fuel_cost}"

    print("Test passed: Agent never in formation.")

    # Plot the paths
    plot_paths(agent_path, formation_path, in_formation_flags)

    # Test with the agent partially in formation
    some_threshold = 0.7  # Set a threshold so some points qualify
    in_formation_flags = []
    fuel_cost = calculate_fuel_cost(agent_path, formation_path, some_threshold)
    # In this case, segments from (0, 0) to (10, 0) and (40, 0) to (50, 0) are not in formation
    expected_fuel_cost = 10 + 10 * 0.9 + 10 * 0.9 + 10 * 0.9 + 10  # Two full segments, rest with 10% savings

    for i in range(1, len(agent_path)):
        in_formation_flags.append(is_in_formation(agent_path[i], formation_path, some_threshold))

    assert np.isclose(fuel_cost, expected_fuel_cost), \
        f"Fuel cost calculation error. Expected: {expected_fuel_cost}, Got: {fuel_cost}"

    print("Test passed: Agent partially in formation.")

    # Plot the paths
    plot_paths(agent_path, formation_path, in_formation_flags)

if __name__ == "__main__":
    test_calculate_fuel_cost()
