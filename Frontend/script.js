async function matchItems() {
  const lost = document.getElementById("lostText").value.trim();
  const found = document.getElementById("foundText").value.trim();

  if (!lost || !found) {
    alert("Please enter both descriptions");
    return;
  }

  document.getElementById("result").innerHTML = "Matching...";

  try {
    const response = await fetch("http://127.0.0.1:5000/match", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ lost, found })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
      <p><b>Similarity:</b> ${data.similarity * 100}%</p>
      <p><b>Confidence:</b> ${data.confidence}</p>
    `;
  } catch (error) {
    document.getElementById("result").innerHTML =
      "Error connecting to backend";
  }
}
