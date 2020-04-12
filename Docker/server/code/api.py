from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
	def get(self):
		return {
			'product': ['Ice cream',
						'Chocolate',
						'Fruit']
		}
api.add_resource(Product, '/api/v1/resources/product/all')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)

#import flask
#from flask import request, jsonify
#from flask import Flask

#app = Flask(__name__)

#products = [
#	{'product': ['Ice cream',
#				'Chocolate',
#				'Fruit']
#	}
#	]

#@app.route('/api/v1/resources/product/all', methods=['GET'])
#def home():
#    return jsonify(products)
	
#if __name__ == '__main__':
#	app.run(host='0.0.0.0', port=80, debug=True)