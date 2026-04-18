---
layout: page
title: Backend Notes
permalink: /backend/
---

<div id="gate-shell">
  <h1>Restricted Page</h1>
  <p>This page is for private portfolio planning and backend notes.</p>
  <p><strong>Enter secret code to continue.</strong></p>

  <form id="secret-form" style="margin-top: 1rem;">
    <input
      id="secret-input"
      type="password"
      placeholder="Enter secret code"
      style="width: min(360px, 100%); padding: 0.8rem 0.9rem; border-radius: 12px; border: 1px solid #d2d2d7;"
    />
    <button
      type="submit"
      style="margin-left: 0.5rem; min-height: 44px; padding: 0 1rem; border-radius: 999px; border: 0; background: #0071e3; color: white; font-weight: 600;"
    >
      Unlock
    </button>
  </form>

  <p id="secret-error" style="display: none; color: #b42318; margin-top: 0.8rem;">
    Incorrect code.
  </p>
</div>

<div id="private-content" style="display: none;">
  <h1>Backend Notes</h1>
  <p>This is the hidden planning page for future portfolio work.</p>

  <h2>Pending content to add</h2>
  <ul>
    <li>Real backend projects with architecture summary</li>
    <li>FastAPI or Rails API examples</li>
    <li>Frontend project screenshots or links</li>
    <li>Cybersecurity lab notes and tools used</li>
    <li>Certifications and learning roadmap</li>
    <li>Resume and social/profile cleanup</li>
  </ul>

  <h2>Note</h2>
  <p>
    This gate is client-side only. Anyone with access to page source can still inspect it, so use it as a convenience layer, not as real protection.
  </p>
</div>

<script>
  (function () {
    var SECRET_CODE = "open-backend";
    var STORAGE_KEY = "lokesh-portfolio-backend-unlocked";
    var form = document.getElementById("secret-form");
    var input = document.getElementById("secret-input");
    var error = document.getElementById("secret-error");
    var gate = document.getElementById("gate-shell");
    var content = document.getElementById("private-content");

    function unlock() {
      gate.style.display = "none";
      content.style.display = "block";
    }

    if (sessionStorage.getItem(STORAGE_KEY) === "true") {
      unlock();
      return;
    }

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (input.value === SECRET_CODE) {
        sessionStorage.setItem(STORAGE_KEY, "true");
        unlock();
      } else {
        error.style.display = "block";
      }
    });
  })();
</script>
