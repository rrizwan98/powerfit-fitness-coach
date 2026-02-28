'use client'

import { useEffect, useState } from 'react'

export function Hero() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    setIsVisible(true)
  }, [])

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-black">
      {/* Animated Background Grid */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-black via-gray-900 to-black"></div>

        {/* Animated Grid Lines */}
        <div className="absolute inset-0 opacity-10">
          <div className="h-full w-full" style={{
            backgroundImage: `
              linear-gradient(to right, white 1px, transparent 1px),
              linear-gradient(to bottom, white 1px, transparent 1px)
            `,
            backgroundSize: '80px 80px',
            animation: 'grid-move 20s linear infinite'
          }}></div>
        </div>

        {/* Floating Gym Equipment Icons */}
        <div className="absolute top-20 left-10 text-6xl opacity-20 animate-float">🏋️</div>
        <div className="absolute top-40 right-20 text-7xl opacity-15 animate-float-delayed">💪</div>
        <div className="absolute bottom-32 left-1/4 text-5xl opacity-10 animate-float">🤸</div>
        <div className="absolute bottom-20 right-1/3 text-6xl opacity-20 animate-float-delayed">⚡</div>
      </div>

      {/* Main Content */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center">

          {/* Glowing Badge */}
          <div
            className={`inline-flex items-center gap-3 bg-white text-black px-6 py-3 rounded-full font-bold mb-12 shadow-2xl transition-all duration-1000 ${
              isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 -translate-y-10'
            }`}
            style={{
              boxShadow: '0 0 40px rgba(255,255,255,0.3)',
              animation: 'pulse-glow 3s ease-in-out infinite'
            }}
          >
            <span className="text-2xl animate-pulse">💪</span>
            <span className="text-sm uppercase tracking-wider">AI-Powered Training</span>
          </div>

          {/* Giant Bold Heading with Animation */}
          <h1 className={`heading-display mb-8 transition-all duration-1000 delay-200 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'
          }`}>
            <div className="text-white text-7xl sm:text-8xl lg:text-9xl mb-4 relative">
              <span className="relative inline-block">
                NO LIMITS
                <div className="absolute -inset-1 bg-gradient-to-r from-gray-600 to-gray-800 opacity-50 blur-xl"></div>
              </span>
            </div>
            <div className="text-white text-7xl sm:text-8xl lg:text-9xl mb-4">
              NO EXCUSES
            </div>
            <div className="text-white text-7xl sm:text-8xl lg:text-9xl relative">
              <span className="relative inline-block">
                JUST
                <span className="absolute inset-0 bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent blur-sm">
                  JUST
                </span>
              </span>
              {' '}
              <span className="relative inline-block bg-gradient-to-r from-white via-gray-200 to-white bg-clip-text text-transparent animate-shimmer">
                RESULTS
              </span>
            </div>
          </h1>

          {/* Subheading */}
          <p className={`text-xl sm:text-2xl text-gray-400 max-w-3xl mx-auto mb-12 font-medium transition-all duration-1000 delay-500 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'
          }`}>
            Train smarter with <span className="text-white font-bold">AI-powered coaching</span>.
            <br />
            Personalized workouts. Real-time guidance. Unstoppable progress.
          </p>

          {/* CTA Buttons */}
          <div className={`flex flex-col sm:flex-row gap-6 justify-center items-center mb-20 transition-all duration-1000 delay-700 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'
          }`}>
            <button
              onClick={() => {
                const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
                if (button) button.click()
              }}
              className="group relative px-10 py-5 bg-white text-black font-black text-lg uppercase tracking-wider hover:scale-105 transition-all duration-300 overflow-hidden rounded-none"
              style={{
                boxShadow: '0 0 30px rgba(255,255,255,0.5)',
              }}
            >
              <span className="relative z-10 flex items-center justify-center gap-3">
                START NOW
                <svg className="w-6 h-6 group-hover:translate-x-2 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
              <div className="absolute inset-0 bg-black transform scale-x-0 group-hover:scale-x-100 transition-transform origin-left duration-300"></div>
              <span className="absolute inset-0 flex items-center justify-center gap-3 text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300 font-black">
                START NOW
                <svg className="w-6 h-6 translate-x-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </button>

            <button className="group px-10 py-5 bg-transparent text-white font-bold text-lg uppercase tracking-wider border-2 border-white hover:bg-white hover:text-black transition-all duration-300 rounded-none">
              WATCH DEMO
            </button>
          </div>

          {/* Stats with Animation */}
          <div className={`grid grid-cols-3 gap-8 max-w-4xl mx-auto pt-16 border-t border-gray-700 transition-all duration-1000 delay-1000 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'
          }`}>
            <div className="text-center group cursor-default">
              <div className="text-5xl sm:text-6xl font-black text-white mb-2 group-hover:scale-110 transition-transform">
                <span className="bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
                  24/7
                </span>
              </div>
              <div className="text-xs sm:text-sm text-gray-500 font-bold uppercase tracking-widest">AI COACHING</div>
            </div>
            <div className="text-center group cursor-default">
              <div className="text-5xl sm:text-6xl font-black text-white mb-2 group-hover:scale-110 transition-transform">
                <span className="bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
                  ∞
                </span>
              </div>
              <div className="text-xs sm:text-sm text-gray-500 font-bold uppercase tracking-widest">WORKOUTS</div>
            </div>
            <div className="text-center group cursor-default">
              <div className="text-5xl sm:text-6xl font-black text-white mb-2 group-hover:scale-110 transition-transform">
                <span className="bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
                  100%
                </span>
              </div>
              <div className="text-xs sm:text-sm text-gray-500 font-bold uppercase tracking-widest">CUSTOM</div>
            </div>
          </div>

        </div>
      </div>

      {/* Animated Scroll Indicator */}
      <div className="absolute bottom-10 left-1/2 transform -translate-x-1/2 flex flex-col items-center gap-2 animate-bounce">
        <span className="text-gray-500 text-xs uppercase tracking-widest font-bold">Scroll</span>
        <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>

      {/* CSS Animations */}
      <style jsx>{`
        @keyframes float {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          50% { transform: translateY(-20px) rotate(5deg); }
        }

        @keyframes float-delayed {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          50% { transform: translateY(-30px) rotate(-5deg); }
        }

        @keyframes grid-move {
          0% { transform: translateY(0); }
          100% { transform: translateY(80px); }
        }

        @keyframes pulse-glow {
          0%, 100% { box-shadow: 0 0 40px rgba(255,255,255,0.3); }
          50% { box-shadow: 0 0 60px rgba(255,255,255,0.5); }
        }

        @keyframes shimmer {
          0% { background-position: -1000px 0; }
          100% { background-position: 1000px 0; }
        }

        .animate-float {
          animation: float 6s ease-in-out infinite;
        }

        .animate-float-delayed {
          animation: float-delayed 8s ease-in-out infinite;
        }

        .animate-shimmer {
          background-size: 200% auto;
          animation: shimmer 3s linear infinite;
        }
      `}</style>
    </section>
  )
}
