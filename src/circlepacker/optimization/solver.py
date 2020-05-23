import scipy
from typing import List, Any
from scipy.optimize import Bounds
import numpy as np
import matplotlib.pyplot as plt


def overlapping_area(xy_array, radii):
    dist = scipy.spatial.distance.cdist(xy_array, xy_array)
    r1 = np.repeat(radii[:, np.newaxis], len(radii), axis=1)
    r2 = r1.T
    r_scale = r1 + r2
    d1 = (np.power(r1, 2.0) - np.power(r2, 2.0) + np.power(dist, 2.0)) / (2.0 * dist)
    d2 = dist - d1

    overlap_map = dist <= r1 - r2
    non_diag = ~np.eye(overlap_map.shape[0], dtype=bool)
    scaling_map = np.logical_and(overlap_map, non_diag)

    a_p1 = np.power(r1, 2.0) * np.arccos(d1 / r1)
    a_p2 = -1.0 * d1 * np.sqrt(np.power(r1, 2.0) - np.power(d1, 2.0))
    a_p3 = np.power(r2, 2.0) * np.arccos(d2 / r2)
    a_p4 = -1.0 * d2 * np.sqrt(np.power(r2, 2.0) - np.power(d2, 2.0))
    total_area = np.nan_to_num(a_p1 + a_p2 + a_p3 + a_p4)
    total_area[scaling_map] += r_scale[scaling_map]
    return total_area


def max_distance(xy_array, radii):
    return np.nanmax(scipy.spatial.distance.cdist(xy_array, np.zeros_like(xy_array)))


def cost(xy_pairs, *args) -> float:
    xy_array = np.reshape(xy_pairs, (-1, 2))
    radii = np.array([args]).flatten()
    if np.any(radii <= 0):
        raise AssertionError(f"One of your radii is less than zero: {radii}")

    def final_cost():
        return np.max(overlapping_area(xy_array, radii)) + np.max(
            max_distance(xy_array, radii)
        )

    return final_cost()


if __name__ == "__main__":
    points = [0.0, 0.0, 0.0, 0.0]
    radii = [10.0, 10.0]
    value_to_min = cost(points, radii)
    print(value_to_min)

    n = 5
    bounds_of_points = []
    radii = []
    for _ in range(n * 2):
        bounds_of_points.append((-20.0, 20.0))
    for _ in range(n):
        radii.append(np.random.triangular(0.5, 1.0, 2.5))
    res = scipy.optimize.differential_evolution(cost, bounds_of_points, args=(*radii,))
    xy_points = np.reshape(res.x, (n, -1))
    overlap = overlapping_area(xy_points, np.array([radii]).flatten())
    fig, ax = plt.subplots()
    for i, point in enumerate(xy_points):
        ax.add_artist(plt.Circle((point[0], point[1]), radii[i], color="r", fill=False))
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))
    fig.savefig("plotcircles.svg")

    print(res.x)
