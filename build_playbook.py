# Master playbook builder - writes ML_Strategy_Playbook.html
# Run: python3 build_playbook.py

SECTIONS = {}

# ── HEAD + CSS ────────────────────────────────────────────────────────────────
SECTIONS['head'] = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ML Strategy Playbook — Archishman Bandyopadhyay</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
/* ── RESET & ROOT ── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --ink:#1a1714;
  --ink2:#3d3830;
  --ink3:#7a7060;
  --ink4:#b0a898;
  --cream:#f7f4ef;
  --cream2:#ede8df;
  --cream3:#e2dbd0;
  --accent:#8b2500;
  --accent2:#c4440d;
  --accent3:#e8c4a0;
  --blue:#1a3a5c;
  --blue2:#2d5f8a;
  --green:#1a4a2e;
  --green2:#2d7a4a;
  --gold:#7a5a00;
  --gold2:#c49a00;
  --border:#d4cdc4;
  --border2:#c4bdb4;
  --serif:'Source Serif 4',Georgia,serif;
  --display:'Playfair Display',Georgia,serif;
  --mono:'JetBrains Mono',monospace;
  --radius:4px;
  --shadow:0 1px 3px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04);
  --shadow-lg:0 4px 16px rgba(0,0,0,0.1), 0 1px 4px rgba(0,0,0,0.06);
}
html{scroll-behavior:smooth;font-size:15px}
body{
  font-family:var(--serif);
  background:var(--cream);
  color:var(--ink);
  line-height:1.7;
  -webkit-font-smoothing:antialiased;
}

/* ── LAYOUT ── */
.page-wrap{display:grid;grid-template-columns:280px 1fr;min-height:100vh}
.sidebar{
  position:sticky;top:0;height:100vh;overflow-y:auto;
  background:var(--ink);color:var(--cream2);
  padding:0;border-right:1px solid rgba(255,255,255,0.06);
  font-family:var(--serif);
  scrollbar-width:thin;scrollbar-color:var(--ink3) transparent;
}
.sidebar::-webkit-scrollbar{width:4px}
.sidebar::-webkit-scrollbar-thumb{background:var(--ink3);border-radius:2px}
.main-content{padding:0;min-width:0}

/* ── SIDEBAR ── */
.sidebar-header{
  padding:28px 24px 20px;
  border-bottom:1px solid rgba(255,255,255,0.08);
}
.sidebar-logo{
  font-family:var(--display);font-size:15px;font-weight:700;
  color:#fff;letter-spacing:0.01em;line-height:1.3;
  margin-bottom:6px;
}
.sidebar-sub{font-size:10px;color:var(--ink4);letter-spacing:0.06em;text-transform:uppercase}
.sidebar-search{
  padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.06);
}
.sidebar-search input{
  width:100%;padding:7px 10px;
  background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1);
  border-radius:var(--radius);color:var(--cream2);font-family:var(--serif);font-size:12px;
  outline:none;
}
.sidebar-search input::placeholder{color:var(--ink4)}
.sidebar-search input:focus{border-color:rgba(255,255,255,0.25);background:rgba(255,255,255,0.1)}

