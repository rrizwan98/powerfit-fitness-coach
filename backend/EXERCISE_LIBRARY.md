# PowerFit Exercise Library

## Overview

The Exercise Library contains **30+ comprehensive exercises** covering all major muscle groups. Each exercise includes:
- Detailed instructions (5-7 steps)
- Form tips and common mistakes
- Video tutorials (YouTube links)
- Alternative exercises
- Injury-specific modifications
- Progression paths
- Recommended rep ranges

## Exercise Categories

### 1. Chest (3 exercises)
- **Bench Press** - Intermediate barbell compound movement
- **Push-ups** - Beginner bodyweight staple
- **Dumbbell Flyes** - Intermediate chest isolator

### 2. Back (3 exercises)
- **Pull-ups** - Advanced bodyweight compound
- **Barbell Rows** - Intermediate compound movement
- **Deadlift** - Advanced compound (full body)

### 3. Legs (3 exercises)
- **Squats** - Intermediate compound (lower body)
- **Lunges** - Beginner unilateral movement
- **Romanian Deadlift** - Intermediate hamstring focused

### 4. Shoulders (3 exercises)
- **Overhead Press** - Intermediate barbell compound
- **Lateral Raises** - Beginner isolation exercise
- **Face Pulls** - Beginner rear deltoid exercise

### 5. Arms (3 exercises)
- **Barbell Curl** - Beginner bicep exercise
- **Tricep Dips** - Intermediate compound movement
- **Skull Crushers** - Intermediate tricep isolator

### 6. Core (3 exercises)
- **Plank** - Beginner isometric core exercise
- **Russian Twists** - Beginner oblique exercise
- **Hanging Leg Raises** - Advanced lower ab exercise

## Using the Exercise Library

### For AI Coach
The fitness coach agent uses these tools:

1. **`search_exercises(category, difficulty, equipment, muscle_group)`**
   - Find exercises by any criteria
   - Returns matching exercises with key details
   - Example: "Search for beginner chest exercises with dumbbells"

2. **`get_exercise_details(exercise_name)`**
   - Get complete details for one exercise
   - Includes instructions, form tips, video link
   - Returns injury-specific alternatives

3. **`get_exercise_alternatives(exercise_name, injury_type)`**
   - Find alternatives for an exercise
   - Filter by injury (shoulder, knee, elbow, lower_back, wrist)
   - Helps accommodate member injuries

### For Members

Members can ask for:
- "How do I do a bench press?"
- "Show me beginner chest exercises"
- "What can I do instead of squats? I have a knee injury"
- "Exercises using dumbbells for shoulders"

## Exercise Data Structure

Each exercise contains:

```python
{
    "category": "Chest",  # Chest, Back, Legs, Shoulders, Arms, Core
    "primary_muscles": ["Pectoralis Major"],  # Main muscles worked
    "secondary_muscles": ["Triceps"],  # Supporting muscles
    "difficulty": "Intermediate",  # Beginner, Intermediate, Advanced
    "equipment": ["Barbell", "Bench"],  # Required equipment
    "instructions": ["Step 1", "Step 2", ...],  # 5-7 step instructions
    "form_tips": "Keep shoulder blades...",  # Form focus
    "video_url": "https://youtube.com/...",  # Video tutorial
    "alternatives": ["Exercise 1", "Exercise 2"],  # General alternatives
    "injury_alternatives": {  # Injury-specific modifications
        "shoulder": ["Floor Press", "Cable Press"],
        "lower_back": ["Incline Press"],
        "wrist": ["Machine Press"]
    },
    "common_mistakes": "Bouncing bar...",  # What to avoid
    "rep_range": "Strength: 3-6 reps..."  # Rep ranges for goals
}
```

## Injury Accommodations

For members with injuries, the library offers modifications:

### Common Injuries
- **Shoulder Injuries** - Use neutral grip, machines, cables
- **Elbow Injuries** - Avoid sharp bends, use cables
- **Lower Back Injuries** - Use machines, short ranges, less weight
- **Knee Injuries** - Avoid deep squats, use leg press
- **Wrist Injuries** - Use machines, avoid heavy barbell

### Example Modifications

**Member with shoulder injury:**
- Can't do: Bench Press, Overhead Press, Pull-ups
- Can do: Floor Press, Landmine Press, Cable Rows

**Member with knee injury:**
- Can't do: Deep Squats, Lunges, Jump training
- Can do: Leg Press, Box Squats, Swimming

## Creating Workout Plans

The AI coach uses the library to create personalized plans:

1. **Assess member:** fitness level, injuries, equipment, time
2. **Select exercises:** from library matching criteria
3. **Build routine:** balance muscle groups, progressive overload
4. **Track progress:** log exercises and weight/reps
5. **Adjust:** modify based on feedback and results

## Adding New Exercises

To add new exercises to the library:

1. Include all required fields
2. Add 5-7 clear instruction steps
3. Include form tips and common mistakes
4. Add video tutorial link
5. List alternatives and injury modifications
6. Test with members

---

**PowerFit Exercise Library - Complete and Ready for Coaching!**
