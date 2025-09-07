const searchBtn = document.getElementById("search-btn");
const searchPage = document.getElementById("search-page");
const resultsPage = document.getElementById("results-page");
const wikiContent = document.getElementById("wiki-content");
const timeoutBox = document.getElementById("timeout-box");

const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";

function startDecryptEffect() {
  let interval = setInterval(() => {
    let fakeParagraphs = [];
    let paragraphCount = 2 + Math.floor(Math.random() * 2);

    for (let p = 0; p < paragraphCount; p++) {
      let fakeText = "";
      let length = 80 + Math.floor(Math.random() * 40);
      for (let i = 0; i < length; i++) {
        fakeText += chars[Math.floor(Math.random() * chars.length)];
      }
      fakeParagraphs.push(fakeText);
    }

    wikiContent.textContent = fakeParagraphs.join("\n\n");
  }, 80);

  return interval;
}

function formatDictionaryContent(data) {
  wikiContent.innerHTML = '';
  
  Object.entries(data).forEach(([key, value]) => {
    const titleElement = document.createElement('h3');
    titleElement.style.fontWeight = 'bold';
    titleElement.style.marginTop = '20px';
    titleElement.style.marginBottom = '10px';
    titleElement.textContent = key;
    
    const paragraphElement = document.createElement('p');
    paragraphElement.style.marginBottom = '15px';
    paragraphElement.style.lineHeight = '1.6';
    paragraphElement.textContent = value;
    
    wikiContent.appendChild(titleElement);
    wikiContent.appendChild(paragraphElement);
  });
}

searchBtn.addEventListener("click", async () => {
  searchPage.classList.add("hidden");
  setTimeout(() => {
    resultsPage.classList.remove("hidden");
  }, 600);

  const effect = startDecryptEffect();

  const timeoutWarning = setTimeout(() => {
    timeoutBox.classList.remove("hidden");
  }, 60000);

  try {
    const query = document.getElementById("search-input").value;
    const response = await fetch("Backend api url here ex:http://127.0.0.1:8000/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ topic: query })
    });

    const data = await response.json();

    clearInterval(effect);
    clearTimeout(timeoutWarning);
    timeoutBox.classList.add("hidden");

    if (typeof data.summary === "object" && data.summary !== null) {
      formatDictionaryContent(data.summary);
    } else if (typeof data.summary === "string") {
      wikiContent.textContent = data.summary;
    } else {
      wikiContent.textContent = "No summary available... 😭😂✌️";
    }
  } catch (err) {
    clearInterval(effect);
    clearTimeout(timeoutWarning);
    timeoutBox.classList.add("hidden");
    wikiContent.textContent = "⚠️ ⚠️ Error fetching summary!! ⚠️⚠️";
    console.error(err);
  }
});