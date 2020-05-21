from circlepacker.domain.solution_domain import DesignVariable
from typing import List


class Model():
    def __init__(self):
        pass

    @property
    def design_variables(self) -> List[DesignVariable]:
        raise NotImplementedError()

    def _set_design_variables(self, new_variable_values: Dict[str, float]) -> None:
        for dv in self.get_design_variables():
            dv.val = new_variable_values[dv.attribute_name]

    def set_design_variables(self, new_variable_values: Dict[str, float]) -> None:
        raise NotImplementedError()
    