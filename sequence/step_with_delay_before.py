from typing import Callable
from sequence.step import Step
from time import sleep, time
from sequence.step import StepExecutionMetadata

class StepWithDelayExecutionMetadata(StepExecutionMetadata):
    execution_time_with_delay: float

    def full_execution_time(self):
        return self.execution_time_with_delay

class StepWithDelayBefore:
    def __init__(self, step: Step, delay_before = 0):
        self.step = step
        self.delay_before = delay_before

    def execute(self, context: dict) -> StepWithDelayExecutionMetadata:
        start_time = time()
        sleep(self.delay_before)
        step_ex_metadata = self.step.execute(context)
        end_time = time()
        return StepWithDelayExecutionMetadata(
            execution_time_with_delay=end_time - start_time,
            execution_time_seconds=step_ex_metadata.execution_time_seconds,
            execution_result=step_ex_metadata.execution_result
        )

