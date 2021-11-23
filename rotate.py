"""
rotate.py - Provide rotation matrixes
Written by Shahim Vedaei
"""

def rotate(coords, yaw, pitch, roll):
    """
    rotate agains cartesian axes
    :param coords: coordinate of the point
    :param yaw: rotation around x axis
    :param pitch: rotation around y axis
    :param roll: rotation around z axis
    :return: coordinates of rotated point
    """
    # degree to radian
    yaw = yaw * np.pi / 180
    pitch = pitch * np.pi / 180
    roll = roll * np.pi / 180
    # compute rotation matrix
    rot_x_matrix = np.array([[1, 0, 0],
                             [0, np.cos(yaw), -1 * np.sin(yaw)],
                             [0, np.sin(yaw), np.cos(yaw)]])
    rot_y_matrix = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                             [0, 1, 0],
                             [-1 * np.sin(pitch), 0, np.cos(pitch)]])
    rot_z_matrix = np.array([[np.cos(roll), -1 * np.sin(roll), 0],
                             [np.sin(roll), np.cos(roll), 0],
                             [0, 0, 1]])
    rot_matrix = rot_x_matrix @ rot_y_matrix @ rot_z_matrix
    rot_coords = coords @ rot_matrix
    return rot_coords
