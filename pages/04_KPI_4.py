# Import streamlit and other libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

st.title('KPI 4: Oferta Anual de Cursos en la Plataforma')

st.markdown('### Meta: incrementar en un 5% el numero cursos ofertado en relación al año anterior')

# Connect to the local MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PeliNegraBlanca",
    database="pid_mooc"
)

# Query the udemy_courses table and store the result in a dataframe
query = """
SELECT published_year, is_paid, 
       COUNT(course_id) AS total_courses
FROM udemy_courses
GROUP BY published_year, is_paid
ORDER BY published_year;
"""
df = pd.read_sql(query, db)

# Add a sidebar with a selectbox to choose the type of courses to show
st.sidebar.title("Filters")
course_type = st.sidebar.selectbox("Select the type of courses to show", ["Todos", "Pagado", "Gratis"])

# Filter the dataframe according to the selected course type
if course_type == "Todos":
    df_filtered = df
elif course_type == "Pagado":
    df_filtered = df[df["is_paid"] == "True"]
else:
    df_filtered = df[df["is_paid"] == "False"]

# Pivot the filtered dataframe to get the total courses by year and course type
df_pivoted = df_filtered.pivot(index="published_year", columns="is_paid", values="total_courses")

# Plot the pivoted dataframe as a stacked bar chart using matplotlib
plt.figure(figsize=(10, 6))
df_pivoted.plot(kind="bar", stacked=True, ax=plt.gca())
plt.xlabel('Año')
plt.ylabel('Numero de Cursos')
plt.title(f'KPI: Oferta anual de cursos, {course_type}')
plt.grid()

# Display the chart in the streamlit app
st.pyplot(plt)
