async function shorten() {
  const input = document.getElementById('longUrl');
  const longUrl = input.value.trim();

  if (!longUrl) return;

  try {
    const res = await fetch('http://localhost:5000/shorten', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: longUrl })
    });

    const data = await res.json();
    const shortUrl = `http://short.ly/${data.short}`;

    document.getElementById('result').innerHTML = `
      Shortened URL: 
      <a href="${shortUrl}" target="_blank">${shortUrl}</a>
      <button onclick="copyToClipboard('${shortUrl}')">📋 Copy</button>
    `;
  } catch (error) {
    alert("Backend is not reachable or returned an error.");
    console.error(error);
  }
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('Short URL copied to clipboard!');
  });
}
