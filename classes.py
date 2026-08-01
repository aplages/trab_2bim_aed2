class No:
    # Deve conter três atributos:
        # • dado: O valor armazenado (inteiro)
        # • proximo: Ponteiro para o próximo nó
        # • anterior: Ponteiro para o nó anterior

    def __init__(self, dado, anterior, proximo):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo



class ListaDuplamenteEncadeada:
    def __init__(self) -> None:
        pass

    # Deve gerenciar os ponteiros inicio e fim.
    # Você deve obrigatoriamente implementar as seguintes funções:
    
    
    def inserir_no_inicio(self, valor): # Iterativo
        """
            Insere um novo elemento no começo da lista,
            reajustando adequadamente os ponteiros inicio e
            o anterior do antigo primeiro nó.
        """
        pass

    def inserir_no_fim(self, valor): # Público
        """
            Método que dispara a inserção recursiva no fim.
            Trata o caso especial de a lista estar vazia.
        """
        pass

    def __inserir_no_fim_recursivo_aux(self, no_atual, novo_no): # Privado / Auxiliar
        """
            Percorre a lista até encontrar o final (None).
            Insere o novo_no, ajusta o ponteiro anterior dele e
            atualiza o atributo self.fim da lista.
        """
        pass

    def inserir_no_meio(self, indice, valor): # Público
        """
            Método que recebe um índice (posição baseada em 0) 
            e dispara a função recursiva de inserção na posição correspondente.
            Se o índice for menor ou igual a 0, direciona para o início.
        """
        pass

    def __inserir_no_meio_recursivo_aux(self, no_atual, indice_atual, indice_alvo): # Privado/Auxiliar, RECURSIVO
        """
            Percorre a lista
            incrementando o indice_atual de forma recursiva até encontrar a posição correta
            (indice_alvo). Caso a função alcance o final da lista (no_atual is None) antes de
            atingir o índice, o elemento deve ser inserido no fim da lista. Deve realizar a
            amarração dos 4 ponteiros envolvidos.
        """
        pass

    def exibir_lista(self): # iterativo ou recursivo
        """
            Imprime os elementos da lista do início
            ao fim (exemplo visual: 1 <-> 2 <-> 3)
        """
        pass

    def remover_todos(self, valor): # Público
        """
            Método público que apenas dispara a
            função recursiva de remoção.
        """
        pass

    def __remover_recursivo_aux(self, no_atual, valor): # Privado/Auxiliar - RECURSIVO
        """
            Percorre a lista de forma recursiva, localiza e remove todas as ocorrências do valor.
            Deve garantir que os ponteiros anterior e proximo dos nós vizinhos
            sejam costurados corretamente e tratar a atualização do inicio e fim da lista.
        """
        pass

    def ordernar(self): # Público
        """
            Método que dispara a ordenação por inserção. Deve
            verificar se a lista possui menos de 2 elementos antes de começar.
        """
        pass

    def __insercao_recursiva(self, no_atual): # Privado/Auxiliar - RECURSIVO
        """
            Funciona como o laço externo do Insertion Sort. Visita cada nó da
            lista (da esquerda para a direita), desconecta-o temporariamente e chama a função
            de inserção ordenada para reposicioná-lo na sublista à esquerda.
        """
        pass

    def __inserir_ordenado_recursivo(self, no_lista, novo_no): # Privado/Auxiliar - RECURSIVO
        """
            Funciona como o laço interno do Insertion Sort.
            Procura recursivamente a posição correta para o novo_no dentro da
            sublista já ordenada e faz as amarrações dos ponteiros.
        """
        pass