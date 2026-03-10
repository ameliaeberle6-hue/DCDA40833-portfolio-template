// Lightweight confetti loader and launcher — fires on page load
(function(){
  function loadScript(src, cb){
    var s = document.createElement('script');
    s.src = src; s.async = true;
    s.onload = function(){ cb && cb(null); };
    s.onerror = function(){ cb && cb(new Error('Failed to load ' + src)); };
    document.head.appendChild(s);
  }

  function burst(){
    if(typeof confetti !== 'function') return;
    // two-sided bursts for a pleasant effect
    var duration = 1800;
    var end = Date.now() + duration;
    (function frame(){
      confetti({ particleCount: 18, angle: 60, spread: 55, origin: { x: 0.1, y: 0.2 } });
      confetti({ particleCount: 18, angle: 120, spread: 55, origin: { x: 0.9, y: 0.2 } });
      if (Date.now() < end) requestAnimationFrame(frame);
    })();
  }

  function init(){
    // load CDN then trigger burst shortly after DOM is ready
    loadScript('https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js', function(err){
      if(err) return; // silently fail if CDN blocked
      setTimeout(burst, 200);
    });
  }

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
