from flask import Flask,request,abort

app = Flask(__name__)

usuarios=[1,2,3,4,5]

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def getuser(user_id):
    if request.method == 'GET':
        return ""
    if request.method == 'POST':
        return ""
    if request.method == 'DELETE':
        return ""
    else:
        abort(405,description="Method not allowed")

app.run(host='0.0.0.0', port=5000)
