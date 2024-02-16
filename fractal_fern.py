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

class FractalFern:
    def __init__(self, points=5000):
        # Initialize with a default of 5000 points if not specified
        self.points = max(points, 3000)  # Ensuring at least 3000 points for a denser image
    
    def generate_points(self):
        """
        Generates the fractal points for the Barnsley Fern.

        Returns:
        - A tuple of two lists containing x and y coordinates of the fractal points.
        """
        x, y = 0.0, 0.0
        x_list, y_list = [], []

        transformations = [
            (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),
            (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07),
            (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),
            (lambda x, y: (0.0, 0.16 * y), 0.01)
        ]

        for _ in range(self.points):  # Use self.points to access the object's points attribute
            func, prob = random.choices(transformations, weights=[t[1] for t in transformations])[0]
            x, y = func(x, y)
            x_list.append(x)
            y_list.append(y)

        self.x_points, self.y_list = x_list, y_list  # Store the generated points in instance variables

    def plot(self):
        """
        Plots the generated points of the fern using matplotlib.
        """
        plt.figure(figsize=(6, 9))
        plt.scatter(self.x_points, self.y_list, s=0.1, color='green')
        plt.title("Barnsley Fern")
        plt.axis('off')  # Optionally turn off the axis if desired
     
