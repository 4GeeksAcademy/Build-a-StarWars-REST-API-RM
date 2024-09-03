"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character,Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    try:
        query_results = User.query.all()
        print(query_results)
        results=list(map(lambda item:item.serialize(),query_results))
        print(results)
        if results:
            response_body = {
                "msg": "ok ",
                "results": results
            }

            return jsonify(response_body), 200
        return jsonify({"msg": "users not found"}),404
    except Exception as e:
        return jsonify({'error': 'Internal server error','message':str(e)}),500
    
@app.route('/characters', methods=['GET'])
def get_characters():
    try:
        #consultar al modelo todos los registros
        query_results = Character.query.all()
        print(query_results) #[<Character 1>, <Character 2>] esta informacion es un array []tenemos que transformarla en una informacion que podamos manejar por eso vamos recorrerlo y darle formato con nuestra funcion serialize que se encarga de retornar un objeto legible que yo pueda trabajar
        results= list(map(lambda item: item.serialize(),query_results)) # en el map tenemos que enviarle 2 valores, el primero la funcion lambda con  el parametro item , entonces cada vez que te posiciones sobre ese valor que se esta consultando aplicale el metodo serialize(), y el segundo valor es el nombre del array que se quiere que recorra
        print(results)#<map object at 0x749858a16ef0> nos arroja este valor en consola , tenemos que castear en la linea 62 "list(map())" y luego se obtendria [{'id': 1, 'name': 'Luke'}, {'id': 2, 'name': 'Leia'}]
        
        if results:
            response_body = {
                "msg": "ok",
                "results": results
            }
            return jsonify(response_body), 200
        return jsonify({"msg": "characters not found"}),404
    except Exception as e:
        return jsonify({'error': 'Internal server error','message':str(e)}),500

@app.route('/planets', methods=['GET'])
def get_planets():

    query_results = Planet.query.all()
    print(query_results)

    # try:
    #     query_results = Planet.query.all()
    #     results = list(map(lambda item: item.serialize(), query_results))
        
    #     if results:
    #         response_body = {
    #             "msg": "ok",
    #             "results": results
    #         }
    #         return jsonify(response_body), 200
    #     return jsonify({"msg": "Character not found"}), 404

    # except Exception as e:
    #     return jsonify({"error": "Internal server error", "message": str(e)}), 500


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
