// ============ LeetCode Tutor — Interactive App ============
const $ = (s,p=document)=>p.querySelector(s);
const $$ = (s,p=document)=>[...p.querySelectorAll(s)];
const store = {
  get:(k,d)=>{try{return JSON.parse(localStorage.getItem('lct_'+k))??d}catch(e){return d}},
  set:(k,v)=>localStorage.setItem('lct_'+k,JSON.stringify(v)),
};
let CAT=[], ROADMAP=[], SOLUTIONS={}, STATS={}, MUST_SOLVE={}, CONTENT_CACHE={};
let solved = new Set(store.get('solved',[]));
let visits = new Set(store.get('visits',[]));
let notes  = store.get('notes',{});
let currentView='dashboard', currentFilter={diff:'all',tag:'',text:''};

async function init(){
  [CAT,ROADMAP,SOLUTIONS,STATS,MUST_SOLVE] = await Promise.all([
    fetch('data/catalog.json').then(r=>r.json()),
    fetch('data/roadmap.json').then(r=>r.json()),
    fetch('data/solutions.json').then(r=>r.json()),
    fetch('data/stats.json').then(r=>r.json()),
    fetch('data/must_solve.json').then(r=>r.json()),
  ]);
  Object.keys(SOLUTIONS).forEach(id=>solved.add(+id));
  saveProgress();
  $('#sidebarStats').innerHTML = '<b>'+CAT.length+'</b> problems &bull; <b>'+STATS.with_content+'</b> with full lessons &bull; <b>'+solved.size+'</b> solved';
  bindNav();
  renderDashboard();
  renderRoadmap();
  renderProgress();
  renderSolved();
  bindGlobalSearch();
  bindTheme();
  document.addEventListener('keydown',e=>{
    if(e.key==='/'&&document.activeElement.tagName!=='INPUT'&&document.activeElement.tagName!=='TEXTAREA'){e.preventDefault();$('#globalSearch').focus()}
    if(e.key==='Escape'&&currentView==='detail') showView(store.get('lastView','browse'));
  });
}
function saveProgress(){store.set('solved',[...solved]);store.set('visits',[...visits]);store.set('notes',notes)}

function bindNav(){
  $$('.nav-item').forEach(btn=>btn.onclick=()=>{
    $$('.nav-item').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    showView(btn.dataset.view);
  });
  $('#detailBack').onclick=()=>showView(store.get('lastView','browse'));
}
function showView(name){
  currentView=name;
  $$('.view').forEach(v=>v.classList.remove('active'));
  $('#'+name+'View').classList.add('active');
  if(name==='browse') renderBrowse();
  if(name==='solved') renderSolved();
  if(name==='progress') renderProgress();
  $('.main').scrollTop=0;
}

function renderDashboard(){
  $('#statsGrid').innerHTML=
    '<div class="stat-card accent"><span class="num">'+CAT.length.toLocaleString()+'</span><span class="lbl">Total Problems</span></div>'+
    '<div class="stat-card easy"><span class="num">'+STATS.easy+'</span><span class="lbl">Easy</span></div>'+
    '<div class="stat-card medium"><span class="num">'+STATS.medium+'</span><span class="lbl">Medium</span></div>'+
    '<div class="stat-card hard"><span class="num">'+STATS.hard+'</span><span class="lbl">Hard</span></div>'+
    '<div class="stat-card purple"><span class="num">'+STATS.with_content+'</span><span class="lbl">Full Lessons</span></div>'+
    '<div class="stat-card"><span class="num" style="color:var(--green)">'+solved.size+'</span><span class="lbl">Solved by You</span></div>';
  $('#quickStart').innerHTML=ROADMAP.slice(0,4).map(topicCard).join('');
}
function topicCard(t){
  const probs=t.problems.map(id=>CAT.find(p=>p.id===id)).filter(Boolean);
  const s=probs.filter(p=>solved.has(p.id)).length;
  const pct=probs.length?Math.round(s/probs.length*100):0;
  return '<div class="topic-card"><div class="topic-card-head"><span class="ic">'+t.icon+'</span><h3>'+t.topic+'</h3></div>'+
    '<div class="meta"><span>'+probs.length+' problems</span><span class="dot"></span><span>'+s+' solved</span></div>'+
    '<div class="progress-bar"><div class="fill" style="width:'+pct+'%"></div></div></div>';
}

