#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisilaisasi objek flask
app = Flask(__name__)

#inisialisasi onjek flask restful
api = Api(app)

#inisialisasi objek flask cors
CORS(app)

#inisialisasi variabel kosong bertipe dictionary
identitas = {} #variabel global, dictionary = json terdiri dari key: value

#membuat class Resource
class ContohResource(Resource):
    #method get dan post
    def get(self):
        #response = {"msg": "Halo dunia, ini restfull pertamaku"}
        
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        
        response = {"msg":"Data berhasil dimasukkan"}
        
        return response

#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True)
    
        
    
