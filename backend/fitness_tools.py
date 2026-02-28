from agents import function_tool
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# In-memory databases (in production, use real database)
members_db: Dict[str, dict] = {}
workouts_db: List[dict] = []
progress_db: List[dict] = []
nutrition_db: List[dict] = []  # For meal logging
water_intake_db: List[dict] = []  # For water tracking

# Load data from files if they exist
DATA_DIR = os.path.dirname(__file__)
MEMBERS_FILE = os.path.join(DATA_DIR, "members_data.json")
WORKOUTS_FILE = os.path.join(DATA_DIR, "workouts_data.json")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress_data.json")
NUTRITION_FILE = os.path.join(DATA_DIR, "nutrition_data.json")
WATER_FILE = os.path.join(DATA_DIR, "water_data.json")

def load_data():
    """Load data from JSON files"""
    global members_db, workouts_db, progress_db, nutrition_db, water_intake_db

    if os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, 'r') as f:
            members_db = json.load(f)

    if os.path.exists(WORKOUTS_FILE):
        with open(WORKOUTS_FILE, 'r') as f:
            workouts_db = json.load(f)

    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            progress_db = json.load(f)

    if os.path.exists(NUTRITION_FILE):
        with open(NUTRITION_FILE, 'r') as f:
            nutrition_db = json.load(f)

    if os.path.exists(WATER_FILE):
        with open(WATER_FILE, 'r') as f:
            water_intake_db = json.load(f)

def save_data():
    """Save data to JSON files"""
    with open(MEMBERS_FILE, 'w') as f:
        json.dump(members_db, f, indent=2)

    with open(WORKOUTS_FILE, 'w') as f:
        json.dump(workouts_db, f, indent=2)

    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress_db, f, indent=2)

    with open(NUTRITION_FILE, 'w') as f:
        json.dump(nutrition_db, f, indent=2)

    with open(WATER_FILE, 'w') as f:
        json.dump(water_intake_db, f, indent=2)

# Load data on startup
load_data()


@function_tool
def save_member_profile(
    member_name: str,
    fitness_goal: str,
    fitness_level: str,
    injuries_limitations: str = "",
    equipment_access: str = "full_gym",
    time_per_workout: int = 60,
    workouts_per_week: int = 3,
    diet_type: str = "omnivore",
    allergies: str = "",
    calorie_target: Optional[int] = None,
    current_weight: Optional[float] = None,
    target_weight: Optional[float] = None
) -> str:
    profile = {
        "name": member_name,
        "fitness_goal": fitness_goal,
        "fitness_level": fitness_level,
        "injuries_limitations": injuries_limitations,
        "equipment_access": equipment_access,
        "time_per_workout": time_per_workout,
        "workouts_per_week": workouts_per_week,
        "diet_type": diet_type,
        "allergies": allergies,
        "calorie_target": calorie_target,
        "current_weight": current_weight,
        "target_weight": target_weight,
        "created_at": members_db.get(member_name, {}).get("created_at", datetime.now().isoformat()),
        "updated_at": datetime.now().isoformat()
    }

    members_db[member_name] = profile
    save_data()

    return f"✅ Profile saved for {member_name}! Goal: {fitness_goal}, Level: {fitness_level}. Ready to create your personalized workout plan! 💪"


@function_tool
def get_member_profile(member_name: str) -> str:
    if member_name not in members_db:
        return f"No profile found for {member_name}. Let's create one! What are your fitness goals?"

    profile = members_db[member_name]
    recent_workouts = [w for w in workouts_db if w["member_name"] == member_name]
    recent_workouts = sorted(recent_workouts, key=lambda x: x["date"], reverse=True)[:5]
    recent_progress = [p for p in progress_db if p["member_name"] == member_name]
    recent_progress = sorted(recent_progress, key=lambda x: x["date"], reverse=True)[:3]

    result = f"\n📋 **{member_name}'s Profile**\n\n🎯 **Goal:** {profile['fitness_goal']}\n📊 **Level:** {profile['fitness_level']}\n⏱️ **Workout Time:** {profile['time_per_workout']} min, {profile['workouts_per_week']}x/week\n🏋️ **Equipment:** {profile['equipment_access']}\n🥗 **Diet:** {profile['diet_type']}\n\n"

    if profile.get('injuries_limitations'):
        result += f"⚠️ **Limitations:** {profile['injuries_limitations']}\n"
    if profile.get('allergies'):
        result += f"🚫 **Allergies:** {profile['allergies']}\n"
    if profile.get('current_weight'):
        result += f"⚖️ **Current Weight:** {profile['current_weight']} kg\n"
    if profile.get('target_weight'):
        result += f"🎯 **Target Weight:** {profile['target_weight']} kg\n"
    if profile.get('calorie_target'):
        result += f"🔥 **Calorie Target:** {profile['calorie_target']} cal/day\n"
    if recent_workouts:
        result += f"\n📅 **Recent Workouts:** {len([w for w in workouts_db if w['member_name'] == member_name])} total\n"
    if recent_progress:
        latest = recent_progress[0]
        result += f"\n📈 **Latest Progress** ({latest['date']}):\n"
        if latest.get('weight'):
            result += f"   Weight: {latest['weight']} kg\n"
        if latest.get('body_fat_percentage'):
            result += f"   Body Fat: {latest['body_fat_percentage']}%\n"

    return result


