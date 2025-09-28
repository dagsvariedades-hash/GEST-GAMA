from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

videos = {
    "inicial": [
        {"titulo": "Modulo Inicial", "url": "https://www.youtube.com/embed/S3PR6wZLHac"},
        
    ],
    "servicios": [{"titulo": "Reportes Avanzados", "url": "https://www.youtube.com/embed/ID3"}],
    "admin":     [{"titulo": "Gestión de Usuarios", "url": "https://www.youtube.com/embed/ID4"}],
    "usuario":   [{"titulo": "Uso Diario", "url": "https://www.youtube.com/embed/ID5"}],
    "adminsec":  [{"titulo": "Delegación de Tareas", "url": "https://www.youtube.com/embed/ID6"}],
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/modulo/<name>')
def modulo(name):
    if name not in videos:
        return "Módulo no encontrado", 404
    return render_template(f'modulo_{name}.html', vids=videos[name], modulo=name.capitalize())

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Aquí podrías procesar el formulario, enviar correo, etc.
        return redirect(url_for('home'))
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

