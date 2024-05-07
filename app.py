from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from utility import collect_messages

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

system_context = '''
    You are FitJoe. FitJoe is an expert fitness bot trained to \
    provide personalized food suggestions based on users' goals \
    and nutritional requirements. FitJoe will analyze the input \
    provided by the user and generate customized recommendations \
    to help them achieve their desired fitness outcomes. \
    FitJoe prioritizes the user's health and safety, and it is \
    programmed to promote balanced and nutritious eating habits. \
    FitJoe may also offer additional guidance, motivation, and tips \
    to support users in their fitness journey. Now, how can I assist \
    you today?
'''

class ChatHandler(Resource):
    def __init__(self, **kwargs):
        self.context = [{"role": "system",
                        "content": system_context}]

    def options(self):
        response = jsonify(success=True)
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        return response

    def get(self):
        try:
            response = jsonify(context=self.context)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        except Exception as e:
            print(f"An error occurred while handling GET request: {str(e)}")
            return jsonify(error="An error occurred while handling the request."), 500

    def post(self):
        try:
            rqs = request.json
            prompt = rqs.get('prompt')
            context = rqs.get('context')

            response = jsonify(collect_messages(prompt, context))
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        except Exception as e:
            print(f"An error occurred while handling POST request: {str(e)}")
            return jsonify(error="An error occurred while handling the request."), 500


api.add_resource(ChatHandler, '/')

if __name__ == '__main__':
    app.run(debug=True)
