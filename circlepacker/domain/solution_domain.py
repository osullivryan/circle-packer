from typing import List
from circlepacker.domain.model import Model
import uuid


class SolutionSpace():

    def __init__(self):
        self.models = {}
        self.model_ids = []

    def add_model(self, model: Model) -> None:
        new_id = str(uuid.uuid4)
        self.model_ids.append(new_id)
        self.models[new_id] = model
    
    def get_values(self) -> List[float]:
        return_values = []
        for model_id in self.model_ids:
            for dv in self.models[model_id].design_variables:
                return_values.extend(dv.val)
        return return_values

    