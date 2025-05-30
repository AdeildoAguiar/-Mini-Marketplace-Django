from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    estoque = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
