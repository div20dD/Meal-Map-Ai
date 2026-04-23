import streamlit as st

st.set_page_config(page_title="MealMap AI", page_icon="🍽️")

st.title("🍽️ MealMap AI")
st.subheader("Your Goals. Your Budget. Your Perfect Plate.")

st.divider()

# Inputs
age = st.number_input("Age", 10, 100, 22)
bmi = st.number_input("BMI", 10.0, 50.0, 26.0)
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
goal = st.selectbox("Goal", ["Weight Loss", "Maintenance", "Muscle Gain"])
cuisine = st.selectbox("Cuisine Preference", ["Indian", "Mediterranean", "Mixed"])
ingredients = st.text_area("Available Ingredients")

st.divider()

# Simple logic (no API required for safe demo)
def generate_plan():
    return f"""
7-Day Meal Plan ({cuisine} Style)

Based on:
- Age: {age}
- BMI: {bmi}
- Budget: {budget}
- Goal: {goal}
- Ingredients: {ingredients}

Day 1:
Breakfast: Oats / Eggs
Lunch: Rice + Vegetables
Dinner: Protein + Salad

Day 2:
Breakfast: Fruits + Yogurt
Lunch: Rice + Chicken / Paneer
Dinner: Light Soup + Salad

Day 3–7:
Mix of balanced meals using available ingredients with rotation for variety.

Snack Ideas:
- Fruits
- Nuts
- Yogurt
- Boiled eggs

Grocery Tip:
Focus on affordable proteins, vegetables, and whole grains.
"""

# Button
if st.button("Generate Meal Plan 🍽️"):
    if ingredients.strip() == "":
        st.warning("Please enter ingredients first.")
    else:
        st.success("Meal Plan Generated!")
        st.write(generate_plan())
