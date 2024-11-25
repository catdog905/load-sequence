from typing import Callable
from pydantic import BaseModel

from typing import Any
from time import time


class StepExecutionMetadata(BaseModel):
    execution_time_seconds: float
    execution_result: dict

    def full_execution_time(self):
        return self.execution_time_seconds

class Step:
    def __init__(self, command: Callable, args: dict = {}):
        self.command = command
        self.args = args

    def execute(self, context: dict) -> StepExecutionMetadata:
        all_args = {}
        all_args.update(context)
        all_args.update(self.args)

        start_time = time()
        result = self.command(**all_args).call()
        end_time = time()
        return StepExecutionMetadata(
            execution_time_seconds=end_time - start_time, 
            execution_result=result
        )

