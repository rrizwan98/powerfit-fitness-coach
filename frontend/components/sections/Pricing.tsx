'use client'

import { useState } from 'react'

interface PricingTier {
  name: string
  icon: string
  tagline: string
  monthlyPrice: number
  yearlyPrice: number
  features: string[]
  highlighted?: boolean
  cta: string
}

export function Pricing() {
  const [isYearly, setIsYearly] = useState(false)

  const pricingTiers: PricingTier[] = [
    {
      name: 'BASIC',
      icon: '🏃',
      tagline: 'Start Your Journey',
      monthlyPrice: 29,
      yearlyPrice: 290,
      features: [
        'Access to gym floor',
        'AI workout plans',
        'Basic progress tracking',
        'Mobile app access',
        '24/7 gym access',
        'Locker room access'
      ],
      cta: 'START BASIC'
    },
    {
      name: 'PREMIUM',
      icon: '💪',
      tagline: 'Most Popular',
      monthlyPrice: 59,
      yearlyPrice: 590,
      features: [
        'Everything in Basic',
        'Personal AI coach',
        'Advanced analytics',
        'Nutrition guidance',
        'Exercise video library',
        'Priority support',
        'Guest passes (2/month)',
        'Group classes included'
      ],
      highlighted: true,
      cta: 'GO PREMIUM'
    },
    {
      name: 'VIP',
      icon: '👑',
      tagline: 'Elite Performance',
      monthlyPrice: 99,
      yearlyPrice: 990,
      features: [
        'Everything in Premium',
        '1-on-1 trainer sessions (4/month)',
        'Custom meal plans',
        'Body composition analysis',
        'Supplement consultation',
        'Massage therapy (2/month)',
        'VIP lounge access',
        'Unlimited guest passes',
        'Priority equipment access'
      ],
      cta: 'JOIN VIP'
    }
  ]

  const calculateSavings = (monthly: number, yearly: number) => {
    const monthlyCost = monthly * 12
    const savings = monthlyCost - yearly
    const percentage = Math.round((savings / monthlyCost) * 100)
    return { savings, percentage }
  }

  return (
    <section id="pricing" className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-black text-white px-4 py-2 text-xs font-black uppercase tracking-widest mb-6">
            <span>💰</span>
            <span>Pricing</span>
          </div>

          <h2 className="heading-display text-5xl sm:text-6xl lg:text-7xl text-black mb-6">
            CHOOSE YOUR
            <br />
            <span className="bg-gradient-to-r from-black to-gray-600 bg-clip-text text-transparent">
              POWER LEVEL
            </span>
          </h2>

          <p className="text-lg text-gray-600 max-w-2xl mx-auto font-medium mb-10">
            Select the plan that matches your fitness goals. Upgrade or downgrade anytime.
          </p>

          {/* Billing Toggle */}
          <div className="inline-flex items-center gap-4 bg-gray-100 p-2 border-2 border-black">
            <button
              onClick={() => setIsYearly(false)}
              className={`px-6 py-2 font-black text-sm uppercase tracking-wider transition-all ${
                !isYearly
                  ? 'bg-black text-white'
                  : 'bg-transparent text-black hover:bg-gray-200'
              }`}
            >
              MONTHLY
            </button>
            <button
              onClick={() => setIsYearly(true)}
              className={`px-6 py-2 font-black text-sm uppercase tracking-wider transition-all relative ${
                isYearly
                  ? 'bg-black text-white'
                  : 'bg-transparent text-black hover:bg-gray-200'
              }`}
            >
              YEARLY
              <span className="absolute -top-3 -right-2 bg-white text-black text-xs font-black px-2 py-1 border-2 border-black">
                SAVE 17%
              </span>
            </button>
          </div>
        </div>

        {/* Pricing Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {pricingTiers.map((tier, index) => {
            const { savings, percentage } = calculateSavings(tier.monthlyPrice, tier.yearlyPrice)

            return (
              <div
                key={tier.name}
                className={`relative bg-white border-4 transition-all duration-300 hover:scale-105 ${
                  tier.highlighted
                    ? 'border-black shadow-2xl z-10 md:-mt-4 md:mb-4'
                    : 'border-gray-300 hover:border-black'
                }`}
                style={{
                  animation: `fadeIn 0.6s ease-out ${index * 0.15}s both`
                }}
              >
                {/* Popular Badge */}
                {tier.highlighted && (
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-black text-white px-6 py-2 font-black text-xs uppercase tracking-widest">
                    ⭐ MOST POPULAR
                  </div>
                )}

                {/* Card Content */}
                <div className="p-8">
                  {/* Icon & Name */}
                  <div className="text-center mb-6">
                    <div className="text-6xl mb-4">{tier.icon}</div>
                    <h3 className="text-3xl font-black text-black uppercase tracking-tight mb-2">
                      {tier.name}
                    </h3>
                    <p className="text-sm text-gray-600 font-medium uppercase tracking-wide">
                      {tier.tagline}
                    </p>
                  </div>

                  {/* Price */}
                  <div className="text-center mb-8 pb-8 border-b-2 border-gray-200">
                    <div className="flex items-start justify-center gap-1 mb-2">
                      <span className="text-2xl font-black text-black mt-2">$</span>
                      <span className="text-6xl font-black text-black">
                        {isYearly ? tier.yearlyPrice : tier.monthlyPrice}
                      </span>
                      <span className="text-gray-500 font-bold text-lg mt-8">
                        /{isYearly ? 'year' : 'mo'}
                      </span>
                    </div>

                    {isYearly && (
                      <div className="text-sm">
                        <span className="text-gray-500 line-through font-medium">
                          ${tier.monthlyPrice * 12}/year
                        </span>
                        <span className="ml-2 text-black font-black">
                          Save ${savings}
                        </span>
                      </div>
                    )}
                  </div>

                  {/* Features */}
                  <ul className="space-y-4 mb-8">
                    {tier.features.map((feature, idx) => (
                      <li key={idx} className="flex items-start gap-3">
                        <svg
                          className="w-6 h-6 flex-shrink-0 mt-0.5"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={3}
                            d="M5 13l4 4L19 7"
                            className="text-black"
                          />
                        </svg>
                        <span className="text-gray-700 font-medium text-sm">
                          {feature}
                        </span>
                      </li>
                    ))}
                  </ul>

                  {/* CTA Button */}
                  <button
                    className={`w-full py-4 font-black text-sm uppercase tracking-wider transition-all hover:scale-105 ${
                      tier.highlighted
                        ? 'bg-black text-white hover:bg-gray-900'
                        : 'bg-white text-black border-2 border-black hover:bg-black hover:text-white'
                    }`}
                  >
                    {tier.cta}
                  </button>
                </div>
              </div>
            )
          })}
        </div>

        {/* Bottom Info */}
        <div className="mt-16 text-center">
          <div className="inline-flex flex-col sm:flex-row items-center gap-6 bg-gray-100 px-8 py-6 border-2 border-black">
            <div className="flex items-center gap-3">
              <span className="text-3xl">✅</span>
              <div className="text-left">
                <p className="font-black text-sm uppercase tracking-wide text-black">No Commitment</p>
                <p className="text-xs text-gray-600 font-medium">Cancel anytime</p>
              </div>
            </div>

            <div className="hidden sm:block w-px h-12 bg-gray-300"></div>

            <div className="flex items-center gap-3">
              <span className="text-3xl">💳</span>
              <div className="text-left">
                <p className="font-black text-sm uppercase tracking-wide text-black">7-Day Free Trial</p>
                <p className="text-xs text-gray-600 font-medium">For all new members</p>
              </div>
            </div>

            <div className="hidden sm:block w-px h-12 bg-gray-300"></div>

            <div className="flex items-center gap-3">
              <span className="text-3xl">🔐</span>
              <div className="text-left">
                <p className="font-black text-sm uppercase tracking-wide text-black">Money Back</p>
                <p className="text-xs text-gray-600 font-medium">30-day guarantee</p>
              </div>
            </div>
          </div>
        </div>

        {/* FAQ Link */}
        <div className="mt-12 text-center">
          <p className="text-gray-600 font-medium">
            Have questions?{' '}
            <a href="#faq" className="text-black font-black underline hover:no-underline">
              Check our FAQ
            </a>
            {' '}or{' '}
            <button
              onClick={() => {
                const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
                if (button) button.click()
              }}
              className="text-black font-black underline hover:no-underline"
            >
              chat with AI coach
            </button>
          </p>
        </div>
      </div>
    </section>
  )
}
