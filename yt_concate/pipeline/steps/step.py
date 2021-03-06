from abc import ABC, abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self):
        pass


class StepException(Exception):
    pass
