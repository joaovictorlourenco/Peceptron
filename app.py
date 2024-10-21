import tkinter as tk
from tkinter import messagebox

# Definindo o tamanho da matriz 10x10
size = 10

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

# Treina o modelo usando a Regra de Hebb
def treinar_hebb(entrada, y, w, b):
    for i in range(size):
        for j in range(size):
            w[i][j] += entrada[i][j] * y
    b += y
    return w, b

# Testa a matriz desenhada pelo usuário
def testar_hebb(entrada, w, b):
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
    w, b = treinar_hebb(letra_A, 1, w, b)
    w, b = treinar_hebb(letra_B, -1, w, b)

    # Interface gráfica com tkinter
    root = tk.Tk()
    root.title("Regra de Hebb - Reconhecimento de Letras")

    entrada = inicializar_matriz()
    buttons = [[None for _ in range(size)] for _ in range(size)]

    # Função para alternar o estado de um botão
    def toggle_button(i, j):
        if entrada[i][j] == 1:
            entrada[i][j] = -1
            buttons[i][j].config(text="0")
        else:
            entrada[i][j] = 1
            buttons[i][j].config(text="1")

    # Função para criar os botões
    for i in range(size):
        for j in range(size):
            buttons[i][j] = tk.Button(root, text="0", width=2, command=lambda i=i, j=j: toggle_button(i, j))
            buttons[i][j].grid(row=i, column=j)

    # Rótulo para exibir o resultado
    result_label = tk.Label(root, text="Clique em 'Executar' para ver o resultado")
    result_label.grid(row=size+1, column=0, columnspan=size)

    # Função para rodar o algoritmo da Regra de Hebb
    def run_hebb():
        teste = testar_hebb(entrada, w, b)
        if teste == 1:
            result_label.config(text="O que você escreveu é uma letra A")
        else:
            result_label.config(text="O que você escreveu é uma letra B")

    # Função para limpar a matriz
    def reset_hebb():
        for i in range(size):
            for j in range(size):
                entrada[i][j] = 0
                buttons[i][j].config(text="0")
        result_label.config(text="Clique em 'Executar' para ver o resultado")

    # Botão para executar o algoritmo
    run_button = tk.Button(root, text="Executar", command=run_hebb)
    run_button.grid(row=size+2, column=0, columnspan=size//2)

    # Botão para limpar a matriz
    reset_button = tk.Button(root, text="Limpar", command=reset_hebb)
    reset_button.grid(row=size+2, column=size//2, columnspan=size//2)

    # Inicia a interface
    root.mainloop()

if __name__ == "__main__":
    main()
