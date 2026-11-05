"""Prueba simple del esqueleto del sistema de potencia.
"""
from modelos.barra import Barra
from modelos.carga import Carga
from modelos.generador import Generador
from modelos.linea_transmision import LineaTransmision
from gestores.sistema_potencia import SistemaPotencia
 
# 1. Crear el sistema y las barras
sistema = SistemaPotencia()
b1 = Barra("B1", "Quillota")
b2 = Barra("B2", "Santiago")
sistema.agregar_barra(b1)
sistema.agregar_barra(b2)
 
# 2. Crear y agregar generador, carga y línea
g1 = Generador("G1", "Central Norte", 200, 35, b1)
c1 = Carga("C1", "Demanda Santiago", 150, b2)
l1 = LineaTransmision("L1", "Linea 1-2", b1, b2, 0.1)
sistema.agregar_generador(g1)
sistema.agregar_carga(c1)
sistema.agregar_linea(l1)
 
# 3. Mostrar la red y los totales
print("--- Red ---")
print(sistema.resumen())
print("\nDemanda total:", sistema.demanda_total(), "MW")
print("Capacidad total:", sistema.capacidad_total(), "MW")
 
# 4. Usar los setters (despachar potencia)
print("\n--- Despacho ---")
g1.potencia_despachada = 150
print(g1)
 
# 5. Pruebas de validación (cada una debe dar un error)
print("\n--- Validaciones ---")
 
try:
    g1.potencia_despachada = 500
except ValueError as e:
    print("Despachar de más:", e)
 
try:
    c1.demanda_activa = -10
except ValueError as e:
    print("Demanda negativa:", e)
 
try:
    LineaTransmision("L2", "Linea mala", b1, b1, 0.1)
except ValueError as e:
    print("Origen igual a destino:", e)
 
try:
    LineaTransmision("L3", "Linea mala", b1, b2, 0)
except ValueError as e:
    print("Reactancia cero:", e)
 
try:
    sistema.agregar_generador(Generador("G1", "Repetido", 50, 10, b1))
except ValueError as e:
    print("ID repetido:", e)
 
try:
    sistema.agregar_carga(Carga("C2", "Huérfana", 20, Barra("B9", "Nueva")))
except ValueError as e:
    print("Barra no registrada:", e)
 
try:
    g1.id_elemento = "OTRO"
except AttributeError as e:
    print("Cambiar el ID:", e)
 
# 6. Acceso a una barra por su ID (tabla hash, O(1))
print("\n--- Hash ---")
print("Barra B2:", sistema.obtener_barra("B2"))
try:
    sistema.obtener_barra("B99")
except KeyError as e:
    print("Barra inexistente:", e)

# 7. Despacho económico (Hito 2)
print("\n--- Despacho económico ---")
sistema.agregar_generador(Generador("G2", "Central Barata", 100, 20, b2))
sistema.agregar_generador(Generador("G3", "Central Cara", 80, 60, b1))
print("Demanda total:", sistema.demanda_total(), "MW")
for id_gen, potencia in sistema.despacho_economico().items():
    gen = sistema.generadores[id_gen]
    print(f"{id_gen}: {potencia} MW (costo {gen.costo_operativo} USD/MWh)")

try:
    sistema.agregar_carga(Carga("C3", "Demanda Gigante", 1000, b1))
    sistema.despacho_economico()
except ValueError as e:
    print("Demanda mayor que la capacidad:", e)

# 8. Métodos que se implementan en el Hito 3
print("\n--- Pendientes ---")
try:
    sistema.construir_ybus()
except NotImplementedError as e:
    print("construir_ybus:", e)
 