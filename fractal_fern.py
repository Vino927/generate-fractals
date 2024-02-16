# fractal_fern.py
#
# The Barnsley Fern is a fractal that mimics the appearance of a natural fern using 
# mathematical equations. It is generated through a process called 
# iterated function system (IFS), which involves four affine transformations. 
# Each point (x, y) on the plane is transformed to a new point using one of these 
# transformations, chosen randomly at each iteration but with fixed probabilities 
# that dictate the overall shape of the fern:
#
# 1. f1(x, y) = (0, 0.16y)
#    - Probability: 1%. This transformation maps any point to a position that contributes to the stem of the fern.
# 
# 2. f2(x, y) = (0.85x + 0.04y, -0.04x + 0.85y + 1.6)
#
#    - Probability: 85%. This simulates the larger, successively smaller leaflets of the fern.
# 3. f3(x, y) = (0.2x - 0.26y, 0.23x + 0.22y + 1.6)
#    - Probability: 7%. Represents the bottom left leaflet.
#
# 4. f4(x, y) = (-0.15x + 0.28y, 0.26x + 0.24y + 0.44)
#    - Probability: 7%. Represents the bottom right leaflet.
#
# Starting from an initial point, such as the origin (0,0), the algorithm repeatedly 
# applies one of these transformations, chosen randomly based on the specified 
# probabilities. The result is a detailed pattern that closely resembles a fern.

import matplotlib.pyplot as plt
import random

def generate_fractal_fern_points(points=1000):
    """
    Generates the fractal grtmpoints.

    Parameters:
    - points: Number of points to generate for the fractal.

    Returns:
    - A tuple of two lists containing x and y coordinates of the fractal points.
    """
    if points < 0:
        raise ValueError("Number of points must be non-negative.")
    elif points > 0 and points < 3000:
        print("Point values < 1000 could result in sparsely populated final image. Using default value of 3000")
        points = 3000  # Use default value if points are positive but less than 1000
        
    x, y = 0.0, 0.0
    x_list, y_list = [], []

    transformations = [
        (lambda x, y: (float(0.85 * x + 0.04 * y), float(-0.04 * x + 0.85 * y + 1.6)), 0.85),
        (lambda x, y: (float(-0.15 * x + 0.28 * y), float(0.26 * x + 0.24 * y + 0.44)), 0.07),
        (lambda x, y: (float(0.2 * x - 0.26 * y), float(0.23 * x + 0.22 * y + 1.6)), 0.07),
        (lambda x, y: (0.0, float(0.16 * y)), 0.01)  # Explicitly casting y as float and x as 0.0 to ensure consistency
        ]

    for _ in range(points):
        func, prob = random.choices(transformations, weights=[t[1] for t in transformations])[0]
        x, y = func(x, y)
        x_list.append(x)
        y_list.append(y)

    return x_list, y_list