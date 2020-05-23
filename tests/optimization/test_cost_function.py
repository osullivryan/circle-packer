import pytest
import numpy as np
from circlepacker.optimization.solver import cost, max_distance, overlapping_area


@pytest.fixture()
def two_overlapping_circles():
    xy_array = np.reshape([-5.0, 0.0, 5.0, 0.0], (-1, 2))
    radii = np.array([10.0, 10.0]).flatten()
    return xy_array, radii


@pytest.fixture()
def two_overlapping_circles_cost_input():
    xy_array = [-5.0, 0.0, 5.0, 0.0]
    radii = (10.0, 10.0)
    return xy_array, radii


def test_two_circles_overlap(two_overlapping_circles):
    xy, radii = two_overlapping_circles
    area = overlapping_area(xy, radii)

    assert np.max(area) == pytest.approx(122.8, 0.1)
    assert np.min(area) == pytest.approx(0.0, 0.1)


def test_two_circles_max_distance(two_overlapping_circles):
    xy, radii = two_overlapping_circles
    distance = max_distance(xy, radii)

    assert distance == pytest.approx(5.0)


def test_two_circles_cost(two_overlapping_circles_cost_input):
    xy, radii = two_overlapping_circles_cost_input
    function_cost = cost(xy, radii)

    assert function_cost == pytest.approx(122.8 + 5.0, 0.01)


def test_negative_radii_fail():
    xy = [-5.0, 0.0, 5.0, 0.0]
    radii = (-10.0, 10.0)

    with pytest.raises(AssertionError):
        cost(xy, radii)