@function_tool
def log_workout(
    member_name: str,
    date: str,
    workout_type: str,
    exercises: str,
    duration_minutes: int,
    notes: str = ""
) -> str:
    try:
        exercises_list = json.loads(exercises) if isinstance(exercises, str) else exercises
    except:
        exercises_list = [{"name": exercises, "sets": 0, "reps": 0, "weight": 0}]

    workout = {
        "member_name": member_name,
        "date": date,
        "workout_type": workout_type,
        "exercises": exercises_list,
        "duration_minutes": duration_minutes,
        "notes": notes,
        "logged_at": datetime.now().isoformat()
    }

    workouts_db.append(workout)
    save_data()
    exercise_count = len(exercises_list)

    return f"✅ Workout logged for {member_name} on {date}! 💪\n\n🏋️ {workout_type.title()} workout: {exercise_count} exercises, {duration_minutes} min\n\nKeep up the great work! 🔥"


@function_tool
def log_progress(
    member_name: str,
    date: str,
    weight: Optional[float] = None,
    body_fat_percentage: Optional[float] = None,
    measurements: Optional[str] = None,
    notes: str = ""
) -> str:
    try:
        measurements_dict = json.loads(measurements) if measurements and isinstance(measurements, str) else measurements
    except:
        measurements_dict = None

    progress = {
        "member_name": member_name,
        "date": date,
        "weight": weight,
        "body_fat_percentage": body_fat_percentage,
        "measurements": measurements_dict,
        "notes": notes,
        "logged_at": datetime.now().isoformat()
    }

    progress_db.append(progress)
    save_data()
    previous = [p for p in progress_db if p["member_name"] == member_name and p["date"] < date]
    previous = sorted(previous, key=lambda x: x["date"], reverse=True)

    result = f"✅ Progress logged for {member_name} on {date}! 📈\n\n"

    if weight:
        result += f"⚖️ Weight: {weight} kg"
        if previous and previous[0].get('weight'):
            diff = weight - previous[0]['weight']
            if diff > 0:
                result += f" (+{diff:.1f} kg)"
            elif diff < 0:
                result += f" ({diff:.1f} kg)"
        result += "\n"

    if body_fat_percentage:
        result += f"📊 Body Fat: {body_fat_percentage}%"
        if previous and previous[0].get('body_fat_percentage'):
            diff = body_fat_percentage - previous[0]['body_fat_percentage']
            if diff > 0:
                result += f" (+{diff:.1f}%)"
            elif diff < 0:
                result += f" ({diff:.1f}%)"
        result += "\n"

    if measurements_dict:
        result += f"📏 Measurements updated\n"

    result += "\nKeep tracking your progress! 💪🔥"
    return result


@function_tool
def get_workout_history(member_name: str, days: int = 30) -> str:
    cutoff_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    member_workouts = [w for w in workouts_db if w["member_name"] == member_name and w["date"] >= cutoff_date]
    member_workouts = sorted(member_workouts, key=lambda x: x["date"], reverse=True)

    if not member_workouts:
        return f"No workout history found for {member_name} in the last {days} days. Let's start logging your workouts! 💪"

    total_workouts = len(member_workouts)
    total_minutes = sum(w["duration_minutes"] for w in member_workouts)
    workout_types = {}

    for w in member_workouts:
        wtype = w["workout_type"]
        workout_types[wtype] = workout_types.get(wtype, 0) + 1

    result = f"\n📊 **{member_name}'s Workout History** (Last {days} days)\n\n✅ **Total Workouts:** {total_workouts}\n⏱️ **Total Time:** {total_minutes} minutes ({total_minutes/60:.1f} hours)\n📅 **Average:** {total_workouts/(days/7):.1f} workouts/week\n\n🏋️ **Workout Types:**\n"

    for wtype, count in sorted(workout_types.items(), key=lambda x: x[1], reverse=True):
        result += f"   • {wtype.title()}: {count}x\n"

    result += f"\n📝 **Recent Workouts:**\n"

    for workout in member_workouts[:5]:
        result += f"\n   {workout['date']} - {workout['workout_type'].title()}" 
        result += f" ({workout['duration_minutes']} min)\n"

        if workout['exercises']:
            for ex in workout['exercises'][:3]:
                result += f"      • {ex.get('name', 'Exercise')}"
                if ex.get('sets') and ex.get('reps'):
                    result += f": {ex['sets']}x{ex['reps']}"
                if ex.get('weight'):
                    result += f" @ {ex['weight']}kg"
                result += "\n"

    result += "\nKeep up the great work! 💪🔥"
    return result


from datetime import timedelta

# ============================================================================
# EXERCISE LIBRARY - 30+ Exercises with Complete Details
# ============================================================================

