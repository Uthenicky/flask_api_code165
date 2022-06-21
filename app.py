from ast import Try
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

api = Api(app)
CORS(app)

db = SQLAlchemy(app)
basedir = os.path.dirname(os.path.abspath(__file__))
database = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database


class ModelDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    umur = db.Column(db.Integer)
    alamat = db.Column(db.TEXT)

    # membuat method untuk menyimpan data agar lebih simple
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True

        except:
            return False


db.create_all()

identitas = {}


class ExResource(Resource):
    def get(self):
        # response = {"msg": "Wellcome"}
        return identitas

    def post(self):
        namax = request.form['nama']
        umurx = request.form['umur']
        alamatx = request.form['alamat']

        model = ModelDatabase(nama=namax, umur=umurx, alamat=alamatx)
        model.save()

        response = {
            "msg": "Berhasil",
            "code": 200,
            "data": identitas
        }
        return response


api.add_resource(ExResource, "/api", methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
