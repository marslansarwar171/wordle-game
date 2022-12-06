import { useEffect, useState } from 'react'
import Wordle from './components/Wordle'

function App() {
  const [solution, setSolution] = useState(null)
  const tempWord = ["ninja", "plate", "plain", "pours", "pools", "spade", "drive", "relax", "times", "train", "cores", "blame", "banks", "phone", "bling", "hello", "coins", "apple"]
  
  useEffect(() => {
    fetch('https://wordle-game-api.vercel.app/wordle-list/',{ headers: {
      'Content-Type': 'application/json'
    }})
      .then(res => res.json())
      .then(json => {
        const randomSolution = json[Math.floor(Math.random()*json.length)]
        setSolution(randomSolution.word)
      })
      .catch(err => setSolution(tempWord[Math.floor(Math.random()*tempWord.length)]))
  }, [setSolution])

  return (
    <div className="App">
      <h1>WORDLE</h1>
      {solution && <Wordle solution={solution} />}
    </div>
  )
}

export default App