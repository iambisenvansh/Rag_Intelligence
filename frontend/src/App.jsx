import { useState } from "react";
import "./App.css";

export default function App() {
  const [file, setFile] = useState(null);
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadPDF = async () => {
    if (!file) return alert("Upload PDF first");

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://localhost:8000/ingest/", {
      method: "POST",
      body: formData,
    });
    setMessages([]);
    alert("PDF uploaded successfully");
  };

  const askQuestion = async () => {
    if (!question.trim()) return;

    setMessages((prev) => [...prev, { role: "user", text: question }]);
    setLoading(true);

    const res = await fetch("http://localhost:8000/query/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: question }),
    });

    const data = await res.json();

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text: data.answer,
        citations: data.citations,
      },
    ]);

    setQuestion("");
    setLoading(false);
  };

  return (
    <div className="app">
      <header className="header">RAG Document Intelligence</header>

      <div className="chat-wrapper">
        <div className="chat-container">

          {/* Upload */}
          <div className="upload">
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={uploadPDF}>Upload PDF</button>
          </div>

          {/* Chat */}
          <div className="chat">

            {/* ✅ CENTER WELCOME (ChatGPT-style) */}
            {messages.length === 0 && !loading && (
              <div className="welcome">
                What’s on the agenda today?
              </div>
            )}

            {messages.map((m, i) => (
              <div key={i} className={`bubble ${m.role}`}>
                <p>{m.text}</p>

                {m.citations && (
                  <div className="citations">
                    {m.citations.map((c, idx) => (
                      <small key={idx}>
                        📄 {c.source} — page {c.page}
                      </small>
                    ))}
                  </div>
                )}
              </div>
            ))}

            {loading && (
              <div className="bubble assistant typing">Thinking…</div>
            )}
          </div>

          {/* Input */}
          <div className="input">
            <input
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask something about the document..."
              onKeyDown={(e) => e.key === "Enter" && askQuestion()}
            />
            <button onClick={askQuestion}>Send</button>
          </div>

        </div>
      </div>
    </div>
  );
}
