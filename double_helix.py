import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interact, FloatSlider, IntSlider


def create_helix_points(radius, pitch, num_turns, points_per_turn, phase_shift=0):
    """
    Generate points for a single helix strand.

    Parameters:
    - radius: Radius of the helix
    - pitch: Distance between consecutive turns
    - num_turns: Number of complete turns
    - points_per_turn: Number of points to plot per turn
    - phase_shift: Phase shift for the second strand (default: 0)

    Returns:
    - x, y, z coordinates for the helix points
    """
    t = np.linspace(0, 2 * np.pi * num_turns, points_per_turn * num_turns)
    x = radius * np.cos(t + phase_shift)
    y = radius * np.sin(t + phase_shift)
    z = (pitch * t) / (2 * np.pi)
    return x, y, z


def create_base_pairs(x1, y1, z1, x2, y2, z2, num_pairs):
    """
    Generate base pairs connecting the two strands.

    Parameters:
    - x1, y1, z1: Coordinates of first strand
    - x2, y2, z2: Coordinates of second strand
    - num_pairs: Number of base pairs to create

    Returns:
    - Lists of x, y, z coordinates for base pair lines
    """
    # Select evenly spaced points for base pairs
    indices = np.linspace(0, len(x1) - 1, num_pairs, dtype=int)

    # Create arrays for base pair coordinates
    base_x = np.zeros((num_pairs, 2))
    base_y = np.zeros((num_pairs, 2))
    base_z = np.zeros((num_pairs, 2))

    for i, idx in enumerate(indices):
        base_x[i] = [x1[idx], x2[idx]]
        base_y[i] = [y1[idx], y2[idx]]
        base_z[i] = [z1[idx], z2[idx]]

    return base_x, base_y, base_z


def plot_double_helix(
    radius=1.0, pitch=3.4, num_turns=10, points_per_turn=100, num_base_pairs=20
):
    """
    Create and display a 3D double helix visualization with interactive controls.

    Parameters:
    - radius: Radius of the helix
    - pitch: Distance between consecutive turns
    - num_turns: Number of complete turns
    - points_per_turn: Number of points to plot per turn
    - num_base_pairs: Number of base pairs to display
    """
    # Clear any existing plots
    plt.clf()

    # Create figure and 3D axes
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Generate points for both strands
    x1, y1, z1 = create_helix_points(radius, pitch, num_turns, points_per_turn)
    x2, y2, z2 = create_helix_points(
        radius, pitch, num_turns, points_per_turn, phase_shift=np.pi
    )

    # Generate base pairs
    base_x, base_y, base_z = create_base_pairs(x1, y1, z1, x2, y2, z2, num_base_pairs)

    # Plot both strands
    ax.plot(x1, y1, z1, color="blue", linewidth=2, label="Strand 1")
    ax.plot(x2, y2, z2, color="red", linewidth=2, label="Strand 2")

    # Plot base pairs
    for i in range(num_base_pairs):
        ax.plot(base_x[i], base_y[i], base_z[i], color="green", linewidth=1, alpha=0.5)

    # Customize the plot
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Double Helix Structure")

    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])

    # Add legend
    ax.legend(["Strand 1", "Strand 2", "Base Pairs"])

    # Set viewing angle for better visualization
    ax.view_init(elev=20, azim=45)

    # Add grid
    ax.grid(True)

    # Set axis limits
    max_range = max(radius * 1.5, pitch * num_turns / 2)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(0, pitch * num_turns)

    plt.show()


def interactive_helix():
    """
    Create an interactive visualization with sliders for all parameters.
    """
    interact(
        plot_double_helix,
        radius=FloatSlider(
            min=0.5, max=3.0, step=0.1, value=1.0, description="Radius:"
        ),
        pitch=FloatSlider(min=1.0, max=5.0, step=0.1, value=3.4, description="Pitch:"),
        num_turns=IntSlider(min=1, max=20, step=1, value=10, description="Turns:"),
        points_per_turn=IntSlider(
            min=50, max=200, step=10, value=100, description="Points/Turn:"
        ),
        num_base_pairs=IntSlider(
            min=5, max=50, step=5, value=20, description="Base Pairs:"
        ),
    )


if __name__ == "__main__":
    # Create the interactive visualization
    interactive_helix()
