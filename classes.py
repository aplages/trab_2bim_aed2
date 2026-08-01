class No:
    # Deve conter três atributos:
        # • dado: O valor armazenado (inteiro)
        # • proximo: Ponteiro para o próximo nó
        # • anterior: Ponteiro para o nó anterior

    def __init__(self, dado, anterior: No | None=None, proximo: No | None=None):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo

    def exibirse(self):
        """ Mostra o dado """
        if (self.anterior != None) and (self.proximo != None):
            print(f'Dado: {self.dado} | Anterior: {self.anterior.dado} | Próximo: {self.proximo.dado}')
        elif self.anterior != None:
            print(f'Dado: {self.dado} | Anterior: {self.anterior.dado} | Próximo: {None}')
        elif self.proximo != None:
            print(f'Dado: {self.dado} | Anterior: {None} | Próximo: {self.proximo.dado}')
        else:
            print(f'Dado: {self.dado} | Anterior: {None} | Próximo: {None}')



class ListaDuplamenteEncadeada:
    """
        Deve gerenciar os ponteiros inicio e fim.
    """

    def __init__(self):
        self.tam = 0
        self.ini = None
        self.fim = None

    def isVazia(self) -> bool:
        """
            Se for Vazia retorna True
            \nSenão, retorna False
        """
        return self.ini == None # Se ini == None, retorna True; caso contrário, retorna False

    
    ##
    # >> Você deve obrigatoriamente implementar as seguintes funções: <<

    def inserir_no_inicio(self, valor): # Iterativo
        """
            Insere um novo elemento no começo da lista,
            reajustando adequadamente os ponteiros inicio e
            o anterior do antigo primeiro nó.
        """
        novo = No(valor)
        
        if self.isVazia():  # Caso a lista seja vazia
            self.tam = 1
            self.ini = novo
            self.fim = novo
        else:   # Caso a lista já contenha N itens
            if self.ini != None:
                self.tam += 1
                novo_prox = self.ini
                self.ini = novo
                self.ini.proximo = novo_prox
                novo_prox.anterior = self.ini
            else:
                print('> Erro:  self.ini = None')

    def inserir_no_fim(self, valor): # Público
        """
            Método que dispara a inserção recursiva no fim.
            Trata o caso especial de a lista estar vazia.
        """
        novo = No(valor)

        if self.isVazia(): # Caso a lista seja vazia
            self.tam = 1
            self.ini = novo
            self.fim = novo
        else:   # Caso a lista já contenha N itens
            ''' Usando apenas o ponteiro self.fim

            if self.fim != None:
                self.tam += 1
                novo_ant = self.fim
                self.fim = novo
                self.fim.anterior = novo_ant
                novo_ant.proximo = self.fim
                
            '''
            # Usando recursão:
            no_atual = self.ini
            if no_atual == self.fim:
                if no_atual != None:
                    self.tam += 1
                    novo.anterior = no_atual
                    no_atual.proximo = novo
                    self.fim = novo
                else:
                    print('> Erro:    no_atual = None')
            else:
                # Chama a funcao auxiliar
                self.__inserir_no_fim_recursivo_aux(no_atual, novo)


    def __inserir_no_fim_recursivo_aux(self, no_atual, novo_no): # Privado / Auxiliar
        """
            Percorre a lista até encontrar o final (None).
            Insere o novo_no, ajusta o ponteiro anterior dele e
            atualiza o atributo self.fim da lista.
        """

        novo = novo_no
        if no_atual.proximo == None:
            if no_atual != None:
                self.tam += 1
                novo.anterior = no_atual
                no_atual.proximo = novo
                self.fim = novo
        else:
            no_atual = no_atual.proximo
            # Chama a funcao auxiliar novamente
            self.__inserir_no_fim_recursivo_aux(no_atual, novo)


    def inserir_no_meio(self, indice: int, valor): # Público
        """
            Método que recebe um índice (posição baseada em 0) 
            e dispara a função recursiva de inserção na posição correspondente.
            Se o índice for menor ou igual a 0, direciona para o início.
        """
        
        if self.isVazia(): # Cria uma independente do indice
            novo = No(valor)
            self.tam = 1
            self.ini = novo
            self.fim = novo
        elif indice <= 0:
            self.inserir_no_inicio(valor)   # Usa a funcao de inserir no incio para inserir no indice 0
        else:
            self.__inserir_no_meio_recursivo_aux(self.ini, 0, indice, valor)   # Chama a função auxiliar


    def __inserir_no_meio_recursivo_aux(self, no_atual, indice_atual, indice_alvo, valor): # Privado/Auxiliar, RECURSIVO
        """
            Percorre a lista
            incrementando o indice_atual de forma recursiva até encontrar a posição correta
            (indice_alvo). Caso a função alcance o final da lista (no_atual is None) antes de
            atingir o índice, o elemento deve ser inserido no fim da lista. Deve realizar a
            amarração dos 4 ponteiros envolvidos.
        """
        indice = indice_atual+1
        print(indice)
        if no_atual.proximo == None:
            self.inserir_no_fim(valor)  # Usa a funcao de inserir no fim caso o indice desejado ultrapasse o fim da lista
            
        else:
            no_atual = no_atual.proximo
            if indice != indice_alvo:
                self.__inserir_no_meio_recursivo_aux(no_atual, indice, indice_alvo, valor)

            else:
                # temp_proximo = no_atual
                # temp_anterior = no_atual.anterior
                novo = No(valor, anterior=no_atual.anterior, proximo=no_atual)
                novo.proximo.anterior = novo
                novo.anterior.proximo = novo
                



    def exibir_lista(self): # iterativo ou recursivo
        """
            Imprime os elementos da lista do início
            ao fim (exemplo visual: 1 <-> 2 <-> 3)
        """
        if self.isVazia():
            return "Lista Vazia"

        print('\n-=============================-')
        print('>>      Exibindo Lista       <<\n')

        nodo = self.ini
        print(f'Início:')
        if nodo != None:
            nodo.exibirse()
            print()
            if (nodo.proximo != None) and (nodo.proximo != self.ini):
                self.__exibir_auxiliar(nodo.proximo)
        else:
            print(None)
            print()
        print('\n-============ Fim =============-\n')


    def __exibir_auxiliar(self, nodo: No): # Privado
        """
            Auxilia recursivamente a função "exibir_lista"
            recebe um No como parêmetro
        """
        if nodo != None:

            if nodo == self.fim:
                print('\nFim:')
            nodo.exibirse()
            if (nodo.proximo != None):
                self.__exibir_auxiliar(nodo.proximo)

    def remover_todos(self, valor): # Público
        """
            Método público que apenas dispara a
            função recursiva de remoção.
        """
        no_atual = self.ini
        self.__remover_recursivo_aux(no_atual, valor)

    def __remover_recursivo_aux(self, no_atual, valor): # Privado/Auxiliar - RECURSIVO
        """
            Percorre a lista de forma recursiva, localiza e remove todas as ocorrências do valor.
            Deve garantir que os ponteiros anterior e proximo dos nós vizinhos
            sejam costurados corretamente e tratar a atualização do inicio e fim da lista.
        """
        if no_atual.dado != valor:
            if no_atual.proximo != None:
                self.__remover_recursivo_aux(no_atual.proximo, valor)
        else:
            if (no_atual == self.ini) and (no_atual == self.fim):   # Caso a lista possua apenas 1 item
                self.tam = 0
                self.ini = None
                self.fim = None
            elif (no_atual == self.fim): # Caso o no atual seja o fim
                self.fim = no_atual.anterior # fim recebe anterior
                self.fim.proximo = None
            elif (no_atual == self.ini):    # Caso o nó atual seja o inicio
                self.ini = no_atual.proximo # ini recebe proximo
                self.ini.anterior = None
                self.__remover_recursivo_aux(no_atual.proximo, valor)
            else:
                no_atual.anterior.proximo = no_atual.proximo    # o proximo do anterior recebe o proximo do atual
                no_atual.proximo.anterior = no_atual.anterior   # o anterior do proximo recebe o anterior do atual
                self.__remover_recursivo_aux(no_atual.proximo, valor)


    def ordernar(self): # Público
        """
            Método que dispara a ordenação por inserção. 
            Deve verificar se a lista possui menos de 2 elementos antes de começar.
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




### Testes

teste = ListaDuplamenteEncadeada()
#print(teste.isVazia())
teste.inserir_no_fim('teste_fim_vazio')
teste.inserir_no_inicio(valor='teste')
teste.exibir_lista()

teste_nodo = No('teste')

teste2 = No('adada', anterior=teste_nodo)


teste.inserir_no_inicio('teste_inicio')

print('--')
teste.exibir_lista()



teste.inserir_no_fim('teste fim')
print('--')
teste.exibir_lista()



teste.inserir_no_meio(indice=2, valor='teste_meio')

print('--')
teste.exibir_lista()


teste.inserir_no_meio(indice=-1, valor='teste_meio_inicio')

print('--')
teste.exibir_lista()

teste.remover_todos('teste')

print('--')
teste.exibir_lista()
'''
teste.inserir_no_meio(indice=3, valor='teste')

print('--')
teste.exibir_lista()
'''