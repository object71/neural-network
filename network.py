#

import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_(x):
    return x * (1 - x)

def cost()

class Network:
    def __init__(self, count_hidden_layers, count_hidden_nodes, count_input_nodes, count_output_nodes):
        self.count_hidden_layers = count_hidden_layers
        self.count_hidden_nodes = count_hidden_nodes
        self.count_input_nodes = count_input_nodes
        self.count_output_nodes = count_output_nodes
        self.layers = list();

        for level in range(0, count_hidden_nodes + 1):
            nextCount = 0
            previousCount = 0

            if(level == count_hidden_nodes):
                nextCount = count_output_nodes
                previousCount = count_hidden_nodes
            elif(level == 0):
                nextCount = count_hidden_nodes
                previousCount = count_input_nodes
            else:
                nextCount = count_hidden_nodes
                previousCount = count_hidden_nodes

            layer {"nodes": list()}

            for nodeGroup in range(0, nextCount):
                node = {"inputWeights": list(), "bias": random.random() * 10 }

                for x in range(0, previousCount):
                    node["inputWeights"].append(random.random())

                layer.append(node)
            self.layers.append(layer)

    def feed_forward(self, input, level = 0):
        count_output_nodes = self.count_hidden_nodes if level != self.count_hidden_layers else self.count_output_nodes
        length = self.count_input_nodes if level == 0 else self.count_hidden_nodes
        output_layer_nodes = [None]*(count_output_nodes)
        for x in range(0, count_output_nodes):
            sum_of_wb = 0
            for i in range(0, length):
                # where input is the activation on the previous layer
                sum_of_wb += (self.all_weights[level][x][i] * input[i])
            output_layer_nodes[x] = sigmoid(sum_of_wb - self.all_biases[level][x])

        if(level == self.count_hidden_layers):
            print(output_layer_nodes)
        else:
            level += 1
            self.feed_forward(output_layer_nodes, level)

    def feed_backward(self, output_layer_nodes, expected_output):

        # sum(weight_i * previous_activation_i) - bias = output_activation
        # cost = ((output_activation - expected_activation) ** 2) / 2

g = Network(3, 3, 2, 1)
g.feed_forward([2,3])
