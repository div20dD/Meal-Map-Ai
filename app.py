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
        
Day 7 #
import streamlit as st
import random

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="MealMap AI",
    page_icon="🍽️",
    layout="centered"
)

# -----------------------
# TITLE
# -----------------------
st.title("🍽️ MealMap AI")
st.subheader("Your Goals. Your Budget. Your Perfect Plate.")

st.write("Generate a personalized 7-day meal plan based on your lifestyle and preferences.")

st.divider()

# -----------------------
# INPUTS
# -----------------------
age = st.number_input("Age", min_value=10, max_value=100, value=22)

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=26.0, step=0.1)

budget = st.selectbox(
    "Budget",
    ["Low", "Medium", "High"]
)

goal = st.selectbox(
    "Health Goal",
    ["Weight Loss", "Maintenance", "Muscle Gain"]
)

cuisine = st.selectbox(
    "Cuisine Preference",
    ["Indian", "Mediterranean", "Mixed"]
)

ingredients = st.text_area(
    "Available Ingredients (comma separated)",
    placeholder="eggs, chicken, rice, tomato"
)

# -----------------------
# DATA
# -----------------------
breakfasts = {
    "Indian": ["Idli + Sambar", "Upma", "Poha", "Masala Omelette", "Dosa + Chutney"],
    "Mediterranean": ["Greek Yogurt + Fruit", "Omelette + Salad", "Hummus Toast", "Oats + Nuts", "Egg Wrap"],
    "Mixed": ["Oats", "Eggs Toast", "Fruit Bowl", "Smoothie", "Yogurt Bowl"]
}

lunches = {
    "Indian": ["Rice + Dal", "Chicken Curry + Rice", "Paneer + Roti", "Vegetable Pulao", "Egg Curry + Rice"],
    "Mediterranean": ["Grilled Chicken Bowl", "Rice + Chickpeas", "Salad + Protein", "Wrap + Veggies", "Fish + Rice"],
    "Mixed": ["Rice + Chicken", "Pasta + Veggies", "Wrap + Protein", "Salad Bowl", "Rice + Beans"]
}

dinners = {
    "Indian": ["Soup + Roti", "Grilled Chicken", "Khichdi", "Paneer Stir Fry", "Light Curry + Rice"],
    "Mediterranean": ["Soup + Salad", "Chicken + Veggies", "Rice Bowl", "Lentil Soup", "Grilled Fish"],
    "Mixed": ["Soup", "Chicken Salad", "Rice + Veggies", "Omelette", "Sandwich"]
}

snacks = ["Fruit", "Nuts", "Boiled Eggs", "Yogurt", "Dark Chocolate", "Roasted Chickpeas"]

# -----------------------
# LOGIC
# -----------------------
def calorie_note(goal):
    if goal == "Weight Loss":
        return "Focus on portion control and lean proteins."
    elif goal == "Muscle Gain":
        return "Increase protein intake and balanced calories."
    return "Maintain balanced portions and consistency."

def grocery_tip(budget):
    if budget == "Low":
        return "Buy eggs, rice, lentils, oats, frozen vegetables in bulk."
    elif budget == "Medium":
        return "Mix fresh proteins, vegetables, and grains."
    return "Use premium fresh produce and lean protein options."

def generate_plan():
    plan = []

    for day in range(1, 8):
        breakfast = random.choice(breakfasts[cuisine])
        lunch = random.choice(lunches[cuisine])
        dinner = random.choice(dinners[cuisine])
        snack = random.choice(snacks)

        day_plan = f"""
### Day {day}
**Breakfast:** {breakfast}  
**Lunch:** {lunch}  
**Dinner:** {dinner}  
**Snack Swap:** {snack}
"""
        plan.append(day_plan)

    return plan

# -----------------------
# BUTTON
# -----------------------
st.divider()

if st.button("🍽️ Generate Meal Plan"):

    if ingredients.strip() == "":
        st.warning("Please enter available ingredients.")
    else:
        st.success("Meal Plan Ready!")

        st.write("## 📅 Your 7-Day Plan")

        weekly_plan = generate_plan()

        for day in weekly_plan:
            st.markdown(day)

        st.divider()

        st.write("## 🧠 Health Note")
        st.info(calorie_note(goal))

        st.write("## 🛒 Grocery Tip")
        st.success(grocery_tip(budget))

        st.write("## 📌 Based On Your Inputs")
        st.write(f"Age: {age} | BMI: {bmi} | Goal: {goal} | Cuisine: {cuisine}")
