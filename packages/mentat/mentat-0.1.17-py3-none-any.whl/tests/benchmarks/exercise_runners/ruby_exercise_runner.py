import os
import subprocess

from .abstract_exercise_runner import AbstractExerciseRunner


class RubyExerciseRunner(AbstractExerciseRunner):
    def __init__(self, exercise):
        super().__init__(exercise, "rb")

    def run_test(self):
        self._run_test_command(["rake", "test:" + self.exercise])

    def exercise_passed(self):
        try:
            with open(self.test_output_file, "r") as f:
                lines = f.readlines()
                return "0 failures, 0 errors, 0 skips" in lines[-1]
        except FileNotFoundError:
            return False
