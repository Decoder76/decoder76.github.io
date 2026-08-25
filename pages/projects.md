---
layout: default
title: Projects
permalink: /pages/projects/
---

<div class="min-h-screen bg-slate-950">
  <!-- Header Section -->
  <section class="pt-32 pb-16 border-b border-slate-800">
    <div class="max-w-6xl mx-auto px-6">
      <div class="space-y-4">
        <span class="inline-block px-3 py-1 bg-amber-500/10 border border-amber-500/20 rounded-full text-amber-500 text-xs font-bold uppercase tracking-widest">Portfolio</span>
        <h1 class="brand-font text-5xl md:text-6xl font-bold text-white">Engineering Projects</h1>
        <p class="text-slate-400 text-lg max-w-2xl leading-relaxed">A selection of production-oriented AI systems and backend architectures built with a focus on modular design, security, and maintainability.</p>
      </div>
    </div>
  </section>

  <!-- Projects Grid -->
  <section class="py-20">
    <div class="max-w-6xl mx-auto px-6">
      <!-- Featured Projects from Data -->
      {% if site.data.projects %}
      <div class="grid md:grid-cols-2 lg:grid-cols-2 gap-8 mb-20">
        {% for project in site.data.projects %}
        <article class="group glass-panel p-8 rounded-2xl border border-slate-700 hover:border-amber-500/50 transition-all duration-300 hover:shadow-2xl hover:shadow-amber-500/10">
          <!-- Project Header -->
          <div class="flex flex-col h-full">
            <div class="flex justify-between items-start gap-4 mb-6">
              <div>
                <h2 class="brand-font text-2xl font-bold text-white group-hover:text-amber-500 transition-colors">
                  {{ project.title }}
                </h2>
              </div>
              <div class="flex-shrink-0 w-10 h-10 rounded-lg bg-amber-500/10 border border-amber-500/20 flex items-center justify-center">
                <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
            </div>

            <!-- Description -->
            <p class="text-slate-300 text-base leading-relaxed mb-8 flex-grow">{{ project.summary }}</p>

            <!-- Tech Stack -->
            <div class="space-y-4">
              <div class="flex flex-wrap gap-2">
                {% for tech in project.stack %}
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 text-amber-400 border border-slate-700">
                  {{ tech }}
                </span>
                {% endfor %}
              </div>

              <!-- CTA -->
              <a href="{{ site.baseurl }}/projects/{{ project.slug }}/" class="inline-flex items-center gap-2 text-amber-500 font-bold text-sm group-hover:gap-3 transition-all duration-300">
                View Architecture 
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                </svg>
              </a>
            </div>
          </div>
        </article>
        {% endfor %}
      </div>
      {% endif %}

      <!-- Additional Section for Collections Projects -->
      {% if site.projects %}
      <div class="mt-20 border-t border-slate-800 pt-20">
        <h2 class="brand-font text-3xl font-bold text-white mb-12">Additional Projects</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
          {% for project in site.projects %}
          <article class="group glass-panel p-8 rounded-2xl border border-slate-700 hover:border-amber-500/50 transition-all duration-300">
            <div class="flex flex-col h-full">
              <h3 class="brand-font text-xl font-bold text-white mb-4 group-hover:text-amber-500 transition-colors">
                <a href="{{ project.url }}" class="hover:underline">{{ project.title }}</a>
              </h3>
              <p class="text-slate-300 text-sm leading-relaxed mb-6 flex-grow">{{ project.overview }}</p>
              <div class="flex flex-wrap gap-2">
                {% for tech in project.stack %}
                <span class="px-2 py-1 text-xs font-mono bg-slate-800 text-amber-400 rounded border border-slate-700">{{ tech }}</span>
                {% endfor %}
              </div>
            </div>
          </article>
          {% endfor %}
        </div>
      </div>
      {% endif %}
    </div>
  </section>

  <!-- Call to Action Section -->
  <section class="py-20 border-t border-slate-800 bg-gradient-to-b from-slate-950 to-slate-900/50">
    <div class="max-w-6xl mx-auto px-6 text-center">
      <h2 class="brand-font text-3xl font-bold text-white mb-6">Interested in collaboration?</h2>
      <p class="text-slate-400 text-lg mb-8 max-w-2xl mx-auto">Explore more about my experience, skills, and how I approach production engineering.</p>
      <div class="flex flex-wrap gap-4 justify-center">
        <a href="{{ site.baseurl }}/pages/about/" class="px-8 py-3 bg-amber-500 text-slate-950 rounded-lg font-bold hover:bg-amber-400 transition-all shadow-lg shadow-amber-500/20">
          Learn More About Me
        </a>
        <a href="{{ site.baseurl }}/pages/resume/" class="px-8 py-3 border border-slate-700 text-slate-300 rounded-lg font-bold hover:bg-slate-800 transition-all">
          View Resume
        </a>
      </div>
    </div>
  </section>
</div>

<style>
  /* Project Grid Animation */
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  article {
    animation: fadeInUp 0.6s ease-out forwards;
  }

  article:nth-child(2) { animation-delay: 0.1s; }
  article:nth-child(3) { animation-delay: 0.2s; }
  article:nth-child(4) { animation-delay: 0.3s; }

  /* Hover Effect Enhancement */
  .glass-panel {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .glass-panel:hover {
    transform: translateY(-4px);
  }
</style>
