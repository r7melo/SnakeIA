import pickle
from entities import Neuron, NeuronType

"""

[L ->    Cx ->
[R ->            D]
[U ->            L]
[D ->    Cy ->

"""

class Brain:
    def __init__(self) -> None:
        self.motion_neurons:list[Neuron]
        self.position_neurons:list[Neuron]
        self.survival_neurons:list[Neuron]

        self.survival_neurons = [
            Neuron(NeuronType.LIFE, 0, None),
            Neuron(NeuronType.DEAD, 0, None)
        ]

        self.position_neurons = [
            Neuron(NeuronType.X, 0, self.survival_neurons),
            Neuron(NeuronType.Y, 0, self.survival_neurons)
        ]

        self.motion_neurons = [
            Neuron(NeuronType.LEFT, 0, self.position_neurons),
            Neuron(NeuronType.RIGHT, 0, self.position_neurons),
            Neuron(NeuronType.UP, 0, self.position_neurons),
            Neuron(NeuronType.DOWN, 0, self.position_neurons)
        ]

    def activate_neuron(self, motion:Neuron, position:Neuron, survival:Neuron):
        for motion_neuron in self.motion_neurons:
            if motion_neuron.type == motion.type:
                motion_neuron.value += motion.value
                
                for position_neuron in motion_neuron.next_neuron:
                    if position_neuron.type == position.type:
                        position_neuron.value += position.value

                        for survival_neuron in position_neuron.next_neuron:
                            if survival_neuron.type == survival.type:
                                survival_neuron.value += survival.value
                
    def to_memorize(self):
        with open('brain_memories/motion_neurons.pkl', 'wb') as brain_memories:
            pickle.dump(self.motion_neurons, brain_memories)
        with open('brain_memories/position_neurons.pkl', 'wb') as position_neurons:
            pickle.dump(self.motion_neurons, position_neurons)
        with open('brain_memories/motion_neurons.pkl', 'wb') as survival_neurons:
            pickle.dump(self.motion_neurons, survival_neurons)

    def to_remember(self):
        with open('brain_memories/motion_neurons.pkl', 'rb') as brain_memories:
            self.motion_neurons = pickle.load(brain_memories)
        with open('brain_memories/position_neurons.pkl', 'rb') as position_neurons:
            self.position_neurons = pickle.load(position_neurons)
        with open('brain_memories/motion_neurons.pkl', 'rb') as survival_neurons:
            self.survival_neurons = pickle.load(survival_neurons)

    def show_network(self):
        for motion in self.motion_neurons:
            print("[{0}:{1}]".format(motion.type, motion.value))

            for position in motion.next_neuron:
                print("\t[{0}:{1}]".format(position.type, position.value))

                for survival in position.next_neuron:
                    print("\t\t[{0}:{1}]".format(survival.type, survival.value))
        

        