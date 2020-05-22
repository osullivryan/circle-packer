import uuid
from typing import Dict


class Bounds:
    def __init__(self, lower: float, upper: float) -> None:
        self.lower = lower
        self.upper = upper


class DesignVariable:
    def __init__(
        self, attribute_name: str, bounds: Bounds, initial_condition: float = None
    ):
        self.attribute_name = attribute_name
        self.bounds = bounds
        self.initial_condition = initial_condition
        self.val = None

    def update(self, val: float) -> None:
        self.val = val


class DesignVariables:
    def __init__(self):
        self.design_variables = {}
        self.attribute_ids = []

    def add_design_variable(self, design_variable: DesignVariable) -> None:
        new_id = str(uuid.uuid4)
        self.attribute_ids.append(new_id)
        self.design_variables[str(uuid.uuid4)] = design_variable

    def get_values(self):
        return [dv.val for dv in self.design_variables]

    def set_values(self, values: Dict[str, float]) -> None:
        for attribute_id, value in values.items():
            self.design_variables[attribute_id] = value
