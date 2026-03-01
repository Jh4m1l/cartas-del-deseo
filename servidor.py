from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return open("editor.html", encoding="utf-8").read()

@app.route("/agregar", methods=["POST"])
def agregar():
    carta_nueva = request.json

    with open("cartas2.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    categoria = carta_nueva["categoria"]
    nivel = carta_nueva["nivel"]
    tipo = carta_nueva["tipo"]
    carta = {"emoji": carta_nueva["emoji"], "texto": carta_nueva["texto"]}

    if "termino" in carta_nueva:
        carta["termino"] = carta_nueva["termino"]
        carta["definicion"] = carta_nueva["definicion"]

    data[categoria][nivel][tipo].append(carta)

    with open("cartas2.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return jsonify({"ok": True})

@app.route("/cartas")
def cartas():
    categoria = request.args.get("categoria")
    nivel = request.args.get("nivel")
    tipo = request.args.get("tipo")

    with open("cartas2.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    resultado = data[categoria][nivel][tipo]
    return jsonify(resultado)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    datos = request.json

    with open("cartas2.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    categoria = datos["categoria"]
    nivel = datos["nivel"]
    tipo = datos["tipo"]
    indice = datos["indice"]

    data[categoria][nivel][tipo].pop(indice)

    with open("cartas2.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return jsonify({"ok": True})

app.run(port=5000)