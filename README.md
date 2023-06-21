# <h1 align=center> **PROYECTO INDIVIDUAL Nº2** </h1>

# <h1 align=center>**`Data Analytics`**</h1>

**Omar Giovanni Russi**

<hr>  

# **Descripción del problema**
A partir de datasets de plataformas de cursos online, se pide analizar los datos y determinar factores que aumenten la probabilidad de exito de una nueva plataforma MOOC.

# **Desarrolo del Proyecto**

## **EDA**
Se analizan los dataset con MS VS studio:
+ Se determinan las dimensiones de ambos dataset, y sus respectivos campos.

+ Al archivo de Udemy se agrega una columna aparte para el año de publicacion de cada curso.

+ El archivo donde se desarrolla el proceso es: EDA_UDEMY.ipynb

## **ETL**
Se carga dataset en una base de datos local MySQL.

## **Dashboard**

Se utiliza la libreria de python 'streamlit' para hacer la lectura y visualizacion de los datos desde la base de datos MySQL.

Las instrucciones se desarrollan en los archivos 'Resumen.py' y los que estan en la carpeta 'pages'.

El deployment se hace local.

## **KPIs**

Se analizo el dataset de Udemy. Este tiene registros en un periodo de 5 años (2012-2017), donde registra inscripciones a su oferta de cursos. Tiene cursos gratis y de pago, en los cuales detalla el valor del curso.
El KPI_1 es el sugerido. Se plantea como una tasa de conversión. Pero no es posible determinar cuando un usuario pasa de estar en un curso gratis a uno pago, si es que ese proceso se da.
Para el caso de Udemy a partir del segundo año hay un incremento de esta tasa, pero luego se estabiliza-disminuye.
El KPI_2 es el numero de suscriptores anuales en la plataforma. Los ingresos son proporcionales al numero de usuarios, incluidos los de no pago, porque eventualmente podrían acceder a cursos pagos. Al plantear una meta en este indicador se visibiliza la necesidad de establecer estrategias para captar nuevos usuarios como campanas de marketing, o en las estrategias para retener los usuarios actuales. 

El KPI_3 son los ingresos anuales totales de la plataforma, es un indicador importante desde el punto de vista financiero. Se requiere además conocer los gastos de la plataforma para saber en que momento se tiene rendimientos positivos. 
El KPI_4 es la oferta anual de cursos de la plataforma. Se observa que al aumentar este numero así mismo lo hace la cantidad de usuarios y el ingreso monetario. Mantener o aumentar la oferta de cursos puede impactar el éxito de la plataforma.
