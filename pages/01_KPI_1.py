# Import streamlit and other libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

st.title('KPI 1: cursos pagados / número de inscriptos en cursos gratuitos * 100')

st.markdown('### Meta: incrementar la tasa en un 15% en relación al año anterior')


# Connect to the local MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PeliNegraBlanca",
    database="pid_mooc"
)

# Query the udemy_courses table and store the result in a dataframe
query = """
SELECT published_year, 
       SUM(CASE WHEN is_paid = 'True' THEN num_subscribers ELSE 0 END) AS paid_subscribers, 
       SUM(CASE WHEN is_paid = 'False' THEN num_subscribers ELSE 0 END) AS free_subscribers
FROM udemy_courses
GROUP BY published_year
ORDER BY published_year;
"""
df = pd.read_sql(query, db)

# Calculate the ratio of paid subscribers to free subscribers and add it as a new column
df['ratio'] = (df['paid_subscribers'] / df['free_subscribers'])*100

# Plot the ratio column as a line chart using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['published_year'], df['ratio'], color='blue')
plt.xlabel('Año')
plt.ylabel('Porcentaje')
plt.title('KPI: Suscritores pagos sobre suscriptores gratis')
plt.grid()

# Display the chart in the streamlit app
st.pyplot(plt)
