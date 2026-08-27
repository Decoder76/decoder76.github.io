---
layout: page
title: "AI Portfolio Assistant"
permalink: /pages/ai-assistant/
---

<div class="max-w-3xl mx-auto my-6">
  <div class="bg-slate-900/90 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden flex flex-col h-[650px]">
    
    <!-- Chat Header -->
    <div class="px-6 py-4 bg-slate-950 border-b border-slate-800 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></div>
        <div>
          <h2 class="text-sm font-bold text-white tracking-wide">Lokesh's Knowledge Core</h2>
          <p class="text-[11px] text-slate-400 font-mono">DYNAMIC_COLLECTION_FEED: ACTIVE</p>
        </div>
      </div>
      <span class="text-xs bg-amber-500/10 text-amber-400 border border-amber-500/20 px-2.5 py-1 rounded-full font-mono">Dynamic Jekyll Feed</span>
    </div>

    <!-- Quick Prompts -->
    <div class="px-6 py-3 bg-slate-950/40 border-b border-slate-800/60 flex gap-2 overflow-x-auto text-xs scrollbar-none">
      <button onclick="sendQuickPrompt('What projects have you built?')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">🚀 All Projects</button>
      <button onclick="sendQuickPrompt('What is your tech stack?')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">⚡ Tech Stack</button>
      <button onclick="sendQuickPrompt('Tell me about your experience')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">💼 Experience</button>
      <button onclick="sendQuickPrompt('Where are you located and how to contact?')" class="whitespace-nowrap px-3 py-1 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">📫 Contact</button>
    </div>

    <!-- Messages Container -->
    <div id="chatMessages" class="flex-1 overflow-y-auto p-6 space-y-4 text-sm">
      <div class="flex items-start gap-3">
        <div class="w-8 h-8 rounded-lg bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-amber-400 text-xs font-bold flex-shrink-0">AI</div>
        <div class="bg-slate-800/80 border border-slate-700/60 rounded-2xl rounded-tl-none px-4 py-3 text-slate-200 leading-relaxed max-w-[85%]">
          Hello! I dynamically index all project architectures from <code>_projects/</code>, skills, and experience. Ask me about any specific model, API, or system design.
        </div>
      </div>
    </div>

    <!-- Input Form -->
    <div class="p-4 bg-slate-950 border-t border-slate-800">
      <form id="chatForm" class="flex gap-2">
        <input 
          type="text" 
          id="userInput" 
          placeholder="Ask about FastAPI, Bi-LSTM, LMS AI Core, or system metrics..." 
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

<!-- Dynamically compiled knowledge feed built directly from Jekyll collections & data -->
<script id="dynamic-knowledge" type="application/json">
[
  {% for project in site.projects %}
  {
    "type": "project",
    "title": {{ project.title | jsonify }},
    "url": {{ project.url | relative_url | jsonify }},
    "keywords": [
      {{ project.title | downcase | jsonify }},
      {% if project.stack %}{% for s in project.stack %}{{ s | downcase | jsonify }},{% endfor %}{% endif %}
      "project", "architecture", "system", "performance"
    ],
    "content": {{ project.content | strip_html | normalize_whitespace | truncate: 450 | jsonify }}
  },
  {% endfor %}

  {% for skill in site.data.skills %}
  {
    "type": "skills",
    "title": {{ skill.category | jsonify }},
    "keywords": ["skills", "stack", "tools", "languages", {{ skill.category | downcase | jsonify }}, {% for item in skill.items %}{{ item | downcase | jsonify }}{% unless forloop.last %},{% endunless %}{% endfor %}],
    "content": "Core competencies in <strong>{{ skill.category }}</strong> include: {{ skill.items | join: ', ' }}."
  },
  {% endfor %}

  {% for exp in site.data.experience %}
  {
    "type": "experience",
    "title": {{ exp.title | jsonify }},
    "keywords": ["experience", "work", "career", "background", {{ exp.title | downcase | jsonify }}, {{ exp.organization | downcase | jsonify }}],
    "content": "<strong>{{ exp.title }}</strong> at <strong>{{ exp.organization }}</strong> ({{ exp.period }}): {{ exp.description }} — Technologies: {{ exp.tech | join: ', ' }}."
  },
  {% endfor %}

  {
    "type": "contact",
    "title": "Contact & Location",
    "keywords": ["contact", "email", "github", "reach", "hire", "location", "city"],
    "content": "Lokesh Kumar Jayswal is based in Gorakhpur, UP, India. You can connect on GitHub at <a href='https://github.com/Decoder76' target='_blank' class='text-amber-400 underline font-medium'>github.com/Decoder76</a> or visit the <a href='{{ '/pages/contact/' | relative_url }}' class='text-amber-400 underline font-medium'>Contact page</a>."
  }
]
</script>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const chatMessages = document.getElementById("chatMessages");
  const chatForm = document.getElementById("chatForm");
  const userInput = document.getElementById("userInput");

  let dynamicIndex = [];
  try {
    const rawFeed = document.getElementById("dynamic-knowledge").textContent;
    dynamicIndex = JSON.parse(rawFeed) || [];
  } catch (err) {
    console.error("Error reading dynamic Jekyll feed:", err);
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
    const cleanQuery = query.toLowerCase().trim();

    // Natural greetings
    const greetings = ["hi", "hello", "hey", "who are you", "what can you do"];
    if (greetings.some(g => cleanQuery === g || cleanQuery.startsWith(g + " "))) {
      return "Hello! I dynamically parse Lokesh's project architectures, technical stack, and career background. You can ask about projects like <strong>FastAPI Prediction API</strong>, <strong>Deep Sequence NLP</strong>, or general skills.";
    }

    if (!dynamicIndex.length) {
      return "Dynamic knowledge feed is building. Please refresh in a moment.";
    }

    const tokens = cleanQuery.replace(/[^\w\s]/gi, '').split(/\s+/).filter(Boolean);
    let bestScore = 0;
    let bestMatch = null;

    dynamicIndex.forEach(item => {
      let score = 0;
      const title = (item.title || "").toLowerCase();
      const content = (item.content || "").toLowerCase();
      const keywords = (item.keywords || []).map(k => String(k).toLowerCase());

      tokens.forEach(token => {
        if (title.includes(token)) score += 6;
        if (keywords.some(k => k.includes(token))) score += 4;
        if (content.includes(token)) score += 2;
      });

      if (score > bestScore) {
        bestScore = score;
        bestMatch = item;
      }
    });

    if (bestScore > 0 && bestMatch) {
      if (bestMatch.type === "project") {
        return `<strong>${bestMatch.title}</strong><br><br>${bestMatch.content}<br><br><a href="${bestMatch.url}" class="text-amber-400 underline font-medium">Examine Architecture Case Study &rarr;</a>`;
      }
      return bestMatch.content;
    }

    return "I couldn't find an exact match in the current project case studies. Browse the <a href='{{ '/pages/projects/' | relative_url }}' class='text-amber-400 underline font-medium'>Projects Showcase</a> or <a href='{{ '/pages/resume/' | relative_url }}' class='text-amber-400 underline font-medium'>Resume</a> for full details.";
  }

  window.sendQuickPrompt = function(text) {
    userInput.value = text;
    chatForm.dispatchEvent(new Event("submit"));
  };

  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const query = userInput.value.trim();
    if (!query) return;

    appendMessage("User", query);
    userInput.value = "";

    setTimeout(() => {
      const response = matchQuery(query);
      appendMessage("AI", response);
    }, 150);
  });
});
</script>
