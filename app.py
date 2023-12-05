from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    #def get(self):
        #data = pd.read_csv('users.csv')
        #data = data.to_dict('records')
        #return {'data' : data}, 200

    def get(self):
        try:
            data = pd.read_csv('users.csv')
            data = data.to_dict('records')
            return {'data': data}, 200
        except FileNotFoundError:
            # Dosya bulunamazsa 404 hatası döndürür.
            return {'error': 'Dosya bulunamadı'}, 404
        except Exception as e:
            # Diğer hatalar için genel bir hata mesajı döndürür.
            return {'error': f'Hata oluştu: {str(e)}'}, 500

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'name'      : [args['name']],
            'age'       : [args['age']],
            'city'      : [args['city']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('users.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        name = request.args['name']
        data = pd.read_csv('users.csv')

        if name in data['name'].values:
            data = data[data['name'] != name]
            data.to_csv('users.csv', index=False)
            return {'message': 'Record successfully deleted.'}, 200
        else:
            return {'message': 'Record not found.'}, 404

class Cities(Resource):
    def get(self):
        data = pd.read_csv('users.csv',usecols=[2])
        data = data.to_dict('records')
        return {'data' : data}, 200

class Name(Resource):
    def get(self,name):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this name !'}, 404


# Add URL endpoints
api.add_resource(Users, '/users')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/<string:name>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
    app.run()
