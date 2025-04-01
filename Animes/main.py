from flask import Flask, jsonify, request
from flask_cors import CORS
from random import choice

api = Flask(__name__)
CORS(api)

animes = ["Dragon Ball Z","MHA","Pokemon","Digimon","Cavaleiros do zodiaco","Dr.Stone","Spy X Family"]

@api.route('/animes', methods=['GET'])
def getAnimes():
    if len(animes) == 0: return jsonify({"ERRO":"Nenhum anime encontrado."}),404

    resposta = {
        "contagem" : len(animes),
        "animes" : animes
    }
    return jsonify(resposta), 200

# api.run(host="0.0.0.0", port=5000)

@api.route('/animes/create', methods=['POST'])
def addAnime():
    data = request.get_json()
    if ("anime" not in data): return jsonify({"error":"você precisa fornecer um nome de anime..."}),400

    anime = data["anime"].strip()
    if(not anime): return jsonify({"error":"Esse anime já existe"}),400

    animes.append(anime)
    return jsonify({"status":"success", "message":f"O anime {anime} foi inserido com sucesso!"}), 200

@api.route('/animes/<int:id>', methods=['GET'])
def getAnimeById(id):
    if (len(animes) == 0) or (id < 0) or (id >= len(animes)):
        return jsonify({"erro":"Nenhum anime encontrado"}),404
    
    resposta = {
        "anime":animes[id]
    }
    return jsonify(resposta), 200

@api.route('/animes/random', methods=['GET'])
def getRandomAnime():
    if len(animes) == 0: return jsonify({"erro":"Nenhum anime encontrado"}),404

    resposta = {
        "anime":choice(animes)
    }
    return jsonify(resposta),200

@api.route("/animes/update/<int:id>", methods=["PUT"])
def updateAnime(id:int):
    if (len(animes) == 0) or (id < 0) or (id >= len(animes)):
        return jsonify({"erro":"Nenhum anime encontrado"}),404
    data = request.get_json()
    if ("anime" not in data): return jsonify({"erro":"você precisa fornecer um nome de anime..."}),400

    animeAntigo = animes[id]
    animeNovo = data["anime"]
    animes[id] = animeNovo
    return jsonify({"status":"success", "message":F"O anime de id {id} foi alterado de {animeAntigo} para {animeNovo}"}), 200

@api.route("/animes/delete/<int:id>", methods=['DELETE'])
def deleteAnime(id:int):
    if (len(animes) == 0) or (id < 0) or (id >= len(animes)):
        return jsonify({"erro":"Nenhum anime encontrado"}),404
    
    anime = animes[id]
    animes.remove(anime)
    return jsonify({"status":"success","message":F"O anime {anime} de id {id} foi removido do sistema"}), 200