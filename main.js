// v1_01 WhatsApp Widget toggle
(function(){
  var fab = document.getElementById('waFab');
  var menu = document.getElementById('waMenu');
  if(!fab || !menu) return;
  function show(){ menu.hidden = false; fab.setAttribute('aria-expanded','true'); }
  function hide(){ menu.hidden = true; fab.setAttribute('aria-expanded','false'); }
  fab.addEventListener('click', function(e){ menu.hidden ? show() : hide(); });
  document.addEventListener('click', function(e){
    if(!menu.contains(e.target) && !fab.contains(e.target)) hide();
  });
})();