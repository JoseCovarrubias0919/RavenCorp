from flask import Flask, render_template, request, url_for, redirect, jsonify
from Calificar_Encuesta import Calificar

app = Flask(__name__)
#@app.before_request()
#def before_request():
  #print("Antes de la peticion")

#@app.after_request()
#def after_request(response):
  #print("Despues de la peticion")
  #return response

@app.route('/')
def principal():

  return render_template('encuestaCoca.html')

@app.route('/enviar', methods=['POST'])
def recibir_datos():
    data = request.get_json()

    #print(data)
    # Procesar los datos recibidos
    ids = []
    respuestas = []
    clasificacion = Calificar()
    
    for item in data:
        id = item['id']
        texto = item['texto']
        ids.append(id)
        respuestas.append(texto)
    
    calificacion_total = clasificacion.ejecutar(numero_pregunta = ids, respuesta = respuestas)
    print(calificacion_total)
    return render_template('encuestaCoca.html', calificacion_total = calificacion_total)

#Sirve para pasar parametros cambiantes de manera dinamica podemos pasar todo lo que queramos siempre y cuando sepamos la cantida
#de datos que van a pasar
def query_string():
  print(request)
  print(request.args)
  print(request.args.get('param1'))
  print(request.args.get('param2'))
  return "OK"

#Sireve para cuando ecurra el error 404 se redireccione a 404.html que una pagina que nosotros hemos diseñado en caso de que se busque
#una pagina existente
#El segundo return es un redireccinaminto de otra manera un html ya existente
def pagina_no_encontrada (error):
  return render_template('404.html'), 404
  #return redirect(url_for('Pruebas'))

if __name__ == '__main__':
  app.add_url_rule('/query_string', view_func=query_string)
  app.register_error_handler(404, pagina_no_encontrada)
  app.run(debug=True)