EXERCISE_LIBRARY = {
    "Bench Press": {"category": "Chest", "primary_muscles": ["Pectoralis Major", "Anterior Deltoids"], "secondary_muscles": ["Triceps", "Serratus Anterior"], "difficulty": "Intermediate", "equipment": ["Barbell", "Bench"], "instructions": ["Lie flat on bench with feet firmly on ground", "Grip barbell slightly wider than shoulder-width", "Lower bar to mid-chest with controlled motion", "Press bar up explosively until arms fully extended", "Keep elbows at 45-degree angle to body"], "form_tips": "Keep shoulder blades retracted, don't bounce bar off chest, maintain arch in lower back", "video_url": "https://www.youtube.com/watch?v=rT7DgCr-3pg", "alternatives": ["Dumbbell Bench Press", "Push-ups", "Machine Chest Press"], "injury_alternatives": {"shoulder": ["Floor Press", "Cable Chest Press"], "wrist": ["Machine Chest Press", "Cable Flyes"], "lower_back": ["Incline Bench Press", "Dumbbell Press"]}, "common_mistakes": "Bouncing bar, flaring elbows, lifting butt off bench", "rep_range": "Strength: 3-6 reps, Hypertrophy: 8-12 reps, Endurance: 12-15+ reps"},
    "Push-ups": {"category": "Chest", "primary_muscles": ["Pectoralis Major", "Triceps"], "secondary_muscles": ["Anterior Deltoids", "Core"], "difficulty": "Beginner", "equipment": ["Bodyweight"], "instructions": ["Start in plank position, hands slightly wider than shoulders", "Keep body in straight line from head to heels", "Lower body until chest nearly touches floor", "Push back up to starting position", "Keep core engaged throughout"], "form_tips": "Don't let hips sag, keep elbows at 45 degrees, full range of motion", "video_url": "https://www.youtube.com/watch?v=IODxDxX7oi4", "alternatives": ["Incline Push-ups", "Knee Push-ups", "Diamond Push-ups"], "injury_alternatives": {"shoulder": ["Wall Push-ups", "Incline Push-ups"], "wrist": ["Fist Push-ups", "Parallel Bar Push-ups"], "lower_back": ["Incline Push-ups", "Wall Push-ups"]}, "progressions": "Wall pushups → Incline → Standard → Decline → One-arm", "common_mistakes": "Sagging hips, incomplete range of motion, flaring elbows"},
    "Dumbbell Flyes": {"category": "Chest", "primary_muscles": ["Pectoralis Major"], "secondary_muscles": ["Anterior Deltoids"], "difficulty": "Intermediate", "equipment": ["Dumbbells", "Bench"], "instructions": ["Lie on flat bench with dumbbells above chest", "Keep slight bend in elbows throughout movement", "Lower dumbbells out to sides in wide arc", "Feel stretch in chest at bottom position", "Bring dumbbells back together at top"], "form_tips": "Don't go too heavy, maintain slight elbow bend, control the descent", "video_url": "https://www.youtube.com/watch?v=eozdVDA78K0", "alternatives": ["Cable Flyes", "Pec Deck Machine"], "injury_alternatives": {"shoulder": ["Cable Flyes (lower angle)", "Machine Flyes"], "elbow": ["Cable Flyes", "Machine Chest Press"]}, "common_mistakes": "Going too heavy, straightening arms completely, bouncing at bottom"},
    "Pull-ups": {"category": "Back", "primary_muscles": ["Latissimus Dorsi", "Biceps"], "secondary_muscles": ["Rhomboids", "Trapezius", "Rear Deltoids"], "difficulty": "Advanced", "equipment": ["Pull-up Bar"], "instructions": ["Hang from bar with hands shoulder-width apart, palms facing away", "Pull yourself up until chin is above bar", "Keep core tight and avoid swinging", "Lower yourself with control to full extension", "Repeat without momentum"], "form_tips": "Full range of motion, no kipping, engage lats not just arms", "video_url": "https://www.youtube.com/watch?v=eGo4IYlbE5g", "alternatives": ["Lat Pulldowns", "Assisted Pull-ups", "Inverted Rows"], "injury_alternatives": {"shoulder": ["Lat Pulldowns (neutral grip)", "Cable Rows"], "elbow": ["Lat Pulldowns", "Seated Cable Rows"]}, "progressions": "Assisted → Negative → Full → Weighted → One-arm", "common_mistakes": "Kipping/swinging, partial range of motion, not engaging lats"},
    "Barbell Rows": {"category": "Back", "primary_muscles": ["Latissimus Dorsi", "Rhomboids"], "secondary_muscles": ["Biceps", "Erector Spinae", "Rear Deltoids"], "difficulty": "Intermediate", "equipment": ["Barbell"], "instructions": ["Bend at hips with slight knee bend, back straight", "Grip barbell slightly wider than shoulder-width", "Pull bar to lower chest/upper abs", "Squeeze shoulder blades together at top", "Lower with control to starting position"], "form_tips": "Keep back flat, pull to chest not neck, engage lats", "video_url": "https://www.youtube.com/watch?v=FWJR5Ve8bnQ", "alternatives": ["Dumbbell Rows", "Cable Rows", "T-Bar Rows"], "injury_alternatives": {"lower_back": ["Chest-Supported Rows", "Cable Rows (seated)"], "shoulder": ["Neutral Grip Rows", "Machine Rows"]}, "common_mistakes": "Rounding back, using momentum, pulling to wrong position"},
    "Deadlift": {"category": "Back", "primary_muscles": ["Erector Spinae", "Glutes", "Hamstrings"], "secondary_muscles": ["Trapezius", "Latissimus Dorsi", "Forearms", "Core"], "difficulty": "Advanced", "equipment": ["Barbell"], "instructions": ["Stand with feet hip-width, bar over mid-foot", "Bend down and grip bar just outside legs", "Keep back neutral, chest up, shoulders over bar", "Drive through heels, lift bar by extending hips and knees", "Stand tall, then lower bar with control"], "form_tips": "Keep bar close to body, neutral spine critical, brace core", "video_url": "https://www.youtube.com/watch?v=op9kVnSso6Q", "alternatives": ["Romanian Deadlift", "Trap Bar Deadlift", "Sumo Deadlift"], "injury_alternatives": {"lower_back": ["Trap Bar Deadlift", "Rack Pulls", "Cable Pull-throughs"], "knee": ["Romanian Deadlift", "Good Mornings"], "grip": ["Trap Bar Deadlift", "Straps for conventional"]}, "common_mistakes": "Rounding back, not bracing core, bar drifting away from body", "rep_range": "Strength: 1-5 reps, Hypertrophy: 6-10 reps"},
    "Squats": {"category": "Legs", "primary_muscles": ["Quadriceps", "Glutes"], "secondary_muscles": ["Hamstrings", "Adductors", "Core", "Erector Spinae"], "difficulty": "Intermediate", "equipment": ["Barbell", "Squat Rack"], "instructions": ["Position bar on upper traps, feet shoulder-width apart", "Unrack bar and take 2-3 steps back", "Descend by pushing hips back and bending knees", "Go down until thighs are at least parallel to ground", "Drive through heels to return to standing"], "form_tips": "Keep knees tracking over toes, chest up, core braced", "video_url": "https://www.youtube.com/watch?v=ultWZbUMPL8", "alternatives": ["Front Squats", "Goblet Squats", "Leg Press", "Bulgarian Split Squats"], "injury_alternatives": {"knee": ["Box Squats", "Leg Press", "Step-ups"], "lower_back": ["Goblet Squats", "Safety Bar Squats", "Leg Press"], "ankle": ["Box Squats", "Heels Elevated Squats"]}, "common_mistakes": "Knees caving in, rounding back, not going deep enough", "rep_range": "Strength: 3-6 reps, Hypertrophy: 8-12 reps, Endurance: 15-20 reps"},
    "Lunges": {"category": "Legs", "primary_muscles": ["Quadriceps", "Glutes"], "secondary_muscles": ["Hamstrings", "Calves", "Core"], "difficulty": "Beginner", "equipment": ["Bodyweight", "Dumbbells (optional)"], "instructions": ["Stand tall with feet hip-width apart", "Step forward with one leg, lowering hips", "Lower until both knees are at 90 degrees", "Front knee should not pass toes", "Push through front heel to return to start"], "form_tips": "Keep torso upright, knee tracking over toes, full range of motion", "video_url": "https://www.youtube.com/watch?v=QOVaHwm-Q6U", "alternatives": ["Reverse Lunges", "Walking Lunges", "Bulgarian Split Squats", "Step-ups"], "injury_alternatives": {"knee": ["Reverse Lunges", "Step-ups", "Split Squats (shorter range)"], "ankle": ["Static Lunges", "Step-ups"], "balance": ["Supported Lunges", "Static Split Squats"]}, "common_mistakes": "Knee passing toes, leaning forward, not going low enough"},
    "Romanian Deadlift": {"category": "Legs", "primary_muscles": ["Hamstrings", "Glutes"], "secondary_muscles": ["Erector Spinae", "Forearms"], "difficulty": "Intermediate", "equipment": ["Barbell", "Dumbbells"], "instructions": ["Stand with feet hip-width, holding barbell at thighs", "Push hips back while keeping slight knee bend", "Lower bar along legs, feeling stretch in hamstrings", "Keep back flat and bar close to body", "Drive hips forward to return to standing"], "form_tips": "Hinge at hips not waist, keep bar close, feel hamstring stretch", "video_url": "https://www.youtube.com/watch?v=JCXUYuzwNrM", "alternatives": ["Dumbbell RDL", "Single-Leg RDL", "Good Mornings"], "injury_alternatives": {"lower_back": ["Single-Leg RDL (lighter)", "Stability Ball Hamstring Curls"], "grip": ["Dumbbell RDL", "Trap Bar RDL"]}, "common_mistakes": "Rounding back, bending knees too much, not feeling hamstrings"},
    "Overhead Press": {"category": "Shoulders", "primary_muscles": ["Anterior Deltoids", "Medial Deltoids"], "secondary_muscles": ["Triceps", "Upper Chest", "Core"], "difficulty": "Intermediate", "equipment": ["Barbell", "Dumbbells"], "instructions": ["Start with bar at shoulder height, hands just outside shoulders", "Brace core and squeeze glutes", "Press bar straight overhead until arms locked", "Move head back slightly to allow bar path", "Lower bar with control to shoulders"], "form_tips": "Keep core tight, don't lean back excessively, full lockout", "video_url": "https://www.youtube.com/watch?v=2yjwXTZQDDI", "alternatives": ["Dumbbell Shoulder Press", "Arnold Press", "Machine Shoulder Press"], "injury_alternatives": {"shoulder": ["Landmine Press", "Neutral Grip Dumbbell Press"], "lower_back": ["Seated Overhead Press", "Machine Press"], "wrist": ["Dumbbell Press", "Machine Press"]}, "common_mistakes": "Excessive back arch, not full lockout, pressing forward not up"},
    "Lateral Raises": {"category": "Shoulders", "primary_muscles": ["Medial Deltoids"], "secondary_muscles": ["Anterior Deltoids", "Trapezius"], "difficulty": "Beginner", "equipment": ["Dumbbells"], "instructions": ["Stand with dumbbells at sides, slight bend in elbows", "Raise arms out to sides until parallel to floor", "Lead with elbows, not hands", "Pause briefly at top", "Lower with control"], "form_tips": "Don't go too heavy, control the movement, slight forward lean okay", "video_url": "https://www.youtube.com/watch?v=3VcKaXpzqRo", "alternatives": ["Cable Lateral Raises", "Machine Lateral Raises"], "injury_alternatives": {"shoulder": ["Cable Lateral Raises (lighter)", "Machine Lateral Raises"], "elbow": ["Cable Lateral Raises"]}, "common_mistakes": "Using momentum, going too heavy, shrugging shoulders"},
    "Face Pulls": {"category": "Shoulders", "primary_muscles": ["Rear Deltoids", "Rhomboids"], "secondary_muscles": ["Trapezius", "Rotator Cuff"], "difficulty": "Beginner", "equipment": ["Cable Machine", "Resistance Band"], "instructions": ["Set cable to upper chest height with rope attachment", "Pull rope towards face, separating hands", "Focus on pulling elbows back and externally rotating", "Squeeze shoulder blades together", "Return with control"], "form_tips": "High reps, focus on rear delts, external rotation important", "video_url": "https://www.youtube.com/watch?v=rep-qVOkqgk", "alternatives": ["Band Pull-aparts", "Reverse Flyes", "Bent-over Reverse Flyes"], "injury_alternatives": {"shoulder": ["Band Pull-aparts (lighter)", "Prone Y-raises"]}, "common_mistakes": "Pulling too low, not externally rotating, using too much weight"},
    "Barbell Curl": {"category": "Arms", "primary_muscles": ["Biceps Brachii"], "secondary_muscles": ["Brachialis", "Forearms"], "difficulty": "Beginner", "equipment": ["Barbell", "EZ Bar"], "instructions": ["Stand with feet shoulder-width, holding barbell at thighs", "Keep elbows close to torso", "Curl bar up towards shoulders", "Squeeze biceps at top", "Lower with control, don't swing"], "form_tips": "No swinging, keep elbows stationary, full range of motion", "video_url": "https://www.youtube.com/watch?v=kwG2ipFRgfo", "alternatives": ["Dumbbell Curls", "Hammer Curls", "Cable Curls"], "injury_alternatives": {"elbow": ["Cable Curls", "Preacher Curls (lighter)"], "wrist": ["EZ Bar Curls", "Hammer Curls"]}, "common_mistakes": "Swinging weight, moving elbows, partial range of motion"},
    "Tricep Dips": {"category": "Arms", "primary_muscles": ["Triceps"], "secondary_muscles": ["Chest", "Anterior Deltoids"], "difficulty": "Intermediate", "equipment": ["Parallel Bars", "Dip Station"], "instructions": ["Support yourself on bars with arms straight", "Lower body by bending elbows to 90 degrees", "Keep elbows close to body for tricep focus", "Press back up to starting position", "Maintain slight forward lean"], "form_tips": "Control descent, don't go too deep if shoulder pain, full extension", "video_url": "https://www.youtube.com/watch?v=2z8JmcrW-As", "alternatives": ["Bench Dips", "Close-Grip Push-ups", "Tricep Pushdowns"], "injury_alternatives": {"shoulder": ["Bench Dips", "Cable Tricep Pushdowns"], "elbow": ["Cable Pushdowns", "Overhead Extensions (light)"]}, "common_mistakes": "Going too deep, flaring elbows, using momentum"},
    "Skull Crushers": {"category": "Arms", "primary_muscles": ["Triceps"], "secondary_muscles": None, "difficulty": "Intermediate", "equipment": ["EZ Bar", "Dumbbells", "Bench"], "instructions": ["Lie on bench holding EZ bar above chest", "Keep upper arms stationary", "Lower bar towards forehead by bending elbows", "Extend arms back to starting position", "Keep elbows pointing forward throughout"], "form_tips": "Control the weight, keep upper arms still, don't hit forehead!", "video_url": "https://www.youtube.com/watch?v=d_KZxkY_0cM", "alternatives": ["Overhead Tricep Extension", "Cable Tricep Pushdowns"], "injury_alternatives": {"elbow": ["Cable Pushdowns", "Close-Grip Push-ups"], "shoulder": ["Cable Pushdowns", "Bench Dips"]}, "common_mistakes": "Moving upper arms, going too heavy, uncontrolled descent"},
    "Plank": {"category": "Core", "primary_muscles": ["Rectus Abdominis", "Transverse Abdominis"], "secondary_muscles": ["Obliques", "Lower Back", "Shoulders"], "difficulty": "Beginner", "equipment": ["Bodyweight"], "instructions": ["Start in forearm plank position", "Keep body in straight line from head to heels", "Engage core, glutes, and quads", "Don't let hips sag or pike up", "Hold position while breathing steadily"], "form_tips": "Full body tension, neutral spine, squeeze everything", "video_url": "https://www.youtube.com/watch?v=ASdvN_XEl_c", "alternatives": ["Side Plank", "RKC Plank", "Ab Wheel Rollouts"], "injury_alternatives": {"shoulder": ["Elevated Plank", "Dead Bug"], "lower_back": ["Dead Bug", "Bird Dog"], "wrist": ["Forearm Plank (already is)"]}, "progressions": "Knee plank → Full plank → Weighted → Single-arm/leg variations", "common_mistakes": "Sagging hips, piking hips, not breathing, holding too long with bad form"},
    "Russian Twists": {"category": "Core", "primary_muscles": ["Obliques"], "secondary_muscles": ["Rectus Abdominis", "Hip Flexors"], "difficulty": "Beginner", "equipment": ["Medicine Ball", "Dumbbell", "Bodyweight"], "instructions": ["Sit on floor with knees bent, feet elevated", "Lean back slightly, keeping back straight", "Hold weight at chest with both hands", "Rotate torso side to side, touching weight to floor", "Keep core engaged throughout"], "form_tips": "Control rotation, keep feet off ground for more difficulty", "video_url": "https://www.youtube.com/watch?v=wkD8rjkodUI", "alternatives": ["Cable Wood Chops", "Bicycle Crunches", "Side Plank Rotations"], "injury_alternatives": {"lower_back": ["Pallof Press", "Dead Bugs"], "neck": ["Slow controlled twists", "Pallof Press"]}, "common_mistakes": "Rounding back, using momentum, not rotating enough"},
    "Hanging Leg Raises": {"category": "Core", "primary_muscles": ["Lower Abs", "Hip Flexors"], "secondary_muscles": ["Obliques", "Forearms"], "difficulty": "Advanced", "equipment": ["Pull-up Bar"], "instructions": ["Hang from pull-up bar with straight arms", "Keep legs together and straight (or bent for easier)", "Raise legs up by contracting abs", "Lift until legs are parallel to ground or higher", "Lower with control, don't swing"], "form_tips": "Control movement, minimize swinging, focus on abs not just hip flexors", "video_url": "https://www.youtube.com/watch?v=Pr1ieGZ5atk", "alternatives": ["Lying Leg Raises", "Knee Raises", "Ab Wheel"], "injury_alternatives": {"shoulder": ["Lying Leg Raises", "Reverse Crunches"], "lower_back": ["Lying Leg Raises", "Dead Bugs"], "grip": ["Captain's Chair Leg Raises"]}, "progressions": "Knee raises → Straight leg raises → Toes to bar → Weighted", "common_mistakes": "Swinging, using momentum, not engaging abs"}
}


