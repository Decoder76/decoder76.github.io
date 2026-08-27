---
layout: page
title: "AI Portfolio Assistant"
permalink: /pages/ai-assistant/
---

<div class="max-w-3xl mx-auto my-6">
  <!-- Chat Container -->
  <div class="bg-slate-900/90 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden flex flex-col h-[650px]">
    
    <!-- Chat Header -->
    <div class="px-6 py-4 bg-slate-950 border-b border-slate-800 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></div>
        <div>
          <h2 class="text-sm font-bold text-white tracking-wide">Lokesh's Knowledge Core</h2>
          <p class="text-[11px] text-slate-400 font-mono">CLIENT_INFERENCE: ACTIVE</p>
        </div>
      </div>
      <span class="text-xs bg-amber-500/10 text-amber-400 border border-amber-500/20 px-2.5 py-1 rounded-full font-mono">v1.0-static</span>
    </div>

    <!-- Suggested Quick Prompts -->
    <div class="px-6 py-3 bg-slate-950/40 border-b border-slate-800/60 flex gap-2 overflow-x-auto text-xs scrollbar-none">
      <button onclick="sendQuickPrompt('What is your core tech stack?')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">⚡ Tech Stack</button>
      <button onclick="sendQuickPrompt('Tell me about the FastAPI Inference API')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">🚀 FastAPI Project</button>
      <button onclick="sendQuickPrompt('What is your background and experience?')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">💼 Experience</button>
      <button onclick="sendQuickPrompt('How can I contact you?')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">📫 Contact Info</button>
    </div>

    <!-- Message History Area -->
    <div id="chatMessages" class="flex-1 overflow-y-auto p-6 space-y-4 text-sm">
      <div class="flex items-start gap-3">
        <div class="w-8 h-8 rounded-lg bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-amber-400 text-xs font-bold flex-shrink-0">AI</div>
        <div class="bg-slate-800/80 border border-slate-700/60 rounded-2xl rounded-tl-none px-4 py-3 text-slate-200 leading-relaxed max-w-[85%]">
          Hello! I am Lokesh's interactive assistant. Ask me anything about his backend projects, AI/ML models, system metrics, or technical background.
        </div>
      </div>
    </div>

    <!-- Input Form -->
    <div class="p-4 bg-slate-950 border-t border-slate-800">
      <form id="chatForm" class="flex gap-2">
        <input 
          type="text" 
          id="userInput" 
          placeholder="Ask a question about systems, skills, or projects..." 
          autocomplete="off"
          class="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-500 transition-colors"
        />
        <button 
          type="submit" 
          class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-6 py-3 rounded-xl transition-all shadow-lg shadow-amber-500/10 flex items-center justify-center text-sm"
        >
          Send
        </button>
      </form>
    </div>
  </div>
</div>

<!-- Embedded Knowledge Base & Client-Side Search Engine -->
<script id="chatbot-knowledge" type="application/json">
{{ site.data.chatbot_knowledge | jsonify }}
</script>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const chatMessages = document.getElementById("chatMessages");
  const chatForm = document.getElementById("chatForm");
  const userInput = document.getElementById("userInput");

  let knowledgeData = [];
  try {
    const rawData = document.getElementById("chatbot-knowledge").textContent;
    knowledgeData = JSON.parse(rawData) || [];
  } catch (err) {
    console.error("Could not parse chatbot knowledge data:", err);
  }

  function appendMessage(sender, text) {
    const isUser = sender === "User";
    const msgWrapper = document.createElement("div");
    msgWrapper.className = `flex items-start gap-3 ${isUser ? "flex-row-reverse" : ""}`;

    const avatar = document.createElement("div");
    avatar.className = isUser 
      ? "w-8 h-8 rounded-lg bg-slate-700 flex items-center justify-center text-white text-xs font-bold flex-shrink-0"
      : "w-8 h-8 rounded-lg bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-amber-400 text-xs font-bold flex-shrink-0";
    avatar.innerText = isUser ? "YOU" : "AI";

    const bubble = document.createElement("div");
    bubble.className = isUser
      ? "bg-amber-500 text-slate-950 font-medium rounded-2xl rounded-tr-none px-4 py-3 leading-relaxed max-w-[85%]"
      : "bg-slate-800/80 border border-slate-700/60 rounded-2xl rounded-tl-none px-4 py-3 text-slate-200 leading-relaxed max-w-[85%]";
    bubble.innerHTML = text;

    msgWrapper.appendChild(avatar);
    msgWrapper.appendChild(bubble);
    chatMessages.appendChild(msgWrapper);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function matchQuery(query) {
    if (!knowledgeData.length) {
      return "Knowledge base is currently empty or indexing.";
    }

    const tokens = query.toLowerCase().replace(/[^\w\s]/gi, '').split(/\s+/).filter(Boolean);
    let bestScore = 0;
    let bestAnswer = null;

    knowledgeData.forEach(item => {
      let score = 0;
      const qText = (item.question || "").toLowerCase();
      const aText = (item.answer || "").toLowerCase();
      const keywords = (item.keywords || []).map(k => k.toLowerCase());

      tokens.forEach(token => {
        if (keywords.includes(token)) score += 4;
        if (qText.includes(token)) score += 3;
        if (aText.includes(token)) score += 1;
      });

      if (score > bestScore) {
        bestScore = score;
        bestAnswer = item.answer;
      }
    });

    if (bestScore > 0 && bestAnswer) {
      return bestAnswer;
    }

    return "I don't have exact metrics on that query yet. Feel free to explore my <a href='/pages/projects/' class='text-amber-400 underline'>Projects page</a> or inspect my <a href='/pages/resume/' class='text-amber-400 underline'>Resume</a> for technical specifications.";
  }

  window.sendQuickPrompt = function(promptText) {
    userInput.value = promptText;
    chatForm.dispatchEvent(new Event("submit"));
  };

  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const query = userInput.value.trim();
    if (!query) return;

    appendMessage("User", query);
    userInput.value = "";

    // Simulate micro-inference delay
    setTimeout(() => {
      const response = matchQuery(query);
      appendMessage("AI", response);
    }, 250);
  });
});
</script>
