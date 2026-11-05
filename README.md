# Sistemas de Potencia: Despacho Económico y Flujo de Red

**Universidad de Chile**
Facultad de Ciencias Físicas y Matemáticas
Departamento de Ingeniería Eléctrica

EL4203 – Programación Avanzada · Proyecto Semestral · Primavera 2026

---

## Descripción

El presente repositorio contiene el desarrollo del proyecto semestral del curso EL4203, correspondiente a la Opción A del catálogo: un simulador de sistemas de potencia. Se busca modelar una red eléctrica compuesta por barras interconectadas mediante líneas de transmisión, en las cuales se conectan generadores que inyectan energía y cargas que la consumen.

El simulador tiene como objetivo resolver dos problemas fundamentales de la operación de un sistema interconectado:

1. **Despacho económico:** determinar qué generadores deben encenderse, y con cuánta potencia, para satisfacer la demanda al menor costo posible, considerando sus costos marginales.
2. **Flujo de potencia simplificado (DC):** ensamblar la matriz de admitancia nodal ($Y_{bus}$) a partir de la topología de la red y resolver los voltajes de cada barra ante distintas inyecciones de corriente.

## Estructura del repositorio

```
.
├── gestores/
│   ├── __init__.py
│   └── sistema_potencia.py
├── modelos/
│   ├── __init__.py
│   ├── elemento_red.py
│   ├── barra.py
│   ├── generador.py
│   ├── carga.py
│   └── linea_transmision.py
├── main.py
├── LICENSE
└── README.md
```

La carpeta `modelos/` agrupa las clases que representan los elementos físicos de la red, mientras que `gestores/` contiene la clase encargada de administrarlos en conjunto. Se optó por esta separación para que cada paquete tenga una responsabilidad única: los modelos describen *qué es* cada elemento, y el gestor define *cómo se relacionan* dentro del sistema.

## Arquitectura orientada a objetos

La arquitectura se diseñó en torno a una superclase abstracta de la cual heredan todos los elementos de la red, y una clase gestora que los administra.

- **`ElementoRed`:** clase abstracta que concentra lo común a todo elemento de la red, es decir, un identificador único de solo lectura y un nombre. Declara además el método abstracto `resumen()`, el cual cada subclase implementa a su manera, de modo que el sistema puede describir cualquier elemento sin conocer su tipo concreto (polimorfismo).
- **`Barra`:** representa un nodo de la red, en el cual se conectan generadores, cargas y extremos de líneas. Almacena su voltaje en p.u., que se valida para que no sea negativo.
- **`Generador`:** representa una central conectada a una barra. Su potencia máxima, costo operativo y potencia despachada se protegen mediante atributos privados, accesibles únicamente a través de *getters* y *setters* que impiden despachar más energía de la físicamente posible.
- **`Carga`:** representa una demanda de potencia activa conectada a una barra, la cual no puede ser negativa.
- **`LineaTransmision`:** une dos barras distintas y almacena su reactancia, que se exige positiva, ya que el modelo considera líneas puramente inductivas y en el flujo DC se utiliza su inverso.
- **`SistemaPotencia`:** clase gestora que almacena barras, generadores, cargas y líneas en diccionarios indexados por ID. Se encarga de rechazar identificadores duplicados, de verificar que cada elemento se conecte a una barra previamente registrada y de exponer las colecciones únicamente en modo de lectura.

Cabe destacar que la validación de cada elemento es responsabilidad de su propia clase, mientras que la coherencia de la red en su conjunto es responsabilidad del gestor.

## Estado del proyecto

| Hito | Contenido | Estado |
|------|-----------|--------|
| Hito 1 | Arquitectura POO, diagrama UML y repositorio | Completado |
| Hito 2 | Ordenamiento, tablas hash y análisis Big-O | En desarrollo |
| Hito 3 | Ensamblaje de $Y_{bus}$ con NumPy y gráficos IEEE | Pendiente |

Los métodos `despacho_economico()`, `construir_ybus()` y `resolver_flujo()` se encuentran declarados en `SistemaPotencia`, aunque su implementación se realizará en los hitos correspondientes.

## Ejecución

Se requiere Python 3. Desde la carpeta raíz del repositorio, se ejecuta:

```bash
python main.py
```

El script construye una red de ejemplo con dos barras, un generador, una carga y una línea, muestra su resumen y los totales de demanda y capacidad, y luego intenta una serie de operaciones inválidas para evidenciar que cada validación las rechaza.

## Autor

Ignacio Figueroa

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Para más detalles, se puede consultar el archivo [LICENSE](LICENSE).