# ============================================================================
# EXERCISE LIBRARY TOOLS
# ============================================================================

@function_tool
def search_exercises(category: str = "all", difficulty: str = "all", equipment: str = "all", muscle_group: str = "all") -> str:
    category, difficulty, equipment_search, muscle_group = category.lower(), difficulty.lower(), equipment.lower(), muscle_group.lower()
    matching = []
    for name, data in EXERCISE_LIBRARY.items():
        if category != "all" and data["category"].lower() != category:
            continue
        if difficulty != "all" and data["difficulty"].lower() != difficulty:
            continue
        if equipment_search != "all":
            exercise_equipment = [e.lower() for e in data["equipment"]]
            if equipment_search not in exercise_equipment and "bodyweight" not in exercise_equipment:
                continue
        if muscle_group != "all":
            all_muscles = data["primary_muscles"] + (data["secondary_muscles"] or [])
            muscle_match = any(muscle_group in muscle.lower() for muscle in all_muscles)
            if not muscle_match:
                continue
        matching.append((name, data))
    if not matching:
        return f"No exercises found matching: category={category}, difficulty={difficulty}, equipment={equipment}, muscle={muscle_group}"
    result = f"🏋️ **Found {len(matching)} Exercise(s):**\n\n"
    for name, data in matching[:15]:
        result += f"**{name}** ({data['category']}) - {data['difficulty']}\n"
        result += f"   🎯 Primary: {', '.join(data['primary_muscles'])}\n"
        result += f"   🔧 Equipment: {', '.join(data['equipment'])}\n\n"
    if len(matching) > 15:
        result += f"\n...and {len(matching) - 15} more exercises. Use get_exercise_details to see full information.\n"
    return result


