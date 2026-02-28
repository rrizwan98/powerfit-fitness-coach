'use client'

interface ProgramItem {
  id: string
  name: string
  description: string
  icon: string
  intensity: string
}

export function Features() {
  const programs: ProgramItem[] = [
    {
      id: 'strength',
      name: 'STRENGTH',
      description: 'Build explosive power and muscle mass with progressive overload training',
      icon: '🏋️',
      intensity: 'HIGH',
    },
    {
      id: 'cardio',
      name: 'CARDIO',
      description: 'Burn fat and boost endurance with high-intensity interval training',
      icon: '🏃',
      intensity: 'EXTREME',
    },
    {
      id: 'flexibility',
      name: 'MOBILITY',
      description: 'Enhance range of motion and prevent injuries through dynamic stretching',
      icon: '🧘',
      intensity: 'MEDIUM',
    },
    {
      id: 'nutrition',
      name: 'NUTRITION',
      description: 'AI-calculated meal plans and macro tracking for optimal performance',
      icon: '🥗',
      intensity: 'ESSENTIAL',
    },
    {
      id: 'hybrid',
      name: 'HYBRID',
      description: 'Combine strength and conditioning for complete athletic dominance',
      icon: '⚡',
      intensity: 'BRUTAL',
    },
    {
      id: 'beginner',
      name: 'FOUNDATION',
      description: 'Master form and build habits for long-term fitness success',
      icon: '🎯',
      intensity: 'START',
    },
  ]

  return (
    <section id="programs" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-black text-white px-4 py-2 text-xs font-black uppercase tracking-widest mb-6">
            <span>⚡</span>
            <span>TRAINING PROGRAMS</span>
          </div>
          <h2 className="heading-display text-5xl sm:text-6xl lg:text-7xl text-black mb-6">
            CHOOSE YOUR
            <br />
            <span className="bg-gradient-to-r from-black to-gray-600 bg-clip-text text-transparent">
              PATH TO POWER
            </span>
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto font-medium">
            AI-personalized programs designed to push your limits and deliver results
          </p>
        </div>

        {/* Programs Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {programs.map((program, index) => (
            <div
              key={program.id}
              className="group relative bg-white border-2 border-black hover:bg-black transition-all duration-300 overflow-hidden"
              style={{
                animation: `fadeIn 0.6s ease-out ${index * 0.1}s both`
              }}
            >
              {/* Intensity Badge */}
              <div className="absolute top-4 right-4 bg-black group-hover:bg-white px-3 py-1 z-10">
                <span className="text-white group-hover:text-black text-xs font-black tracking-wider">
                  {program.intensity}
                </span>
              </div>

              {/* Icon */}
              <div className="h-48 flex items-center justify-center bg-gradient-to-br from-gray-50 to-white group-hover:from-gray-900 group-hover:to-black transition-all duration-300">
                <span className="text-8xl group-hover:scale-110 transition-transform duration-300">
                  {program.icon}
                </span>
              </div>

              {/* Content */}
              <div className="p-6">
                <h3 className="text-2xl font-black text-black group-hover:text-white mb-3 tracking-tight transition-colors">
                  {program.name}
                </h3>
                <p className="text-gray-600 group-hover:text-gray-300 text-sm leading-relaxed mb-6 transition-colors">
                  {program.description}
                </p>

                {/* Action Button */}
                <button
                  onClick={() => {
                    const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
                    if (button) button.click()
                  }}
                  className="w-full py-3 bg-transparent border-2 border-black group-hover:border-white group-hover:bg-white text-black group-hover:text-black font-black text-sm uppercase tracking-wider transition-all hover:scale-105"
                >
                  START PROGRAM
                </button>
              </div>

              {/* Corner Accent */}
              <div className="absolute bottom-0 right-0 w-16 h-16 bg-black group-hover:bg-white transform rotate-45 translate-x-8 translate-y-8 transition-colors"></div>
            </div>
          ))}
        </div>

        {/* Bottom CTA */}
        <div className="text-center mt-16">
          <p className="text-gray-600 mb-6 font-medium">
            Not sure which program fits you? Let AI analyze your goals.
          </p>
          <button
            onClick={() => {
              const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
              if (button) button.click()
            }}
            className="px-10 py-4 bg-black text-white font-black text-sm uppercase tracking-wider hover:bg-gray-900 transition-all hover:scale-105"
          >
            GET AI RECOMMENDATION
          </button>
        </div>
      </div>
    </section>
  )
}
