from django.test import TestCase
from django.urls import reverse
from loja.models import Produto

class LojaTestesGerais(TestCase):
    def setUp(self):
        self.produto1 = Produto.objects.create(nome='Camiseta', preco=49.90, estoque=10)
        self.produto2 = Produto.objects.create(nome='Calça', preco=89.90, estoque=5)

    # ---------- MODELO PRODUTO ----------
    def test_criacao_produto(self):
        self.assertEqual(self.produto1.nome, 'Camiseta')
        self.assertEqual(self.produto1.preco, 49.90)
        self.assertEqual(self.produto1.estoque, 10)

    def test_str_produto(self):
        self.assertEqual(str(self.produto2), 'Calça')

    # ---------- VIEW LISTA PRODUTOS ----------
    def test_view_lista_produtos_status_code(self):
        response = self.client.get(reverse('lista_produtos'))
        self.assertEqual(response.status_code, 200)

    def test_view_lista_produtos_template(self):
        response = self.client.get(reverse('lista_produtos'))
        self.assertTemplateUsed(response, 'loja/lista_produtos.html')

    def test_view_lista_produtos_conteudo(self):
        response = self.client.get(reverse('lista_produtos'))
        self.assertContains(response, 'Camiseta')
        self.assertContains(response, 'Calça')

    # ---------- CARRINHO ----------
    def test_adicionar_ao_carrinho_novo_produto(self):
        response = self.client.get(reverse('adicionar_ao_carrinho', args=[self.produto1.id]))
        self.assertEqual(response.status_code, 302)  # redireciona após adicionar
        session = self.client.session
        carrinho = session.get('carrinho', {})
        self.assertIn(str(self.produto1.id), carrinho)
        self.assertEqual(carrinho[str(self.produto1.id)], 1)

    def test_adicionar_produto_ja_existente_no_carrinho(self):
        self.client.get(reverse('adicionar_ao_carrinho', args=[self.produto1.id]))
        self.client.get(reverse('adicionar_ao_carrinho', args=[self.produto1.id]))
        session = self.client.session
        carrinho = session.get('carrinho', {})
        self.assertEqual(carrinho[str(self.produto1.id)], 2)

    def test_adicionar_dois_produtos_diferentes(self):
        self.client.get(reverse('adicionar_ao_carrinho', args=[self.produto1.id]))
        self.client.get(reverse('adicionar_ao_carrinho', args=[self.produto2.id]))
        session = self.client.session
        carrinho = session.get('carrinho', {})
        self.assertEqual(len(carrinho), 2)
        self.assertEqual(carrinho[str(self.produto1.id)], 1)
        self.assertEqual(carrinho[str(self.produto2.id)], 1)
