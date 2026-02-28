import type { Metadata } from 'next'
import Script from 'next/script'
import './globals.css'
import { Header } from '@/components/layout/Header'
import { Footer } from '@/components/layout/Footer'
import ChatWidget from '@/components/chat/ChatWidget'

export const metadata: Metadata = {
  title: 'PowerFit Gym - Transform Your Fitness Journey',
  description: 'AI-powered fitness coaching for personalized workouts, nutrition guidance, and progress tracking.',
  keywords: ['fitness', 'gym', 'workout', 'training', 'nutrition', 'health'],
  authors: [{ name: 'PowerFit Gym' }],
  openGraph: {
    title: 'PowerFit Gym',
    description: 'Transform your fitness journey with AI-powered coaching',
    type: 'website',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        {/* ChatKit CDN Script - REQUIRED */}
        <Script
          src="https://cdn.platform.openai.com/deployments/chatkit/chatkit.js"
          strategy="beforeInteractive"
        />
      </head>
      <body className="bg-white text-gray-900">
        <Header />
        <main className="min-h-screen">
          {children}
        </main>
        <Footer />
        <ChatWidget />
      </body>
    </html>
  )
}
