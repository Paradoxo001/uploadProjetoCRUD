from flask import Flask, request, render_template, Response, json
from mongoapi import MongoAPI

app = Flask(__name__)

@app.route('/')
def home():
    # flask (arquivo, parametro)
    return render_template('teste.html')
    

# methods HTTP - GET, POST, PUT, DELETE...(CRUD)
@app.route('/read', methods=['GET'])
def mongo_read():
    data = request.json
    # print(data)
    mongo = MongoAPI(data)
    response = mongo.read()
    # print(response)
   
    

@app.route('/create', methods=['POST'])
def mongo_write():
    data = request.json
    print(data)
    mongo = MongoAPI(data)
    response = mongo.write(data)
    # print(response)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/update', methods=['PUT'])
def mongo_update():
    data = request.json
    if data is None or data == {} or 'nova_info' not in data:
        return {"Erro": "Por favor digite corretamente"}
        
    mongo = MongoAPI(data)
    response = mongo.update()
    # print(response)
    

@app.route('/delete', methods=['DELETE'])
def mongo_delete():
    data = request.json
        
    mongo = MongoAPI(data)
    response = mongo.delete(data)
    # print(response)
    
  
if __name__ == '__main__':
    # create/delete
    # data = {                             
    #     "database": "CRUD_test",
    #     "collection": "Livros",
    #     "Document": {
    #         "titulo": "Harry Potter",
    #         "autor": "JK Rowling",
    #         "paginas": 342
    #      }
    # }

    #update
    data = { 
        "database": "CRUD_test",
        "collection": "Livros",
        "Document": {
            "titulo": "Harry Potter",
        },
        "nova_info": {
            "paginas": 400   
    }
    }
    mongo_obj = MongoAPI(data)
    # print(json.dumps(mongo_obj.update(), indent=3))
    print(json.dumps(mongo_obj.read(), indent=4))
    # app.run(debug=True, port=5001, host='0.0.0.0')