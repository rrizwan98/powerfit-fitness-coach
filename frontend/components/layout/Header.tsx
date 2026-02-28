'use client'

import { useState } from 'react'
import Link from 'next/link'

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const navItems = [
    { label: 'HOME', href: '/' },
    { label: 'PROGRAMS', href: '#programs' },
    { label: 'FAQ', href: '#faq' },
    { label: 'CONTACT', href: '/contact' },
  ]

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-black border-b border-gray-800 backdrop-blur-sm bg-opacity-95">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-3 group">
            <div className="text-4xl group-hover:scale-110 transition-transform">💪</div>
            <div>
              <h1 className="text-2xl font-black text-white tracking-tight">
                POWERFIT
              </h1>
              <p className="text-xs text-gray-400 uppercase tracking-widest">Gym</p>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="text-white hover:text-gray-300 font-bold text-sm tracking-wider transition-all hover:scale-105"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          {/* CTA Button */}
          <div className="hidden sm:block">
            <button
              onClick={() => {
                const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
                if (button) button.click()
              }}
              className="px-6 py-3 bg-white text-black font-black text-sm uppercase tracking-wider hover:bg-gray-200 transition-all hover:scale-105"
            >
              START NOW
            </button>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2 rounded-none hover:bg-gray-900 transition-all"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle menu"
          >
            <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              {isMenuOpen ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <nav className="md:hidden pb-4 space-y-1 border-t border-gray-800 pt-4">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-3 text-white hover:bg-gray-900 font-bold text-sm tracking-wider transition-all"
                onClick={() => setIsMenuOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <button
              onClick={() => {
                const button = document.querySelector('[aria-label*="Start fitness"]') as HTMLButtonElement
                if (button) button.click()
                setIsMenuOpen(false)
              }}
              className="w-full px-4 py-3 bg-white text-black font-black text-sm uppercase tracking-wider hover:bg-gray-200 transition-all"
            >
              START NOW
            </button>
          </nav>
        )}
      </div>
    </header>
  )
}
