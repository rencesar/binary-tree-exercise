import os

from faker import Faker
from time import sleep

from library import BinaryTree, Book


binary_tree = BinaryTree()


def show_books():
    print("Seus Livros: ")
    print(binary_tree)


def insert_book():
    binary_tree.insert(Book(
        input("Digite o titulo do livro: "),
        int(input("Digite o ano de lançamento: "))
    ))
    show_books()
    input("Pressione enter para continuar")


def loop_through():
    for i in binary_tree.root:
        print(i.get_data())
    input("Pressione enter para continuar")


def tree_height():
    print(f"A arvore possui {binary_tree.height()}")
    input("Pressione enter para continuar")


def search_by_name():
    print(binary_tree.search(input("Digite o titulo do livro que está procurando: ")))
    input("Pressione enter para continuar")


def search_by_year():
    books_by_year = binary_tree.search_by_year(int(input("Digite o ano do livro que está procurando: ")))
    for book in books_by_year:
        print(book)
    if len(books_by_year) == 0:
        print("Nenhum livro encontrado")
    input("Pressione enter para continuar")


def remove_item():
    binary_tree.remove_item(input("Digite o nome do livro que deseja ser removido: "))
    input("Pressione enter para continuar")


def generate_test_data():
    fake = Faker()
    for _ in range(15):
        binary_tree.insert(Book(
            fake.name(),
            int(fake.year())
        ))
    show_books()
    input("Pressione enter para continuar")


option = 0
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
        insert_book()
    elif option == 2:
        search_by_name()
    elif option == 3:
        search_by_year()
    elif option == 4:
        remove_item()
    elif option == 5:
        loop_through()
    elif option == 6:
        tree_height()
    elif option == 8:
        generate_test_data()
    elif option == 9:
        show_books()
        input("Pressione enter para continuar")
