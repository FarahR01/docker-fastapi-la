async function api(path, opts={}){
  const res = await fetch(path, opts);
  if(!res.ok) throw new Error(await res.text());
  return res.json().catch(()=>null);
}

function el(tag, cls, text){ const e = document.createElement(tag); if(cls) e.className = cls; if(text) e.textContent = text; return e }

async function load(){
  const list = document.getElementById('list');
  try{
    const tasks = await api('/tasks');
    if(!tasks.length){ list.innerHTML = '<p class="muted">No tasks yet</p>'; return }
    list.innerHTML = '';
    tasks.forEach(t=>{
      const card = el('div','card');
      const meta = el('div','meta');
      const title = el('div','title', t.title);
      const sub = el('div','muted', `#${t.id} ${t.completed? '• completed':''}`);
      meta.appendChild(title); meta.appendChild(sub);
      const actions = el('div','actions');

      const toggle = el('button','toggle', t.completed? 'Undo':'Done');
      toggle.onclick = async ()=>{ await api(`/tasks/${t.id}/toggle`, {method:'PUT'}); load(); };

      const del = el('button','delete','Delete');
      del.onclick = async ()=>{ if(confirm('Delete this task?')){ await api(`/tasks/${t.id}`, {method:'DELETE'}); load(); } };

      actions.appendChild(toggle); actions.appendChild(del);
      card.appendChild(meta); card.appendChild(actions);
      list.appendChild(card);
    })
  }catch(err){ list.innerHTML = '<p class="muted">Failed to load tasks</p>'; console.error(err) }
}

document.getElementById('add').addEventListener('click', async ()=>{
  const titleEl = document.getElementById('title');
  const title = titleEl.value.trim(); if(!title) return;
  await api('/tasks', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({title})});
  titleEl.value=''; load();
});

window.addEventListener('load', load);
