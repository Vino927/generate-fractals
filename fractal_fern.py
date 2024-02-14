# fractal_fern.py
import matplotlib.pyplot as plt
import random

def generate_fractal_fern(points=100000):
    """
    Generates and plots the Barnsley Fern fractal.

    Parameters:
    - points: Number of points to generate for the fractal.
    """
    # Starting point
    x, y = 0, 0

    # Lists to store x and y coordinates of points
    x_list, y_list = [], []

    # Define transformations and their probabilities
    transformations = [
        (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),
        (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07),
        (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),
        (lambda x, y: (0, 0.16 * y), 0.01)
    ]

    # Generate points
    for _ in range(points):
        func, prob = random.choices(transformations, weights=[t[1] for t in transformations])[0]
        x, y = func(x, y)
        x_list.append(x)
        y_list.append(y)

    # Plot the points
    plt.scatter(x_list, y_list, s=0.1, color="green")
    plt.axis('off')  # Hides the axis
    plt.show()
    input("Press Enter to continue...")