@function_tool
def get_exercise_details(exercise_name: str) -> str:
    exercise, exact_match = None, None
    for name, data in EXERCISE_LIBRARY.items():
        if name.lower() == exercise_name.lower():
            exact_match = (name, data)
            break
        elif exercise_name.lower() in name.lower():
            exercise = (name, data)
    if exact_match:
        exercise = exact_match
    if not exercise:
        available = ", ".join(list(EXERCISE_LIBRARY.keys())[:10])
        return f"❌ Exercise '{exercise_name}' not found in library.\n\nAvailable exercises include: {available}...\n\nUse search_exercises to find exercises by category."
    name, data = exercise
    result = f"\n🏋️ **{name}** ({data['category']})\n\n**DIFFICULTY:** {data['difficulty']}\n**EQUIPMENT:** {', '.join(data['equipment'])}\n\n**PRIMARY MUSCLES:** {', '.join(data['primary_muscles'])}\n"
    if data['secondary_muscles']:
        result += f"**SECONDARY MUSCLES:** {', '.join(data['secondary_muscles'])}\n"
    result += "\n📋 **INSTRUCTIONS:**\n"
    for i, instruction in enumerate(data['instructions'], 1):
        result += f"{i}. {instruction}\n"
    result += f"\n💡 **FORM TIPS:** {data['form_tips']}\n"
    if data.get('common_mistakes'):
        result += f"\n⚠️ **COMMON MISTAKES:** {data['common_mistakes']}\n"
    if data.get('rep_range'):
        result += f"\n🎯 **REP RANGES:** {data['rep_range']}\n"
    if data.get('progressions'):
        result += f"\n📈 **PROGRESSIONS:** {data['progressions']}\n"
    result += f"\n🎥 **VIDEO TUTORIAL:** {data['video_url']}\n\n🔄 **ALTERNATIVES:** {', '.join(data['alternatives'])}\n"
    if data.get('injury_alternatives'):
        result += "\n🩹 **INJURY-SPECIFIC ALTERNATIVES:**\n"
        for injury, alts in data['injury_alternatives'].items():
            result += f"   • {injury.replace('_', ' ').title()}: {', '.join(alts)}\n"
    return result


