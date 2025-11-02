from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_rout = Blueprint("cliente", __name__)

"""listar os clientes"""
@cliente_rout.route('/')
def lista():
    return render_template('lista_cliente.html', clientes= CLIENTES)

"""inserir os dados do cliente"""
@cliente_rout.route('/', methods=['POST'])
def obeter_cliente():
    
    data = request.get_json(silent=True) or request.form  

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data.get('nome'),   
        "gmail": data.get('gmail')  
    }

    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)


"""formulário para cadrastrar o cliente""" 
@cliente_rout.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

"""Exibir detalhes de um cliente"""
@cliente_rout.route('/<int:client_id>')
def detalhe_cliente(client_id):
    cliente= list(filter(lambda c: c['id'] == client_id, CLIENTES))[0]
    return render_template('detalhes_cliente.html', cliente= cliente)

"""Formulário para editar um cliente"""
@cliente_rout.route('/<int:client_id>/edit')
def form_edit_cliente(client_id):
    
    cliente = None
    for c in CLIENTES:
        if c ['id'] == client_id:
            cliente= c 

    return render_template('form_cliente.html', cliente= cliente)

"""Atualizar informações do cliente"""
@cliente_rout.route('/<int:client_id>/update', methods=['POST'])
def update_cliente(client_id):
    cliente_editado = None
    data = request.json

    for c in CLIENTES:
        if c['id'] == client_id:
            c['nome'] = data ['nome']
            c['gmail'] = data ['gmail']

            cliente_editado = c 

    return render_template('item_cliente.html', cliente= cliente_editado)
    
"""Deletar informações do cliente"""
@cliente_rout.route('/<int:client_id>/delete', methods=['DELETE'])
def deletar_cliente(client_id):
    
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c ['id'] != client_id  ]

    return {"Cliente deletado": "ok"}  


