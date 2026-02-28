'use client'

import { useState, useEffect, useRef } from 'react'

declare global {
  interface Window {
    customElements: any
  }
}

interface ChatKitElement extends HTMLElement {
  setOptions: (options: any) => void
}

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false)
  const [isChatKitLoaded, setIsChatKitLoaded] = useState(false)
  const chatKitRef = useRef<ChatKitElement | null>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const isInitialized = useRef(false)

  useEffect(() => {
    const checkChatKit = () => {
      if (typeof window !== 'undefined' && window.customElements?.get('openai-chatkit')) {
        setIsChatKitLoaded(true)
      }
    }

    checkChatKit()
    const interval = setInterval(checkChatKit, 500)
    return () => clearInterval(interval)
  }, [])

  useEffect(() => {
    if (isChatKitLoaded && !isInitialized.current && containerRef.current) {
      const chatkit = document.createElement('openai-chatkit') as ChatKitElement
      chatkit.style.width = '100%'
      chatkit.style.height = '100%'

      containerRef.current.appendChild(chatkit)
      chatKitRef.current = chatkit
      isInitialized.current = true

      setTimeout(() => {
        if (chatkit.setOptions) {
          const backendUrl = process.env.NEXT_PUBLIC_CHATKIT_API_URL || 'http://localhost:8000/chatkit'

          chatkit.setOptions({
            api: {
              domainKey: 'local-dev',
              url: backendUrl,
              fetch: async (url: string, init?: RequestInit) => {
                const response = await window.fetch(url, init)
                return response
              }
            },
          })

          console.log('💪 ChatKit configured with backend:', backendUrl)
        }
      }, 100)
    }
  }, [isChatKitLoaded])

  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.style.display = isOpen ? 'block' : 'none'
    }
  }, [isOpen])

  return (
    <>
      {/* Chat Panel - Bottom Right */}
      <div
        ref={containerRef}
        className="fixed bottom-24 right-6 w-96 h-[600px] bg-white rounded-2xl shadow-2xl z-50 overflow-hidden border-2 border-black"
        style={{ display: 'none' }}
      >
        {!isChatKitLoaded && (
          <div className="flex items-center justify-center h-full bg-white">
            <div className="text-center">
              <div className="animate-spin rounded-full h-12 w-12 border-b-4 border-black mx-auto"></div>
              <p className="mt-4 text-black font-semibold">💪 Loading ChatKit...</p>
            </div>
          </div>
        )}
      </div>

      {/* Floating Fitness Button - Bottom Right */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="fixed bottom-6 right-6 w-16 h-16 bg-black hover:bg-gray-900 text-white rounded-full shadow-2xl flex items-center justify-center z-50 transition-all duration-300 hover:scale-110 border-2 border-white"
        aria-label={isOpen ? 'Close chat' : 'Start fitness coaching chat'}
      >
        {isOpen ? (
          // Close Icon
          <svg className="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        ) : (
          // Fitness Icon
          <>
            <span className="text-3xl">💪</span>
            <span className="absolute inset-0 rounded-full bg-black animate-ping opacity-20"></span>
          </>
        )}
      </button>
    </>
  )
}
