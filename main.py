#!/usr/bin/env python3
# main.py
from matplotlib import pyplot as plt
from fractal_fern import FractalFern
from seashell import generate_double_seashell
from fractal_tree import draw_fractal_tree_3d
from utils import rotate_points
import numpy as np

# Usage: After each window pops up, close the window then press Enter in the terminal 
# window to continue with the next plot

def main():
    # Generate and plot a fern with a specific number of points

    plt.figure(figsize=(6, 9))  # Create a new figure for the Barnsley Fern
    fern = FractalFern(100000)
    fern.generate_points()
    fern.plot()

    # Generate 3D Double Seashell
    # Parameters for the shell
    a = 0.1
    b = 0.2
    c = 0.15
    n_turns = 10
    n_turns_inv = 5
    thickness = 0.05
    points = 8000  # Number of points in the spiral

    # Generate double shell curve
    x, y, z = generate_double_seashell(a, b, c, n_turns, n_turns_inv, thickness, points)

    angle_y= np.pi / 2  # 90 degrees rotation around the x-axis
    x_rot, y_rot, z_rot = rotate_points(np.array(x), np.array(y), np.array(z), angle_y=angle_y)

    # Plotting the rotated shell
    print("Plotting seashell...")
    fig = plt.figure(figsize=(8, 6))
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.scatter(x_rot, y_rot, z_rot, color='goldenrod')
    ax1.set_xlabel('X axis')
    ax1.set_ylabel('Y axis')
    ax1.set_zlabel('Z axis')
    plt.axis('off')
   

    # Draw 3D Fractal Tree
    print("Plotting the fractal tree...")
    fig = plt.figure(figsize=(10, 10))
    ax2 = fig.add_subplot(111, projection='3d')
    draw_fractal_tree_3d(ax2, np.array([0, 0, 0]), 1, np.array([.001, .001, 1]), 7, np.pi / 4, 0.5)
    ax2.set_xlim([-1, 1])
    ax2.set_ylim([-1, 1])
    ax2.set_zlim([0, 2])
    ax2.view_init(elev=10, azim=60)
    plt.axis('off')
    plt.show(block=True)
    plt.close('all')  # Close all figures


if __name__ == "__main__":
    main()