# PowerFit Frontend - Setup Guide

## Quick Start (5 minutes)

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment

```bash
# Create .env.local
echo "NEXT_PUBLIC_CHATKIT_API_URL=http://localhost:8000/chatkit" > .env.local
```

### 3. Start Development Server

```bash
npm run dev
```

### 4. Open in Browser

```
http://localhost:3000
```

## Full Setup Guide

### System Requirements

- **Node.js:** 18.17 or higher
- **npm:** 8.0 or higher (or yarn/pnpm)
- **Disk Space:** 500MB minimum
- **RAM:** 2GB minimum

### Step 1: Clone & Navigate

```bash
cd powerfit/frontend
```

### Step 2: Install Dependencies

```bash
# Using npm (recommended)
npm install

# Or using yarn
yarn install

# Or using pnpm
pnpm install
```

**Dependencies:**
- `next@14.2.3` - React framework
- `react@18.3.1` - UI library
- `tailwindcss@3.4.3` - Styling
- `typescript@5.4.5` - Type safety
- `clsx` & `tailwind-merge` - Utility helpers

### Step 3: Environment Setup

**Create `.env.local` file:**

```bash
cat > .env.local << EOF
# ChatKit Backend Configuration
NEXT_PUBLIC_CHATKIT_API_URL=http://localhost:8000/chatkit
EOF
```

**Environment Variables:**
- `NEXT_PUBLIC_CHATKIT_API_URL` - Backend API endpoint (REQUIRED)
  - Development: `http://localhost:8000/chatkit`
  - Production: Update with your backend URL

### Step 4: Start Development

```bash
# Start dev server
npm run dev

# Or with specific port
NEXT_PUBLIC_PORT=3001 npm run dev
```

**Output:**
```
➜  Local:        http://localhost:3000
➜  Environments: .env.local
```

### Step 5: Verify Installation

Open `http://localhost:3000` and check:

1. **Page loads** without errors
2. **Black header** with PowerFit logo visible
3. **Hero section** displays with animations
4. **Chat button** (💪) appears in bottom-right
5. **Console** shows no errors

## Backend Integration

### Prerequisites

Ensure PowerFit backend is running:

```bash
# In another terminal, from powerfit/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
uvicorn main:app --reload
```

Backend should be available at: `http://localhost:8000`

### ChatKit Connection

The frontend connects to ChatKit backend at:

```
http://localhost:8000/chatkit
```

**To verify connection:**

1. Open DevTools (F12)
2. Click chat button (💪)
3. Check Network tab for API calls
4. Console should show: `💪 ChatKit configured with backend: ...`

## Development Workflow

### Hot Reload

Changes are automatically reloaded:

```bash
# Edit any file and save
vim components/sections/Hero.tsx
# Browser refreshes automatically
```

### Code Structure

**Components:**
```
components/
├── sections/      # Page sections (Hero, Features, etc)
├── layout/        # Layout (Header, Footer)
├── chat/          # Chat widget
└── ui/            # Reusable UI (Button, Card, Badge)
```

**Styling:**
- Tailwind CSS classes
- Utility function: `cn()` for conditional classes
- CSS-in-JS for animations

### Common Tasks

#### Add New Section

1. Create `components/sections/NewSection.tsx`
2. Add to `app/page.tsx`
3. Use Tailwind for styling

#### Modify Styling

1. Update Tailwind classes in component
2. Or edit `tailwind.config.ts` for custom theme
3. Changes reflect immediately in dev mode

#### Update ChatKit Backend URL

1. Edit `.env.local`
2. Update `NEXT_PUBLIC_CHATKIT_API_URL`
3. Dev server restarts automatically

## Build & Deploy

### Development Build

```bash
# Check for TypeScript errors
npx tsc --noEmit

# Start dev server
npm run dev
```

### Production Build

```bash
# Create optimized production build
npm run build

# Verify build succeeded
ls -la .next/

# Start production server
npm start
```

### Deploy to Vercel (Recommended)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy (links to GitHub repo)
vercel

# Or deploy from GitHub
# Connect repo in vercel.com dashboard
```

### Deploy to Other Platforms

**Netlify:**
```bash
npm run build
# Deploy 'out' folder or connect GitHub
```

**Docker:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install && npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## Troubleshooting

### Issue: `Module not found`

**Solution:**
```bash
rm -rf node_modules package-lock.json
npm install
```

### Issue: Port 3000 already in use

**Solution:**
```bash
# Use different port
npm run dev -- -p 3001

# Or kill process on port 3000
lsof -i :3000
kill -9 <PID>
```

### Issue: ChatKit button not working

**Check:**
1. Backend is running at correct URL
2. `.env.local` has correct `NEXT_PUBLIC_CHATKIT_API_URL`
3. Browser console for errors
4. Network tab shows successful API calls

**Fix:**
```bash
# Restart dev server
Ctrl+C
npm run dev
```

### Issue: Styling looks wrong

**Solution:**
```bash
# Clear Next.js cache and rebuild
rm -rf .next
npm run dev
```

## Scripts

```json
{
  "dev": "next dev",           // Start dev server
  "build": "next build",       // Create production build
  "start": "next start",       // Start production server
  "lint": "next lint"          // Check code quality
}
```

## Next Steps

1. ✅ **Verify setup** - All files in place, no errors
2. 🎨 **Customize** - Update colors, fonts, content
3. 📱 **Test responsive** - Check mobile, tablet, desktop
4. 🔗 **Connect backend** - Ensure ChatKit works
5. 🚀 **Deploy** - Push to production

## Getting Help

If you encounter issues:

1. Check browser console for errors (F12)
2. Review `.next/` build output
3. Check backend is running (`http://localhost:8000`)
4. Verify all environment variables set
5. Try clearing cache: `rm -rf .next && npm run build`

---

**PowerFit Frontend - Ready to Go! 🚀**
