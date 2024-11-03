import random

# Função para gerar um cromossomo aleatório
def generate_chromosome(length):
    return [random.randint(0, 1) for _ in range(length)]

# Função de avaliação (fitness)
def fitness_function(chromosome):
    return sum(chromosome)  # Exemplo simples: maximizar a soma dos genes

# Seleção por roleta
def roulette_selection(population, fitness_values, num_parents):
    total_fitness = sum(fitness_values)
    selected_parents = []
    for _ in range(num_parents):
        pick = random.uniform(0, total_fitness)
        current = 0
        for i, chromosome in enumerate(population):
            current += fitness_values[i]
            if current > pick:
                selected_parents.append(chromosome)
                break
    return selected_parents

# Seleção por torneio
def tournament_selection(population, fitness_values, num_parents, tournament_size):
    selected_parents = []
    for _ in range(num_parents):
        tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected_parents.append(winner)
    return selected_parents

# Cruzamento de um ponto
def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Cruzamento de dois pontos
def two_point_crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)
    return (parent1[:point1] + parent2[point1:point2] + parent1[point2:],
            parent2[:point1] + parent1[point1:point2] + parent2[point2:])

# Mutação
def mutate(chromosome, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in chromosome]

# Função principal do Algoritmo Genético
def genetic_algorithm(chromosome_length, population_size, crossover_rate,
                      mutation_rate, max_generations, selection_method,
                      crossover_method, tournament_size=None):
    
    # Gerar população inicial
    population = [generate_chromosome(chromosome_length) for _ in range(population_size)]
    
    for generation in range(max_generations):
        fitness_values = [fitness_function(chromosome) for chromosome in population]
        print(f"Geração {generation}: Melhor Fitness = {max(fitness_values)}")
        
        # Seleção dos pais
        num_parents = int(population_size * crossover_rate)
        if selection_method == 'roleta':
            parents = roulette_selection(population, fitness_values, num_parents)
        elif selection_method == 'torneio':
            parents = tournament_selection(population, fitness_values, num_parents, tournament_size)
        else:
            raise ValueError("Método de seleção inválido.")

        # Geração de nova população
        next_population = []
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            
            # Cruzamento
            if crossover_method == 'um_ponto':
                child1, child2 = one_point_crossover(parent1, parent2)
            elif crossover_method == 'dois_pontos':
                child1, child2 = two_point_crossover(parent1, parent2)
            else:
                raise ValueError("Método de cruzamento inválido.")
            
            # Mutação
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            next_population.extend([child1, child2])
        
        # Atualizar população
        population = next_population[:population_size]
        
        # Condição de parada (pode ser ajustada conforme necessário)
        if max(fitness_values) == chromosome_length:
            print("Solução ótima encontrada!")
            break

    # Retornar o melhor cromossomo e sua avaliação final
    best_chromosome = max(population, key=fitness_function)
    return best_chromosome, fitness_function(best_chromosome)

# Função para configurar e executar o algoritmo
def main():
    chromosome_length = int(input("Tamanho do cromossomo: "))
    population_size = int(input("Tamanho da população: "))
    crossover_rate = float(input("Porcentagem de cruzamento (0-1): "))
    mutation_rate = float(input("Probabilidade de mutação (0-1): "))
    max_generations = int(input("Quantidade máxima de gerações: "))

    print("Método de seleção (roleta/torneio):")
    selection_method = input().strip().lower()
    if selection_method == 'torneio':
        tournament_size = int(input("Tamanho do torneio: "))
    else:
        tournament_size = None
    
    print("Método de cruzamento (um_ponto/dois_pontos):")
    crossover_method = input().strip().lower()
    
    best_chromosome, best_fitness = genetic_algorithm(
        chromosome_length, population_size, crossover_rate, mutation_rate,
        max_generations, selection_method, crossover_method, tournament_size
    )
    
    print(f"Melhor Cromossomo: {best_chromosome}")
    print(f"Fitness do Melhor Cromossomo: {best_fitness}")

if __name__ == "__main__":
    main()
