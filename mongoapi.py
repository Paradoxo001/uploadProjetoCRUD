from pymongo import MongoClient
from flask import Request
# import logging as log

class MongoAPI:
    def __init__(self, data):
        # base MongoDB
        self.client = MongoClient("mongodb://localhost:27017/")
        # coletar database, colletion, itens
        database = data['database']             
        collection = data["collection"]
        cursor = self.client[database]
        self.Livros = cursor[collection]
        self.data = data

    def read(self):
        # log.info('Reading All Data')
        # identificar dentro da collection / comando read .find()
        documentos = self.Livros.find()
        saida = [{item: data[item] for item in data if item != '_id'} for data in documentos]
        print(saida)
        return saida

    def write(self, data):
        # log.info('Writing Data')
        # adquirir valores do item
        novo_item = data['Document']
        # comando de create .insert_one()
        response = self.Livros.insert_one(novo_item)
        saida = {'Status': 'CRIADO COM SUCESSO',}
        return saida

    def update(self):
        # log.info('Updating Data')
        # identificar um já existente e alterar (self)
        filtro = self.data['Document']
        updated_data = {"$set": self.data['nova_info']}
        # comando update .update()
        response = self.Livros.update_one(filtro, updated_data)
        saida = {'Status': 'ATUALIZADO COM SUCESSO' if response.modified_count > 0 else "NADA FOI ATUALIZADO"}
        return saida

    def delete(self, data):
        # log.info('Deleting Data')
        # identificar um já existente (args)
        filtro = data['Document']
        # comando delete .delete()
        response = self.Livros.delete_one(filtro)
        saida = {'Status': 'DELETADO COM SUCESSO' if response.deleted_count > 0 else "DOCUMENTO NAO ENCONTRADO"}
        return saida