function renderRoadmap(){
  $('#roadmapGrid').innerHTML=ROADMAP.map((t)=>{
    const probs=t.problems.map(id=>CAT.find(p=>p.id===id)).filter(Boolean);
    const s=probs.filter(p=>solved.has(p.id)).length;
    const pct=probs.length?Math.round(s/probs.length*100):0;
    return '<div class="topic-card"><div class="topic-card-head"><span class="ic">'+t.icon+'</span><h3>'+t.topic+'</h3></div>'+
      '<div class="meta"><span>'+probs.length+' problems</span><span class="dot"></span><span>'+s+' solved</span><span class="dot"></span><span>'+pct+'%</span></div>'+
      '<div class="progress-bar"><div class="fill" style="width:'+pct+'%"></div></div></div>';
  }).join('');
  $$('#roadmapGrid .topic-card').forEach((c,i)=>c.onclick=()=>openTopic(ROADMAP[i]));
}
function openTopic(t){
  const probs=t.problems.map(id=>CAT.find(p=>p.id===id)).filter(Boolean);
  $('#filterBar').innerHTML='<button class="back-btn" onclick="showView(\'roadmap\')">&larr; All topics</button><span style="font-weight:700;font-size:16px">'+t.icon+' '+t.topic+'</span>';
  // If this topic has "why" explanations, show them
  if(t.why){
    const whyHtml='<div style="margin-left:auto;color:var(--text3);font-size:12px;font-style:italic">'+probs.length+' hand-picked classics &bull; click any to learn why it matters</div>';
    $('#filterBar').innerHTML+=whyHtml;
    $('#problemsList').innerHTML=probs.map((p)=>{
      const why=t.why[p.id];
      const row=problemRow(p);
      if(why){
        // Insert the "why" text after the title
        return row.replace('<span class="ptitle">',
          '<span class="ptitle"><div style="font-size:11px;color:var(--text3);font-style:italic;margin-top:2px">'+why+'</div><span style="display:none">');
      }
      return row;
    }).join('');
  } else {
    $('#problemsList').innerHTML=probs.map(problemRow).join('');
  }
  $('#loadMoreWrap').style.display='none';
  bindProblemRows();
  showView('browse');
  $$('.nav-item').forEach(b=>b.classList.remove('active'));
}

