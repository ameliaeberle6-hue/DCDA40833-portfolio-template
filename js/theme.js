// Shared theme toggle script for site-wide dark mode
(function(){
  function applyTheme(theme){
    if(theme === 'dark') document.body.classList.add('dark');
    else document.body.classList.remove('dark');
  }

  function updateButton(toggle){
    const isDark = document.body.classList.contains('dark');
    if(!toggle) return;
    toggle.textContent = isDark ? '☀️ Light' : '🌙 Dark';
    toggle.setAttribute('aria-pressed', String(isDark));
  }

  function init(){
    const toggle = document.getElementById('theme-toggle');
    const stored = localStorage.getItem('theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initial = stored ? stored : (prefersDark ? 'dark' : 'light');
    applyTheme(initial);
    updateButton(toggle);

    if(toggle){
      toggle.addEventListener('click', ()=>{
        const isDark = document.body.classList.toggle('dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        updateButton(toggle);
      });
    }

    // Sync theme across tabs/windows
    window.addEventListener('storage', (e)=>{
      if(e.key === 'theme') applyTheme(e.newValue || 'light');
      updateButton(document.getElementById('theme-toggle'));
    });
  }

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
