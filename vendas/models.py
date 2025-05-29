from django.db import models

class Venda(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    dt_venda = models.DateField
    
    def valor_total(self):
        return self.quantidade * self.produto.preco
    
    def __str__(self):
        return f"Cliente: {self.cliente}/nProduto: {self.produto.nome}\nValor total: {self.valor_total()}"