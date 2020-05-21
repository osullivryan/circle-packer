from circlepacker.domain.variables import Bounds, DesignVariable
from circlepacker.domain.solution_domain import SolutionSpace
from circlepacker.domain.circle import Circle


def create_circles(n):
    solution_space = SolutionSpace()
    bounds = Bounds(-10, 10)
    for _ in range(n):
        x = DesignVariable('x', bounds=bounds)
        y = DesignVariable('y', bounds=bounds)
        cirlce = Circle(x, y, 1.0)

        solution_space.add_model(cirlce)

    return solution_space



if __name__ == '__main__':
    n = 5
    dvs = create_circles(5)
