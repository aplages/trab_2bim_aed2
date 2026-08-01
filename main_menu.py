"""

>> O MENU INTERATIVO

O script principal deve rodar em um laço (while) que exiba exatamente o seguinte
menu:

=== MENU LISTA DUPLAMENTE ENCADEADA ===
1. Inserir elemento no início
2. Inserir elemento no fim (Recursivo)
3. Inserir elemento no meio (por índice - Recursivo)
4. Remover todas as ocorrências de um valor (Recursivo)
5. Ordenar a lista com Insertion Sort (Recursivo)
6. Exibir lista
0. Sair
Digite sua opção:


"""

from lista_dup_encadeada import No, ListaDuplamenteEncadeada

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

def main_menu():
    escreve_menu()
    entrada = int(input())

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
