# 💪 PowerFit Gym - AI Fitness Coach

A complete AI-powered fitness coaching platform with personalized workout plans, nutrition tracking, exercise library, and a beautiful black & white fitness website.

## ✨ Features

### 🤖 AI Fitness Coach Backend
- **Personalized Workout Plans** - Custom routines based on fitness level, goals, and equipment
- **Exercise Library** - 30+ exercises with detailed instructions, form tips, and video tutorials
- **Nutrition Tracker** - Log meals, track calories/macros, get meal suggestions
- **Water Tracking** - Monitor daily hydration with 8-glass goal
- **Progress Tracking** - Track weight, measurements, workouts, and personal records
- **Member Profiles** - Save fitness goals, diet preferences, injuries, and restrictions

### 🌐 PowerFit Website (Frontend)
- **Hero Section** - Dramatic black & white design with animated grid
- **Training Programs** - 3 program tiers (Beginner, Intermediate, Advanced)
- **Pricing Section** - 3 membership plans with monthly/yearly billing
- **FAQ Section** - Common questions with expandable answers
- **ChatKit Integration** - AI coach chat widget for instant support
- **Fully Responsive** - Mobile, tablet, and desktop optimized

## 🏗️ Tech Stack

### Backend
- **Python 3.9+**
- **FastAPI** - Modern web framework
- **OpenAI Agents SDK** - AI agent framework
- **ChatKit** - Streaming chat interface
- **Uvicorn** - ASGI server

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS
- **ChatKit React** - AI chat widget

## 🚀 Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
echo "NEXT_PUBLIC_CHATKIT_API_URL=http://localhost:8000/chatkit" > .env.local
npm run dev
```

## 📚 Features

### 🏋️ Exercise Library
- 30+ exercises across 6 categories
- Difficulty levels: Beginner, Intermediate, Advanced
- Complete info: Instructions, form tips, video tutorials
- Injury support for shoulder, knee, back, elbow, wrist

### 🥗 Nutrition Tracker
- Meal logging (breakfast, lunch, dinner, snacks)
- Macro tracking (calories, protein, carbs, fat)
- Daily nutrition summaries
- 20+ meal suggestions based on calories
- Diet-aware (vegan, vegetarian, keto, omnivore)

### 💧 Water Tracking
- Daily goal: 8 glasses (8oz each)
- Progress bar and weekly trends

### 💰 Membership Plans
1. **Basic** - $29/month ($290/year)
2. **Premium** - $59/month ($590/year) ⭐ Most Popular
3. **VIP** - $99/month ($990/year)

---

**PowerFit Gym** - Transform Your Fitness Journey with AI 💪🔥