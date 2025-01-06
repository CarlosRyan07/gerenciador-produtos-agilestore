
# AgileStore - Gerenciador de Inventário de Produtos

Esse projeto foi um desafio de criar uma aplicação simples e eficiente para o gerenciamento de inventário de produtos. Nesse projeto você pode adicionar, listar, buscar, atualizar e excluir produtos, mantendo seus dados persistentes em um arquivo JSON.

# 🚀 Funcionalidades Principais

Ao rodar o programa, você terá acesso a um menu com as seguintes opções:

```bash
         ___         _ __    _____ __
        /   | ____ _(_) /__ / ___// /_____  ________ 
=======/ /| |/ __ `/ / / _ \__ \/ __/ __ \/ ___/ _ \========
======/ ___ / /_/ / / /  __/__/ / /_/ /_/ / /  /  __/========
=====/_/  |_|\_, /_/_/\___/____/\__/\____/_/   \___/=========  
           /____/

    Bem-vindo ao Gerenciamento de Produtos da AgileStore!
=============================================================


Menu:
1. Adicionar Produto
2. Listar Produtos
3. Buscar Produto
4. Atualizar Produto
5. Excluir Produto
6. Sair

Escolha uma opção: 
```

e agora irei detalhar mais sobre cada uma delas.

## 1. Adicionar Produto

Permite que o usuário insira um novo produto no inventário. Durante o processo:

É solicitado o preenchimento de:

* Nome do Produto
* Categoria
* Quantidade em Estoque
* Preço

O sistema valida os dados e assegura que campos obrigatórios não sejam deixados em branco.

Um ID único é gerado automaticamente para cada produto.

## 2. Listar Produtos

Exibe todos os produtos cadastrados em formato de tabela, incluindo:

* ID
* Nome do Produto
* Categoria
* Quantidade em Estoque
* Preço

Opcionalmente, permite:

* Filtrar produtos por categoria.
* Ordenar produtos por nome, quantidade ou preço.

Exemplo da estrutura utilizada na tabela:

   ```bash
    ID    | Nome                                | Categoria       | Quantidade | Preço
    =====================================================================================
    2     | Fusca                               | Carro           | 10         | 30000.00
    3     | Cerveja Skol                        | Bebidas         | 120        | 2.50
    4     | Honda CBR 1000                      | Moto            | 8          | 45000.00
    6     | Suco                                | Bebidas         | 30         | 4.99
    7     | Civic 2024                          | Carro           | 3          | 95000.00
    8     | Ficando rico rápido(Não funciona)   | Curso           | 99         | 99.99
    9     | Boleto á pagar                      | Contas          | 50         | 19.99
   ```


## 3. Buscar Produto

Facilita a localização de um produto específico. Você pode:

* Buscar pelo ID.
* Buscar por parte do nome.

Caso um produto seja encontrado, suas informações detalhadas são exibidas. Caso contrário, uma mensagem apropriada é apresentada.

## 4. Atualizar Produto

Permite modificar as informações de um produto existente:

* O sistema verifica se o ID informado existe.
* Você pode escolher quais campos deseja atualizar.
* Validações garantem a consistência dos novos dados.

## 5. Excluir Produto

Remove um produto do inventário pelo ID informado:

* Confirmação é solicitada antes de excluir o produto.
* Após a confirmação, o produto é removido permanentemente do arquivo JSON.

## 🗂 Persistência de Dados

Todos os produtos são armazenados em um arquivo `products.json`, garantindo que os dados sejam preservados mesmo após o encerramento da aplicação.

# ⚙️ Como Executar

1. Clone este repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd AgileStore
   ```

3. Execute o programa:

   ```bash
   main.py
   ```

# 🛠 Tecnologias Utilizadas

* **Python**: Linguagem principal do projeto.
* **JSON**: Para armazenamento persistente dos dados.
