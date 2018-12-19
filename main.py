import os

from faker import Faker
from time import sleep

from library import BinaryTree, Book

def show_books(binary_tree):
    print("Seus Livros: ")
    print(binary_tree)


def insert_book(binary_tree):
    binary_tree.insert(Book(
        input("Digite o titulo do livro: "),
        int(input("Digite o ano de lançamento: "))
    ))
    show_books(binary_tree)
    input("Pressione enter para continuar")


def loop_through(binary_tree):
    for i in binary_tree.root:
        print(i.get_data())
    input("Pressione enter para continuar")


def tree_height(binary_tree):
    print(f"A arvore possui {binary_tree.root.get_height()}")
    input("Pressione enter para continuar")


def generate_test_data(binary_tree):
    fake = Faker()
    for _ in range(15):
        os.system('cls' if os.name == 'nt' else 'clear')
        show_books(binary_tree)
        name = fake.name() + " n." +str(_)
        print("\n\n\n\t DEPPPPOOOIIIIISSSS " + name)
        binary_tree.insert(Book(
            name,
            int(fake.year())
        ))
        show_books(binary_tree)
    print("ACACCAACACAACCABBBOOOUUUUU")
    input("Pressione enter para continuar")


option = 0
binary_tree = BinaryTree()
while option != 7:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    \t - MENU -
(1) Inserir livro
(2) Buscar livro por titulo
(3) Buscar livros por ano
(4) Remover livro
(5) Listar livros em ordem alfabética
(6) Altura da arvore
(7) Sair do programa.
(8) Generate teste data.
(9) Apresentar Arvore\n\n
    """)
    option = int(input("Digite a opção desejada: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == 1:
        insert_book(binary_tree)
    elif option == 5:
        loop_through(binary_tree)
    elif option == 6:
        tree_height(binary_tree)
    elif option == 8:
        generate_test_data(binary_tree)
    elif option == 9:
        show_books(binary_tree)
        input("Pressione enter para continuar")
