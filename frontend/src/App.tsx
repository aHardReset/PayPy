import MainPage from './pages/MainPage'

function App() {
  // Hardcoded to user_id = 1 for now (no login required)
  const userId = 1
  const nickname = 'johnd'

  const handleLogout = () => {
    // TODO: Implement logout when auth is added
    console.log('Logout not implemented yet')
  }

  return <MainPage userId={userId} nickname={nickname} onLogout={handleLogout} />
}

export default App
