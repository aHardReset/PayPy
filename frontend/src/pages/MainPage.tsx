import { useState, useEffect } from 'react'

interface Transaction {
  id: number
  sender_id: number | null
  recipient_id: number | null
  amount: number
  note: string
  created_at: string
}

interface UserInfo {
  id: number
  legal_name: string
  nickname: string
  country_id: number
  balance: number
}

interface MainPageProps {
  userId: number
  nickname: string
  onLogout: () => void
}

export default function MainPage({ userId, nickname, onLogout }: MainPageProps) {
  const [userInfo, setUserInfo] = useState<UserInfo | null>(null)
  const [transactions, setTransactions] = useState<Transaction[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [userResponse, transactionsResponse] = await Promise.all([
          fetch(`http://localhost:8000/api/users/${userId}`),
          fetch(`http://localhost:8000/api/users/${userId}/transactions`),
        ])

        const userData = await userResponse.json()
        const transactionsData = await transactionsResponse.json()

        setUserInfo(userData)
        setTransactions(transactionsData)
      } catch (error) {
        console.error('Error fetching data:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [userId])

  if (loading) {
    return (
      <main className="container">
        <p aria-busy="true">Cargando...</p>
      </main>
    )
  }

  return (
    <main className="container">
      <nav>
        <ul>
          <li><strong>PayPy</strong></li>
        </ul>
        <ul>
          <li><a href="#" onClick={onLogout}>Cerrar sesión</a></li>
        </ul>
      </nav>

      <h1>¡Bienvenido, {nickname}!</h1>

      <article>
        <h2>Balance</h2>
        <h3>${userInfo?.balance.toFixed(2)}</h3>
      </article>

      <article>
        <h2>Transacciones</h2>
        {transactions.length === 0 ? (
          <p>No hay transacciones</p>
        ) : (
          <table>
            <thead>
              <tr>
                <th>Fecha</th>
                <th>Monto</th>
                <th>Nota</th>
              </tr>
            </thead>
            <tbody>
              {transactions.map((transaction) => (
                <tr key={transaction.id}>
                  <td>{new Date(transaction.created_at).toLocaleString()}</td>
                  <td style={{ color: transaction.amount >= 0 ? 'green' : 'red' }}>
                    ${transaction.amount.toFixed(2)}
                  </td>
                  <td>{transaction.note}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </article>

      <button disabled>Transferir (próximamente)</button>
    </main>
  )
}
