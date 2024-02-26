#!/usr/bin/env python3
# fractal_tree.py

# Copyright (C) [2024] [Vino Gupta]
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
# If you modify this Program, or any covered work, by linking or combining it with generate_fractals (or a modified version of that library), containing parts covered by the terms of GPL v3.0, the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of generate_fractals used as well as that of the covered work.}

# =====================
# 3D Fractal Tree
# Draws a 3D fractal tree using recursive algorithm.
# =====================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import rotation_matrix_from_vectors

class FractalTree3D:
    def __init__(self, base, length, direction, depth, branch_angle, scale_factor):

               # Type checking
        if not isinstance(base, np.ndarray) or not isinstance(direction, np.ndarray):
            raise TypeError("Base and direction must be numpy arrays")
        if not all(isinstance(x, (int, float)) for x in [length, branch_angle, scale_factor]):
            raise TypeError("Length, branch_angle, and scale_factor must be numbers")
        if not isinstance(depth, int):
            raise TypeError("Depth must be an integer")
        
        # Value checking
        if length <= 0:
            raise ValueError("Length must be positive")
        if scale_factor <= 0:
            raise ValueError("Scale factor must be positive")
        if depth < 0:
            raise ValueError("Depth cannot be negative")
        if not (0 <= branch_angle <= 2 * np.pi):
            raise ValueError("Branch angle must be between 0 and 2π radians")

        self.base = base
        self.length = length
        self.direction = direction
        self.depth = depth
        self.branch_angle = branch_angle
        self.scale_factor = scale_factor
        self.branches = []  # List to store branch information

    def generate_points(self):
        """
        Generates the fractal tree structure and stores each branch in self.branches.
        """
        print("Generating the fractal tree...")
        self._generate_recursive(self.base, self.length, self.direction, self.depth)

    def _generate_recursive(self, base, length, direction, depth):
        if depth == 0:
            return

        end = base + length * direction
        self.branches.append((base, end))  # Store the branch's start and end points

        # Calculate the rotation matrix to align the new branches with the current branch's direction.
        # This matrix rotates the standard up direction (0, 0, 1) to the current branch's direction vector.
        rotation_matrix = rotation_matrix_from_vectors(np.array([0, 0, 1]), direction)
        
        
        # Generate new direction vectors for the branches at the current node.
        # Four new directions are calculated using the branch angle to spread the branches outwards.
        # Each direction is rotated to align with the end of the current branch using the rotation matrix.
        # - The first and second directions are opposites in the plane perpendicular to the up direction,
        #   creating a bifurcation that spreads horizontally.
        # - The third and fourth directions add vertical bifurcation by adjusting the branch angle
        #   upwards and downwards respectively.

        new_directions = [
            np.dot(rotation_matrix, np.array([np.sin(self.branch_angle), 0, np.cos(self.branch_angle)])),
            np.dot(rotation_matrix, np.array([-np.sin(self.branch_angle), 0, np.cos(self.branch_angle)])),
            np.dot(rotation_matrix, np.array([0, np.sin(self.branch_angle), np.cos(self.branch_angle)])),
            np.dot(rotation_matrix, np.array([0, -np.sin(self.branch_angle), np.cos(self.branch_angle)]))
        ]

        # Recursively generate branches for each new direction.
        # The recursive call generates further branches from the end of the current branch,
        # scaling the length of each subsequent branch by the scale factor to create the fractal pattern.
        # This process repeats until the specified recursion depth is reached.

        for new_direction in new_directions:
            self._generate_recursive(end, length * self.scale_factor, new_direction, depth - 1)

    def plot(self, ax=None, set_limits=True, view_init_elev=10, view_init_azim=60):
        """
        Draws the generated fractal tree structure on a matplotlib 3D axis.
        """
        print("Plotting the fractal tree...")
        if ax is None:
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(111, projection='3d')

        for base, end in self.branches:
            ax.plot([base[0], end[0]], [base[1], end[1]], [base[2], end[2]], color='brown', lw=self.depth)

        # if set_limits:
        #     ax.set_xlim([-1, 1])
        #     ax.set_ylim([-1, 1])
        #     ax.set_zlim([0, 2])

        ax.view_init(elev=view_init_elev, azim=view_init_azim)
        plt.axis('off')  

