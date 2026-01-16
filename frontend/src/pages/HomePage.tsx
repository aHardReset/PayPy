import { useState, useEffect } from 'react'

export default function HomePage() {
  const [message, setMessage] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(response => response.json())
      .then(data => {
        setMessage(data.message)
        setLoading(false)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
        setMessage('Failed to connect to backend')
        setLoading(false)
      })
  }, [])

  return (
    <main className="container">
      <h1>PayPy - Hello World</h1>
      <article>
        {loading ? (
          <p aria-busy="true">Loading...</p>
        ) : (
          <p>{message}</p>
        )}
      </article>
    </main>
  )
}
