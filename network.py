#

import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_(x): 
    return x * (1 - x) 

class Network:
    def __init__(self, count_hidden_layers, count_hidden_nodes, count_input_nodes, count_output_nodes):
        self.count_hidden_layers = count_hidden_layers
        self.count_hidden_nodes = count_hidden_nodes
        self.count_input_nodes = count_input_nodes
        self.count_output_nodes = count_output_nodes
        self.all_weights = [None]*(count_hidden_layers + 1)
        self.all_biases = [None]*(count_hidden_layers + 1)

        for level in range(0, count_hidden_nodes + 1):
            nextCount = 0
            previousCount = 0
            self.all_biases[level] = [None]*(nextCount)
            self.all_weights[level] = [None]*(nextCount)

            if(level == count_hidden_nodes):
                nextCount = count_output_nodes
                previousCount = count_hidden_nodes
            elif(level == 0):
                nextCount = count_hidden_nodes
                previousCount = count_input_nodes
            else:
                nextCount = count_hidden_nodes
                previousCount = count_hidden_nodes


            for nodeGroup in range(0, nextCount):
                self.all_weights[level][nodeGroup] = [None]*(previousCount)
                self.all_biases[level][nodeGroup] = random.random * 10

                for x in range(0, previousCount):
                    self.all_weights[level][nodeGroup][x] = random.random()


    def feed_forward(self, input, level = 0):
        if(level == self.count_hidden_layers)
            print(level)
        
        length = self.count_input_nodes if level == 0 else self.count_hidden_nodes
        hidden_layer_nodes = [None]*(self.count_hidden_nodes)
        for x in range(0, self.count_hidden_nodes):
            sum_of_wb = 0
            for i in range(0, length):
                sum_of_wb += (self.all_weights[level][x][i])
            hidden_layer_nodes[x] = sigmoid(sum_of_wb - self.all_biases[level][x])


g = Network(3, 16, 700, 10)