let browsePage=0; const PAGE=60;
function renderBrowse(){
  buildFilterBar();
  browsePage=1;
  $('#problemsList').innerHTML='';
  loadPage();
  $('#loadMoreBtn').onclick=()=>{browsePage++;loadPage()};
}
function buildFilterBar(){
  const topTags=['Array','Hash Table','String','Dynamic Programming','Math','Tree','Depth-First Search','Breadth-First Search','Greedy','Sorting','Two Pointers','Binary Search','Stack','Linked List','Matrix','Backtracking','Bit Manipulation','Heap (Priority Queue)','Graph','Sliding Window','Recursion','Memoization','Queue','Prefix Sum'];
  $('#filterBar').innerHTML=
    '<div class="filter-group">'+
      '<button class="filter-btn active" data-diff="all">All</button>'+
      '<button class="filter-btn easy" data-diff="Easy">Easy</button>'+
      '<button class="filter-btn medium" data-diff="Medium">Medium</button>'+
      '<button class="filter-btn hard" data-diff="Hard">Hard</button>'+
    '</div>'+
    '<select class="select" id="tagFilter"><option value="">All topics</option>'+topTags.map(t=>'<option value="'+t+'">'+t+'</option>').join('')+'</select>'+
    '<label class="filter-btn" style="border:1px solid var(--border);cursor:pointer"><input type="checkbox" id="solvedOnly" style="margin-right:5px">Solved only</label>'+
    '<label class="filter-btn" style="border:1px solid var(--border);cursor:pointer"><input type="checkbox" id="freeOnly" style="margin-right:5px">Free only</label>'+
    '<span class="results-count" id="resultsCount"></span>';
  $$('#filterBar .filter-btn[data-diff]').forEach(b=>b.onclick=()=>{
    $$('#filterBar .filter-btn[data-diff]').forEach(x=>x.classList.remove('active'));
    b.classList.add('active');currentFilter.diff=b.dataset.diff;renderBrowse();
  });
  $('#tagFilter').onchange=e=>{currentFilter.tag=e.target.value;renderBrowse()};
  $('#solvedOnly').onchange=()=>renderBrowse();
  $('#freeOnly').onchange=()=>renderBrowse();
}
function matchesFilter(p){
  if(currentFilter.diff!=='all'&&p.difficulty!==currentFilter.diff)return false;
  if(currentFilter.tag&&!p.tags.includes(currentFilter.tag))return false;
  if($('#solvedOnly')&&$('#solvedOnly').checked&&!solved.has(p.id))return false;
  if($('#freeOnly')&&$('#freeOnly').checked&&p.paid)return false;
  if(currentFilter.text){
    const q=currentFilter.text.toLowerCase();
    if(!p.title.toLowerCase().includes(q)&&!(''+p.id).includes(q)&&!p.tags.some(t=>t.toLowerCase().includes(q)))return false;
  }
  return true;
}
function filteredList(){return CAT.filter(matchesFilter)}
function loadPage(){
  const all=filteredList();
  const slice=all.slice(0,browsePage*PAGE);
  $('#problemsList').innerHTML=slice.map(problemRow).join('');
  $('#resultsCount').textContent=all.length.toLocaleString()+' problems';
  $('#loadMoreWrap').style.display=all.length>slice.length?'block':'none';
  bindProblemRows();
}
function problemRow(p){
  const tagsHtml=p.tags.slice(0,2).map(t=>'<span class="ptag">'+t+'</span>').join('');
  const prem=p.paid?'<span class="premium-tag">PRO</span>':'';
  return '<div class="problem-row" data-id="'+p.id+'">'+
    '<span class="check '+(solved.has(p.id)?'solved':'')+'">'+(solved.has(p.id)?'\u2713':'\u25CB')+'</span>'+
    '<span class="pid">'+p.id+'.</span>'+
    '<span class="ptitle">'+p.title+(p.solved?' <span class="badge-small">YOU</span>':'')+' '+prem+'</span>'+
    '<span class="ptags">'+tagsHtml+'</span>'+
    '<span class="acrate">'+p.ac_rate+'%</span>'+
    '<span class="diff-badge '+p.difficulty+'">'+p.difficulty+'</span></div>';
}
function bindProblemRows(){
  $$('.problem-row').forEach(r=>r.onclick=()=>openDetail(+r.dataset.id));
}

function renderSolved(){
  const list=CAT.filter(p=>p.solved||solved.has(p.id)).sort((a,b)=>a.id-b.id);
  $('#solvedCount').textContent='\u2014 '+list.length+" problems you've worked on";
  $('#solvedList').innerHTML=list.length?list.map(problemRow).join(''):'<div class="empty"><div class="big">\uD83D\uDCDD</div>No solutions yet. Open any problem and start learning!</div>';
  bindProblemRows();
}

function renderProgress(){
  const visitedArr=[...visits].map(id=>CAT.find(p=>p.id===id)).filter(Boolean);
  const byDiff={Easy:[0,0],Medium:[0,0],Hard:[0,0]};
  CAT.forEach(p=>{if(byDiff[p.difficulty]){byDiff[p.difficulty][1]++;if(solved.has(p.id))byDiff[p.difficulty][0]++}});
  const tagProgress={};
  visitedArr.forEach(p=>p.tags.forEach(t=>{tagProgress[t]=(tagProgress[t]||0)+1}));
  const topTags=Object.entries(tagProgress).sort((a,b)=>b[1]-a[1]).slice(0,12);
  $('#progressContent').innerHTML=
    '<div class="stats-grid">'+
      '<div class="stat-card accent"><span class="num">'+solved.size+'</span><span class="lbl">Solved</span></div>'+
      '<div class="stat-card"><span class="num">'+visits.size+'</span><span class="lbl">Problems Viewed</span></div>'+
      '<div class="stat-card"><span class="num">'+Object.keys(notes).length+'</span><span class="lbl">Notes Saved</span></div>'+
      '<div class="stat-card easy"><span class="num">'+byDiff.Easy[0]+'/'+byDiff.Easy[1]+'</span><span class="lbl">Easy Solved</span></div>'+
      '<div class="stat-card medium"><span class="num">'+byDiff.Medium[0]+'/'+byDiff.Medium[1]+'</span><span class="lbl">Medium Solved</span></div>'+
      '<div class="stat-card hard"><span class="num">'+byDiff.Hard[0]+'/'+byDiff.Hard[1]+'</span><span class="lbl">Hard Solved</span></div>'+
    '</div>'+
    '<h3 class="section-title">\uD83C\uDFAF Patterns you\'ve explored</h3>'+
    (topTags.length?'<div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px">'+topTags.map(([t,c])=>'<span class="tag-chip">'+t+' <b style="color:var(--accent)">'+c+'</b></span>').join('')+'</div>':'<p style="color:var(--text2);margin-bottom:24px">Start exploring problems to see your pattern coverage.</p>')+
    '<h3 class="section-title">\uD83E\uDDF9 Reset</h3>'+
    '<p style="color:var(--text2);margin-bottom:12px">Clear all local progress (solved marks, viewed history, notes). This only affects this browser.</p>'+
    '<button class="back-btn" onclick="resetProgress()" style="border-color:var(--hard);color:var(--hard)">Reset all progress</button>';
}
function resetProgress(){
  if(confirm('Reset ALL local progress? This cannot be undone.')){
    solved=new Set(Object.keys(SOLUTIONS).map(Number));visits=new Set();notes={};
    saveProgress();location.reload();
  }
}