@function_tool
def get_exercise_alternatives(exercise_name: str, injury_type: str = None) -> str:
    exercise = None
    for name, data in EXERCISE_LIBRARY.items():
        if exercise_name.lower() in name.lower():
            exercise = (name, data)
            break
    if not exercise:
        return f"❌ Exercise '{exercise_name}' not found in library."
    name, data = exercise
    result = f"🔄 **Alternatives for {name}:**\n\n"
    if injury_type:
        injury_key = injury_type.lower().replace(' ', '_')
        if data.get('injury_alternatives') and injury_key in data['injury_alternatives']:
            result += f"🩹 **For {injury_type.replace('_', ' ').title()} Injury:**\n"
            for alt in data['injury_alternatives'][injury_key]:
                result += f"   • {alt}\n"
        else:
            result += f"No specific alternatives found for {injury_type} injury.\n\n**General alternatives:** {', '.join(data['alternatives'])}\n"
    else:
        result += f"**General alternatives:** {', '.join(data['alternatives'])}\n\n"
        if data.get('injury_alternatives'):
            result += "🩹 **Injury-specific alternatives:**\n"
            for injury, alts in data['injury_alternatives'].items():
                result += f"   • **{injury.replace('_', ' ').title()}:** {', '.join(alts)}\n"
    return result


# ============================================================================
# NUTRITION TRACKER - Meal Logging & Tracking
# ============================================================================

