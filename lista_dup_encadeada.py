def escreve_menu():
    print('\n=== MENU LISTA DUPLAMENTE ENCADEADA ===\n' \
    '1. Inserir elemento no início\n' \
    '2. Inserir elemento no fim (Recursivo)\n' \
    '3. Inserir elemento no meio (por índice - Recursivo)\n' \
    '4. Remover todas as ocorrências de um valor (Recursivo)\n' \
    '5. Ordenar a lista com Insertion Sort (Recursivo)\n' \
    '6. Exibir lista\n' \
    '0. Sair\n' \
    'Digite sua opção:', end='\t')

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
        if no_atual.proximo == None:
            self.inserir_no_fim(valor)  # Usa a funcao de inserir no fim caso o indice desejado ultrapasse o fim da lista
            
        else:
            no_atual = no_atual.proximo
            if indice != indice_alvo:
                self.__inserir_no_meio_recursivo_aux(no_atual, indice, indice_alvo, valor)

            else:
                # temp_proximo = no_atual
                # temp_anterior = no_atual.anterior
                self.tam += 1
                novo = No(valor, anterior=no_atual.anterior, proximo=no_atual)
                if novo.proximo != None:
                    novo.proximo.anterior = novo
                if novo.anterior != None:
                    novo.anterior.proximo = novo


    def exibir_lista(self): # iterativo ou recursivo
        """
            Imprime os elementos da lista do início ao fim de forma detalhada\n
            Depois mostra a lista bonita (exemplo visual: 1 <-> 2 <-> 3)

        """
        if self.isVazia():
            return "Lista Vazia"

        print('\n-=============================-')
        print('>>      Exibindo Lista       <<\n')
        print(f'Tamanho: {self.tam}\n')
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

        self.__exibir_bonitinho(self.ini)
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


    def __exibir_bonitinho(self, no):
        """
            Exibe a lista de forma visualmente bonita
            Ex: ] 1 ⇄ 2 ⇄ 3 [
            Já parte do principio de que a lista não é vazia, etc. (todas verificações foram feitas anteriormente)
        """
        if no == self.ini:
            print('\n[', end=" ")
        print(no.dado, end=" ")
        if no.proximo != None:
            print('⇄', end=" ")
            self.__exibir_bonitinho(no.proximo)
        else:
            print(']')


    def remover_todos(self, valor): # Público
        """
            Remove todos Nós que possuem dado valor no dado\n
            Método público que apenas dispara a função recursiva de remoção.
        """
        self.__remover_recursivo_aux(self.ini, valor)   # Chama a função auxiliar a partir do inicio


    def __remover_recursivo_aux(self, no_atual, valor): # Privado/Auxiliar - RECURSIVO
        """
            Percorre a lista de forma recursiva, localiza e remove todas as ocorrências do valor.\n
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
            else:
                self.tam -= 1
                if (no_atual == self.fim): # Caso o no atual seja o fim
                    self.fim = no_atual.anterior # fim recebe anterior
                    self.fim.proximo = None
                elif (no_atual == self.ini):    # Caso o nó atual seja o inicio
                    self.ini = no_atual.proximo # ini recebe proximo
                    self.ini.anterior = None
                    self.__remover_recursivo_aux(no_atual.proximo, valor)   # Chama a função novamente
                else:
                    no_atual.anterior.proximo = no_atual.proximo    # o proximo do anterior recebe o proximo do atual
                    no_atual.proximo.anterior = no_atual.anterior   # o anterior do proximo recebe o anterior do atual
                    self.__remover_recursivo_aux(no_atual.proximo, valor)   # Chama a função novamente


    def ordernar(self): # Público
        """
            Método que dispara a ordenação por inserção.\n
            Deve verificar se a lista possui menos de 2 elementos antes de começar.
        """
        if self.tam >= 2:
            if self.ini != None:
                self.__insercao_recursiva(self.ini.proximo) # Chama a funcao auxiliar a partir do inicio


    def __insercao_recursiva(self, no_atual): # Privado/Auxiliar - RECURSIVO
        """
            Funciona como o laço externo do Insertion Sort. Visita cada nó da
            lista (da esquerda para a direita), desconecta-o temporariamente e chama a função
            de inserção ordenada para reposicioná-lo na sublista à esquerda.
        """
        if no_atual.dado < no_atual.anterior.dado:
            if no_atual.proximo != None:
                # Conecta os anterior e proximo (desconecta o alvo)
                no_atual.anterior.proximo = no_atual.proximo
                no_atual.proximo.anterior = no_atual.anterior
                #
                # Chama a função auxiliar para inserir o alvo no lugar correto
            else:
                no_atual.anterior.proximo = None
                self.fim = no_atual.anterior
            self.__inserir_ordenado_recursivo(no_atual.anterior, no_atual)
        if no_atual.proximo != None:
            self.__insercao_recursiva(no_atual.proximo) # Chama a funcao auxiliar a partir do inicio


    def __inserir_ordenado_recursivo(self, no_lista, novo_no): # Privado/Auxiliar - RECURSIVO
        """
            Funciona como o laço interno do Insertion Sort.
            Procura recursivamente a posição correta para o novo_no dentro da
            sublista já ordenada e faz as amarrações dos ponteiros.
        """
        if no_lista.anterior == None:
            # Conecta o vizinho ao novo e vice-versa
            no_lista.anterior = novo_no
            novo_no.proximo = no_lista
            novo_no.anterior = None
            self.ini = novo_no  # inicio vira o novo

        elif no_lista.anterior.dado <= novo_no.dado:
            # Conecta o novo aos prox e ant
            novo_no.anterior = no_lista.anterior
            novo_no.proximo = no_lista

            # Conecta os vizinhos ao novo
            novo_no.anterior.proximo = novo_no
            novo_no.proximo.anterior = novo_no
        elif no_lista.anterior.dado > novo_no.dado:
            self.__inserir_ordenado_recursivo(no_lista.anterior, novo_no)
        


if __name__ == '__main__':
    lista_main = ListaDuplamenteEncadeada()
    entrada = ''
    while True:
        escreve_menu()
        entrada = int(input())
        if (entrada < 0) and (entrada > 6):
            print('>> Input inválido.')
        else:
            if entrada == 0:
                break

            elif entrada == 1:
                valor = int(input('\nDigite o valor que deseja adicionar ao inicio da lista:\t'))
                lista_main.inserir_no_inicio(valor)

            elif entrada == 2:
                valor = int(input('\nDigite o valor que deseja adicionar ao fim da lista:\t'))
                lista_main.inserir_no_fim(valor)

            elif entrada == 3:
                valor = int(input('\nDigite o valor que deseja adicionar no meio da lista:\t'))
                indice = int(input(f'Digite o indice no qual deseja adicionar o valor {valor}:\t'))
                lista_main.inserir_no_meio(indice, valor)

            elif entrada == 4:
                valor = int(input('\nDigite o valor que deseja remover da lista:\t'))
                lista_main.remover_todos(valor)
                print(f'\n>> Removidas todas ocorrências do valor {valor} da lista.')
                
            elif entrada == 5:
                lista_main.ordernar()
                print('\n>> Lista Ordenada.')

            elif entrada == 6:
                lista_main.exibir_lista()

    print('\nFim')
