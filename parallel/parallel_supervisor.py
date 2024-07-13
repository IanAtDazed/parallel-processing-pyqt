"""Module containing the parallel processing code.

- Here, we are using [Ray](https://www.ray.io/)
- This could be Python [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ray.util.queue import Queue
    from typing import NamedTuple

import ray

from helpers.process_instructions import QuitProcessing
from parallel.data_generator import DataGenerator


@ray.remote
class ParallelSupervisor:
    """Class to run the parallel processing."""

    def __init__(self, instruction_queue: Queue, result_queue: Queue) -> None:
        """Initialize the class."""

        self._instruction_queue = instruction_queue
        self._result_queue = result_queue
        self._data_generator = DataGenerator.remote()
        self._is_running = False

    def start(self) -> None:
        """Create data."""

        self._is_running = True

        while self._is_running:
            self._process_latest_instructions()
            self._process_data()

    def _process_latest_instructions(self) -> None:
        """Process any latest instructions."""

        while not self._instruction_queue.empty():
            self._process_instruction(
                self._instruction_queue.get())

    def _process_instruction(self, instruction: NamedTuple) -> None:
        """Process an instruction.

        Args:
            instruction (any): The instruction to process.
        
        **Note:**
        - This allows for more instruction to easily be added.
        - The additonal instructions can contain fields with additional arguments.
        """

        INSTRUCTIONS = {
            QuitProcessing: self._quit
        }

        INSTRUCTIONS[type(instruction)](instruction)
    
    def _quit(self, *args) -> None:
        """Quit processing."""

        self._is_running = False

    def _process_data(self) -> None:
        """Get the latest data and put it on the queue."""

        result = ray.get(self._data_generator.get_latest_data.remote())

        # In the console, this shows it is running on a
        # separate process to the GUI.
        print(result)
        
        self._result_queue.put(result)
