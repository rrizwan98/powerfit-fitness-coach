'use client'

import Link from 'next/link'

export function Footer() {
  const currentYear = new Date().getFullYear()

  const footerLinks = {
    'QUICK LINKS': [
      { label: 'HOME', href: '/' },
      { label: 'PROGRAMS', href: '#programs' },
      { label: 'FAQ', href: '#faq' },
      { label: 'CONTACT', href: '/contact' },
    ],
    'COMPANY': [
      { label: 'ABOUT', href: '/about' },
      { label: 'PRIVACY POLICY', href: '#' },
      { label: 'TERMS OF SERVICE', href: '#' },
      { label: 'CAREERS', href: '#' },
    ],
    'FOLLOW US': [
      { label: 'INSTAGRAM', href: '#', icon: '📷' },
      { label: 'FACEBOOK', href: '#', icon: '👍' },
      { label: 'TWITTER', href: '#', icon: '🐦' },
      { label: 'YOUTUBE', href: '#', icon: '▶️' },
    ],
  }

  return (
    <footer className="bg-black border-t-2 border-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          {/* Brand Section */}
          <div className="md:col-span-1">
            <div className="flex items-center space-x-3 mb-6">
              <div className="text-5xl">💪</div>
              <div>
                <h3 className="text-2xl font-black text-white tracking-tight">POWERFIT</h3>
                <p className="text-xs text-gray-500 uppercase tracking-widest">Gym</p>
              </div>
            </div>
            <p className="text-gray-400 text-sm leading-relaxed font-medium mb-6">
              Transform your fitness journey with AI-powered coaching and personalized training.
            </p>

            {/* Contact Info */}
            <div className="space-y-3">
              <a href="tel:+15551234567" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm font-medium group">
                <span className="text-lg group-hover:scale-110 transition-transform">📞</span>
                (555) 123-4567
              </a>
              <a href="mailto:hello@powerfitgym.com" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm font-medium group">
                <span className="text-lg group-hover:scale-110 transition-transform">✉️</span>
                hello@powerfitgym.com
              </a>
            </div>
          </div>

          {/* Link Sections */}
          {Object.entries(footerLinks).map(([title, links]) => (
            <div key={title}>
              <h4 className="font-black text-white mb-6 text-sm uppercase tracking-widest">{title}</h4>
              <ul className="space-y-3">
                {links.map((link) => (
                  <li key={link.href}>
                    <Link
                      href={link.href}
                      className="text-gray-400 hover:text-white transition-colors text-sm font-medium uppercase tracking-wide hover:translate-x-1 inline-block transition-transform"
                    >
                      {link.icon && <span className="mr-2">{link.icon}</span>}
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Newsletter Section */}
        <div className="border-t-2 border-gray-800 pt-10 mb-10">
          <h4 className="font-black text-white mb-4 text-sm uppercase tracking-widest">💌 STAY UPDATED</h4>
          <p className="text-gray-400 text-sm mb-4 font-medium">
            Get exclusive fitness tips, workout plans, and special offers delivered to your inbox.
          </p>
          <div className="flex flex-col sm:flex-row gap-3 max-w-lg">
            <input
              type="email"
              placeholder="ENTER YOUR EMAIL"
              className="flex-1 px-5 py-3 bg-white text-black placeholder-gray-500 font-bold text-sm uppercase tracking-wide focus:outline-none focus:ring-2 focus:ring-white border-2 border-white"
            />
            <button className="px-8 py-3 bg-white text-black font-black text-sm uppercase tracking-wider hover:bg-gray-200 transition-all hover:scale-105">
              SUBSCRIBE
            </button>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="border-t-2 border-gray-800 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-gray-500 text-xs uppercase tracking-widest font-bold">
              &copy; {currentYear} POWERFIT GYM. ALL RIGHTS RESERVED.
            </p>
            <div className="flex items-center gap-6">
              <a href="#" className="text-gray-500 hover:text-white transition-colors text-xs uppercase tracking-widest font-bold">
                PRIVACY
              </a>
              <span className="text-gray-700">|</span>
              <a href="#" className="text-gray-500 hover:text-white transition-colors text-xs uppercase tracking-widest font-bold">
                TERMS
              </a>
              <span className="text-gray-700">|</span>
              <a href="#" className="text-gray-500 hover:text-white transition-colors text-xs uppercase tracking-widest font-bold">
                COOKIES
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* Decorative Bottom Strip */}
      <div className="h-2 bg-gradient-to-r from-black via-white to-black"></div>
    </footer>
  )
}
