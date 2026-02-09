export default function Answer({ data }) {
  if (!data) return null

  return (
    <div>
      <h3>Answer</h3>
      <p>{data.answer}</p>

      <h4>Citations</h4>
      <ul>
        {data.citations.map((c, i) => (
          <li key={i}>
            {c.source} — page {c.page} (score {c.score.toFixed(2)})
          </li>
        ))}
      </ul>
    </div>
  )
}
