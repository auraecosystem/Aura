# Re-run build for the branded site. (Second attempt after state reset)
import os, shutil, json, zipfile
from pathlib import Path

root = Path("/mnt/data/web4application-site-branded")
if root.exists():
    shutil.rmtree(root)
assets = root / "assets"
assets.mkdir(parents=True, exist_ok=True)

# Copy mindmap image and generated logo into assets
src_map = Path("/mnt/data/B85C713A-4238-4616-9333-5B98BDF64079.png")
if src_map.exists():
    shutil.copy(src_map, assets / "project-mindmap.png")
logo_src = Path("/mnt/data/A_digital_vector_logo_design_features_a_neon_teal_.png")
if logo_src.exists():
    shutil.copy(logo_src, assets / "gpt5-mini-logo.png")

site_data = {
  "title": "Web4application — Project Knowledge Base",
  "org": "Web4application",
  "sections": [
    {
      "id": "apps",
      "label": "Apps / Projects",
      "type": "apps",
      "items": ["Lola", "ChatGPT5 Mini", "ROO4AI", "Swiftbot", "Web4Asset", "Web4AI_Project_Assistant"]
    },
    {
      "id": "repos",
      "label": "Repositories (by theme)",
      "type": "repo",
      "items": [
        "fadaka-blockhaain",
        "fadaka-dashboard",
        "fadaka-factory",
        "Fadakacoin",
        "assets",
        "btc-hack",
        "Btchack",
        "etck333",
        "Failenbae-AI-Generative-Systems",
        "Failenbae-Web4-Infra-DevOps",
        "Failenbae-Chat-Social-Fun"
      ]
    },
    {
      "id": "templates",
      "label": "Templates & Demos",
      "type": "repo",
      "items": [
        "BEEZ-Chat",
        "Bizz",
        "BLACKPINKchat",
        "Discord",
        "blank-app",
        "demo-repository",
        "bnb-chain.github.io"
      ]
    },
    {
      "id": "domains",
      "label": "Domains",
      "type": "domain",
      "items": ["api.kubu-hai.com", "web4app.com", "konga-gateway.example", "github.com/Web4application/actions", "alembic.docs"]
    },
    {
      "id": "tools",
      "label": "Tools / Infrastructure",
      "type": "tool",
      "items": ["Docker Compose", "Homebrew packaging", "ChatGPT5 Mini logo", "Fadaka Blockchain", "Web4AI identity"]
    }
  ]
}

(root / "data.json").write_text(json.dumps(site_data, indent=2))

index_html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{site_data['title']}</title>
  <meta name="description" content="Branded snapshot of the Web4application project knowledge base." />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
<header class="site-header">
  <div class="brand">
    <img src="assets/gpt5-mini-logo.png" alt="ChatGPT5 Mini logo" class="brand-logo" />
    <div>
      <h1>Web4application</h1>
      <p class="tag">Project Knowledge Base</p>
    </div>
  </div>
  <nav class="nav" aria-label="Primary">
    <a href="#apps">Apps</a>
    <a href="#repos">Repositories</a>
    <a href="#templates">Templates</a>
    <a href="#domains">Domains</a>
    <a href="#tools">Tools</a>
  </nav>
</header>

<main class="container">
  <section class="hero">
    <div class="hero-copy">
      <h2>Everything in one clean map</h2>
      <p>Browse projects, repos, infra, and domains. Search the entire knowledge base instantly.</p>
      <div class="search-wrap">
        <input id="search" type="search" placeholder="Search projects, repos, tools…" aria-label="Search" />
      </div>
      <div class="meta">
        <a class="cta" href="https://github.com/{site_data['org']}" target="_blank" rel="noopener">View GitHub Org</a>
        <a class="cta ghost" href="https://web4app.com" target="_blank" rel="noopener">Visit web4app.com</a>
      </div>
    </div>
    <figure class="hero-figure">
      <img src="assets/project-mindmap.png" alt="Mind map of Web4application knowledge base" />
      <figcaption>Project mind-map</figcaption>
    </figure>
  </section>

  <div id="sections" class="grid"></div>
</main>

<footer class="site-footer">
  <p>© {site_data['title'].split(' — ')[0]} · Built with vanilla HTML/CSS/JS · Auto-links to GitHub org: {site_data['org']}</p>
</footer>

<script>window.__SITE_DATA__ = {json.dumps(site_data)};</script>
<script>window.__ORG__ = "{site_data['org']}";</script>
<script src="app.js"></script>
</body>
</html>
"""
(root / "index.html").write_text(index_html)

styles_css = """
:root{
  --bg: #071022;
  --card: #0d1420;
  --muted: #9fb3c9;
  --text: #e6f7f6;
  --teal: #00e6c3;
  --accent: #00d1b3;
  --glass: rgba(255,255,255,0.03);
  --radius: 12px;
  --shadow: 0 6px 30px rgba(0,0,0,0.6);
}

*{box-sizing:border-box}
html,body{height:100%}
body{
  margin:0; font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  background: radial-gradient(800px 400px at 10% 10%, rgba(0,210,179,0.06), transparent), var(--bg);
  color:var(--text); line-height:1.5;
}

.site-header{position:sticky; top:0; display:flex; align-items:center; justify-content:space-between; gap:1rem; padding:12px 18px; background:linear-gradient(180deg, rgba(6,10,15,0.6), rgba(6,10,15,0.35)); border-bottom:1px solid rgba(255,255,255,0.03)}
.brand{display:flex; align-items:center; gap:12px}
.brand-logo{width:56px; height:56px; object-fit:contain; border-radius:10px; box-shadow: 0 6px 24px rgba(0,220,190,0.12); background:linear-gradient(180deg, rgba(0,0,0,0.2), rgba(255,255,255,0.02))}
.site-header h1{margin:0; font-size:1.1rem}
.tag{margin:0; color:var(--muted); font-size:0.85rem}
.nav a{color:var(--muted); text-decoration:none; margin-left:10px; padding:6px 8px; border-radius:8px}
.nav a:hover{color:var(--text); background:rgba(0,0,0,0.15)}

