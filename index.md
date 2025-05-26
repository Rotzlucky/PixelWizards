---
layout: default
title: Spellcode Academy - Choose Your Language
lang: en
---

# Welcome to the Spellcode Academy!

<div style="text-align: center; margin: 50px 0;">
  <h2>🧙‍♂️ Choose Your Magical Language 🧙‍♀️</h2>
  <p>Select your preferred language to begin your coding adventure:</p>
  
  <div style="display: flex; justify-content: center; gap: 30px; margin: 40px 0; flex-wrap: wrap;">
    <a href="{{ '/en/' | relative_url }}" style="text-decoration: none; color: inherit;">
      <div style="border: 3px solid #D4AF37; border-radius: 15px; padding: 30px; background: linear-gradient(135deg, #f5f5f5, #e8e8e8); box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.3s; min-width: 200px;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        <div style="font-size: 48px; margin-bottom: 15px;">🇬🇧</div>
        <h3 style="margin: 10px 0; color: #2c3e50;">English</h3>
        <p style="margin: 0; color: #7f8c8d;">Learn Python programming in English</p>
      </div>
    </a>
    
    <a href="{{ '/de/' | relative_url }}" style="text-decoration: none; color: inherit;">
      <div style="border: 3px solid #D4AF37; border-radius: 15px; padding: 30px; background: linear-gradient(135deg, #f5f5f5, #e8e8e8); box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.3s; min-width: 200px;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        <div style="font-size: 48px; margin-bottom: 15px;">🇩🇪</div>
        <h3 style="margin: 10px 0; color: #2c3e50;">Deutsch</h3>
        <p style="margin: 0; color: #7f8c8d;">Lerne Python-Programmierung auf Deutsch</p>
      </div>
    </a>
  </div>
</div>

<script>
// Auto-detect and redirect based on browser language preference
(function() {
  const browserLang = navigator.language || navigator.userLanguage;
  const savedLang = localStorage.getItem('spellcode-language');
  
  // Only auto-redirect if no saved preference and this is the first visit
  if (!savedLang && !sessionStorage.getItem('language-selected')) {
    sessionStorage.setItem('language-selected', 'true');
    
    if (browserLang.startsWith('de')) {
      window.location.href = '{{ "/de/" | relative_url }}';
    } else {
      window.location.href = '{{ "/en/" | relative_url }}';
    }
  }
})();

// Save language preference when user clicks
document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('a[href*="/en/"], a[href*="/de/"]');
  links.forEach(link => {
    link.addEventListener('click', function() {
      const lang = this.href.includes('/en/') ? 'en' : 'de';
      localStorage.setItem('spellcode-language', lang);
    });
  });
});
</script>
