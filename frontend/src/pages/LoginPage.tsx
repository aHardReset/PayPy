import { useState } from 'react'

interface LoginPageProps {
  onLogin: (userId: number, nickname: string) => void
}

export default function LoginPage({ onLogin }: LoginPageProps) {
  const [nickname, setNickname] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const response = await fetch('http://localhost:8000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nickname, password }),
      })

      if (!response.ok) {
        throw new Error('Invalid credentials')
      }

      const data = await response.json()
      onLogin(data.id, data.nickname)
    } catch (err) {
      setError('Usuario o contraseña incorrectos')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="container">
      <article>
        <h1>PayPy - Login</h1>
        <form onSubmit={handleSubmit}>
          <label>
            Usuario
            <input
              type="text"
              name="nickname"
              placeholder="johnd"
              value={nickname}
              onChange={(e) => setNickname(e.target.value)}
              required
            />
          </label>
          <label>
            Contraseña
            <input
              type="password"
              name="password"
              placeholder="password123"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          {error && <p style={{ color: 'var(--pico-color-red-500)' }}>{error}</p>}
          <button type="submit" aria-busy={loading} disabled={loading}>
            Ingresar
          </button>
        </form>
        <small>
          Usuarios de prueba: johnd, janes, bobj, alicew, carlosg, marial
          <br />
          Todas las contraseñas están en el código fuente
        </small>
      </article>
    </main>
  )
}
