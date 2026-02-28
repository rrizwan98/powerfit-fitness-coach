'use client'

export function CTA() {
  return (
    <section className="relative py-24 overflow-hidden bg-black">
      {/* Diagonal Stripe Background */}
      <div className="absolute inset-0 opacity-5">
        <div className="h-full w-full" style={{
          backgroundImage: `repeating-linear-gradient(
            45deg,
            white,
            white 10px,
            transparent 10px,
            transparent 20px
          )`
        }}></div>
      </div>

      {/* Floating Icons */}
      <div className="absolute top-10 left-10 text-5xl opacity-10 animate-float">💪</div>
      <div className="absolute top-20 right-20 text-6xl opacity-10 animate-float-delayed">🏋️</div>
      <div className="absolute bottom-10 left-1/4 text-4xl opacity-10 animate-float">⚡</div>

      <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 bg-white text-black px-5 py-2 mb-10">
            <span className="text-xl">⚡</span>
            <span className="text-xs font-black uppercase tracking-widest">Join the Elite</span>
          </div>

          {/* Main Heading */}
          <h2 className="heading-display text-6xl sm:text-7xl lg:text-8xl text-white mb-8">
            READY TO
            <br />
            <span className="bg-gradient-to-r from-white via-gray-200 to-white bg-clip-text text-transparent">
              DOMINATE?
            </span>
          </h2>

          <p className="text-xl sm:text-2xl text-gray-400 mb-12 max-w-3xl mx-auto font-medium leading-relaxed">
            Join <span className="text-white font-black">5,000+ warriors</span> crushing limits with AI-powered coaching.
            <br />
            Your transformation starts <span className="text-white font-black">NOW</span>.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-6 justify-center items-center mb-16">
            <button
              onClick={() => {
                const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
                if (button) button.click()
              }}
              className="group relative px-12 py-5 bg-white text-black font-black text-lg uppercase tracking-wider hover:scale-105 transition-all duration-300 overflow-hidden"
              style={{
                boxShadow: '0 0 40px rgba(255,255,255,0.3)',
              }}
            >
              <span className="relative z-10 flex items-center justify-center gap-3">
                START NOW
                <svg className="w-6 h-6 group-hover:translate-x-2 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </button>

            <button className="px-12 py-5 bg-transparent text-white font-bold text-lg uppercase tracking-wider border-2 border-white hover:bg-white hover:text-black transition-all duration-300">
              CALL: (555) 123-4567
            </button>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-8 pt-12 border-t-2 border-gray-800">
            <div className="group cursor-default">
              <div className="text-5xl mb-3 group-hover:scale-110 transition-transform">🏃‍♂️</div>
              <h3 className="text-white font-black text-lg mb-2 uppercase tracking-wider">24/7 AI COACH</h3>
              <p className="text-gray-500 text-sm font-medium uppercase tracking-wide">Instant answers anytime</p>
            </div>

            <div className="group cursor-default">
              <div className="text-5xl mb-3 group-hover:scale-110 transition-transform">⭐</div>
              <h3 className="text-white font-black text-lg mb-2 uppercase tracking-wider">4.9/5 RATING</h3>
              <p className="text-gray-500 text-sm font-medium uppercase tracking-wide">From 5,000+ members</p>
            </div>

            <div className="group cursor-default">
              <div className="text-5xl mb-3 group-hover:scale-110 transition-transform">🎯</div>
              <h3 className="text-white font-black text-lg mb-2 uppercase tracking-wider">GOAL TRACKING</h3>
              <p className="text-gray-500 text-sm font-medium uppercase tracking-wide">Monitor every milestone</p>
            </div>
          </div>
        </div>
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

        .animate-float {
          animation: float 6s ease-in-out infinite;
        }

        .animate-float-delayed {
          animation: float-delayed 8s ease-in-out infinite;
        }
      `}</style>
    </section>
  )
}
