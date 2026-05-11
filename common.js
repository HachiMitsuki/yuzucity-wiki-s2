// Sidebar definition - shared across all pages
const NAV = [
  {title:"概要", links:[
    {slug:"index", label:"街の概要", icon:"🏙️"},
    {slug:"guide", label:"初心者ガイド", icon:"📖"},
    {slug:"commands", label:"コマンド一覧", icon:"⌨️"},
    {slug:"terms", label:"配信用語集", icon:"💬"},
  ]},
  {title:"ルール", links:[
    {slug:"rules-general", label:"一般ルール", icon:"📜"},
    {slug:"rules-rp", label:"RPルール", icon:"🎭"},
    {slug:"rules-combat", label:"戦闘ルール", icon:"⚔️"},
    {slug:"rules-vehicle", label:"車両ルール", icon:"🚗"},
    {slug:"rules-relationship", label:"恋愛RP", icon:"💕"},
  ]},
  {title:"職業", links:[
    {slug:"job-pd", label:"警察 (PD)", icon:"🚓"},
    {slug:"job-ems", label:"EMS（救急）", icon:"🚑"},
    {slug:"job-doctor", label:"個人医", icon:"⚕️"},
    {slug:"job-mechanic", label:"メカニック", icon:"🔧"},
    {slug:"job-food", label:"飲食店", icon:"🍔"},
    {slug:"job-crime", label:"犯罪", icon:"💀"},
  ]},
  {title:"カタログ", links:[
    {slug:"dealer", label:"ディーラー", icon:"🚗"},
    {slug:"icarus", label:"Icarus", icon:"🍰"},
    {slug:"jointshop", label:"Jointshop", icon:"🍃"},
  ]},
  {title:"最新情報", links:[
    {slug:"news", label:"お知らせ", icon:"📢"},
    {slug:"updates", label:"機能変更", icon:"🔄"},
    {slug:"streams", label:"配信中", icon:"📺"},
    {slug:"socials", label:"住民SNS", icon:"𝕏"},
    {slug:"clips", label:"クリップ", icon:"🎬"},
  ]},
  {title:"外部リンク", links:[
    {url:"https://x.com/yuzu_server", label:"公式 Twitter", icon:"𝕏"},
    {url:"https://discord.gg/gHCeUWFyyc", label:"Discord", icon:"💬"},
  ]},
];

// Build flat list for prev/next navigation
const FLAT_NAV = NAV.flatMap(s => s.links.filter(l => l.slug));

// Render sidebar
function renderSidebar(currentSlug){
  const html = NAV.map(section => `
    <div class="nav-section">
      <div class="nav-section-title">${section.title}</div>
      ${section.links.map(link => {
        if(link.url) return `<a href="${link.url}" class="nav-link" target="_blank" rel="noopener"><span class="nav-link-icon">${link.icon}</span>${link.label}</a>`;
        const active = link.slug === currentSlug ? ' active' : '';
        const href = link.slug === 'index' ? 'index.html' : `${link.slug}.html`;
        return `<a href="${href}" class="nav-link${active}"><span class="nav-link-icon">${link.icon}</span>${link.label}</a>`;
      }).join('')}
    </div>
  `).join('');
  return html;
}

// Render top bar
function renderTopbar(){
  return `
    <a href="index.html" class="topbar-brand">🍋 Yuzu City Wiki</a>
    <input type="text" class="topbar-search" id="topSearch" placeholder="🔍 このページを検索">
    <div class="topbar-actions">
      <a href="https://x.com/yuzu_server" target="_blank">𝕏</a>
      <a href="https://discord.gg/gHCeUWFyyc" target="_blank">Discord</a>
      <button class="menu-toggle" onclick="document.getElementById('sidebar').classList.toggle('open')">☰</button>
    </div>
  `;
}

// Render prev/next nav
function renderPageNav(currentSlug){
  const idx = FLAT_NAV.findIndex(l => l.slug === currentSlug);
  if(idx === -1) return '';
  const prev = idx > 0 ? FLAT_NAV[idx-1] : null;
  const next = idx < FLAT_NAV.length - 1 ? FLAT_NAV[idx+1] : null;
  const prevHref = prev ? (prev.slug === 'index' ? 'index.html' : prev.slug + '.html') : '#';
  const nextHref = next ? (next.slug === 'index' ? 'index.html' : next.slug + '.html') : '#';
  return `
    <div class="page-nav">
      ${prev ? `<a href="${prevHref}" class="page-nav-link"><div class="page-nav-link-arrow">←</div><div><div class="page-nav-link-label">前のページ</div><div class="page-nav-link-title">${prev.icon} ${prev.label}</div></div></a>` : '<div class="page-nav-spacer"></div>'}
      ${next ? `<a href="${nextHref}" class="page-nav-link next"><div class="page-nav-link-arrow">→</div><div><div class="page-nav-link-label">次のページ</div><div class="page-nav-link-title">${next.icon} ${next.label}</div></div></a>` : '<div class="page-nav-spacer"></div>'}
    </div>
  `;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  const slug = document.body.dataset.page || 'index';

  // Inject topbar
  const topbar = document.getElementById('topbar');
  if(topbar) topbar.innerHTML = renderTopbar();

  // Inject sidebar
  const sidebar = document.getElementById('sidebar');
  if(sidebar) sidebar.innerHTML = renderSidebar(slug);

  // Inject page nav
  const pageNav = document.getElementById('pageNav');
  if(pageNav) pageNav.innerHTML = renderPageNav(slug);

  // Setup search
  const search = document.getElementById('topSearch');
  if(search){
    search.addEventListener('input', e => {
      const q = e.target.value.trim().toLowerCase();
      const items = document.querySelectorAll('.rule-item, .card, .cmd-item, .term-item, .timeline-item, tbody tr');
      if(!q){
        items.forEach(i => i.classList.remove('hidden-by-search'));
        return;
      }
      items.forEach(i => {
        const text = i.textContent.toLowerCase();
        i.classList.toggle('hidden-by-search', !text.includes(q));
      });
    });
  }

  // Close sidebar on link click (mobile)
  document.querySelectorAll('.sidebar .nav-link').forEach(l => {
    l.addEventListener('click', () => {
      document.getElementById('sidebar').classList.remove('open');
    });
  });
});

// Tab switching (used on some pages)
function showTab(group, btn, idx){
  const tabs = btn.parentElement.querySelectorAll('.tab');
  const contents = document.querySelectorAll('.tab-content[data-group="'+group+'"]');
  tabs.forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  contents.forEach((c,i) => c.classList.toggle('active', i===idx));
}
