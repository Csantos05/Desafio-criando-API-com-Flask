from flask import Flask, jsonify, request
app = Flask(__name__)

clientes = [

    {
        'id': 1,
        'nome': 'Jorge Santos',
        'CPF': '000.000.000.10',
        'endereco': 'Rua das Flores/ n. 10',
        'email': 'jorgesantos@email.com',
        'telefone': '(21)00000-0001'
    },
    {
        'id': 2,
        'nome': 'Paulo Almeida',
        'CPF': '111.111.111.20',
        'endereco': 'Rua Imperador/ n. 1102',
        'email': 'pauloalmeida@email.com',
        'telefone': '(11)11111-1110'
    },

    {
        'id': 3,
        'nome': 'Sandra Silva',
        'CPF': '222.222.222.30',
        'endereco': 'Rua Imperador/ n. 1102',
        'email': 'sandrasilva@email.com',
        'telefone': '(45)22222-2220'
    },

    {
        'id': 4,
        'nome': 'Maria dos Anjos',
        'CPF': '333.333.333.40',
        'endereco': 'Rua da Esperança/ n. 28',
        'email': 'jmariadosanjos.com',
        'telefone': '(24)33333-3330'
    },

    {
        'id': 5,
        'nome': 'Carlos Novaes',
        'CPF': '444.444.444.50',
        'endereco': 'Rua da Independência/ n. 300',
        'email': 'jorgesantos@email.com',
        'telefone': '(22)44444-4440'

    },
]




# Consultar (Clientes)

@app.route('/clientes',methods=['GET'])
def consultar_cliente():
    return jsonify(clientes)



# Consultar(id)

@app.route('/clientes/<int:id>',methods=['GET'])
def consultar_cliente_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)

# Editar (Clientes)

@app.route('/clientes/<int:id>',methods=['PUT'])
def editar_cliente_id(id):
    cliente_editado = request.get_json()
    for nome in enumerate(clientes):
        if clientes.get('id') == id:
            clientes[nome].update(cliente_editado)
            return jsonify(nome[clientes])

# Cadastrar (Clientes)

@app.route('/clientes',methods=['POST'])
def cadastrar_novo_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)

# Excluir um (Cliente)

@app.route('/clientes/<int:id>',methods=['DELETE'])
def excluir_cliente(cliente):
    for nome in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[nome]
            return jsonify(clientes)

app.run(port=5000,host='localhost',debug=True)

from flask import Flask, jsonify, request
app = Flask(__name__)

contas = [

    {
    'id': 1,
    'nome': 'Jorge Santos',
    'agencia': '0001',
    'tipo_conta': 'C/C',
    'deposito': 'R$ 5200,00',
    'saque': 'R$ 500,00',
    'saldo': 'R$ 4700,00'

    },
    {
        'id': 2,
        'nome': 'Paulo Almeida',
        'agencia': '0001',
        'tipo_conta': 'C/C',
        'deposito': 'R$ 2000,00',
        'saque': 'R$ 500,00',
        'saldo': 'R$ 1500,00'

    },
    {
        'id': 3,
        'nome': 'Sandra Silva',
        'agencia': '0001',
        'tipo_conta': 'C/C',
        'deoósito': 'R$ 2800,00',
        'saque': 'R$ 100,00',
        'saldo': 'R$ 2700,00'
    },
    {
        'id': 4,
        'nome': 'Maria dos Anjos',
        'agencia': '0001',
        'tipo_conta': 'C/C',
        'deposito': 'R$ 3000,00',
        'saque': 'R$ 200,00',
        'saldo': 'R$ 2800,00'

    },
    {
        'id': 5,
        'nome': 'Carlos Novaes',
        'agencia': '0001',
        'tipo_conta': 'C/C',
        'deposito': 'R$ 4850,00',
        'saque': 'R$ 500,00',
        'saldo': 'R$ 4350,00'

    },
]


# Consultar (Contas)

@app.route('/contas',methods=['GET'])
def consultar_contas():
    return jsonify(contas)








