#import library

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#import library sqlalchemy
from flask_sqlalchemy import SQLAlchemy 
import os

# Inisilaisasi objek flask
app = Flask(__name__)

#inisialisasi onjek flask restful
api = Api(app)

#inisialisasi objek flask cors
CORS(app)

#inisialisasi objek flask sqlalchemy
db = SQLAlchemy(app)

#mengkonfigurasi database 
basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database

#membuat database model
class ModelDatabase(db.Model):
    #membuat field/column
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    umur = db.Column(db.Integer)
    alamat = db.Column(db.TEXT) #field tambahan
    
    #membuat method untuk menyimpan data agar lebih simple
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            
            return True
        except:
            return False
     
   
#mengcreate database
db.create_all()
        
#inisialisasi variabel kosong bertipe dictionary
identitas = {} #variabel global, dictionary = json terdiri dari key: value

#membuat class Resource
class ContohResource(Resource):
    #method get dan post
    def get(self):
        #response = {"msg": "Halo dunia, ini restfull pertamaku"}
        
        return identitas
    
    def post(self):
        data_nama = request.form["nama"]
        data_umur = request.form["umur"]
        data_alamat = request.form["alamat"]
        
        #memasukkan data ke database model
        model = ModelDatabase(
            nama=data_nama, 
            umur=data_umur, 
            alamat=data_alamat
        )
        model.save()
        
        response = {
            "msg":"Sukses mazseeee",
            "code": 200
        }
        
        return response

#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True)
    