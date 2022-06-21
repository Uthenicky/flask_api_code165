from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


identitas = {}


class ExResource(Resource):
    def get(self):
        # response = {"msg": "Wellcome"}
        return identitas

    def post(self):
        nama = request.form['nama']
        umur = request.form['umur']

        identitas['nama'] = nama
        identitas['umur'] = umur

        response = {"msg": "Berhasil"}
        return response


api.add_resource(ExResource, "/api", methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
