Paralelismo > Velocidad, resolver rapido
Concurrencia > Non-deterministic, manejar lo impredecible.
Distribución > Computar en red. Paralelismo + Concurrencia + Trust + Fault tolerance


PARALELISMO

Esto aplica a DATA y a TASKs
-Paralelismo implicito > Nace del compilador o runtime.
-Threading implícito > Annotations del Dev.
-Threading explicito > Dev especifica sectores con paralelismo.


DETERMINISMO

Multiples hilos de ejecucion pueden generar resultados distintos en distintos runs.
Lenguajes con:
-Paralelismo implicito.
-Threading implícito.
Ocultan el no-determinismo y garantizan semántica secuencial.

Lenguajes con
-Threading explicito
Manejan la concurrencia naturalmente desde design.


SHARED MEM VS SHARED-NOTHING

Lenguajes con Shared-mem, threads se comunican con mecanismos simil lenguajes 
imperativos.
Lenguajes con Shared-nothing, threads se comunican por mensajería entre ellos.
Shared-nothing igual puede ser implementado con espacios de direccion de memoria compartidos.


POR QUE CONCURRENCIA?

-Para sistemas REACTIVOS que lidian con no determinismo (ejecuciones no lineales).
-Es una abstraccion clara para esas interacciones, sin acoplar al Dev a los
procesos internos de ejecución (abstraccion de alto nivel).
-Desacoplarse del manejo de hilos de ejecucion permite implementar mas paralelismo.


SINCRONIZACION Y COMUNICACION

Son dos tipos de interaccion entre threads.
-Comunicacion: Como pasar data de un thread a otro?
-Sincronizacion: Como ordenar la ejecucion de threads?
	-Exclusion mutua > mutex
	-Sincronizacion condicionada > signal de uno dispara al otro (Semaforos)
Sus implementaciones son condiciones criticas de diseño.


COMPLEJIDAD DE LA CONCURRENCIA

La dificultad de la concurrencia esta cementada en que en el modelo dominante
de desarrollo en lenguajes concurrentes, la memoria compartida fuerza el uso
de locks y condiciones de acceso a variables.
La programacion con memoria compartida requiere approach defensivo para 
proteger los datos de los races de threads.
La syncro y comunicacion estan desacopladas.
Shared States conllevan baja modularidad.


SOFTWARE TRANSACTIONAL MEMORY (STM)

Instrucciones atomicas aseguran transaccionalidad protegida y potencian
el paralelismo de forma simple e intuitiva. Pero internamente conflictuan
en anidamientos, excepciones, I/O y atomicidad fuerte o debil.
Ademas, no soporta de forma directa syncro condicional.


MESSAGE PASSING (CSP)

by Tony Hoare (1978).
Sistema de mensajeria con interfaces definidas entre componentes independientes,
secuenciales. Genera encapsulamiento natural y permite extender a sistemas
distribuidos mas facilmente. Compatible con programacion funcional (cada hilo 
es una funcion recursiva).
DA ORIGEN A ConcurrentML Y OCCAM family languages.


CHANNELS

De aqui en adelante, consideraremos unicamente canales con pasajes de
mensajes sincronizados. 


STREAMS CONCURRENTES

Un programa concurrente generador y otro filtrador de los valores generadores.

CONCURRENCIA CLIENTE-SERVIDOR

Queues de consumidor y productor. Cada instancia tiene un par de canales
de set y get.

CHOICE OPERATOR

Operador que permite a un thread el bloqueo de multiples canales a la espera
de nuevos mensajes.


COMUNICACION INTEPROCESOS (IPC)

* Suelen involucrar multiples mensajes.
* Los procesos interactuan con distintos partners (operador choice no
deterministico)

Estas caracteristicas de IPC puede generar conflictos .


CONCURRENT ML

* Choice dificulta severamente la abstraccion del manejo de mensajes.
* CML usa eventos para syncro.
* Ademas provee event combinators para construir protocolos abstractos.
* Los eventos son abstracciones first-class de operaciones sincronicas. ie:
recibir un mensaje, o un timeout.
* Constructores de eventos-base crean valores para primitivas de comunicacion.

OTRAS ABSTRACCIONES:

* Futures
* Promises (async RPC)
* Actors
* Join patterns


FAMILIA LINDA

Tuple spaces, memoria asociativa compartida. Tiene 3 operaciones:
* output: agrega tuplas al espacio.
* input: borra una tupla de un espacio de tuplas.
* read: lee una tupla de un espacio de tupla sin quitarlo.

Funciona como un stack, parece.

Un tuple spaces puede implementarse de dos formas:
* READ-ALL, WRITE-ONE
	Las operaciones write solo las realiza un procesador unico.
	Todos los procesadores trabajan en operaciones input y read.
* READ-ONE, WRITE-ALL

Son espacios de memoria concurrentes.


IMPLEMENTACION DE CONCURRENCIA EN LENGUAJES FUNCIONALES

Los lenguajes funcionales son plataformas eficientes de implementaciones de 
features de concurrencia.
Donde mas se lucen este maridaje es con lenguajes que aceptan first-class 
continuations.

CONTINUATIONS

Concepto semanticos que capturan el significado de RESTO DEL PROGRAMA.
Son utiles para controles de flujo y composiciones de funciones.

COROUTINES

Forks, de procesos o funciones, se llevan bien con continuations.


