import React, { useState } from "react";

const CUISINES = ["Indian","Italian","Chinese","Mexican","Japanese","Korean","Mediterranean"];

const SAMPLE = ["eggs","rice","chicken","milk","tomatoes","onions","spinach","bread","yogurt"];

export default function App() {
  const [ingredients, setIngredients] = useState([]);
  const [plan, setPlan] = useState(null);

  const scanFridge = () => {
    const detected = SAMPLE.sort(() => 0.5 - Math.random()).slice(0,5);
    setIngredients(detected);
  };

  const generatePlan = () => {
    const days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
    setPlan(days.map(d => ({
      day: d,
      meal: "Healthy " + CUISINES[Math.floor(Math.random()*CUISINES.length)] + " bowl"
    })));
  };

  return (
    <div style={{padding:20}}>
      <h1>🍽️ MealMap AI</h1>

      {/* FRIDGE */}
      <div style={box}>
        <h2>🧊 Fridge Scan</h2>
        <button onClick={scanFridge}>Scan Fridge</button>
        <p>{ingredients.join(", ")}</p>
      </div>

      {/* PLAN */}
      <div style={box}>
        <h2>📅 Meal Plan</h2>
        <button onClick={generatePlan}>Generate Plan</button>

        {plan && plan.map((p,i)=>(
          <p key={i}>{p.day}: {p.meal}</p>
        ))}
      </div>

      {/* GROCERY */}
      <div style={box}>
        <h2>🛒 Grocery List</h2>
        {ingredients.map((i,idx)=>(
          <div key={idx}>
            <input type="checkbox"/> {i}
          </div>
        ))}
      </div>
    </div>
  );
}

const box = {
  background: "white",
  padding: 15,
  marginTop: 15,
  borderRadius: 10,
  boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
};
