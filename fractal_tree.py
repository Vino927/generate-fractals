
# =====================
# 3D Fractal Tree
# Draws a 3D fractal tree using recursive algorithm.
# =====================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import rotation_matrix_from_vectors


def draw_fractal_tree_3d(ax, base, length, direction, depth, branch_angle, scale_factor):
    """
    This function generates and plots a 3D fractal tree based on specified parameters,
    including the base position, initial branch length, direction, recursion depth,
    branching angle, and scale factor for subsequent branch lengths. The fractal is
    visualized using matplotlib to create a 3D representation of the tree. 

    Parameters:
    - ax: matplotlib 3D axis object where the tree will be plotted.
    - base: A numpy array specifying the starting point (x, y, z) of the tree's trunk.
    - length: Initial length of the trunk.
    - direction: A numpy array indicating the initial direction vector of the trunk.
    - depth: The recursion depth specifying how many times the branches will split.
    - branch_angle: Angle in radians for the divergence of each branch split.
    - scale_factor: Factor by which the branch length is scaled down each recursion.

    The function does not return any value; it directly modifies the matplotlib 3D axis
    object passed as the parameter with the plotted tree.
    """
    if depth == 0:
        return

    # Calculate end point of the branch
    end = base + length * direction

    # Draw the branch
    ax.plot([base[0], end[0]], [base[1], end[1]], [base[2], end[2]], color='brown', lw=depth)

    # Calculate new directions for branches
    new_directions = [
        np.array([np.sin(branch_angle), 0, np.cos(branch_angle)]),
        np.array([-np.sin(branch_angle), 0, np.cos(branch_angle)]),
        np.array([0, np.sin(branch_angle), np.cos(branch_angle)]),
        np.array([0, -np.sin(branch_angle), np.cos(branch_angle)])
    ]

    # Rotate directions to align with the current branch direction
    rotation_matrix = rotation_matrix_from_vectors(np.array([0, 0, 1]), direction)
    new_directions = [np.dot(rotation_matrix, d) for d in new_directions]

    # Recursively draw branches
    new_length = length * scale_factor
    new_depth = depth - 1
    for new_direction in new_directions:
        draw_fractal_tree_3d(ax, end, new_length, new_direction, new_depth, branch_angle, scale_factor)





   
