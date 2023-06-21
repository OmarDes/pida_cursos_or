# Import streamlit and other libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

st.title('KPI 3: Ingresos Anuales de la Plataforma')

st.markdown('### Meta: incrementar en un 5% el ingreso monetario en relación al año anterior')

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
       SUM(price * num_subscribers) AS total_income
FROM udemy_courses
GROUP BY published_year
ORDER BY published_year;
"""
df = pd.read_sql(query, db)

# Plot the total_income column as a line chart using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df['published_year'], df['total_income'], marker='o', color='red')
plt.xlabel('Año')
plt.ylabel('Ingreso Total en cientos de millones de dolares')
plt.title('KPI: Ingreso anual de la plataforma')
plt.grid()

# Display the chart in the streamlit app
st.pyplot(plt)
