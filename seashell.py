# Copyright (C) [2024] [Vino Gupta]
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
# If you modify this Program, or any covered work, by linking or combining it with [name of library] (or a modified version of that library), containing parts covered by the terms of [name of library's license], the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of [name of library] used as well as that of the covered work.}


# =====================
# 3D Double Seashell
# This script generates a 3D conical mollusc shell with tapered ends.
# =====================


import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

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
