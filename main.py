# main.py
from matplotlib import pyplot as plt
from fractal_fern import generate_fractal_fern
from fractal_seashell import generate_double_seashell
from fractal_tree import draw_fractal_tree_3d
from utils import rotate_points
import numpy as np

# Usage: After each window pops up, close the window then press Enter in the terminal 
# window to continue with the next plot

def main():
    # Generate and plot the Barnsley Fern with a specific number of points
    generate_fractal_fern(100000)


    # Generate 3D Double Seashell
    # Parameters for the shell

    x, y, z = generate_double_seashell(0.1, 0.2, 0.15, 10, 5, 0.05, 8000)

    angle_y= np.pi / 2  # 90 degrees rotation around the x-axis
    x_rot, y_rot, z_rot = rotate_points(np.array(x), np.array(y), np.array(z), angle_y=angle_y)

    # Plotting the rotated shell
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_rot, y_rot, z_rot, color='goldenrod')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
    input("Press Enter to continue...")

    # Draw 3D Fractal Tree
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    draw_fractal_tree_3d(ax, np.array([0, 0, 0]), 1, np.array([.001, .001, 1]), 7, np.pi / 4, 0.5)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([0, 2])
    ax.view_init(elev=10, azim=60)
    plt.show()
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()