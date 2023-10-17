from flask import Flask, request, jsonify

app = Flask(__name__)

existing_api_key=["Wkikfjcvl24659sadlnlagfnlafnldng"]
def authenticate_api_key():
    if request.method=='POST':
        api_key=request.headers.get('API-KEY')
        if api_key not in existing_api_key:
            return False
        else:
            return True
def extract_entities(text):

    entities = ["entity1", "entity2", "entity3"]
    return entities


@app.route('/extract-entities', methods=['POST'])
def api_extract_entities():
    if request.method == 'POST':
        try:
            if authenticate_api_key():
                data = request.get_json()
                text = data['text']
                entities = extract_entities(text)
                response = {'entities': entities}
                return jsonify(response)
            else:
                return {'Error':' Invalid API KEY'},401
        except Exception as e:
            return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
