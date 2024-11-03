import numpy as np

class Madaline:
    def __init__(self, input_size, output_size, learning_rate=0.01):
        self.learning_rate = learning_rate
        # Inicializa os pesos e bias
        self.weights = np.random.rand(output_size, input_size)
        self.bias = np.random.rand(output_size)
    
    def activation(self, x):
        # Função de ativação (limiar)
        return np.where(x >= 0, 1, -1)
    
    def predict(self, inputs):
        # Calcula a saída para cada unidade Adaline
        net_input = np.dot(self.weights, inputs) + self.bias
        output = self.activation(net_input)
        return output
    
    def train(self, training_inputs, labels, epochs=1000):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                output = self.predict(inputs)
                # Atualiza pesos e bias com base no erro
                for i in range(len(label)):
                    error = label[i] - output[i]
                    self.weights[i] += self.learning_rate * error * inputs
                    self.bias[i] += self.learning_rate * error

# Dados de treino binários para as letras
# Cada vetor representa uma letra em binário
# A: [1, -1, -1, -1, 1]
# B: [1, 1, -1, -1, -1]
# C: [-1, -1, 1, -1, -1]
# D: [-1, -1, -1, 1, 1]
# E: [1, -1, 1, 1, -1]
training_data = np.array([
    [1, -1, -1, -1, 1],    # Letra A
    [1, 1, -1, -1, -1],    # Letra B
    [-1, -1, 1, -1, -1],   # Letra C
    [-1, -1, -1, 1, 1],    # Letra D
    [1, -1, 1, 1, -1]      # Letra E
])

# Rótulos para as letras
labels = np.array([
    [1, -1, -1, -1, -1],  # Letra A
    [-1, 1, -1, -1, -1],  # Letra B
    [-1, -1, 1, -1, -1],  # Letra C
    [-1, -1, -1, 1, -1],  # Letra D
    [-1, -1, -1, -1, 1]   # Letra E
])

# Treina o modelo Madaline
madaline = Madaline(input_size=5, output_size=5, learning_rate=0.1)
madaline.train(training_data, labels, epochs=1000)

# Testa o modelo
test_input = np.array([1, -1, -1, -1, 1])
prediction = madaline.predict(test_input)
print("Previsão para o teste:", prediction)
