from neuron import Neuron

class Synapse:
    def __init__(self):
        self.neurons= [Neuron() for i in range(0,100)]

