# EL4203 - Programación Avanzada

## Proyecto Semestral: Sistemas de Potencia (Opción A)

Universidad de Chile — Facultad de Ciencias Físicas y Matemáticas
Departamento de Ingeniería Eléctrica

## Descripción

Este repositorio contiene el desarrollo del proyecto semestral del curso
EL4203, correspondiente a la Opción A del catálogo: un simulador de una red
eléctrica de potencia. El objetivo del proyecto es que el software sea
capaz de realizar, en etapas sucesivas, el despacho económico de
generadores y la resolución del flujo de potencia simplificado (DC) de la
red, a partir de una arquitectura orientada a objetos que represente los
elementos físicos del sistema.

El desarrollo se organiza en tres hitos, de acuerdo con la pauta del curso.
Actualmente el repositorio se encuentra en la etapa correspondiente al
Hito 2, en la que se implementó el despacho económico de los generadores
mediante un algoritmo de ordenamiento propio y se incorporó el acceso a
las barras mediante tablas hash.

## Estructura del repositorio

El paquete `modelos` agrupa las clases que representan los elementos
físicos de la red (`ElementoRed` y sus subclases), mientras que `gestores`
agrupa las clases encargadas de administrar la topología y la operación
del sistema, actualmente representada por `SistemaPotencia`. Por último,
el paquete `algoritmos` reúne los algoritmos implementados desde cero que
utiliza el sistema, como el ordenamiento de los generadores.

## Arquitectura orientada a objetos

Para esta primera etapa, se diseñó una jerarquía de clases que abstrae los
elementos físicos del sistema eléctrico a entidades lógicas:

- **`ElementoRed`**: superclase abstracta de la que heredan todos los
  elementos de la red. Define los atributos comunes (`id_elemento`,
  `nombre`) y obliga a cada subclase a implementar su propio método
  `resumen()`.
- **`Barra`**: representa un nodo de la red, donde se conectan
  generadores, cargas y líneas de transmisión.
- **`Generador`**: modela un generador, con su potencia máxima, costo
  operativo y potencia despachada. Estos atributos se protegen mediante
  encapsulamiento, de forma que no sea posible despachar más potencia de
  la físicamente disponible.
- **`Carga`**: representa una demanda del sistema conectada a una barra.
- **`LineaTransmision`**: conecta dos barras de la red a través de su
  reactancia.
- **`SistemaPotencia`**: clase gestora que administra la topología
  completa, validando que cada elemento agregado sea del tipo correcto,
  que no existan identificadores duplicados y que las barras referenciadas
  estén previamente registradas en el sistema.

El diagrama de clases UML correspondiente a esta arquitectura se encuentra
en el informe entregado para el Hito 1.

## Despacho económico y tablas hash

Para el Hito 2, se implementó en `SistemaPotencia` el despacho económico
por orden de mérito. Los generadores se ordenan desde el más barato hasta
el más caro según su costo operativo, y luego se despachan en ese orden,
entregando cada uno la potencia que falta por cubrir sin superar su
potencia máxima. En caso de que dos generadores tengan el mismo costo, se
despacha primero el de menor identificador.

El ordenamiento se realiza mediante **Mergesort**, implementado desde cero
en `algoritmos/ordenamiento.py`, sin recurrir a las funciones de
ordenamiento nativas de Python. Se optó por este algoritmo debido a que su
complejidad es O(n log n) incluso en el peor caso, a diferencia de
Quicksort, que puede degradarse a O(n²). De esta forma, el despacho
completo resulta O(n log n) para n generadores.

Por otra parte, las barras, generadores, cargas y líneas se almacenan en
diccionarios indexados por su identificador. Esto permite acceder a
cualquier barra mediante `obtener_barra()` en tiempo constante O(1) en
promedio, en lugar del tiempo O(n) que requeriría una búsqueda secuencial
en una lista.

## Estado del proyecto

- **Hito 1 (completado)**: arquitectura orientada a objetos,
  encapsulamiento de los límites físicos del sistema y esqueleto funcional
  del código.
- **Hito 2 (actual)**: implementación de Mergesort para el despacho
  económico, uso de tablas hash para el acceso a las barras y análisis de
  complejidad Big-O. Los métodos `construir_ybus()` y `resolver_flujo()`
  se encuentran declarados, pero su implementación corresponde al Hito 3.
- **Hito 3 (pendiente)**: vectorización con NumPy para el ensamblaje de la
  matriz de admitancia nodal y la resolución del flujo de potencia, junto
  con la generación de gráficos bajo el estándar IEEE.

## Ejecución

El archivo `main.py` construye una red de ejemplo y permite verificar el
correcto funcionamiento de las clases y sus validaciones, el acceso a las
barras por su identificador y el despacho económico. Para ejecutarlo,
basta con correr, desde la raíz del repositorio:

```
python main.py
```