.nav-section{padding:16px 0 4px}
.nav-section-label{
  padding:0 20px 6px;
  font-size:9px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;
  color:var(--ink4);
}
.nav-item{
  display:block;padding:6px 20px 6px 20px;
  font-size:12px;color:var(--ink4);text-decoration:none;
  transition:all 0.15s;cursor:pointer;border-left:2px solid transparent;
  line-height:1.45;
}
.nav-item:hover{color:#fff;background:rgba(255,255,255,0.05);border-left-color:rgba(255,255,255,0.2)}
.nav-item.active{color:#fff;background:rgba(255,255,255,0.08);border-left-color:var(--accent2)}
.nav-item .nav-badge{
  display:inline-block;float:right;font-size:9px;padding:1px 6px;
  border-radius:10px;background:rgba(255,255,255,0.1);color:var(--ink4);
  font-family:var(--mono);
}
.nav-sub{padding-left:30px;font-size:11px}

/* ── MAIN SECTIONS ── */
.section{
  padding:64px 72px;border-bottom:1px solid var(--border);
  max-width:960px;
}
.section:last-child{border-bottom:none}
.section-hero{
  padding:80px 72px 64px;background:var(--ink);color:var(--cream);
  border-bottom:none;max-width:none;
}

/* ── TYPOGRAPHY ── */
h1.hero-title{
  font-family:var(--display);font-size:48px;font-weight:700;
  line-height:1.15;letter-spacing:-0.02em;color:#fff;
  margin-bottom:16px;
}
h1.hero-title em{color:var(--accent3);font-style:normal}
.hero-desc{font-size:17px;color:rgba(255,255,255,0.65);max-width:560px;line-height:1.65}
.hero-meta{
  display:flex;flex-wrap:wrap;gap:20px;margin-top:32px;
  font-size:11px;color:rgba(255,255,255,0.45);letter-spacing:0.05em;text-transform:uppercase;
  font-family:var(--mono);
}
.hero-meta span em{color:rgba(255,255,255,0.7);font-style:normal}

h2.section-title{
  font-family:var(--display);font-size:30px;font-weight:600;
  color:var(--ink);line-height:1.2;margin-bottom:8px;letter-spacing:-0.01em;
}
h2.section-title .title-num{
  font-family:var(--mono);font-size:12px;font-weight:500;
  color:var(--ink4);margin-right:12px;vertical-align:middle;letter-spacing:0.02em;
}
.section-intro{
  font-size:15px;color:var(--ink3);line-height:1.7;max-width:680px;
  margin-bottom:36px;border-left:3px solid var(--accent3);padding-left:16px;
}
h3.subsection-title{
  font-family:var(--display);font-size:20px;font-weight:600;
  color:var(--ink);margin:36px 0 12px;letter-spacing:-0.01em;
}
h4.card-title{
  font-family:var(--display);font-size:16px;font-weight:600;
  color:var(--ink);margin-bottom:8px;
}
p{margin-bottom:12px;font-size:14.5px;line-height:1.75;color:var(--ink2)}
p:last-child{margin-bottom:0}

/* ── CALLOUT BOXES ── */
.callout{
  padding:16px 20px;border-radius:var(--radius);margin:20px 0;
  border-left:3px solid;font-size:13.5px;line-height:1.65;
}
.callout-insight{background:#faf5ee;border-color:var(--gold2);color:var(--ink2)}
.callout-warning{background:#fef5f0;border-color:var(--accent2);color:var(--ink2)}
.callout-rule{background:#f0f5fa;border-color:var(--blue2);color:var(--ink2)}
.callout strong{font-weight:600;display:block;margin-bottom:4px;font-size:12px;
  letter-spacing:0.05em;text-transform:uppercase;opacity:0.7}

/* ── MODEL CARDS ── */
.model-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin:24px 0}
.model-card{
  background:#fff;border:1px solid var(--border);border-radius:6px;
  padding:20px;transition:all 0.2s;cursor:pointer;position:relative;
  box-shadow:var(--shadow);
}
.model-card:hover{transform:translateY(-2px);box-shadow:var(--shadow-lg);border-color:var(--border2)}
.model-card.active{border-color:var(--accent2);box-shadow:0 0 0 2px rgba(139,37,0,0.1),var(--shadow-lg)}
.model-card-header{display:flex;align-items:flex-start;gap:12px;margin-bottom:12px}
.model-icon{
  width:36px;height:36px;border-radius:6px;display:flex;align-items:center;
  justify-content:center;font-size:16px;flex-shrink:0;
}
.model-card-meta{flex:1}
.model-name{font-family:var(--display);font-size:15px;font-weight:600;color:var(--ink);margin-bottom:2px}
.model-family{font-size:10px;letter-spacing:0.06em;text-transform:uppercase;color:var(--ink4);font-family:var(--mono)}
.model-desc{font-size:12.5px;color:var(--ink3);line-height:1.6;margin-bottom:12px}
.model-tags{display:flex;flex-wrap:wrap;gap:4px}
.tag{font-size:10px;padding:2px 8px;border-radius:3px;font-family:var(--mono)}
.model-notebook-link{
  display:inline-flex;align-items:center;gap:5px;margin-top:12px;
  font-size:11px;color:var(--accent2);text-decoration:none;font-family:var(--mono);
  border:1px solid currentColor;padding:3px 8px;border-radius:3px;
  transition:all 0.15s;
}
.model-notebook-link:hover{background:var(--accent2);color:#fff}

/* ── DETAIL PANEL ── */
.model-detail{
  display:none;background:#fff;border:1px solid var(--border);
  border-radius:6px;padding:32px;margin-top:16px;box-shadow:var(--shadow);
}
.model-detail.visible{display:block;animation:fadeIn 0.2s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

/* ── TABLES ── */
.data-table{width:100%;border-collapse:collapse;margin:16px 0;font-size:13px}
.data-table th{
  background:var(--ink);color:var(--cream);padding:8px 14px;text-align:left;
  font-family:var(--mono);font-size:10px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;
}
.data-table td{padding:8px 14px;border-bottom:1px solid var(--border);color:var(--ink2);vertical-align:top}
.data-table tr:last-child td{border-bottom:none}
.data-table tr:nth-child(even) td{background:var(--cream)}
.data-table .good{color:var(--green2);font-weight:600}
.data-table .bad{color:var(--accent2);font-weight:600}

/* ── PROPERTY BADGES ── */
.prop-grid{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}
.prop-badge{
  display:flex;align-items:center;gap:6px;padding:6px 12px;
  background:var(--cream2);border:1px solid var(--border);border-radius:4px;
  font-size:11.5px;
}
.prop-label{color:var(--ink4);font-size:10px;text-transform:uppercase;letter-spacing:0.05em;font-family:var(--mono)}
.prop-value{color:var(--ink);font-weight:600}

/* ── PROS/CONS GRID ── */
.pros-cons{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0}
.pros,.cons{padding:14px 16px;border-radius:4px;font-size:13px}
.pros{background:#f0f7f3;border:1px solid #bde0ca}
.cons{background:#fef5f0;border:1px solid #f4c4aa}
.pros h5,.cons h5{font-size:10px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:8px;font-family:var(--mono)}
.pros h5{color:var(--green2)}
.cons h5{color:var(--accent2)}
.pros ul,.cons ul{list-style:none;padding:0}
.pros ul li,.cons ul li{padding:2px 0;color:var(--ink2);line-height:1.5}
.pros ul li::before{content:"✓  ";color:var(--green2);font-weight:700}
.cons ul li::before{content:"✗  ";color:var(--accent2);font-weight:700}

/* ── ASK-YOUR-TEAM ── */
.ask-list{list-style:none;padding:0;margin:8px 0}
.ask-list li{
  padding:8px 12px 8px 36px;position:relative;border-left:2px solid var(--cream3);
  margin-bottom:4px;font-size:13px;color:var(--ink2);line-height:1.6;
}
.ask-list li::before{
  content:"?";position:absolute;left:10px;top:8px;
  width:16px;height:16px;background:var(--ink);color:var(--cream);
  border-radius:50%;font-size:10px;font-weight:700;font-family:var(--mono);
  display:flex;align-items:center;justify-content:center;
}

/* ── USE CASE SCENARIOS ── */
.scenarios{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px;margin:16px 0}
.scenario{
  padding:14px 16px;background:var(--cream);border:1px solid var(--border);
  border-radius:4px;border-left:3px solid;
}
.scenario-label{font-size:10px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;
  font-family:var(--mono);margin-bottom:4px;opacity:0.7}
.scenario-title{font-weight:600;font-size:13px;color:var(--ink);margin-bottom:4px}
.scenario-desc{font-size:12px;color:var(--ink3);line-height:1.55}

/* ── VISUAL DIAGRAMS ── */
.diagram-wrap{
  background:#fff;border:1px solid var(--border);border-radius:6px;
  padding:28px;margin:20px 0;text-align:center;overflow-x:auto;
}
.diagram-title{font-family:var(--mono);font-size:11px;color:var(--ink4);
  text-transform:uppercase;letter-spacing:0.06em;margin-bottom:20px}
svg text{font-family:var(--serif)}

/* ── INTERACTIVE DECISION TREE ── */
.decision-tree-wrap{
  background:#fff;border:1px solid var(--border);border-radius:6px;
  padding:28px;margin:20px 0;
}
.dt-node{
  display:none;animation:fadeIn 0.25s ease;
}
.dt-node.active{display:block}
.dt-question{
  font-family:var(--display);font-size:20px;font-weight:600;color:var(--ink);
  line-height:1.3;margin-bottom:20px;padding-bottom:16px;
  border-bottom:1px solid var(--border);
}
.dt-options{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px}
.dt-option{
  padding:10px 18px;border:1.5px solid var(--border2);border-radius:4px;
  background:var(--cream);cursor:pointer;font-size:13px;color:var(--ink2);
  transition:all 0.15s;font-family:var(--serif);text-align:left;
}
.dt-option:hover{border-color:var(--accent2);color:var(--accent);background:#fff}
.dt-result{
  padding:20px;background:var(--ink);color:var(--cream);border-radius:4px;
}
.dt-result-title{font-family:var(--display);font-size:18px;font-weight:600;
  color:#fff;margin-bottom:8px}
.dt-result-desc{font-size:13px;color:rgba(255,255,255,0.7);line-height:1.6;margin-bottom:12px}
.dt-result-models{display:flex;flex-wrap:wrap;gap:6px}
.dt-model-tag{font-size:11px;padding:3px 10px;background:rgba(255,255,255,0.1);
  border-radius:3px;color:rgba(255,255,255,0.85);font-family:var(--mono)}
.dt-back{
  background:none;border:1px solid rgba(255,255,255,0.2);color:rgba(255,255,255,0.6);
  padding:6px 14px;border-radius:3px;cursor:pointer;font-size:12px;margin-top:12px;
  font-family:var(--serif);transition:all 0.15s;
}
.dt-back:hover{border-color:rgba(255,255,255,0.5);color:#fff}
.dt-breadcrumb{font-size:11px;color:var(--ink4);font-family:var(--mono);margin-bottom:16px}
.dt-progress{height:3px;background:var(--cream3);border-radius:2px;margin-bottom:20px}
.dt-progress-fill{height:100%;background:var(--accent2);border-radius:2px;transition:width 0.3s}

/* ── MATH NOTATION ── */
.math{font-family:var(--mono);font-size:13px;background:var(--cream2);
  padding:12px 16px;border-radius:var(--radius);display:block;margin:12px 0;
  border-left:3px solid var(--border2);overflow-x:auto;color:var(--ink2)}

/* ── COMPARISON CHART ── */
.comparison-chart{margin:20px 0;overflow-x:auto}
.bar-chart{width:100%;height:320px}

/* ── TABS ── */
.tab-group{margin:20px 0}
.tab-bar{display:flex;gap:0;border-bottom:2px solid var(--border);margin-bottom:20px}
.tab-btn{
  padding:8px 18px;background:none;border:none;cursor:pointer;
  font-family:var(--serif);font-size:13px;color:var(--ink4);
  border-bottom:2px solid transparent;margin-bottom:-2px;transition:all 0.15s;
}
.tab-btn.active{color:var(--ink);border-bottom-color:var(--accent2);font-weight:600}
.tab-btn:hover:not(.active){color:var(--ink2)}
.tab-panel{display:none}
.tab-panel.active{display:block;animation:fadeIn 0.15s ease}

/* ── METRIC CARDS ── */
.metric-row{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}
.metric-card{
  flex:1;min-width:140px;padding:14px 16px;
  background:#fff;border:1px solid var(--border);border-radius:4px;
  border-top:3px solid;
}
.metric-name{font-size:10px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;
  font-family:var(--mono);color:var(--ink4);margin-bottom:4px}
.metric-desc{font-size:12.5px;color:var(--ink2);line-height:1.5;margin-bottom:6px}
.metric-when{font-size:11px;color:var(--ink4);font-style:italic}

/* ── FORMULA DISPLAY ── */
.formula-block{
  background:var(--ink);color:var(--cream);padding:16px 20px;
  border-radius:4px;margin:16px 0;font-family:var(--mono);font-size:13px;
  line-height:1.7;overflow-x:auto;
}
.formula-block .comment{color:var(--ink4)}
.formula-block .highlight{color:var(--accent3)}

/* ── NOTEBOOK LINK BANNER ── */
.notebook-banner{
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;
  padding:14px 18px;background:var(--ink);border-radius:4px;margin:24px 0;
}
.nb-text{font-size:12px;color:rgba(255,255,255,0.65);font-family:var(--mono)}
.nb-text strong{color:#fff}
.nb-link{
  display:inline-flex;align-items:center;gap:6px;
  font-size:11px;font-family:var(--mono);color:var(--accent3);
  text-decoration:none;border:1px solid var(--accent3);padding:5px 12px;border-radius:3px;
  transition:all 0.15s;
}
.nb-link:hover{background:var(--accent3);color:var(--ink)}

/* ── INTERACTIVE CHART CANVAS ── */
.chart-container{position:relative;height:280px;margin:16px 0}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .page-wrap{grid-template-columns:1fr}
  .sidebar{position:relative;height:auto}
  .section,.section-hero{padding:40px 24px}
  .pros-cons{grid-template-columns:1fr}
  h1.hero-title{font-size:32px}
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--ink4)}

/* ── PRINT ── */
@media print{.sidebar{display:none}.page-wrap{grid-template-columns:1fr}}
</style>
</head>
<body>
'''

print("Head section ready:", len(SECTIONS['head']), "chars")