@function_tool
def log_meal(member_name: str, date: str, meal_type: str, food_items: str, calories: int, protein: float, carbs: float, fat: float, notes: str = "") -> str:
    meal_type = meal_type.lower()
    if meal_type not in ["breakfast", "lunch", "dinner", "snack"]:
        return "❌ Meal type must be: breakfast, lunch, dinner, or snack"
    meal = {"member_name": member_name, "date": date, "meal_type": meal_type, "food_items": food_items, "calories": calories, "protein": protein, "carbs": carbs, "fat": fat, "notes": notes, "logged_at": datetime.now().isoformat()}
    nutrition_db.append(meal)
    save_data()
    result = f"✅ **{meal_type.title()} Logged!** 🍽️\n\n📅 Date: {date}\n🍴 Foods: {food_items}\n\n📊 **Nutrition:**\n   🔥 Calories: {calories} kcal\n   🥩 Protein: {protein}g\n   🍞 Carbs: {carbs}g\n   🥑 Fat: {fat}g\n"
    if notes:
        result += f"\n💭 Notes: {notes}\n"
    daily_meals = [m for m in nutrition_db if m["member_name"] == member_name and m["date"] == date]
    total_cals = sum(m["calories"] for m in daily_meals)
    result += f"\n📈 **Daily Total So Far:** {total_cals} kcal\n\nGreat job tracking your nutrition! 💪"
    return result


@function_tool
def get_daily_nutrition_summary(member_name: str, date: str) -> str:
    member = members_db.get(member_name, {})
    calorie_target = member.get("calorie_target")
    daily_meals = [m for m in nutrition_db if m["member_name"] == member_name and m["date"] == date]
    if not daily_meals:
        return f"No meals logged for {member_name} on {date}. Start logging your meals! 🍽️"
    total_calories, total_protein, total_carbs, total_fat = sum(m["calories"] for m in daily_meals), sum(m["protein"] for m in daily_meals), sum(m["carbs"] for m in daily_meals), sum(m["fat"] for m in daily_meals)
    result = f"📊 **Daily Nutrition Summary - {date}**\n\n🔥 **CALORIES**\n   Consumed: {total_calories} kcal\n"
    if calorie_target:
        remaining = calorie_target - total_calories
        if remaining > 0:
            result += f"   Target: {calorie_target} kcal\n   Remaining: {remaining} kcal ✅\n"
        else:
            result += f"   Target: {calorie_target} kcal\n   Over by: {abs(remaining)} kcal ⚠️\n"
    result += f"\n🥗 **MACROS**\n   🥩 Protein: {total_protein}g ({int(total_protein * 4)} kcal, {int(total_protein * 4 / total_calories * 100) if total_calories > 0 else 0}%)\n   🍞 Carbs: {total_carbs}g ({int(total_carbs * 4)} kcal, {int(total_carbs * 4 / total_calories * 100) if total_calories > 0 else 0}%)\n   🥑 Fat: {total_fat}g ({int(total_fat * 9)} kcal, {int(total_fat * 9 / total_calories * 100) if total_calories > 0 else 0}%)\n\n🍽️ **MEALS BREAKDOWN**\n"
    for meal_type in ["breakfast", "lunch", "dinner", "snack"]:
        meals = [m for m in daily_meals if m["meal_type"] == meal_type]
        if meals:
            meal_cals = sum(m["calories"] for m in meals)
            result += f"\n   **{meal_type.title()}** - {meal_cals} kcal\n"
            for meal in meals:
                result += f"      • {meal['food_items']}\n      P: {meal['protein']}g | C: {meal['carbs']}g | F: {meal['fat']}g\n"
    result += "\n💪 Keep up the great nutrition tracking!"
    return result


