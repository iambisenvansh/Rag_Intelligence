export default function Upload({ onUploaded }) {
  const uploadFile = async (e) => {
    const file = e.target.files[0]
    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    await fetch("http://127.0.0.1:8000/ingest/", {
      method: "POST",
      body: formData
    })

    onUploaded()
  }

  return (
    <div>
      <h3>Upload PDF</h3>
      <input type="file" accept=".pdf" onChange={uploadFile} />
    </div>
  )
}