async function openDetail(id){
  store.set('lastView',currentView);
  visits.add(id);saveProgress();
  $$('.nav-item').forEach(b=>b.classList.remove('active'));
  $$('.view').forEach(v=>v.classList.remove('active'));
  $('#detailView').classList.add('active');
  $('.main').scrollTop=0;
  const p=CAT.find(x=>x.id===id);
  if(!p)return;
  $('#detailTitle').innerHTML='<span class="did">'+p.id+'.</span>'+p.title;
  $('#detailLink').href='https://leetcode.com/problems/'+p.slug+'/';
  $('#detailContent').innerHTML='<div class="empty"><div class="big spin">\u23F3</div>Loading lesson...</div>';
  const content=await loadContent(p);
  renderDetail(p,content);
}
async function loadContent(p){
  const bucket=Math.floor(p.id/200);
  if(!CONTENT_CACHE[bucket]){
    try{CONTENT_CACHE[bucket]=await fetch('data/content/chunk_'+bucket+'.json').then(r=>r.json())}
    catch(e){CONTENT_CACHE[bucket]={}}
  }
  return CONTENT_CACHE[bucket][p.slug];
}
function esc(s){return(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}

function renderDetail(p,c){
  const desc=c?c.content:'';
  const tags=(c&&c.tags)||p.tags||[];
  const hints=(c&&c.hints)||[];
  const mySol=SOLUTIONS[p.id];
  const starter=(c&&c.code_snippets&&c.code_snippets['Python3'])||'';
  $('#detailContent').innerHTML=
    '<div class="solve-toggle">'+
      '<label class="toggle-switch"><input type="checkbox" id="solvedCheck" '+(solved.has(p.id)?'checked':'')+'><span class="toggle-slider"></span></label>'+
      '<span style="font-weight:600">Mark as solved</span>'+
      '<span style="margin-left:auto;color:var(--text3);font-size:13px">Acceptance: '+p.ac_rate+'%</span>'+
    '</div>'+
    '<div class="tags-row">'+tags.map(t=>'<span class="tag-chip">'+t+'</span>').join('')+'</div>'+
    '<div class="tabs">'+
      (c?'<button class="tab active" data-tab="problem">\uD83D\uDCD6 Problem</button>':'')+
      (hints.length?'<button class="tab '+(c?'':'active')+'" data-tab="hints">\uD83D\uDCA1 Hints ('+hints.length+')</button>':'')+
      '<button class="tab" data-tab="approach">\uD83E\uDDE0 Approach</button>'+
      (mySol?'<button class="tab" data-tab="solution">\u2705 Your Solution</button>':'')+
      '<button class="tab" data-tab="practice">\u2328\uFE0F Practice</button>'+
      '<button class="tab" data-tab="notes">\uD83D\uDCDD Notes</button>'+
    '</div>'+
    '<div class="tab-panel '+(c?'active':'')+'" id="panel-problem">'+(desc?renderHTML(desc):noContent(p))+'</div>'+
    '<div class="tab-panel" id="panel-hints">'+renderHints(hints)+'</div>'+
    '<div class="tab-panel" id="panel-approach">'+renderApproach(p,c,mySol)+'</div>'+
    '<div class="tab-panel" id="panel-solution">'+(mySol?renderSolution(mySol):'<div class="empty">No saved solution yet. Write one in the Practice tab!</div>')+'</div>'+
    '<div class="tab-panel" id="panel-practice">'+renderPractice(starter,mySol)+'</div>'+
    '<div class="tab-panel" id="panel-notes">'+renderNotes(p.id)+'</div>';
  bindDetail(p);
}
function noContent(p){
  return '<div class="desc"><p>This is a <b>premium (LeetCode-only)</b> problem, so the full statement isn\'t included here.</p>'+
    '<p>Open it on LeetCode to read the problem:</p>'+
    '<p><a class="muted-link" href="https://leetcode.com/problems/'+p.slug+'/" target="_blank">https://leetcode.com/problems/'+p.slug+'/ \u2197</a></p></div>';
}
function renderHints(hints){
  if(!hints.length)return '<div class="empty"><div class="big">\uD83D\uDCA1</div>No hints for this problem. Try the Approach tab!</div>';
  return '<p style="color:var(--text2);margin-bottom:16px">\uD83D\uDCA1 Stuck? Reveal hints one at a time, from most general to most specific \u2014 just like a real tutor would guide you.</p>'+
    hints.map((h,i)=>'<div class="hint-card"><div class="hint-q"><span class="hn">'+(i+1)+'</span>Hint '+(i+1)+'</div>'+
      '<button class="hint-reveal-btn" data-hint="'+i+'">\uD83D\uDC41\uFE0F Reveal hint '+(i+1)+'</button>'+
      '<div class="hint-body" id="hint-'+i+'">'+renderHTML(h)+'</div></div>').join('');
}
function renderApproach(p,c,mySol){
  const tags=(c&&c.tags)||p.tags;
  const patternHint=tags.map(t=>'<span class="tag-chip">'+t+'</span>').join('');
  let docstringTip='';
  if(mySol){const m=mySol.code.match(/"""([\s\S]*?)"""/);if(m)docstringTip=m[1].trim();}
  return '<div class="approach-card"><h4>\uD83C\uDFAF Key Concepts</h4>'+
      '<div class="tags-row">'+(patternHint||'<span class="tag-chip">General</span>')+'</div>'+
      '<p style="color:var(--text2);margin-top:8px;font-size:14px">This problem tests your understanding of the patterns above. Focus on <b>which data structure</b> and <b>which algorithmic technique</b> makes the solution efficient.</p></div>'+
    '<div class="approach-card"><h4>\uD83E\uDEA2 Step-by-Step Strategy</h4>'+
      '<ol style="color:var(--text2);font-size:14px;line-height:2">'+
        '<li><b>Understand the problem:</b> Read the statement carefully. Identify the exact input, output, and constraints. Work through the examples by hand.</li>'+
        '<li><b>Brute force first:</b> Think of the simplest correct solution, even if slow. This builds intuition and gives you a baseline.</li>'+
        '<li><b>Identify the bottleneck:</b> What makes the brute force slow? Repeated work? Unnecessary search?</li>'+
        '<li><b>Apply a pattern:</b> Use the tags above as clues. Hash table for O(1) lookup, two pointers for sorted/linear scans, BFS/DFS for graphs, DP for overlapping subproblems.</li>'+
        '<li><b>Optimize:</b> Trade space for time (or vice versa). Reduce nested loops. Use the right data structure.</li>'+
        '<li><b>Verify complexity:</b> Confirm your time and space complexity before coding.</li>'+
      '</ol></div>'+
    (docstringTip?'<div class="approach-card"><h4>\uD83E\uDDE0 Your own approach notes</h4><p style="color:var(--text2);font-size:14px;white-space:pre-wrap">'+esc(docstringTip)+'</p></div>':'')+
    '<div class="approach-card"><h4>\u23F1\uFE0F Complexity targets</h4>'+
      '<div class="complexity">'+
        '<div class="cx"><b>Easy</b> \u2014 usually O(n) or O(n log n)</div>'+
        '<div class="cx"><b>Medium</b> \u2014 often O(n) with the right trick, or O(n\u00B2)\u2192O(n log n)</div>'+
        '<div class="cx"><b>Hard</b> \u2014 demands an optimal O(n) or O(n log n) insight</div>'+
      '</div>'+
      '<p style="color:var(--text2);margin-top:10px;font-size:13px">Then check the <b>Hints</b> tab for guided nudges, and the <b>Practice</b> tab to code it up.</p></div>';
}
function renderSolution(sol){
  const m=sol.code.match(/"""([\s\S]*?)"""/);
  const doc=m?'<div class="approach-card" style="margin-bottom:14px"><h4>\uD83D\uDCD6 Solution explanation</h4><div style="color:var(--text2);font-size:14px;white-space:pre-wrap">'+esc(m[1].trim())+'</div></div>':'';
  return doc+codeBlock(sol.code,'python','Your Python solution')+
    '<p style="color:var(--text3);font-size:13px;margin-top:8px">\uD83D\uDCC1 Studied under: <b>'+sol.topic+'</b></p>';
}
function renderPractice(starter,mySol){
  const init=mySol?mySol.code:(starter||'# Write your solution here\n');
  return '<div class="editor-wrap">'+
    '<div class="editor-toolbar">'+
      '<select class="lang-select" id="langSel"><option>Python 3</option></select>'+
      '<button class="run-btn" id="runBtn">\u25B6 Run Code</button>'+
      '<span id="runStatus" style="font-size:13px;color:var(--text3)"></span>'+
    '</div>'+
    '<textarea id="codeEditor" spellcheck="false">'+esc(init)+'</textarea>'+
    '<div style="margin-top:14px;font-size:13px;color:var(--text2);margin-bottom:6px"><b>Test input / custom stdin</b> (optional)</div>'+
    '<textarea id="customInput" spellcheck="false" style="width:100%;min-height:60px;border-radius:var(--radius);border:1px solid var(--border);background:var(--bg2);color:var(--text);font-family:monospace;font-size:13px;padding:12px;resize:vertical" placeholder="stdin for your program"></textarea>'+
    '<div class="test-output" id="testOutput">// Click "Run Code" to execute your Python solution in the browser (via Pyodide)</div></div>';
}
function renderNotes(id){
  return '<p style="color:var(--text2);margin-bottom:10px">Write your own notes for this problem. Saved automatically in your browser.</p>'+
    '<textarea id="noteArea" spellcheck="false" style="width:100%;min-height:220px;border-radius:var(--radius);border:1px solid var(--border);background:var(--bg2);color:var(--text);font-family:inherit;font-size:14px;padding:16px;resize:vertical;line-height:1.7" placeholder="What did you learn? What trick did you use?">'+esc(notes[id]||'')+'</textarea>'+
    '<button class="run-btn" style="margin-top:10px" id="saveNote">\uD83D\uDCBE Save note</button>';
}
function codeBlock(code,lang,label){
  return '<div class="code-block"><div class="code-block-head"><span class="lang">'+lang+'</span><button class="copy-btn" data-copy="'+encodeURIComponent(code)+'">\uD83D\uDCCB Copy</button></div><pre>'+highlight(esc(code))+'</pre></div>';
}
function bindDetail(p){
  $('#solvedCheck').onchange=e=>{e.target.checked?solved.add(p.id):solved.delete(p.id);saveProgress();toast(e.target.checked?'Marked as solved':'Unmarked solved')};
  $$('#detailContent .tab').forEach(t=>t.onclick=()=>{
    $$('#detailContent .tab').forEach(x=>x.classList.remove('active'));
    $$('#detailContent .tab-panel').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');$('#panel-'+t.dataset.tab).classList.add('active');
  });
  $$('#detailContent .hint-reveal-btn').forEach(b=>b.onclick=()=>{
    $('#hint-'+b.dataset.hint).classList.add('shown');b.style.display='none';
  });
  $$('#detailContent .copy-btn').forEach(b=>b.onclick=()=>{navigator.clipboard.writeText(decodeURIComponent(b.dataset.copy));toast('Copied to clipboard')});
  if($('#runBtn'))$('#runBtn').onclick=()=>runCode();
  if($('#saveNote'))$('#saveNote').onclick=()=>{notes[p.id]=$('#noteArea').value;saveProgress();toast('Note saved')};
  const ed=$('#codeEditor');
  if(ed)ed.addEventListener('keydown',e=>{
    if(e.key==='Tab'){e.preventDefault();const s=ed.selectionStart,en=ed.selectionEnd;ed.value=ed.value.slice(0,s)+'    '+ed.value.slice(en);ed.selectionStart=ed.selectionEnd=s+4}
  });
}
let pyodide=null,pyLoading=null;
async function runCode(){
  const code=$('#codeEditor').value;
  const inp=$('#customInput').value||'';
  const out=$('#testOutput'),status=$('#runStatus');
  out.textContent='';status.textContent='\u23F3 Loading Python runtime...';
  try{
    if(!pyodide){
      if(!pyLoading){
        pyLoading=(async()=>{
          status.textContent='\u23F3 Loading Pyodide (one-time download, ~10s)...';
          await loadScript('https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js');
          pyodide=await loadPyodide();
        })();
      }
      await pyLoading;
    }
    status.textContent='\u25B6 Running...';
    const runner = "import sys, io, traceback\n" +
      "_code=__code__\n" +
      "_inp=__stdin__\n" +
      "sys.stdin=io.StringIO(_inp)\n" +
      "_old=sys.stdout\n" +
      "_buf=io.StringIO()\n" +
      "sys.stdout=_buf\n" +
      "_err=None\n" +
      "try:\n" +
      "  exec(compile(_code,'<editor>','exec'),{'__name__':'__main__'})\n" +
      "except Exception:\n" +
      "  _err=traceback.format_exc()\n" +
      "sys.stdout=_old\n" +
      "_out=_buf.getvalue()";
    pyodide.globals.set('__code__',code);
    pyodide.globals.set('__stdin__',inp);
    pyodide.runPython(runner);
    const outVal=pyodide.globals.get('_out');
    const errVal=pyodide.globals.get('_err');
    let result='';
    if(outVal)result+=outVal;
    if(errVal)result+=(result?'\n':'')+'\u274C Error:\n'+errVal;
    out.textContent=result||'(no output)';
    status.textContent=errVal?'\u274C Finished with error':'\u2705 Done';
  }catch(e){
    out.textContent='\u26A0 '+e.message+'\n\nTip: First run downloads the Python runtime from a CDN. Make sure you are online.';status.textContent='\u274C Error';
  }
}
function loadScript(src){return new Promise((res,rej)=>{const s=document.createElement('script');s.src=src;s.onload=res;s.onerror=rej;document.head.appendChild(s)})}
function renderHTML(h){
  const wrap=document.createElement('div');
  wrap.innerHTML=h;
  wrap.querySelectorAll('script').forEach(s=>s.remove());
  return '<div class="desc">'+wrap.innerHTML+'</div>';
}
function highlight(code){
  const kw=['def','class','return','if','elif','else','for','while','in','not','and','or','import','from','as','with','try','except','finally','raise','pass','break','continue','lambda','None','True','False','self','global','nonlocal','yield','async','await','del','assert','is'];
  let out=code;
  out=out.replace(/(&quot;[^&]*?&quot;|&#39;[^&]*?&#39;)/g,'<span style="color:#a5d6ff">$1</span>');
  out=out.replace(/(#[^\n]*)/g,'<span style="color:#8b949e">$1</span>');
  kw.forEach(k=>{out=out.replace(new RegExp('\\b'+k+'\\b','g'),'<span style="color:#ff7b72">'+k+'</span>')});
  out=out.replace(/\b(\d+)\b/g,'<span style="color:#79c0ff">$1</span>');
  out=out.replace(/<span style="color:#ff7b72">def<\/span>\s+(\w+)/g,'<span style="color:#ff7b72">def</span> <span style="color:#d2a8ff">$1</span>');
  return out;
}
function bindGlobalSearch(){
  let t;
  $('#globalSearch').oninput=e=>{
    clearTimeout(t);
    t=setTimeout(()=>{
      currentFilter.text=e.target.value.trim();
      if(currentView!=='detail'){
        showView('browse');
        $$('.nav-item').forEach(b=>b.classList.toggle('active',b.dataset.view==='browse'));
        $('#globalSearch').value=currentFilter.text;
        $('#globalSearch').focus();
      }
    },200);
  };
}
function bindTheme(){
  const th=store.get('theme','dark');
  document.documentElement.dataset.theme=th;
  $('#themeToggle').textContent=th==='dark'?'\uD83C\uDF19':'\u2600\uFE0F';
  $('#themeToggle').onclick=()=>{
    const n=document.documentElement.dataset.theme==='dark'?'light':'dark';
    document.documentElement.dataset.theme=n;store.set('theme',n);
    $('#themeToggle').textContent=n==='dark'?'\uD83C\uDF19':'\u2600\uFE0F';
  };
}
function toast(msg){const t=$('#toast');t.textContent=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1800)}
init();