@function_tool
def suggest_meals(member_name: str, remaining_calories: int, meal_type: str = "any") -> str:
    member = members_db.get(member_name, {})
    diet_type = member.get("diet_type", "omnivore")
    allergies = member.get("allergies", "")
    result = f"💡 **Meal Suggestions for {member_name}**\n\n🎯 Target: ~{remaining_calories} kcal\n🥗 Diet: {diet_type.title()}\n"
    if allergies:
        result += f"🚫 Allergies: {allergies}\n"
    result += "\n"
    suggestions = []
    if remaining_calories <= 200:
        suggestions = [{"name": "Greek Yogurt & Berries", "cals": 150, "p": 15, "c": 20, "f": 2, "diet": ["all"]}, {"name": "Apple with Almond Butter", "cals": 180, "p": 4, "c": 20, "f": 10, "diet": ["vegan", "vegetarian", "all"]}, {"name": "Protein Shake", "cals": 160, "p": 25, "c": 15, "f": 3, "diet": ["all"]}, {"name": "Carrots & Hummus", "cals": 120, "p": 4, "c": 15, "f": 5, "diet": ["vegan", "vegetarian", "all"]}]
    elif remaining_calories <= 400:
        suggestions = [{"name": "Chicken Salad Bowl", "cals": 350, "p": 35, "c": 25, "f": 12, "diet": ["omnivore", "all"]}, {"name": "Quinoa Buddha Bowl", "cals": 380, "p": 15, "c": 50, "f": 12, "diet": ["vegan", "vegetarian", "all"]}, {"name": "Protein Smoothie Bowl", "cals": 320, "p": 25, "c": 40, "f": 8, "diet": ["all"]}, {"name": "Tuna Avocado Wrap", "cals": 390, "p": 28, "c": 35, "f": 15, "diet": ["omnivore", "all"]}, {"name": "Egg White Omelette & Toast", "cals": 300, "p": 25, "c": 30, "f": 8, "diet": ["vegetarian", "all"]}]
    elif remaining_calories <= 600:
        suggestions = [{"name": "Grilled Chicken & Sweet Potato", "cals": 520, "p": 45, "c": 50, "f": 12, "diet": ["omnivore", "all"]}, {"name": "Salmon & Brown Rice", "cals": 550, "p": 40, "c": 55, "f": 18, "diet": ["omnivore", "all"]}, {"name": "Tofu Stir-Fry with Veggies", "cals": 480, "p": 25, "c": 60, "f": 15, "diet": ["vegan", "vegetarian", "all"]}, {"name": "Turkey Breast & Quinoa", "cals": 500, "p": 42, "c": 48, "f": 14, "diet": ["omnivore", "all"]}, {"name": "Lentil Curry & Rice", "cals": 530, "p": 22, "c": 75, "f": 12, "diet": ["vegan", "vegetarian", "all"]}]
    else:
        suggestions = [{"name": "Steak & Roasted Vegetables", "cals": 650, "p": 50, "c": 40, "f": 28, "diet": ["omnivore", "all"]}, {"name": "Chicken Burrito Bowl", "cals": 680, "p": 45, "c": 70, "f": 22, "diet": ["omnivore", "all"]}, {"name": "Vegetarian Pasta Primavera", "cals": 620, "p": 25, "c": 85, "f": 18, "diet": ["vegetarian", "all"]}, {"name": "Grilled Fish Tacos (3)", "cals": 590, "p": 38, "c": 55, "f": 20, "diet": ["omnivore", "all"]}, {"name": "Chickpea Buddha Bowl", "cals": 640, "p": 28, "c": 80, "f": 22, "diet": ["vegan", "vegetarian", "all"]}]
    diet_key = diet_type.lower()
    if diet_key == "omnivore":
        diet_key = "all"
    filtered = [s for s in suggestions if diet_key in s["diet"] or "all" in s["diet"]]
    if allergies:
        allergy_keywords = allergies.lower().split(",")
        filtered = [s for s in filtered if not any(keyword.strip() in s["name"].lower() for keyword in allergy_keywords)]
    if not filtered:
        filtered = suggestions
    result += f"🍽️ **Suggested Meals:**\n\n"
    for idx, meal in enumerate(filtered[:5], 1):
        result += f"{idx}. **{meal['name']}** - {meal['cals']} kcal\n   P: {meal['p']}g | C: {meal['c']}g | F: {meal['f']}g\n\n"
    result += "💭 These are suggestions! Adjust portions to match your exact calorie needs.\n📱 Need more ideas? Ask me for recipes or specific meal types!"
    return result


@function_tool
def log_water_intake(member_name: str, date: str, glasses: int, notes: str = "") -> str:
    existing = [w for w in water_intake_db if w["member_name"] == member_name and w["date"] == date]
    if existing:
        existing[0]["glasses"] += glasses
        existing[0]["notes"] = notes
        existing[0]["updated_at"] = datetime.now().isoformat()
        total_glasses = existing[0]["glasses"]
    else:
        water_entry = {"member_name": member_name, "date": date, "glasses": glasses, "notes": notes, "logged_at": datetime.now().isoformat()}
        water_intake_db.append(water_entry)
        total_glasses = glasses
    save_data()
    goal, remaining = 8, max(0, 8 - total_glasses)
    percentage = min(100, int((total_glasses / goal) * 100))
    result = f"💧 **Water Intake Logged!**\n\n📅 Date: {date}\n💦 Added: {glasses} glass{'es' if glasses > 1 else ''}\n🎯 Total Today: {total_glasses}/{goal} glasses ({percentage}%)\n\n"
    filled = int(percentage / 10)
    bar = "█" * filled + "░" * (10 - filled)
    result += f"[{bar}] {percentage}%\n\n"
    if remaining > 0:
        result += f"⚠️ Keep hydrating! {remaining} more glass{'es' if remaining > 1 else ''} to reach your goal.\n"
    else:
        result += f"🎉 Hydration goal achieved! Great job!\n"
        if total_glasses > goal:
            result += f"💪 You drank {total_glasses - goal} extra glasses! Keep it up!\n"
    result += "\n💡 Tip: Staying hydrated boosts energy and workout performance!"
    return result


@function_tool
def get_water_intake_summary(member_name: str, days: int = 7) -> str:
    cutoff_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    water_logs = [w for w in water_intake_db if w["member_name"] == member_name and w["date"] >= cutoff_date]
    water_logs = sorted(water_logs, key=lambda x: x["date"], reverse=True)
    if not water_logs:
        return f"💧 No water intake logged in the last {days} days. Start tracking your hydration! 💦"
    result = f"💧 **Water Intake Summary** (Last {days} days)\n\n"
    total_glasses = sum(w["glasses"] for w in water_logs)
    avg_per_day = total_glasses / len(water_logs)
    days_goal_met = len([w for w in water_logs if w["glasses"] >= 8])
    goal_percentage = int((days_goal_met / len(water_logs)) * 100)
    result += f"📊 **Statistics:**\n   💦 Total Glasses: {total_glasses}\n   📈 Avg Per Day: {avg_per_day:.1f} glasses\n   🎯 Goal Met: {days_goal_met}/{len(water_logs)} days ({goal_percentage}%)\n\n📅 **Recent Days:**\n"
    for log in water_logs[:7]:
        glasses = log["glasses"]
        status = "✅" if glasses >= 8 else "⚠️"
        result += f"   {status} {log['date']}: {glasses}/8 glasses\n"
    result += "\n"
    if avg_per_day >= 8:
        result += "🎉 Excellent hydration! Keep it up! 💪\n"
    elif avg_per_day >= 6:
        result += "👍 Good progress! Try to hit 8 glasses daily.\n"
    else:
        result += "💡 Tip: Set reminders to drink water throughout the day!\n"
    return result
