async function analyzeHeader() {
  const header = document.getElementById('headerInput').value;

  const response = await fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ header: header })
  });

  const data = await response.json();
  document.getElementById('result').innerText = JSON.stringify(data, null, 2);
}
