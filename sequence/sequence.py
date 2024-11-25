from sequence.step import Step
from sequence.step import StepExecutionMetadata

from typing import List
from pydantic import BaseModel
import time

class SequenceExecutionMetadata(BaseModel):
    final_context: dict
    step_execution_metadatas: List[StepExecutionMetadata]

    def execution_time(self):
        return sum([step_execution_metadata.execution_time_seconds for step_execution_metadata in self.step_execution_metadatas])

    def full_execution_time(self):
        return sum([step_execution_metadata.full_execution_time() for step_execution_metadata in self.step_execution_metadatas])

class Sequence:

    def __init__(
        self, 
        steps: list[Step], 
        initial_context: dict):
        self.steps = steps
        self.initial_context = initial_context

    def execute(self) -> SequenceExecutionMetadata:
        context = self.initial_context
        step_execution_metadatas = []
        for step in self.steps:
            step_execution_metadata = step.execute(context)
            context.update(step_execution_metadata.execution_result)
            step_execution_metadatas.append(step_execution_metadata)

        return SequenceExecutionMetadata(
            final_context = context,
            step_execution_metadatas = step_execution_metadatas
        )
