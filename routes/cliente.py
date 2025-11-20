from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_rout = Blueprint("cliente", __name__)

"""listar os clientes"""
@cliente_rout.route('/')
def lista():
    
    clientes = Cliente.select()
    return render_template('lista_cliente.html', clientes= clientes)

"""inserir os dados do cliente"""
@cliente_rout.route('/', methods=['POST'])
def obeter_cliente():
    
    data = request.get_json(silent=True) or request.form
    
    novo_usuario= Cliente.create(
        nome= data['nome'],
        gmail= data['gmail'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)

"""formulário para cadrastrar o cliente"""
@cliente_rout.route('/new')
def form_cliente():
   
    return render_template('form_cliente.html')

"""Exibir detalhes de um cliente"""
@cliente_rout.route('/<int:client_id>')
def detalhe_cliente(client_id):
   
    cliente= Cliente.get_by_id(client_id)
    return render_template('detalhes_cliente.html', cliente= cliente)

"""Formulário para editar um cliente"""
@cliente_rout.route('/<int:client_id>/edit')
def form_edit_cliente(client_id):
    
    cliente = Cliente.get_by_id(client_id)
    return render_template('form_cliente.html', cliente=cliente)

"""Atualizar informações do cliente"""
@cliente_rout.route('/<int:client_id>/update', methods=['POST'])
def update_cliente(client_id):
    data = request.json
    
    cliente_editado= Cliente.get_by_id(client_id)
    cliente_editado.nome = data['nome'] 
    cliente_editado.gmail = data ['gmail']
    cliente_editado.save()

    return render_template('item_cliente.html', cliente= cliente_editado)
    
"""Deletar informações do cliente"""
@cliente_rout.route('/<int:client_id>/delete', methods=['DELETE'])
def deletar_cliente(client_id):
    
    cliente_deletado= Cliente.get_by_id(client_id)
    cliente_deletado.delete_instance() 
    return {"Cliente deletado": "ok"}  