import streamlit as st
import requests

st.title("Buscador de Recetas por Ingrediente")

def buscar_recetas(ingrediente):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingrediente}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("meals", [])
    return []

ingrediente_input = st.text_input("Ingresa un ingrediente (ejemplo: chicken, tomato, rice)")

if ingrediente_input:
    recetas = buscar_recetas(ingrediente_input)
    if recetas:
        st.write(f"Recetas con {ingrediente_input}:")
        for receta in recetas:
            st.subheader(receta['strMeal'])
            st.image(receta['strMealThumb'], width=300)
            st.markdown(f"[Ver detalles y pasos](https://www.themealdb.com/meal.php?c={receta['idMeal']})")
            st.write("---")
    else:
        st.write("No se encontraron recetas con ese ingrediente.")
