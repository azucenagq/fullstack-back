
from flask import Flask, render_template


# create the Flask app
app = Flask (__name__)
@app.route("/user/<nombre>") #('/pizza', methods=['POST'])
def user(nombre='Eduardo'):
  nombre = nombre
  apellido = apellido
  
  return render_template ('/user.html', nombre = nombre, apellido = apellido)
      
if __name__=='__main__':
 
         app.run(debug=True, port=8880)

#Debe recoger el parámetro Nombre, Apellidos y 
# hacer un print de losvalores para que se vea en la consola Python.
