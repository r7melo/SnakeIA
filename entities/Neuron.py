from enum import Enum

class NeuronType(Enum):
    LEFT = 0,
    RIGHT = 1,
    UP = 2,
    DOWN = 3,
    X = 4,
    Y = 5,
    DEAD = 6,
    LIFE = 7

class Neuron:
    def __init__(self, type, value, nextn=None) -> None:
        self.type: NeuronType = type
        self.value: int = value
        self.next_neuron: Neuron = nextn