from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    #libros = requests.get('http://api_libros:8000/libros').json()
    #usuarios = requests.get('http://api_usuarios:8001/usuarios').json()
    #prestamos = requests.get('http://api_prestamos:8002/prestamos').json()
    libros = requests.get('http://lb-prod-proyecto-498384887.us-east-1.elb.amazonaws.com:8000/libros').json()
    usuarios = requests.get('http://lb-prod-proyecto-498384887.us-east-1.elb.amazonaws.com:8001/usuarios').json()
    prestamos = requests.get('http://lb-prod-proyecto-498384887.us-east-1.elb.amazonaws.com:8002/prestamos').json()
    return render_template('index.html', libros=libros['libros'], usuarios=usuarios['usuarios'], prestamos=prestamos['prestamos'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)