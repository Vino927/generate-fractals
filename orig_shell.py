def double_seashell_curve(a, b, c, n_turns, n_turns_inv, thickness, points=1000):
    """
    Generates a 3D double seashell curve, with one spiral on top of the inverse of the other.

    :param a, b, c: Parameters controlling the shape of the shell.
    :param n_turns: Number of turns in the first shell.
    :param n_turns_inv: Number of turns in the second, inverse shell.
    :param thickness: Thickness of the shell.
    :param points: Number of points to generate for each curve.
    :return: x, y, z coordinates of the double shell.
    """
    # Generate theta for the first spiral
    theta = np.linspace(0, 2 * np.pi * n_turns, points)
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = c * theta

    # Create the first spiral
    x_shell, y_shell, z_shell = [], [], []
    for (xi, yi, zi) in zip(x, y, z):
        for t in np.linspace(0, 2 * np.pi, 10):
            x_shell.append(xi + thickness * np.cos(t))
            y_shell.append(yi + thickness * np.sin(t))
            z_shell.append(zi)


    theta_inv = np.linspace(0, 2 * np.pi * n_turns_inv, points)
    r_inv_start = a + b * theta[-1]
    r_inv_end = a
    r_inv = np.linspace(r_inv_start, r_inv_end, points)
    x_inv = r_inv * np.cos(theta_inv)
    y_inv = r_inv * np.sin(theta_inv)
    z_inv = c * theta_inv + z[-1]  # Start from the end of the first spiral
    for (xi, yi, zi) in zip(x_inv, y_inv, z_inv):
        for t in np.linspace(0, 2 * np.pi, 10):
            x_shell.append(xi + thickness * np.cos(t))
            y_shell.append(yi + thickness * np.sin(t))
            z_shell.append(zi)

    return x_shell, y_shell, z_shell


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

# Parameters for the shell
a = 0.1
b = 0.2
c = 0.15
n_turns = 10
n_turns_inv = 5
thickness = 0.05
points = 8000  # Number of points in the spiral

# Generate double shell curve
x, y, z = double_seashell_curve(a, b, c, n_turns, n_turns_inv, thickness, points)


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

