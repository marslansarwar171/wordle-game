import { useEffect, useState } from 'react'
import Wordle from './components/Wordle'
import WORD_LIST from './constants/words'



function App() {
  const [solution, setSolution] = useState(null)
  
  useEffect(() => {
    fetch('https://wordle-game-api.vercel.app/wordle-list/',{
      method: 'GET',
      mode: 'no-cors',
      headers: {
      'Content-Type': 'application/json'
    }})
      .then(res => res.json())
      .then(json => {
        const randomSolution = json[Math.floor(Math.random()*json.length)]
        setSolution(randomSolution.word)
      })
      .catch(err => setSolution(WORD_LIST[Math.floor(Math.random()*WORD_LIST.length)]))
  }, [setSolution])

  return (
    <div className="App">
      <h1>WORDLE</h1>
      {solution && <Wordle solution={solution} />}
    </div>
  )
}

export default App