import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
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

# Função para adicionar um produto
def add_product(name, category, quantity, price):
    products = load_products()
    product_id = get_next_id(products)
    product = {
        'id': product_id,
        'name': name,
        'category': category,
        'quantity': quantity,
        'price': price
    }
    products.append(product)
    save_products(products)

# Função para atualizar um produto
def update_product(product_id, name=None, category=None, quantity=None, price=None):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            if name:
                product['name'] = name
            if category:
                product['category'] = category
            if quantity is not None:
                product['quantity'] = quantity
            if price is not None:
                product['price'] = price
            break
    save_products(products)

# Função para excluir um produto
def delete_product(product_id):
    products = load_products()
    products = [product for product in products if product['id'] != product_id]
    save_products(products)

# Função para buscar produtos por ID ou nome
def search_products(query):
    products = load_products()
    return [product for product in products if query.lower() in str(product['id']).lower() or query.lower() in product['name'].lower()]

# Função para aplicar estilos visuais
def apply_styles():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Helvetica", 10, "bold"), foreground="white", background="#007acc")
    style.map("TButton", background=[("active", "#005b99")])
    style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))
    style.configure("Treeview", rowheight=25, font=("Helvetica", 10))
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))

# Interface gráfica
class ProductManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Produtos - AgileStore")

        # Tornar a janela redimensionável, mas limitar o tamanho mínimo
        self.root.resizable(True, True)
        self.root.minsize(600, 500)  # Limitar a redução mínima do tamanho da janela

        self.products = load_products()
        self.original_products = list(self.products)  # Para restaurar a ordem original

        # Aplicar estilos visuais
        apply_styles()

        # Configuração da interface
        self.setup_ui()

    def setup_ui(self):
        # Frame de entrada de dados
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(input_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(input_frame, text="Categoria:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.category_entry = ttk.Entry(input_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(input_frame, text="Quantidade:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.quantity_entry = ttk.Entry(input_frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(input_frame, text="Preço:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.price_entry = ttk.Entry(input_frame)
        self.price_entry.grid(row=3, column=1, padx=5, pady=2)

        add_button = ttk.Button(input_frame, text="Adicionar Produto", command=self.add_product)
        add_button.grid(row=4, columnspan=2, pady=10)

        # Frame da tabela
        table_frame = ttk.Frame(self.root, padding="10")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Nome", "Categoria", "Quantidade", "Preço"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Preço", text="Preço")

        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Nome", width=150, anchor=tk.W)
        self.tree.column("Categoria", width=100, anchor=tk.W)
        self.tree.column("Quantidade", width=80, anchor=tk.CENTER)
        self.tree.column("Preço", width=80, anchor=tk.W)

        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Botões de ações
        action_frame = ttk.Frame(self.root, padding="10")
        action_frame.pack(fill=tk.X, padx=10, pady=5)

        update_button = ttk.Button(action_frame, text="Atualizar Produto", command=self.update_product)
        update_button.grid(row=0, column=0, padx=5)

        delete_button = ttk.Button(action_frame, text="Excluir Produto", command=self.delete_product)
        delete_button.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(action_frame, text="Buscar Produto", command=self.search_product)
        search_button.grid(row=0, column=2, padx=5)

        filter_button = ttk.Button(action_frame, text="Filtrar/Ordenar", command=self.filter_products)
        filter_button.grid(row=0, column=3, padx=5)

        reset_button = ttk.Button(action_frame, text="Restaurar Ordem Original", command=self.reset_order)
        reset_button.grid(row=0, column=4, padx=5)

        self.populate_tree()

    def populate_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for product in self.products:
            self.tree.insert("", "end", values=(product['id'], product['name'], product['category'], product['quantity'], f"R$ {product['price']:.2f}"))

    def add_product(self):
        name = self.name_entry.get().strip()
        category = self.category_entry.get().strip()
        try:
            quantity = int(self.quantity_entry.get().strip())
            price = float(self.price_entry.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e preço devem ser valores numéricos válidos.")
            return

        if not name or not category:
            messagebox.showerror("Erro", "Nome e categoria não podem estar vazios.")
            return

        add_product(name, category, quantity, price)
        self.products = load_products()
        self.original_products = list(self.products)
        self.populate_tree()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

    def update_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um produto para atualizar.")
            return

        item = self.tree.item(selected_item)
        product_id = item['values'][0]

        def save_update():
            name = name_entry.get().strip()
            category = category_entry.get().strip()
            try:
                quantity = int(quantity_entry.get().strip()) if quantity_entry.get().strip() else None
                price = float(price_entry.get().strip()) if price_entry.get().strip() else None
            except ValueError:
                messagebox.showerror("Erro", "Quantidade e preço devem ser valores numéricos válidos.")
                return

            update_product(product_id, name, category, quantity, price)
            self.products = load_products()
            self.original_products = list(self.products)
            self.populate_tree()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            update_window.destroy()

        update_window = tk.Toplevel(self.root)
        update_window.title("Atualizar Produto")

        ttk.Label(update_window, text="Nome:").grid(row=0, column=0)
        name_entry = ttk.Entry(update_window)
        name_entry.grid(row=0, column=1)
        name_entry.insert(0, item['values'][1])

        ttk.Label(update_window, text="Categoria:").grid(row=1, column=0)
        category_entry = ttk.Entry(update_window)
        category_entry.grid(row=1, column=1)
        category_entry.insert(0, item['values'][2])

        ttk.Label(update_window, text="Quantidade:").grid(row=2, column=0)
        quantity_entry = ttk.Entry(update_window)
        quantity_entry.grid(row=2, column=1)
        quantity_entry.insert(0, item['values'][3])

        ttk.Label(update_window, text="Preço:").grid(row=3, column=0)
        price_entry = ttk.Entry(update_window)
        price_entry.grid(row=3, column=1)
        price_entry.insert(0, item['values'][4].replace("R$ ", ""))

        save_button = ttk.Button(update_window, text="Salvar", command=save_update)
        save_button.grid(row=4, columnspan=2, pady=10)

    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir.")
            return

        item = self.tree.item(selected_item)
        product_id = item['values'][0]

        confirm = messagebox.askyesno("Confirmação", f"Deseja realmente excluir o produto ID {product_id}?")
        if confirm:
            delete_product(product_id)
            self.products = load_products()
            self.original_products = list(self.products)
            self.populate_tree()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

    def search_product(self):
        query = simpledialog.askstring("Buscar Produto", "Digite o ID ou parte do nome do produto:")
        if query:
            self.products = search_products(query)
            self.populate_tree()

    def filter_products(self):
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Filtrar/Ordenar Produtos")

        def apply_filter():
            criteria = filter_var.get()
            if criteria == "name":
                self.products.sort(key=lambda x: x['name'].lower())
            elif criteria == "quantity":
                self.products.sort(key=lambda x: x['quantity'])
            elif criteria == "price":
                self.products.sort(key=lambda x: x['price'])
            elif criteria == "category":
                category = category_entry.get().strip()
                self.products = [p for p in self.original_products if category.lower() in p['category'].lower()]

            self.populate_tree()
            filter_window.destroy()

        filter_var = tk.StringVar(value="name")

        ttk.Label(filter_window, text="Ordenar por:").grid(row=0, column=0, pady=5)
        ttk.Radiobutton(filter_window, text="Nome", variable=filter_var, value="name").grid(row=1, column=0, pady=2)
        ttk.Radiobutton(filter_window, text="Quantidade", variable=filter_var, value="quantity").grid(row=2, column=0, pady=2)
        ttk.Radiobutton(filter_window, text="Preço", variable=filter_var, value="price").grid(row=3, column=0, pady=2)

        ttk.Label(filter_window, text="Filtrar por categoria:").grid(row=4, column=0, pady=5)
        category_entry = ttk.Entry(filter_window)
        category_entry.grid(row=5, column=0, pady=2)

        apply_button = ttk.Button(filter_window, text="Aplicar", command=apply_filter)
        apply_button.grid(row=6, column=0, pady=10)

    def reset_order(self):
        self.products = list(self.original_products)
        self.populate_tree()

# Inicializar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManagerApp(root)
    root.mainloop()
