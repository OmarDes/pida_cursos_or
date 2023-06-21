import streamlit as st

st.title('Descripcion de los KPI')

st.markdown('***')
#
st.write('Se analizo el dataset de Udemy. Este tiene registros en un periodo de 5 años (2012-2017), donde registra inscripciones a su oferta de cursos. Tiene cursos gratis y de pago, en los cuales detalla el valor del curso.')

st.write('El KPI_1 es el sugerido. Se plantea como una tasa de conversión. Pero no es posible determinar cuando un usuario pasa de estar en un curso gratis a uno pago, si es que ese proceso se da.')

st.write('Para el caso de Udemy a partir del segundo año hay un incremento de esta tasa, pero luego se estabiliza-disminuye.')

st.write('El KPI_2 es el numero de suscriptores anuales en la plataforma. Los ingresos son proporcionales al numero de usuarios, incluidos los de no pago, porque eventualmente podrían acceder a cursos pagos. Al plantear una meta en este indicador se visibiliza la necesidad de establecer estrategias para captar nuevos usuarios como campanas de marketing, o en las estrategias para retener los usuarios actuales.')

st.write('El KPI_3 son los ingresos anuales totales de la plataforma, es un indicador importante desde el punto de vista financiero. Se requiere además conocer los gastos de la plataforma para saber en que momento se tiene rendimientos positivos.')

st.write('El KPI_4 es la oferta anual de cursos de la plataforma. Se observa que al aumentar este numero así mismo lo hace la cantidad de usuarios y el ingreso monetario. Mantener o aumentar la oferta de cursos puede impactar el éxito de la plataforma')
