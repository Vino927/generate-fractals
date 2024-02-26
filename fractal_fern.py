#!/usr/bin/env python3
# fractal_fern.py

# Copyright (C) [2024] [Vino Gupta]
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
# If you modify this Program, or any covered work, by linking or combining it with generate_fractals (or a modified version of that library), containing parts covered by the terms of GPL v3.0, the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of generate_fractals used as well as that of the covered work.}

## =====================
# Fractal Fern
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
## =====================

import matplotlib.pyplot as plt
import random

class FractalFern:
    def __init__(self, points=5000):
        # Check for negative points and raise ValueError
        if points < 0:
            raise ValueError("Number of points must be non-negative")
        
        # Initialize with a default of 5000 points if not specified
        self.points = max(points, 5000)  
    
    def generate_points(self):
        """
        Generates the fractal points for the Barnsley Fern.

        Returns:
        - A tuple of two lists containing x and y coordinates of the fractal points.
        """
        print("Generating the fractal fern...")
        x, y = 0.0, 0.0
        x_list, y_list = [], []

        # Define the set of transformations for generating the fractal pattern. Each transformation
        # is a function that takes coordinates (x, y) as input and outputs new coordinates.

        # Transformation 1: Represents the largest part of the fern (the stem and the larger leaves).
        # This transformation is applied with an 85% probability, making it the most common transformation,
        # which contributes to the bulk of the fern's structure.

        # Transformation 2: Simulates the smaller leaflets on the left side of the fern.
        # This transformation has a 7% chance of being applied, creating variety in the leaf shapes
        # and positions by pushing the points to the left and slightly up.

        # Transformation 3: Another variation of leaf or offshoot formation, similar probability to Transformation 2.
        # It also applies scaling and rotation but with different parameters, contributing to the fractal's diversity.
    
        # Transformation 4: Represents the smallest probability, contributing to the finer details of the fractal.
        # This transformation primarily affects the y-coordinate, simulating upward growth with minimal horizontal deviation.

        transformations = [

            (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),
            (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07),
            (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),
            (lambda x, y: (0.0, 0.16 * y), 0.01)
        ]

        # Iterate over the number of points to generate for the fractal pattern.
        # `self.points` specifies how many iterations (and thus points) to create.
        for _ in range(self.points):  # Use self.points to access the object's points attribute

            # Randomly select one of the transformation functions based on their associated probabilities.
            # `transformations` is a list of tuples, where each tuple contains a transformation function and its probability.
            # `random.choices` returns a list of one selected function based on the specified weights (probabilities).
            # `[0]` extracts the first (and only) element of this list, which is the tuple containing the function and its probability.
            func, prob = random.choices(transformations, weights=[t[1] for t in transformations])[0]
 
            # Apply the selected transformation function to the current point (x, y).
            # This updates the point's coordinates according to the fractal's generation rules.
            x, y = func(x, y)

            x_list.append(x)
            y_list.append(y)

        self.x_points, self.y_points = x_list, y_list  # Store the generated points in instance variables

    def plot(self, ax=None, scale_factor=.01):
        """
        Plots the generated points of the Fern using matplotlib on the provided axes.

        Parameters:
        - ax: Optional. A matplotlib axes object where the fern will be plotted.
             If None, a new figure and axes will be created.
        """
        print("Plotting the fractal fern...")
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 9))
        
        # Assuming self.x_points and self.y_points are populated by generate_points()
        scaled_x_points = [x * scale_factor for x in self.x_points]
        scaled_y_points = [y * scale_factor for y in self.y_points]

        ax.scatter(scaled_x_points, scaled_y_points, s=0.1, color='green')
        #ax.scatter(self.x_points, self.y_points, s=0.1, color='green')
        ax.set_title("Barnsley Fern")
        ax.axis('off')  # Optionally turn off the axis if desired

        # If ax was provided, plt.show() might be managed outside this method
        if ax is None:
            plt.show()
        
     