.container{max-width:1100px; margin:18px auto; padding:0 18px}

.hero{display:grid; grid-template-columns: 1.1fr .9fr; gap:16px; padding:16px; background:var(--glass); border-radius:14px; border:1px solid rgba(255,255,255,0.03); box-shadow:var(--shadow)}
.hero-copy h2{margin:6px 0; font-size:1.6rem; color:var(--teal)}
.search-wrap{margin-top:12px}
#search{width:100%; padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.03); background:#071122; color:var(--text)}
.meta{margin-top:12px; display:flex; gap:10px}
.cta{padding:8px 12px; border-radius:10px; background:linear-gradient(90deg,var(--teal),var(--accent)); color:#001219; text-decoration:none; font-weight:600}
.cta.ghost{background:transparent; border:1px solid rgba(255,255,255,0.04); color:var(--muted)}

.hero-figure{background:linear-gradient(180deg, rgba(0,0,0,0.18), rgba(255,255,255,0.01)); border-radius:10px; padding:8px; display:flex; flex-direction:column; align-items:stretch}
.hero-figure img{width:100%; border-radius:8px; display:block}
.hero-figure figcaption{margin-top:8px; font-size:0.85rem; color:var(--muted)}

.grid{display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:12px; margin-top:18px}
.card{background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.01)); padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.02)}
.card header{display:flex; align-items:center; justify-content:space-between; margin-bottom:8px}
.card h3{margin:0; font-size:1rem; color:var(--teal)}
.pill{background:rgba(0,0,0,0.2); color:var(--muted); padding:4px 8px; border-radius:999px; font-size:0.8rem}

.list{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:8px}
.item{display:flex; align-items:center; gap:10px; padding:8px; border-radius:10px; background:rgba(0,0,0,0.12); border:1px solid rgba(255,255,255,0.02)}
.item a{color:var(--text); text-decoration:none}
.item a:hover{color:var(--teal)}

.icon{width:30px; height:30px; display:inline-flex; align-items:center; justify-content:center; border-radius:8px; background:linear-gradient(180deg, rgba(0,0,0,0.12), rgba(255,255,255,0.01)); color:var(--teal); font-weight:700}

.site-footer{margin-top:20px; padding:18px; text-align:center; color:var(--muted)}

@media (max-width:860px){ .hero{grid-template-columns:1fr} .brand-logo{width:48px;height:48px} }
"""

(root / "styles.css").write_text(styles_css)

app_js = """
(function(){
  const data = window.__SITE_DATA__ || {};
  const ORG = window.__ORG__ || 'Web4application';
  const container = document.getElementById('sections');
  const searchEl = document.getElementById('search');

  function isDomain(s){
    return /^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\.)+[a-z]{2,}$/i.test(s) || s.includes('.github.io');
  }

  function repoLink(name){
    const slug = name.replace(/\\s+/g, '-');
    return `https://github.com/${ORG}/${encodeURIComponent(slug)}`;
  }

  function render(filter=''){
    container.innerHTML = '';
    const q = (filter||'').trim().toLowerCase();
    for(const section of data.sections || []){
      const items = section.items.map(text => {
        const visible = !q || text.toLowerCase().includes(q);
        return { text, visible };
      }).filter(x=>x.visible);
      if(!items.length) continue;

      const card = document.createElement('section');
      card.className = 'card';
      card.id = section.id;
      card.innerHTML = `
        <header>
          <h3>${section.label}</h3>
          <span class="pill">${items.length}</span>
        </header>
        <ul class="list"></ul>
      `;
      const ul = card.querySelector('.list');
      for(const it of items){
        const li = document.createElement('li');
        li.className = 'item';
        let content = '';
        const text = it.text;
        if(section.type === 'domain' || isDomain(text)){
          const href = text.startsWith('http') ? text : 'https://' + text;
          content = `<span class="icon">🌐</span><a href="${href}" target="_blank" rel="noopener">${text}</a>`;
        } else if(section.type === 'repo' || /^[A-Za-z0-9_\\- ]+$/.test(text)){
          const href = repoLink(text);
          content = `<span class="icon">📦</span><a href="${href}" target="_blank" rel="noopener">${text}</a>`;
        } else {
          const href = repoLink(text);
          content = `<span class="icon">🚀</span><a href="${href}" target="_blank" rel="noopener">${text}</a>`;
        }
        li.innerHTML = content;
        ul.appendChild(li);
      }
      container.appendChild(card);
    }
  }

  searchEl.addEventListener('input', e => render(e.target.value));
  render();
})();
"""
(root / "app.js").write_text(app_js)

readme = f"""
# Web4application — Branded Project Knowledge Base

This build includes:
- Branded neon-teal theme and ChatGPT5 Mini logo (assets/gpt5-mini-logo.png)
- Auto-linking to GitHub org `{site_data['org']}` for repos/apps
- Domain auto-detection and linking
- Live search and responsive layout

## Preview locally
```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

## Deploy
Push to GitHub and enable Pages, or drop into Vercel/Netlify — no build step required.

Edit `data.json` to change content. The app reads `window.__SITE_DATA__` embedded in `index.html`.
"""
(root / "README.md").write_text(readme)

zip_path = Path("/mnt/data/web4application-site-branded.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for p in root.rglob("*"):
        zf.write(p, p.relative_to(root))

zip_path.exists(), str(zip_path)
