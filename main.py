import json
import os

# Caminho do arquivo JSON onde os produtos serão armazenados
FILE_PATH = 'products.json'

# Função para carregar os produtos do arquivo JSON
def load_products():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []

# Função para salvar os produtos no arquivo JSON
def save_products(products):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(products, file, indent=4, ensure_ascii=False)

# Função para obter o próximo ID disponível
def get_next_id(products):
    if products:
        return max(product['id'] for product in products) + 1
    else:
        return 1

# Função para adicionar um novo produto
def add_product(name, category, quantity, price):
    if not all([name.strip(), category.strip()]):
        print("\nErro: Nome e Categoria não podem estar vazios!")
        return

    if quantity <= 0 or price <= 0:
        print("\nErro: Quantidade e Preço devem ser maiores que zero!")
        return

    products = load_products()
    product_id = get_next_id(products)
    product = {
        'id': product_id,
        'name': name.strip(),
        'category': category.strip(),
        'quantity': quantity,
        'price': price
    }
    products.append(product)
    save_products(products)
    print("\nProduto adicionado com sucesso!")
    print("=" * 50)

# Função para listar as categorias existentes
def list_categories(products):
    categories = set(product['category'] for product in products)
    print("\nCategorias disponíveis:")
    for category in categories:
        print(f"- {category}")
    return categories

# Função para listar todos os produtos com opções de filtragem e ordenação
def list_products():
    products = load_products()

    if not products:
        print("\nNenhum produto encontrado.")
    else:
        print("\nFiltros e Ordenação:")
        print("1. Filtrar por categoria")
        print("2. Ordenar por nome")
        print("3. Ordenar por quantidade")
        print("4. Ordenar por preço")
        print("5. Exibir todos os produtos")
        choice = input("\nEscolha uma opção de filtro ou ordenação (1-5): ")

        if choice == '1':
            list_categories(products)
            category = input("\nDigite a categoria para filtrar: ")
            products = [product for product in products if category.lower() in product['category'].lower()]
            if not products:
                print(f"\nNenhum produto encontrado na categoria '{category}'.")
        elif choice == '2':
            products.sort(key=lambda x: x['name'].lower())
            print("\nProdutos ordenados por nome.")
        elif choice == '3':
            products.sort(key=lambda x: x['quantity'])
            print("\nProdutos ordenados por quantidade.")
        elif choice == '4':
            products.sort(key=lambda x: x['price'])
            print("\nProdutos ordenados por preço.")
        elif choice != '5':
            print("\nOpção inválida, mostrando todos os produtos.")

        print("\n{:<5} | {:<35} | {:<15} | {:<10} | {:<10}".format("ID", "Nome", "Categoria", "Quantidade", "Preço"))
        print("=" * 85)
        for product in products:
            print("{:<5} | {:<35} | {:<15} | {:<10} | {:<10.2f}".format(product['id'], product['name'], product['category'], product['quantity'], product['price']))

    input("\nPressione Enter para continuar...")
    print("=" * 50)

# Função para buscar um produto pelo ID ou nome
def search_product():
    products = load_products()

    print("\nBuscar Produto:")
    print("1. Buscar por ID")
    print("2. Buscar por parte do nome")
    choice = input("Escolha uma opção (1-2): ")

    found_products = []

    if choice == '1':
        product_id = input("Digite o ID do produto: ")
        for product in products:
            if str(product['id']) == product_id:
                found_products.append(product)
    elif choice == '2':
        name_part = input("Digite parte do nome do produto: ")
        for product in products:
            if name_part.lower() in product['name'].lower():
                found_products.append(product)
    else:
        print("\nOpção inválida!")

    if found_products:
        print("\n{:<5} | {:<35} | {:<15} | {:<10} | {:<10}".format("ID", "Nome", "Categoria", "Quantidade", "Preço"))
        print("=" * 85)
        for product in found_products:
            print("{:<5} | {:<35} | {:<15} | {:<10} | {:<10.2f}".format(product['id'], product['name'], product['category'], product['quantity'], product['price']))
    else:
        print("\nNenhum produto encontrado.")

    input("\nPressione Enter para continuar...")
    print("=" * 50)

