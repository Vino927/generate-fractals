# -*- coding: utf-8 -*-
"""
This script generates a 3D conical mollusc shell with tapered ends.

"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random


# =====================
# 3D Double Seashell
# =====================
def generate_double_seashell(a, b, c, n_turns, n_turns_inv, thickness, points=1000):
    """
    Generates points for a 3D double seashell curve.

    Parameters:
    - a, b, c: Shape parameters for the seashell.
    - n_turns: Number of turns for the first shell.
    - n_turns_inv: Number of turns for the inverse shell.
    - thickness: Thickness of the shell.
    - points: Number of points to generate for each curve.
    Returns:
    - x, y, z coordinates of the double shell.
    """
    # First spiral calculation
    theta = np.linspace(0, 2 * np.pi * n_turns, points)
    r = a + b * theta
    x, y, z = r * np.cos(theta), r * np.sin(theta), c * theta

    # Shell construction
    x_shell, y_shell, z_shell = [], [], []
    for xi, yi, zi in zip(x, y, z):
        for t in np.linspace(0, 2 * np.pi, 10):
            x_shell.append(xi + thickness * np.cos(t))
            y_shell.append(yi + thickness * np.sin(t))
            z_shell.append(zi)

    # Inverse shell calculation
    theta_inv = np.linspace(0, 2 * np.pi * n_turns_inv, points)
    r_inv_start = a + b * theta[-1]
    r_inv_end = a
    r_inv = np.linspace(r_inv_start, r_inv_end, points)
    x_inv, y_inv, z_inv = r_inv * np.cos(theta_inv), r_inv * np.sin(theta_inv), c * theta_inv + z[-1]

    for xi, yi, zi in zip(x_inv, y_inv, z_inv):
        for t in np.linspace(0, 2 * np.pi, 10):
            x_shell.append(xi + thickness * np.cos(t))
            y_shell.append(yi + thickness * np.sin(t))
            z_shell.append(zi)

    return x_shell, y_shell, z_shell
