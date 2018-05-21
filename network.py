#

import random

class Network:
    def __init__(self, count_hidden_layers, count_hidden_nodes, count_input_nodes, count_output_nodes):
        self.count_hidden_layers = count_hidden_layers
        self.count_hidden_nodes = count_hidden_nodes
        self.count_input_nodes = count_input_nodes
        self.count_output_nodes = count_output_nodes
        self.all_weights = [None]*(count_hidden_nodes + 1)

        for level in range(0, count_hidden_nodes + 1):
            nextCount = 0;
            previousCount = 0;


            if(level == count_hidden_nodes):
                nextCount = count_output_nodes
                previousCount = count_hidden_nodes
            elif(level == 0):
                nextCount = count_hidden_nodes
                previousCount = count_input_nodes
            else:
                nextCount = count_hidden_nodes
                previousCount = count_hidden_nodes

            self.all_weights[level] = [None]*(nextCount)
            for nodeWieghtsGroup in range(0, nextCount):
                self.all_weights[level][nodeWieghtsGroup] = [None]*(previousCount)
                for weightNumber in range(0, previousCount):
                    self.all_weights[level][nodeWieghtsGroup][weightNumber] = random.random()


        print(self.all_weights)

g = Network(3, 16, 700, 10)
