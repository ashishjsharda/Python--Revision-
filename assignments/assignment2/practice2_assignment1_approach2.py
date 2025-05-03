def find_farthest_point(coordinates):
    """
    Takes a list of tuples representing (x, y) coordinates and returns the tuple
    with the largest distance from the origin (0, 0).
    
    Args:
        coordinates: A list of tuples, each containing x and y coordinates
        
    Returns:
        The tuple with the largest distance from origin, or None if list is empty
    """
    if not coordinates:
        return None
    
    max_distance = 0
    farthest_point = None
    
    for point in coordinates:
        x, y = point
        # Calculate Euclidean distance: sqrt(x^2 + y^2)
        distance = (x**2 + y**2)**0.5
        
        if distance > max_distance:
            max_distance = distance
            farthest_point = point
    
    return farthest_point

result=find_farthest_point([(1, 1), (2, 2), (3, 3), (4, 4)])
print(result)  # Output: (4, 4)
