# PowerFit Gym Frontend

## AI Fitness Coaching Platform - Next.js Frontend

A modern, responsive fitness coaching website built with **Next.js 14**, **TypeScript**, and **Tailwind CSS**, integrated with the ChatKit AI coaching platform.

## Features

### Pages & Sections
- **Hero Section** - Dramatic black & white design with animations
- **Training Programs** - 6 fitness programs (Strength, Cardio, Mobility, Nutrition, Hybrid, Foundation)
- **Pricing** - 3 membership tiers (Basic, Premium, VIP) with monthly/yearly toggle
- **FAQ** - 6 common questions with expandable answers
- **CTA** - Call-to-action section with stats and conversion focus
- **ChatKit Integration** - AI coach chat widget (bottom-right corner)

### Components
- Responsive layout components (Header, Footer)
- Animated section components with fade-in effects
- UI components (Button, Card, Badge)
- Chat widget for AI fitness coach

### Design
- **Black & White Theme** - Professional fitness aesthetic
- **Responsive** - Mobile, tablet, desktop optimized
- **Animated** - Smooth transitions and hover effects
- **Accessible** - WCAG compliant, proper aria labels

## Technology Stack

- **Framework:** Next.js 14 (React 18)
- **Language:** TypeScript
- **Styling:** Tailwind CSS 3.4
- **CSS:** PostCSS with Autoprefixer
- **Utilities:** clsx, tailwind-merge

## File Structure

```
frontend/
├── app/
│   ├── layout.tsx          # Root layout with ChatKit CDN
│   ├── page.tsx            # Home page composition
│   └── globals.css         # Global styles
├── components/
│   ├── chat/
│   │   └── ChatWidget.tsx  # AI coach chat widget
│   ├── layout/
│   │   ├── Header.tsx      # Navigation header
│   │   └── Footer.tsx      # Footer with links
│   ├── sections/
│   │   ├── Hero.tsx        # Hero section
│   │   ├── Features.tsx    # Training programs
│   │   ├── Pricing.tsx     # Membership plans
│   │   ├── FAQ.tsx         # Questions section
│   │   └── CTA.tsx         # Call-to-action
│   └── ui/
│       ├── Button.tsx      # Button component
│       ├── Card.tsx        # Card components
│       └── Badge.tsx       # Badge component
├── lib/
│   └── utils.ts            # Utility functions
├── package.json            # Dependencies
├── tsconfig.json           # TypeScript config
├── tailwind.config.ts      # Tailwind configuration
├── next.config.js          # Next.js configuration
├── postcss.config.js       # PostCSS configuration
└── .gitignore              # Git ignore rules
```

## Getting Started

### Prerequisites
- Node.js 18+ or higher
- npm or yarn package manager

### Installation

```bash
# Install dependencies
npm install

# Create environment file
echo "NEXT_PUBLIC_CHATKIT_API_URL=http://localhost:8000/chatkit" > .env.local
```

### Development

```bash
# Start development server
npm run dev

# Open in browser
open http://localhost:3000
```

The application will reload on file changes.

### Production Build

```bash
# Build for production
npm run build

# Start production server
npm start
```

## Configuration

### Environment Variables

Create `.env.local` file:

```env
# ChatKit Backend URL
NEXT_PUBLIC_CHATKIT_API_URL=http://localhost:8000/chatkit
```

### Tailwind Configuration

The theme uses a black & white fitness aesthetic:

- **Primary:** Black (#000000)
- **Accent:** Grayscale (White to Dark Gray)
- **Fonts:** Inter (body), Montserrat (headings)

## ChatKit Integration

### How It Works

1. **CDN Script** - ChatKit is loaded from CDN in `layout.tsx`
2. **Chat Widget** - `ChatWidget.tsx` creates the chat interface
3. **Backend Connection** - Connects to PowerFit backend at `NEXT_PUBLIC_CHATKIT_API_URL`
4. **Floating Button** - Black button with fitness icon in bottom-right corner

### Configuration

Edit `components/chat/ChatWidget.tsx` to customize:
- Button position
- Chat panel size
- Theme colors
- Backend URL

## Styling

### Global Styles

Defined in `app/globals.css`:
- CSS variables
- Animations (fadeIn, pulse-slow)
- Utility classes
- Theme colors

### Component Styles

- **Tailwind Classes** - Utility-first CSS
- **CSS Modules** - Component-scoped styles
- **Inline Styles** - Dynamic styling in components
- **CSS-in-JS** - Styled JSX for animations

## Performance

### Optimizations

- Next.js Image Optimization (disabled for static deployment)
- Code splitting and lazy loading
- CSS minification
- Tree-shaking unused code
- Static export capability

### Build Size

- Initial bundle: ~150KB (gzipped)
- ChatKit CDN: ~200KB (external)

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Development Tips

### Adding New Components

1. Create component file in `components/`
2. Use TypeScript for type safety
3. Follow naming: PascalCase for components
4. Export as default or named export

### Adding New Pages

1. Create folder in `app/`
2. Add `page.tsx` file
3. Next.js automatically handles routing

### Styling New Components

1. Use Tailwind classes for most styles
2. Use `cn()` utility for conditional classes
3. Keep component styles self-contained
4. Use CSS-in-JS for complex animations

## Troubleshooting

### ChatKit Not Loading

1. Check backend is running at `NEXT_PUBLIC_CHATKIT_API_URL`
2. Verify CDN script loaded in Network tab
3. Check browser console for errors
4. Ensure CORS is configured on backend

### Styling Issues

1. Clear `.next` build folder: `rm -rf .next`
2. Rebuild: `npm run build`
3. Check Tailwind config paths
4. Verify CSS imports in layout

### Build Errors

1. Update dependencies: `npm install`
2. Check TypeScript errors: `npx tsc --noEmit`
3. Review Next.js logs
4. Check Node.js version (18+)

## Deployment

This frontend can be deployed to:
- **Vercel** - Recommended for Next.js
- **Netlify** - Static export
- **AWS** - S3 + CloudFront
- **Any HTTP server** - With static export

### Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

### Static Export

```bash
# Configure next.config.js for static export
# Then build
npm run build

# Output in 'out' folder
```

## License

Proprietary - PowerFit Gym

---

**PowerFit Frontend - Ready for Production!**
