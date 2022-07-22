from entities import Brain
from entities.Neuron import Neuron, NeuronType


b = Brain()


b.to_remember()


b.activate_neuron(Neuron(NeuronType.LEFT, 1), Neuron(NeuronType.X, 1), Neuron(NeuronType.LIFE, 1))


b.to_memorize()

print(b.motion_neurons[0].value)
print(b.position_neurons[0].value)
print(b.survival_neurons[0].value)


