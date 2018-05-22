#

import random
import math

def sigmoid(x):
    return (1 / (1 + math.exp(-x)))

def sigmoid_prime(x):
    return (x * (1 - x))

class Node:
    def __init__(self, input_node_count, output_node_count):
        self.input_weights = list()
        self.input_values = list()
        self.weight_modifications = list()
        self.bias_modification = 0
        self.bias = random.random()
        self.input_node_count = input_node_count
        self.output_node_count = output_node_count
        self.active_value = 0

    def calculate(self, input):
        self.input_values = list(input)
        sum_of_wb = 0
        for x in range(0, self.input_node_count):
            # where input is the activation on the previous layer
            sum_of_wb += (self.input_weights[x] * input[x])
        self.active_value = sigmoid(sum_of_wb + self.bias)
        return self.active_value






class Network:
    def __init__(self, count_hidden_layers, count_hidden_nodes, count_input_nodes, count_output_nodes):
        self.count_hidden_layers = count_hidden_layers
        self.count_hidden_nodes = count_hidden_nodes
        self.count_input_nodes = count_input_nodes
        self.count_output_nodes = count_output_nodes
        self.layers = list()

        for level in range(0, count_hidden_layers + 1):
            nextCount = 0
            previousCount = 0

            if(level == count_hidden_layers):
                nextCount = count_output_nodes
                previousCount = count_hidden_nodes
            elif(level == 0):
                nextCount = count_hidden_nodes
                previousCount = count_input_nodes
            else:
                nextCount = count_hidden_nodes
                previousCount = count_hidden_nodes

            layer = list()

            for a in range(0, nextCount):
                node = Node(previousCount, nextCount)

                for b in range(0, previousCount):
                    node.input_weights.append(random.random() / 2)
                    node.weight_modifications.append(0)

                layer.append(node)
            self.layers.append(layer)

    def feed_forward(self, input, expected = None, level = 0):
        #count_output_nodes = self.count_hidden_nodes if level != self.count_hidden_layers else self.count_output_nodes
        #length = self.count_input_nodes if level == 0 else self.count_hidden_nodes
        
        output = list()
        count_of_nodes = len(self.layers[level])
        for i in range(0, count_of_nodes):
            output.append(self.layers[level][i].calculate(input))
        
        if(level == (self.count_hidden_layers)):
            if(expected != None):
                self.feed_backward(expected, level)
            else:
                print(output)
        else:
            level += 1
            self.feed_forward(output, expected, level)

    def feed_backward(self, expected_output, level):
        
        current_layer_node_count = len(self.layers[level])
        next_propagation_values = list()
        error = 0
        for i in range(0, current_layer_node_count):
            node = self.layers[level][i]
            if(level == (self.count_hidden_layers)):
                error = -(expected_output[i] - node.active_value)
            else:
                for o in range(0, len(self.layers[level + 1])):
                    error += expected_output[o][i] * self.layers[level + 1][o].input_weights[i]
            input_weights_count = len(node.input_weights)
            
            error_values = list()
            for x in range(0, input_weights_count):
                a_prev = node.input_values[x]
                sigm = sigmoid_prime(node.active_value)
                weight_error = error * sigm * a_prev
                error_values.append(error * sigm)
                node.weight_modifications[x] = (node.weight_modifications[x] + weight_error) / 2
                node.bias_modification = error * sigm
            next_propagation_values.append(error_values)
        
        if(level != 0):
            level = level - 1
            self.feed_backward(next_propagation_values, level)

    def update(self):
        for level in range(0, self.count_hidden_layers + 1):
            for n in range(0, len(self.layers[level])):
                for x in range(0, len(self.layers[level][n].input_weights)):
                    self.layers[level][n].input_weights[x] = self.layers[level][n].input_weights[x] - self.layers[level][n].weight_modifications[x]
                    self.layers[level][n].weight_modifications[x] = 0
                self.layers[level][n].bias = self.layers[level][n].bias - self.layers[level][n].bias_modification
                self.layers[level][n].bias_modification = 0

def func(x, y):
    return x or y

if __name__ == "__main__":
    net = Network(2, 5, 2, 1)
    i = 0
    while(i < 30000):
        a = random.randint(0,1)
        b = random.randint(0,1)
        c = random.randint(0,1)
        net.feed_forward([a,b], [func(a, b)])
        net.feed_forward([b,c], [func(b, c)])
        net.feed_forward([a,c], [func(a, c)])
        i += 1
        net.update()

    net.feed_forward([0,0])
    net.feed_forward([1,0])
    net.feed_forward([0,1])
    net.feed_forward([1,1])


