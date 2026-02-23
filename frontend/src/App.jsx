import { useState } from 'react'
import './App.css'

function App() {
  // const [count, setCount] = useState(0)
  const [password, updatePassword] = useState('')

  const getPassword = async () => {
    const response = await fetch('http://localhost:8000/json');
    const data = await response.json();
    updatePassword(data.message);
  }
  
  return (
    <>
      <div>
        <input id="password" value={password} readOnly></input>
        <button onClick={getPassword}>Get Password</button>
      </div>    
    </>
  )
}

export default App
