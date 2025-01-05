from flask import Flask, render_template, request
from PIL import Image
import random

app = Flask(__name__)

# Causas del cambio climático
Causas = {
    "Deforestación": "La deforestación contribuye significativamente al cambio climático al liberar grandes cantidades de dióxido de carbono (CO₂) almacenado en los árboles y el suelo, exacerbando el efecto invernadero. Al talar bosques, se pierde la capacidad de los árboles para absorber CO₂, lo que aumenta la concentración de gases de efecto invernadero en la atmósfera. Además, la pérdida de bosques afecta los ecosistemas, disminuyendo la biodiversidad y alterando los patrones climáticos locales. Esta desregulación contribuye a fenómenos climáticos extremos, como sequías, incendios forestales e inundaciones, lo que agrava aún más los impactos del cambio climático en el planeta.",
    "Agricultura intensiva": "La agricultura intensiva contribuye al cambio climático a través de la emisión de gases de efecto invernadero como el metano y el óxido nitroso, generados principalmente por la ganadería y el uso excesivo de fertilizantes y pesticidas. Además, los métodos intensivos tienden a requerir grandes cantidades de agua, lo que puede agotar los recursos hídricos y alterar los ecosistemas acuáticos. La deforestación para la expansión agrícola también reduce la capacidad de los bosques para absorber CO₂, lo que intensifica el calentamiento global. Asimismo, la erosión del suelo y la pérdida de su biodiversidad afectan la estabilidad del medio ambiente, agravando los impactos del cambio climático.",
    "Industrialización": "La industrialización es una de las principales fuentes de emisiones de gases de efecto invernadero, como dióxido de carbono (CO₂) y óxidos de nitrógeno, debido al uso intensivo de combustibles fósiles en procesos de producción y generación de energía. Además, las actividades industriales generan residuos tóxicos y contaminantes que afectan tanto el aire como los cuerpos de agua, lo que agrava la contaminación ambiental. La expansión de infraestructuras industriales también contribuye a la deforestación y la pérdida de hábitats naturales, lo que reduce la capacidad del medio ambiente para mitigar los efectos del cambio climático, exacerbando el calentamiento global y sus efectos adversos en ecosistemas y comunidades humanas.",
    "Transporte": "El transporte es uno de los mayores contribuyentes al cambio climático, principalmente debido a su dependencia de combustibles fósiles como la gasolina y el diésel. Los vehículos, aviones, barcos y trenes emiten grandes cantidades de dióxido de carbono (CO₂) y otros gases contaminantes que aceleran el calentamiento global. Además, la expansión de infraestructuras de transporte, como carreteras y aeropuertos, contribuye a la pérdida de hábitats naturales y ecosistemas, lo que agrava aún más los efectos del cambio climático. El transporte sostenible, como la adopción de vehículos eléctricos y sistemas de transporte público, es fundamental para reducir estos impactos negativos."
}

# Rutas a imágenes
Imagenes = [
    "/static/a.png",
    "/static/b.png",
    "/static/c.png"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    imagen_url = None

    if request.method == 'POST':
        causa = request.form.get('causa')
        if causa in Causas:
            mensaje = Causas[causa]
            imagen_url = random.choice(Imagenes)  # Selecciona una imagen aleatoria
        else:
            mensaje = "Causa no encontrada"

    return render_template('index.html', mensaje=mensaje, imagen_url=imagen_url, causas=Causas.keys())
    

if __name__ == '__main__':
    app.run(debug=True)
