import { useState } from "react"

export default function Query({ onAnswer }) {
  const [query, setQuery] = useState("")

  const ask = async () => {
    const res = await fetch("http://127.0.0.1:8000/query/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    })

    const data = await res.json()
    onAnswer(data)
  }

  return (
    <div>
      <input
        placeholder="Ask a question"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={ask}>Ask</button>
    </div>
  )
}
