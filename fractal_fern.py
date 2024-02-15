# fractal_fern.py
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

def plot_fractal_fern(x_list, y_list):
    """
    Plots the Barnsley Fern fractal from given x and y coordinates.

    Parameters:
    - x_list: List of x coordinates.
    - y_list: List of y coordinates.
    """
    plt.scatter(x_list, y_list, s=0.1, color="green")
    plt.axis('off')
    plt.show()
    input("Press Enter to continue...")
