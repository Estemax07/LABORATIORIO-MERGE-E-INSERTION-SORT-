from typing import Union, Dict

# --- Tiempos promedio (segundos) ---
tiempos: Dict[int, Dict[str, Union[float, str]]] = {
    100:        {"py_quick": 0.000064, "java_quick": 0.000010, "py_rquick": 0.000094, "java_rquick": 0.000016},
    1_000:      {"py_quick": 0.001009, "java_quick": 0.000066, "py_rquick": 0.001203, "java_rquick": 0.000072},
    10_000:     {"py_quick": 0.011514, "java_quick": 0.000701, "py_rquick": 0.014813, "java_rquick": 0.000909},
    100_000:    {"py_quick": 0.137639, "java_quick": 0.009081, "py_rquick": 0.171342, "java_rquick": 0.008229},
    1_000_000:  {"py_quick": "NE",      "java_quick": 0.087794, "py_rquick": 2.007717, "java_rquick": 0.079267},
    10_000_000: {"py_quick": "NE",      "java_quick": 1.100883, "py_rquick": "NE",      "java_rquick": 0.897230},
}

headers = [
    "n",
    "Python/M2 Quick (s)",
    "Java/ASUS Quick (s)",
    "Python/M2 Randomized (s)",
    "Java/ASUS Randomized (s)"
]

orden = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]

def fmt(v: Union[float, str]) -> str:
    if isinstance(v, (int, float)):
        return f"{v:.6f}"
    if isinstance(v, str) and v.strip().upper() == "NE":
        return "NE"
    return str(v)

def get_val(n: int, k: str) -> str:
    if n not in tiempos:
        return "NE"
    return fmt(tiempos[n].get(k, "NE"))

# --- Construcción de filas ---
filas = []
for n in orden:
    filas.append([
        f"{n:,}".replace(",", "."),
        get_val(n, "py_quick"),
        get_val(n, "java_quick"),
        get_val(n, "py_rquick"),
        get_val(n, "java_rquick"),
    ])

# --- Render tabla con bordes ---
tabla = [headers] + filas
anchos = [max(len(str(tabla[r][c])) for r in range(len(tabla))) for c in range(len(headers))]

def sep(l, m, r, fill="─"):
    body = m.join(fill * (anchos[c] + 2) for c in range(len(anchos)))
    return l + body + r
def top(): return sep("┌", "┬", "┐")
def mid(): return sep("├", "┼", "┤")
def bot(): return sep("└", "┴", "┘")
def line(row): return "│ " + " │ ".join(str(row[c]).ljust(anchos[c]) for c in range(len(row))) + " │"

print(top())
print(line(headers))
print(mid())
for row in filas:
    print(line(row))
print(bot())
print("\nNota: 'NE' = no ejecutó en tiempo razonable (o dato no disponible).")
