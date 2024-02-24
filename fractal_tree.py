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
        """
        Initialize a FractalTree3D object with all necessary parameters for tree generation.

        Parameters:
        - base: A numpy array specifying the starting point (x, y, z) of the tree's trunk.
        - length: Initial length of the trunk.
        - direction: A numpy array indicating the initial direction vector of the trunk.
        - depth: The recursion depth specifying how many times the branches will split.
        - branch_angle: Angle in radians for the divergence of each branch split.
        - scale_factor: Factor by which the branch length is scaled down each recursion.
        """
        print("Generating the fractal tree...")
        self.base = base
        self.length = length
        self.direction = direction
        self.depth = depth
        self.branch_angle = branch_angle
        self.scale_factor = scale_factor

    def draw(self, ax=None, set_limits=True, view_init_elev=10, view_init_azim=60):
        """
        Draws the fractal tree on a matplotlib 3D axis.

        Parameters:
        - ax: Optional matplotlib 3D axis object. If not provided, one will be created.
        - set_limits: A boolean to decide if axis limits should be set.
        - view_init_elev: Elevation angle in the z plane for the initial view.
        - view_init_azim: Azimuth angle in the x,y plane for the initial view.
        """
        print("Plotting the fractal tree...")
        if ax is None:
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(111, projection='3d')

        self._draw_recursive(ax, self.base, self.length, self.direction, self.depth)

        if set_limits:
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            ax.set_zlim([0, 2])

        ax.view_init(elev=view_init_elev, azim=view_init_azim)
        plt.axis('off')  # Optionally turn off the axis
        plt.show()

    def _draw_recursive(self, ax, base, length, direction, depth):
        if depth == 0:
            return

        end = base + length * direction
        ax.plot([base[0], end[0]], [base[1], end[1]], [base[2], end[2]], color='brown', lw=depth)

        rotation_matrix = rotation_matrix_from_vectors(np.array([0, 0, 1]), direction)
        new_directions = [
            np.dot(rotation_matrix, np.array([np.sin(self.branch_angle), 0, np.cos(self.branch_angle)])),
            np.dot(rotation_matrix, np.array([-np.sin(self.branch_angle), 0, np.cos(self.branch_angle)])),
            np.dot(rotation_matrix, np.array([0, np.sin(self.branch_angle), np.cos(self.branch_angle)])),
            np.dot(rotation_matrix, np.array([0, -np.sin(self.branch_angle), np.cos(self.branch_angle)]))
        ]

        for new_direction in new_directions:
            self._draw_recursive(ax, end, length * self.scale_factor, new_direction, depth - 1)

