import json

def agregar_carta(categoria, nivel, tipo, carta):
    with open("cartas2.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data[categoria][nivel][tipo].append(carta)

    with open("cartas2.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Carta agregada a {categoria} > nivel {nivel} > {tipo}")

# Preguntas
print("=== AGREGAR CARTA ===")
categoria = input("Categoría (hetero/gay/lesbi): ")
nivel = input("Nivel (1/2/3): ")
tipo = input("Tipo (truths/dares/strips): ")
emoji = input("Emoji: ")
texto = input("Texto de la carta: ")

carta = {"emoji": emoji, "texto": texto}

# ¿Tiene término especial?
tiene_termino = input("¿Tiene término/kink? (s/n): ")
if tiene_termino == "s":
    carta["termino"] = input("Término: ")
    carta["definicion"] = input("Definición: ")

agregar_carta(categoria, nivel, tipo, carta)