# Função para atualizar um produto
def update_product(product_id):
    products = load_products()
    product_found = False

    for product in products:
        if product['id'] == product_id:
            product_found = True

            print("\nAtualize os campos do produto. Deixe em branco para manter o valor atual.")
            name = input(f"Novo nome (Atual: {product['name']}): ").strip()
            category = input(f"Nova categoria (Atual: {product['category']}): ").strip()
            quantity = input(f"Nova quantidade (Atual: {product['quantity']}): ").strip()
            price = input(f"Novo preço (Atual: R$ {product['price']:.2f}): ").strip()

            if name:
                product['name'] = name
            if category:
                product['category'] = category
            if quantity:
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        product['quantity'] = quantity
                    else:
                        print("Quantidade deve ser maior que zero! Valor não alterado.")
                except ValueError:
                    print("Quantidade inválida! Valor não alterado.")
            if price:
                try:
                    price = float(price)
                    if price > 0:
                        product['price'] = price
                    else:
                        print("Preço deve ser maior que zero! Valor não alterado.")
                except ValueError:
                    print("Preço inválido! Valor não alterado.")

            break

    if product_found:
        save_products(products)
        print(f"\nProduto ID {product_id} atualizado com sucesso!")
    else:
        print("\nProduto não encontrado.")

    input("\nPressione Enter para continuar...")
    print("=" * 50)

# Função para excluir um produto
def delete_product(product_id):
    products = load_products()
    product_found = False

    for product in products:
        if product['id'] == product_id:
            product_found = True
            confirm = input(f"\nTem certeza de que deseja excluir o produto '{product['name']}'? (s/n): ").strip().lower()
            if confirm == 's':
                products.remove(product)
                save_products(products)
                print(f"\nProduto ID {product_id} excluído com sucesso!")
            else:
                print("\nExclusão cancelada.")
            break

    if not product_found:
        print("\nProduto não encontrado.")

    input("\nPressione Enter para continuar...")
    print("=" * 50)

# Função principal para exibir o menu
def main():
    print(""" 
         ___         _ __    _____ __                
        /   | ____ _(_) /__ / ___// /_____  ________ 
=======/ /| |/ __ `/ / / _ \\__ \/ __/ __ \/ ___/ _ \========
======/ ___ / /_/ / / /  __/__/ / /_/ /_/ / /  /  __/========
=====/_/  |_|\_, /_/_/\___/____/\__/\____/_/   \___/=========  
           /____/                                  
   
    Bem-vindo ao Gerenciamento de Produtos da AgileStore!
============================================================= 
    """)

    while True:
        print(""" 
Menu:
1. Adicionar Produto
2. Listar Produtos
3. Buscar Produto
4. Atualizar Produto
5. Excluir Produto
6. Sair
""")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do Produto: ")
            category = input("Categoria: ")
            try:
                quantity = int(input("Quantidade em Estoque: "))
                price = float(input("Preço: "))
                add_product(name, category, quantity, price)
            except ValueError:
                print("\nEntrada inválida! Por favor, insira valores numéricos válidos para quantidade e preço.")
        elif choice == '2':
            list_products()
        elif choice == '3':
            search_product()
        elif choice == '4':
            try:
                product_id = int(input("Digite o ID do produto a ser atualizado: "))
                update_product(product_id)
            except ValueError:
                print("\nID inválido! Certifique-se de inserir um número válido.")
        elif choice == '5':
            try:
                product_id = int(input("Digite o ID do produto a ser excluído: "))
                delete_product(product_id)
            except ValueError:
                print("\nID inválido! Por favor, insira um número válido.")
        elif choice == '6':
            print("\nSaindo...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == '__main__':
    main()
