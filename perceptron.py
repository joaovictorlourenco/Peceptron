import tkinter as tk

# Definindo o tamanho da matriz 10x10
size = 10
learning_rate = 0.1  # Taxa de aprendizagem do Perceptron

# Inicializa a matriz 10x10
def inicializar_matriz():
    return [[0 for _ in range(size)] for _ in range(size)]

# Inicializa a matriz 10x10 com a letra A
def inicializar_letra_A():
    matriz = inicializar_matriz()
    matriz[0] = [-1, -1, -1, 1, 1, 1, 1, -1, -1, -1]
    matriz[1] = [-1, -1, -1, 1, 1, 1, 1, -1, -1, -1]
    matriz[2] = [-1, -1, -1, 1, -1, -1, 1, -1, -1, -1]
    matriz[3] = [-1, -1, -1, 1, -1, -1, 1, -1, -1, -1]
    matriz[4] = [-1, -1, -1, 1, -1, -1, 1, -1, -1, -1]
    matriz[5] = [-1, -1, -1, 1, 1, 1, 1, -1, -1, -1]
    matriz[6] = [-1, -1, 1, -1, -1, -1, -1, 1, -1, -1]
    matriz[7] = [-1, 1, -1, -1, -1, -1, -1, -1, 1, -1]
    matriz[8] = [1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
    matriz[9] = [1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
    return matriz

# Inicializa a matriz 10x10 com a letra B
def inicializar_letra_B():
    matriz = inicializar_matriz()
    matriz[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
    matriz[1] = [1, 1, -1, -1, -1, -1, -1, -1, -1, 1]
    matriz[2] = [1, 1, -1, -1, -1, -1, -1, -1, -1, 1]
    matriz[3] = [1, 1, -1, -1, -1, -1, -1, -1, 1, -1]
    matriz[4] = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]
    matriz[5] = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1]
    matriz[6] = [1, 1, -1, -1, -1, -1, -1, -1, 1, -1]
    matriz[7] = [1, 1, -1, -1, -1, -1, -1, -1, -1, 1]
    matriz[8] = [1, 1, -1, -1, -1, -1, -1, -1, -1, 1]
    matriz[9] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return matriz

# Treina o modelo usando o Perceptron
def treinar_perceptron(entrada, y, w, b):
    print(f'Entrada = {entrada}')
    # Itera sobre cada célula da matriz
    for i in range(size):
        for j in range(size):
            # Calcula a soma ponderada dos inputs
            soma_ponderada = sum(w[i][j] * entrada[i][j] for i in range(size) for j in range(size)) + b
            
            # Aplica a função de ativação
            previsao = 1 if soma_ponderada > 0 else -1
            
            # Calcula o erro (delta)
            delta = y - previsao
            
            # Atualiza o peso usando a regra de aprendizado do Perceptron
            w[i][j] += learning_rate * delta * entrada[i][j]
            
            # Imprime informações para aprendizado
            print(f'Posição ({i}, {j}):')
            print(f'Soma ponderada: {soma_ponderada}, Previsão: {previsao}, Delta: {delta}')
            print(f'Peso atualizado: {w[i][j]}')
    
    # Atualiza o viés (bias)
    b += learning_rate * delta
    print(f'Viés atualizado: {b}')
    
    return w, b


# Testa a matriz desenhada pelo usuário
def testar_perceptron(entrada, w, b):
    delta_teste = 0
    for i in range(size):
        for j in range(size):
            delta_teste += w[i][j] * entrada[i][j]
    delta_teste += b
    if delta_teste >= 0:
        return 1  # Letra A
    else:
        return -1  # Letra B

# Função principal para a interface
def main():
    # Inicializa os pesos e bias
    b = 0
    w = inicializar_matriz()

    # Treina o modelo com as letras A e B
    letra_A = inicializar_letra_A()
    letra_B = inicializar_letra_B()
    # Rodar o treinamento 5 vezes
    for _ in range(5):
        w, b = treinar_perceptron(letra_A, 1, w, b)
        # print(f'Após treinar com a letra A: w = {w}, b = {b}')
        
        w, b = treinar_perceptron(letra_B, -1, w, b)
        # print(f'Após treinar com a letra B: w = {w}, b = {b}')

    # Interface gráfica com tkinter
    root = tk.Tk()
    root.title("Perceptron - Reconhecimento de Letras")

    entrada = inicializar_matriz()
    buttons = [[None for _ in range(size)] for _ in range(size)]

    # Função para alternar o estado de um botão (alterar valor e cor)
    def toggle_button(i, j):
        if entrada[i][j] == 1:
            entrada[i][j] = 0
            buttons[i][j].config(text="", bg="white")
        else:
            entrada[i][j] = 1
            buttons[i][j].config(text="", bg="green")

    # Função para criar os botões
    for i in range(size):
        for j in range(size):
            buttons[i][j] = tk.Button(root, text="", width=2, height=1, bg="white", command=lambda i=i, j=j: toggle_button(i, j))
            buttons[i][j].grid(row=i, column=j)

    # Rótulo para exibir o resultado
    result_label = tk.Label(root, text="Clique em 'Executar' para ver o resultado")
    result_label.grid(row=size+1, column=0, columnspan=size)

    # Função para rodar o algoritmo do Perceptron
    def run_perceptron():
        teste = testar_perceptron(entrada, w, b)
        print(teste)
        if teste == 1:
            result_label.config(text="O que você escreveu é uma letra A")
        else:
            result_label.config(text="O que você escreveu é uma letra B")

    # Função para limpar a matriz
    def reset_perceptron():
        for i in range(size):
            for j in range(size):
                entrada[i][j] = 0
                buttons[i][j].config(text="", bg="white")
        result_label.config(text="Clique em 'Executar' para ver o resultado")

    # Botão para executar o algoritmo
    run_button = tk.Button(root, text="Executar", command=run_perceptron)
    run_button.grid(row=size+2, column=0, columnspan=size//2)

    # Botão para limpar a matriz
    reset_button = tk.Button(root, text="Limpar", command=reset_perceptron)
    reset_button.grid(row=size+2, column=size//2, columnspan=size//2)

    # Inicia a interface
    root.mainloop()

if __name__ == "__main__":
    main()
