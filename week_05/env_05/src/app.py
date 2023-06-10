from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query')
    print(query)
    return {'query': query}

@app.route('/route2', methods=['POST', 'GET'])
def route2():
    if request.method == 'POST':
        data = request.get_json()
        return data
    elif request.method == 'GET':
        return 'GET'
    
if __name__ == '__main__':
    app.run(debug=False, port=5000)