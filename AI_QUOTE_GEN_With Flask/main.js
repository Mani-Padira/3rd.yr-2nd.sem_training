document.addEventListener('DOMContentLoaded', ()=>{
  const box = document.querySelector('.box');
  if(box) setTimeout(()=>box.classList.add('visible'), 40);

  // copy quote on click
  const quoteEl = document.querySelector('.quote');
  const copyBtn = document.querySelector('#copy-btn');
  if(quoteEl && copyBtn){
    copyBtn.addEventListener('click', async (e)=>{
      const txt = quoteEl.innerText.trim().replace(/^"|"$/g,'');
      try{ await navigator.clipboard.writeText(txt);
        copyBtn.innerText = 'Copied';
        setTimeout(()=>copyBtn.innerText = 'Copy', 1200);
      }catch(_){
        copyBtn.innerText = 'Copy';
      }
    });
  }

  // keyboard shortcut: N to generate new quote
  document.addEventListener('keydown', (e)=>{
    if(e.key === 'n' || e.key === 'N'){
      const btn = document.querySelector('#gen-btn');
      if(btn) btn.click();
    }
  });
});
