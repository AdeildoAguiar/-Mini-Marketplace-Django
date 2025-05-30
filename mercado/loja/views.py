from django.shortcuts import render, redirect
from .models import Produto, Pedido, ItemPedido

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto = Produto.objects.get(id=produto_id)
    quantidade_atual = carrinho.get(str(produto_id), 0)

    if quantidade_atual < produto.estoque:
        carrinho[str(produto_id)] = quantidade_atual + 1
        request.session['carrinho'] = carrinho
    return redirect('lista_produtos')


def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0
    produtos = Produto.objects.filter(id__in=carrinho.keys())
    produtos_dict = {str(prod.id): prod for prod in produtos}

    for produto_id, quantidade in carrinho.items():
        produto = produtos_dict[str(produto_id)]
        subtotal = produto.preco * quantidade
        total += subtotal
        itens.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal,
        })

    return render(request, 'loja/carrinho.html', {
        'itens': itens,
        'total': total,
        'carrinho': carrinho,
        'produtos': produtos_dict,  # Necessário para o botão "Remover"
    })

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    produto_id_str = str(produto_id)
    if produto_id_str in carrinho:
        del carrinho[produto_id_str]
        request.session['carrinho'] = carrinho  # Atualiza a sessão

    return redirect('ver_carrinho')

def finalizar_pedido(request):
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        return redirect('ver_carrinho')

    pedido = Pedido.objects.create()

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        
        # Verifica estoque suficiente
        if produto.estoque < quantidade:
            messages.error(request, f"Estoque insuficiente para {produto.nome}.")
            pedido.delete()  # Cancela o pedido criado
            return redirect('ver_carrinho')
        
        # Deduz o estoque
        produto.estoque -= quantidade
        produto.save()

        # Cria o item do pedido
        ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade)
    
    # Limpa o carrinho após o pedido ser criado com sucesso
    request.session['carrinho'] = {}

    return render(request, 'loja/pedido_finalizado.html', {'pedido': pedido})