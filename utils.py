# Copyright (C) [2024] [Vino Gupta]
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
# If you modify this Program, or any covered work, by linking or combining it with [name of library] (or a modified version of that library), containing parts covered by the terms of [name of library's license], the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of [name of library] used as well as that of the covered work.}

# utils.py
import numpy as np

# Define rotation function
def rotate_points(x, y, z, angle_x=0, angle_y=0, angle_z=0):
    """
    Rotate points in 3D space.

    :param x, y, z: Coordinates of the points.
    :param angle_x, angle_y, angle_z: Rotation angles around each axis (in radians).
    :return: Rotated coordinates.
    """
    # Rotation matrices
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(angle_x), -np.sin(angle_x)],
                   [0, np.sin(angle_x), np.cos(angle_x)]])

    Ry = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                   [0, 1, 0],
                   [-np.sin(angle_y), 0, np.cos(angle_y)]])

    Rz = np.array([[np.cos(angle_z), -np.sin(angle_z), 0],
                   [np.sin(angle_z), np.cos(angle_z), 0],
                   [0, 0, 1]])

    # Combine rotations
    R = np.dot(Rz, np.dot(Ry, Rx))

    # Apply rotation to points
    rotated_points = np.dot(R, np.array([x, y, z]))
    return rotated_points[0], rotated_points[1], rotated_points[2]


def rotation_matrix_from_vectors(vec1, vec2):
    """
    Calculates the rotation matrix required to rotate vec1 to align with vec2.

    Parameters:
    - vec1: Initial vector.
    - vec2: Target vector.
    Returns:
    - The rotation matrix.
    """
    a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (vec2 / np.linalg.norm(vec2)).reshape(3)
    v = np.cross(a, b)
    c = np.dot(a, b)
    s = np.linalg.norm(v)
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
    return rotation_matrix
