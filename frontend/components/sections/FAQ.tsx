'use client'

import { useState } from 'react'

interface FAQItem {
  id: string
  question: string
  answer: string
  icon: string
}

export function FAQ() {
  const [openId, setOpenId] = useState<string | null>(null)

  const faqs: FAQItem[] = [
    {
      id: 'beginner',
      question: 'I\'m a complete beginner. Is this program right for me?',
      answer: 'Absolutely! Our AI coach adapts to your fitness level. We offer beginner-friendly programs with detailed form guidance and progressive difficulty scaling.',
      icon: '🎯',
    },
    {
      id: 'equipment',
      question: 'What equipment do I need?',
      answer: 'It depends on your chosen program. We offer bodyweight-only programs as well as gym-based routines. Our AI coach will customize workouts based on your available equipment.',
      icon: '🏋️',
    },
    {
      id: 'time',
      question: 'How much time per week do I need to commit?',
      answer: 'Our programs range from 3-6 days per week, with sessions lasting 30-60 minutes. We\'ll design a plan that fits your schedule and goals.',
      icon: '⏱️',
    },
    {
      id: 'nutrition',
      question: 'Do I need to follow a strict diet?',
      answer: 'No strict diets required! We provide flexible nutrition guidance based on your preferences and goals. Our AI coach helps you make sustainable choices.',
      icon: '🥗',
    },
    {
      id: 'results',
      question: 'How quickly will I see results?',
      answer: 'Most clients notice improvements in energy and strength within 2-3 weeks. Visible physical changes typically appear after 4-8 weeks of consistent training.',
      icon: '📈',
    },
    {
      id: 'support',
      question: 'What kind of support do I get?',
      answer: 'You get 24/7 AI coaching through our chat interface, plus access to our community forum and weekly progress check-ins. Premium members also get monthly video consultations.',
      icon: '💬',
    },
  ]

  return (
    <section id="faq" className="py-20 bg-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-black text-white px-4 py-2 text-xs font-black uppercase tracking-widest mb-6">
            <span>❓</span>
            <span>FAQ</span>
          </div>
          <h2 className="heading-display text-5xl sm:text-6xl lg:text-7xl text-black mb-6">
            GOT
            <br />
            <span className="bg-gradient-to-r from-black to-gray-600 bg-clip-text text-transparent">
              QUESTIONS?
            </span>
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto font-medium">
            Find answers to common questions about PowerFit Gym
          </p>
        </div>

        {/* FAQ Items */}
        <div className="space-y-4">
          {faqs.map((faq, index) => (
            <div
              key={faq.id}
              className="bg-white border-2 border-black overflow-hidden transition-all duration-300"
              style={{
                animation: `fadeIn 0.5s ease-out ${index * 0.1}s both`
              }}
            >
              <button
                onClick={() => setOpenId(openId === faq.id ? null : faq.id)}
                className="w-full px-6 py-5 flex items-center justify-between hover:bg-gray-50 transition-all"
              >
                <div className="flex items-center gap-4 text-left">
                  <span className="text-3xl flex-shrink-0">{faq.icon}</span>
                  <h3 className="font-black text-black text-base sm:text-lg uppercase tracking-wide">
                    {faq.question}
                  </h3>
                </div>
                <div
                  className={`flex-shrink-0 w-8 h-8 flex items-center justify-center bg-black text-white transition-transform duration-300 ${
                    openId === faq.id ? 'rotate-180' : ''
                  }`}
                >
                  <svg
                    className="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={3}
                      d="M19 14l-7 7m0 0l-7-7m7 7V3"
                    />
                  </svg>
                </div>
              </button>

              {openId === faq.id && (
                <div className="px-6 pb-6 pt-2 bg-gray-50 border-t-2 border-black">
                  <p className="text-gray-700 leading-relaxed font-medium ml-16">
                    {faq.answer}
                  </p>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Bottom CTA */}
        <div className="mt-16 p-8 bg-black border-2 border-black text-center">
          <p className="text-white text-lg mb-4">
            <span className="font-black uppercase tracking-wide">Still have questions?</span>
          </p>
          <button
            onClick={() => {
              const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
              if (button) button.click()
            }}
            className="px-8 py-3 bg-white text-black font-black text-sm uppercase tracking-wider hover:bg-gray-200 transition-all hover:scale-105"
          >
            ASK AI COACH
          </button>
        </div>
      </div>
    </section>
  )
}
