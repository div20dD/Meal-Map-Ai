# MealMap AI - System Architecture

MealMap AI follows an AI-powered pipeline that transforms user inputs into personalized meal recommendations.

## System Flow:

1. User takes a picture of their refrigerator
2. Computer vision system detects available food ingredients
3. User enters personal data:
   - Age
   - BMI
   - Dietary goal (weight loss / gain / maintenance)
   - Budget

4. LLM processes inputs and generates:
   - Personalized 7-day meal plan
   - Breakfast, lunch, and dinner suggestions

5. Nutrition API enhances results by adding:
   - Calories
   - Protein, carbs, and fats

6. Final output includes:
   - Smart meal plan
   - Grocery list for next week
   - Healthy junk food alternatives
   - Future health impact prediction
