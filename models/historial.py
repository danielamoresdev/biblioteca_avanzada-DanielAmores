from datetime import datetime

class Historial:
    def __init__(self):
        self.registros = []

    def registrar(self, accion, usuario, libro, fecha=datetime.now().isoformat()):
        self.registros.append({
            "accion": accion,
            "usuario": usuario,
            "libro": libro,
            "fecha": fecha,
        })

    def mostrar(self):
        for r in self.registros:
            print(f"[{r['fecha']}] {r['accion']} - {r['usuario']} -> {r['libro']}")