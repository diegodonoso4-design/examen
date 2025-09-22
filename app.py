from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])

            precio_unitario = 9000
            total_sin_descuento = cantidad * precio_unitario

            if edad >= 18 and edad <= 30:
                descuento = total_sin_descuento * 0.15
            elif edad > 30:
                descuento = total_sin_descuento * 0.25
            else:
                descuento = 0


            total = total_sin_descuento - descuento

            return render_template('ejercicio1.html',
                                   nombre=nombre,
                                   total_sin_descuento=round(total_sin_descuento),
                                   descuento=round(descuento),
                                   total=round(total))
        except Exception as e:
            print(f"[ERROR EJ1] {e}")
            return render_template('ejercicio1.html', error="Error en el procesamiento del formulario")
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        'juan': {'clave': 'admin123', 'rol': 'Administrador'},
        'pepe': {'clave': 'usuario123', 'rol': 'Usuario'}
    }

    if request.method == 'POST':
        try:
            usuario = request.form['usuario']
            clave = request.form['clave']

            if usuario in usuarios and usuarios[usuario]['clave'] == clave:
                rol = usuarios[usuario]['rol']
                mensaje = f"Bienvenido {rol} {usuario}"
            else:
                mensaje = "Credenciales incorrectas."

            return render_template('ejercicio2.html', mensaje=mensaje)
        except Exception as e:
            print(f"[ERROR EJ2] {e}")
            return render_template('ejercicio2.html', mensaje="Error en el login")
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)