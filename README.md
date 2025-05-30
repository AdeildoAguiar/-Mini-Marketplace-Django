
````markdown
# 🛒 Mini Marketplace Django

Um sistema simples de marketplace feito com Django, que permite listar produtos, adicionar ao carrinho, visualizar o total e finalizar uma compra. Desenvolvido como desafio avaliativo.

## 📌 Descrição

Este projeto simula um sistema básico de compras, com:

- Listagem de produtos
- Adição de produtos ao carrinho (via sessões)
- Visualização de itens no carrinho com total parcial
- Remoção de itens
- Finalização de compra com geração de pedido
- Painel administrativo Django para gerenciar produtos

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 4.x
- HTML + CSS com Bootstrap (opcional)
- SQLite (padrão do Django)

---

## 🧱 Estrutura de Dados (Models)

- **Product**
  - `nome`: CharField
  - `descricao`: TextField
  - `preco`: DecimalField

- **CartItem** (armazenado na sessão)
  - `produto_id`: ID do Produto
  - `quantidade`: int

- **Order**
  - `itens`: lista de itens (serializados no banco)
  - `total`: DecimalField
  - `data_compra`: DateTimeField

---

## 🧑‍💻 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mini-marketplace-django.git
cd mini-marketplace-django
````

### 2. Crie um ambiente virtual e ative-o

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode as migrações e crie o superusuário

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

### 6. Acesse no navegador:

* Sistema: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🎯 Funcionalidades

✅ **Produtos**

* Listar todos os produtos cadastrados
* Gerenciar produtos via Django Admin

✅ **Carrinho de Compras**

* Adicionar produto ao carrinho
* Visualizar itens e total parcial
* Remover item do carrinho

✅ **Finalizar Compra**

* Gerar pedido (Order) com itens e total
* Zerar carrinho após a finalização

---

## 🧠 Extras Implementados

* 🔒 **Carrinho baseado em sessão:** não precisa de login!
* 🎨 **Estilização com Bootstrap (opcional)**
* 🧪 **Testes automatizados para models e views**
* 📄 **Este README.md explicando tudo que você precisa saber**

---

## 🧪 Testes

Para rodar os testes:

```bash
python manage.py test
```

---

## 📁 Estrutura de Pastas (Simplificada)

```
mini_marketplace/
│
├── loja/                   # App principal
│   ├── models.py           # Models: Product, Order
│   ├── views.py            # Views para produtos, carrinho, pedido
│   ├── templates/          # Templates HTML
│   ├── tests.py            # Testes automatizados
│   └── urls.py             # Rotas do app
│
├── mini_marketplace/       # Configurações do projeto Django
├── manage.py
└── README.md
```

---

## 📦 Requisitos

* Python 3.11 ou superior
* Django 4.x


