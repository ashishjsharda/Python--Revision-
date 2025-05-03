def find_farthest_point(coordinates):
    """
    Find the farthest point from a given location on a map.

    This function takes a list of coordinates representing points on a map
    and returns the farthest point from the first coordinate (origin).

    Parameters:
    coordinates (list of tuples): A list of (x, y) coordinates representing points on a map.

    Returns:
    tuple: The (x, y) coordinate of the farthest point.

    Raises:
    ValueError: If the input list is empty or contains non-numeric values.

    Example:
    >>> find_farthest_point([(0, 0), (1, 1), (2, 2), (3, 3)])
    (3, 3)
    """
    if not coordinates:
        raise ValueError("Input list is empty")

    try:
        origin = coordinates[0]
        max_distance = 0
        farthest_point = None

        for point in coordinates:
            distance = ((point[0] - origin[0])**2 + (point[1] - origin[1])**2)**0.5
            if distance > max_distance:
                max_distance = distance
                farthest_point = point

        return farthest_point

    except (TypeError, IndexError):
        raise ValueError("Invalid input: coordinates must be a list of numeric tuples")
    
points = [(1, 2), (3, 4), (-5, 12), (0, 0)]
result = find_farthest_point(points)  # Returns (-5, 12)
print(f"The farthest point from the origin is: {result}")
