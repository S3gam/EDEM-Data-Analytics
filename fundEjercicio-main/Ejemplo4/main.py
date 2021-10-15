from flask import Flask,request,abort,render_template

app = Flask(__name__)


HOST_IP="x.x.x.x"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bienvenida/', methods = ['POST'])
def presentarse():
    content = request.get_json()
    # POST HOST_IP
    return "Bienvenida realizada"


@app.route('/gettheball/', methods = ['POST'])
def getuser():
    if request.method == 'POST':
        content = request.get_json()
        informPedro(content["value"])
        # post new user
        return "Patata Recibida"
    else:
        abort(405)


def informPedro():
    # POST HOST_IP
    mensaje = "{ usuario: pedro, value=value}"


app.run(host='0.0.0.0', port=5000)
