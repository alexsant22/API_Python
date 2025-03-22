from flask import Flask, jsonify, request

api = Flask(__name__) # Criando o servidor Flask

# Armazenamentos de dados
livros = [
        {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# Rotas e metodos

# Criar
@api.route('/livros/criar', methods = ['POST']) # POST
def cirar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify("Livro criado com sucesso!")

# Consultar todos
@api.route("/livros/buscar", methods = ['GET']) # GET
def obter_livros():
    return jsonify(livros)

# Consultar por ID
@api.route("/livros/buscarID/<int:id>", methods = ['GET']) # GET for by ID
def obter_livro_id(id):
    for livro in livros:
        if (livro.get('id') == id):
            return jsonify(livro)

# Editar
@api.route('/livros/editar/<int:id>', methods = ['PUT']) # PUT
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if (livro.get('id') == id):
            livros[indice].update(livro_alterado)
            
            return jsonify(livros[indice])

# Excluir
@api.route("/livros/excluir/<int:id>", methods = ['DELETE']) # DELETE
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if (livro.get('id') == id):
            del livros[indice]
            
            return jsonify("Livro excluído!")

# Rodando aplicação
api.run(port=5000, host='localhost', debug=True) # http://localhost:5000/