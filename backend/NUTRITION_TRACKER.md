# PowerFit Nutrition Tracker

## Overview

The Nutrition Tracker helps members:
- Log meals with calories and macros
- Track daily nutrition totals
- Get meal suggestions based on calories remaining
- Monitor water intake
- Achieve fitness goals through nutrition

## Core Features

### 1. Meal Logging (`log_meal`)
Log meals with complete nutritional info:

**Parameters:**
- `member_name`: Who's logging the meal
- `date`: When (YYYY-MM-DD)
- `meal_type`: breakfast, lunch, dinner, or snack
- `food_items`: What was eaten (e.g., "2 eggs, whole wheat toast, avocado")
- `calories`: Total calories in the meal
- `protein`: Grams of protein
- `carbs`: Grams of carbohydrates
- `fat`: Grams of fat
- `notes`: Optional notes about the meal

**Example:**
```python
log_meal(
    member_name="John",
    date="2024-03-15",
    meal_type="breakfast",
    food_items="Oatmeal, blueberries, almond butter",
    calories=450,
    protein=15,
    carbs=55,
    fat=12
)
```

### 2. Daily Nutrition Summary (`get_daily_nutrition_summary`)
Show comprehensive daily nutrition:

**Shows:**
- Total calories consumed vs. target
- Remaining calories for the day
- Macro breakdown (protein, carbs, fat)
- Calorie percentages for each macro
- Meals breakdown by type

**Example Output:**
```
Calories: 1850/2000 kcal (remaining: 150)

Macros:
  Protein: 145g (580 kcal, 31%)
  Carbs: 220g (880 kcal, 48%)
  Fat: 65g (585 kcal, 31%)

Meals Breakdown:
  Breakfast - 450 kcal
  Lunch - 750 kcal
  Dinner - 650 kcal
```

### 3. Meal Suggestions (`suggest_meals`)
Suggest meals based on remaining calories and preferences:

**Criteria:**
- `remaining_calories`: How many calories left for the day
- `member_name`: To get diet preferences and allergies
- `meal_type`: Type of meal (breakfast, lunch, dinner, snack)

**Smart Suggestions by Calories:**
- **< 200 kcal**: Light snacks (Greek yogurt, apple, shake)
- **200-400 kcal**: Light meals (salad, wrap, smoothie bowl)
- **400-600 kcal**: Full meals (grilled chicken, fish, tofu stir-fry)
- **600+ kcal**: Large meals (steak, pasta, burrito bowl)

**Diet-Aware:**
- Omnivore: All meals
- Vegetarian: No meat/fish
- Vegan: No animal products
- Keto: Low carb, high fat
- Paleo: No grains, dairy, legumes

**Allergy-Aware:**
- Filters out allergenic foods
- Customizes suggestions

**Example:**
```
Remaining: 350 kcal
Diet: Vegetarian
Allergies: Peanuts

Suggestions:
1. Quinoa Buddha Bowl - 380 kcal
2. Egg White Omelette & Toast - 300 kcal
3. Protein Smoothie Bowl - 320 kcal
```

### 4. Water Tracking (`log_water_intake`, `get_water_intake_summary`)
Monitor daily hydration:

**Daily Goal:** 8 glasses (8oz each = 64oz total)

**Log Water:**
```python
log_water_intake(
    member_name="John",
    date="2024-03-15",
    glasses=3  # 3 glasses consumed
)
```

**Shows:**
- Current progress (e.g., 5/8 glasses - 62%)
- Visual progress bar
- Remaining glasses needed
- Weekly summary and trends

## Nutrition Data Structure

### Meal Record
```python
{
    "member_name": "John",
    "date": "2024-03-15",
    "meal_type": "breakfast",
    "food_items": "Oatmeal, blueberries, almond butter",
    "calories": 450,
    "protein": 15,
    "carbs": 55,
    "fat": 12,
    "notes": "Added honey",
    "logged_at": "2024-03-15T08:30:00"
}
```

### Water Intake Record
```python
{
    "member_name": "John",
    "date": "2024-03-15",
    "glasses": 8,
    "notes": "Hydrated during workout",
    "logged_at": "2024-03-15T18:45:00"
}
```

## Macro Calculations

### Calorie Conversions
- **Protein:** 4 calories per gram
- **Carbs:** 4 calories per gram
- **Fat:** 9 calories per gram

### Macro Percentages
```
Protein % = (Protein grams × 4) / Total calories × 100
Carbs % = (Carbs grams × 4) / Total calories × 100
Fat % = (Fat grams × 9) / Total calories × 100
```

## Common Macro Splits

### Weight Loss (Calorie Deficit)
- **40% Protein, 40% Carbs, 20% Fat**
- High protein to preserve muscle
- Moderate carbs for energy
- Lower fat for calorie reduction

### Muscle Gain (Calorie Surplus)
- **30% Protein, 50% Carbs, 20% Fat**
- Adequate protein for muscle synthesis
- Higher carbs for training fuel
- Moderate fat for hormones

### Balanced/General Fitness
- **30% Protein, 40% Carbs, 30% Fat**
- Balanced approach
- Sustainable long-term
- Good for general health

## Member Nutrition Profile

Stored in member profile:
```python
{
    "diet_type": "vegetarian",  # Dietary preference
    "allergies": "peanuts, shellfish",  # Allergies
    "calorie_target": 2000,  # Daily calorie goal
    "current_weight": 75,  # kg
    "target_weight": 70,  # kg
}
```

## AI Coach Integration

The fitness coach uses nutrition tools to:

1. **Log meals:** When members eat
2. **Track progress:** Daily nutrition summary
3. **Suggest meals:** Based on remaining calories
4. **Provide guidance:** Macro balancing tips
5. **Monitor hydration:** Daily water intake
6. **Celebrate wins:** "You hit your calorie goal!"
7. **Adjust plans:** Based on nutrition progress

## Tips for Accurate Logging

1. **Be honest:** Log everything you eat
2. **Use a food scale:** For accurate portions
3. **Check labels:** For calorie/macro info
4. **Use apps:** MyFitnessPal, Cronometer for database
5. **Log immediately:** Don't rely on memory
6. **Include drinks:** Smoothies, coffee, sodas
7. **Track condiments:** Oils, sauces add calories

---

**PowerFit Nutrition Tracker - Complete and Ready!**
