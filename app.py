from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

videos = {
    "inicial": [
        {"titulo": "Módulo Inicial", "url": "https://www.youtube.com/embed/S3PR6wZLHac"},
    ],
    "servicios": [
        {"titulo": "Servicio Documentos", "url": "https://www.youtube.com/embed/qLTjuXOJPnA"},
        {"titulo": "Servicio Backup", "url": "https://www.youtube.com/embed/WaPmLqCnt9I"},
        {"titulo": "Servicio Actividades", "url": "https://www.youtube.com/embed/l4rX6k936lI"},
    ],
    "admin": [
        {"titulo": "Módulo Administrador", "url": "https://www.youtube.com/embed/CFO7UVCBMog"}
    ],
    "usuario": [
        {"titulo": "Uso Diario", "url": "https://www.youtube.com/embed/ID5"}
    ],
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
        mensaje = request.form['mensaje']

        texto = f"""
📩 Nuevo mensaje desde la web GEST GAMA:

💬 Mensaje:
{mensaje}
"""

        try:
            client.messages.create(
                body=texto,
                from_=twilio_number,
                to=mi_numero
            )
            flash("✅ Tu mensaje fue enviado a nuestro WhatsApp", "success")
        except Exception as e:
            print("Error al enviar a WhatsApp:", e)
            flash("❌ Ocurrió un error al enviar el mensaje", "danger")

        return redirect(url_for("contacto"))

    return render_template("contacto.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
