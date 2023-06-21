# Import streamlit and other libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

st.title('KPI 2: Suscriptores Anuales a la Plataforma')

st.markdown('### Meta: incrementar en un 10% el numero de suscriptores en relación al año anterior')

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
       SUM(num_subscribers) AS total_subscribers
FROM udemy_courses
GROUP BY published_year
ORDER BY published_year;
"""
df = pd.read_sql(query, db)

# Plot the total_subscribers column as a bar chart using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['published_year'], df['total_subscribers'], color='green')
plt.xlabel('Año')
plt.ylabel('Suscriptores en millones')
plt.title('KPI: Suscriptores totales en la plataforma')
plt.grid()

# Display the chart in the streamlit app
st.pyplot(plt)

