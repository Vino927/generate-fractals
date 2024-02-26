#!/usr/bin/env python3
# seashell.py
# Copyright (C) [2024] [Vino Gupta]
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
# If you modify this Program, or any covered work, by linking or combining it with generate_fractals (or a modified version of that library), containing parts covered by the terms of GPL v3.0, the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of generate_fractals used as well as that of the covered work.}


# =====================
# 3D Double Seashell
# This script generates a 3D conical mollusc shell with tapered ends.
# =====================


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


class DoubleSeashell:
    def __init__(self, a, b, c, n_turns, n_turns_inv, thickness, points=1000):
        """
        Initializes the DoubleSeashell object with specific parameters.

        Parameters:
        - a, b, c: Shape parameters for the seashell.
        - n_turns: Number of turns for the first shell.
        - n_turns_inv: Number of turns for the inverse shell.
        - thickness: Thickness of the shell.
        - points: Number of points to generate for each curve.
        """

                # Type and value checking for each parameter
        if not all(isinstance(param, (int, float)) for param in [a, b, c, thickness]) or not isinstance(points, int):
            raise TypeError("Parameters a, b, c, thickness must be int or float, and points must be int.")
        
        if any(param <= 0 for param in [a, b, c, thickness, points]):
            raise ValueError("Parameters a, b, c, thickness, and points must be positive.")
        
        if not all(isinstance(param, int) and param > 0 for param in [n_turns, n_turns_inv]):
            raise ValueError("Parameters n_turns and n_turns_inv must be positive integers.")

        self.a = a
        self.b = b
        self.c = c
        self.n_turns = n_turns
        self.n_turns_inv = n_turns_inv
        self.thickness = thickness
        self.points = points

    def generate_points(self):
        """
        Generates points for a 3D double seashell curve and stores them in instance variables.

        Returns:
        - x, y, z coordinates of the double shell.
        """
        print("Generating the seashell...")
        # First spiral calculation
        theta = np.linspace(0, 2 * np.pi * self.n_turns, self.points)
        r = self.a + self.b * theta
        x, y, z = r * np.cos(theta), r * np.sin(theta), self.c * theta

        # Shell construction
        # Initialize empty lists to hold the x, y, and z coordinates of the shell's surface points.

        self.x_shell, self.y_shell, self.z_shell = [], [], []
            
        # Iterate through each point (xi, yi, zi) that defines the spiral path of the shell.
        for xi, yi, zi in zip(x, y, z):

        # For each point on the spiral, generate a circle perpendicular to the spiral's path.
        # This circle's radius is determined by the shell's thickness parameter.
        # `np.linspace(0, 2 * np.pi, 10)` creates 10 points evenly spaced around the circle.
            for t in np.linspace(0, 2 * np.pi, 10):

                # Calculate the x and y coordinates of each point on the circle using trigonometric functions.
                # The circle's center is offset from the spiral path by the shell's thickness.
                # This effectively "wraps" a circular cross-section around the spiral path, creating the shell's thickness.
                self.x_shell.append(xi + self.thickness * np.cos(t))
                self.y_shell.append(yi + self.thickness * np.sin(t))
                
                # The z coordinate is the same as the current point on the spiral, keeping the circle's plane perpendicular to the spiral's path.
                self.z_shell.append(zi)

        # Inverse shell calculation
        theta_inv = np.linspace(0, 2 * np.pi * self.n_turns_inv, self.points)
        r_inv_start = self.a + self.b * theta[-1]
        r_inv_end = self.a
        r_inv = np.linspace(r_inv_start, r_inv_end, self.points)
        x_inv, y_inv, z_inv = r_inv * np.cos(theta_inv), r_inv * np.sin(theta_inv), self.c * theta_inv + z[-1]

        for xi, yi, zi in zip(x_inv, y_inv, z_inv):
            for t in np.linspace(0, 2 * np.pi, 10):
                self.x_shell.append(xi + self.thickness * np.cos(t))
                self.y_shell.append(yi + self.thickness * np.sin(t))
                self.z_shell.append(zi)


    def plot(self, ax=None):
        """
        Plots the generated points of the Double Seashell using matplotlib on the provided axes.

        Parameters:
        - ax: Optional. A matplotlib 3D axes object where the seashell will be plotted.
             If None, a new figure and 3D axes will be created.
        """
        print("Plotting the seashell...")
        if ax is None:
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
        
        # Plot the generated seashell points on the provided axes
        ax.scatter(self.z_shell, self.x_shell, self.y_shell, color='goldenrod')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title("3D Double Seashell")
        ax.axis('off')  # Optionally turn off the axis if desired

  
        # If ax was provided, plt.show() might be managed outside this method
        if ax is None:
            plt.show()