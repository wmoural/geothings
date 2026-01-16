import streamlit as st

# Configurando página
st.set_page_config(page_title='Easy GeoMax!', layout='wide', page_icon=':material/public:')

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0');

:root {
    --primary: #10b981;
    --primary-dark: #059669;
    --accent: #0f172a;
    --muted: #64748b;
    --light: #f8fafc;
    --card-bg: rgba(255, 255, 255, 0.7);
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}

.material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-weight: normal;
    font-style: normal;
    font-size: 24px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    display: inline-block;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    -webkit-font-smoothing: antialiased;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 50%, #f0fdfa 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

body, .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, div {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}

/* Hero Section */
.hero-section {
    text-align: center;
    padding: 60px 20px 40px;
    max-width: 900px;
    margin: 0 auto;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
}

.hero-badge .material-symbols-outlined {
    font-size: 18px;
}

.hero-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    color: var(--accent);
    margin: 0 0 16px 0;
    line-height: 1.1;
    letter-spacing: -0.02em;
}

.hero-title span {
    background: linear-gradient(135deg, var(--primary) 0%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var(--muted);
    max-width: 600px;
    margin: 0 auto 32px;
    line-height: 1.6;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 48px;
    margin-top: 40px;
    flex-wrap: wrap;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-dark);
}

.stat-label {
    font-size: 14px;
    color: var(--muted);
    margin-top: 4px;
}

/* Section Title */
.section-title {
    text-align: center;
    margin: 60px 0 40px;
}

.section-title h2 {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent);
    margin: 0 0 12px 0;
}

.section-title p {
    color: var(--muted);
    font-size: 1.1rem;
}

/* Cards */
.card {
    background: var(--card-bg);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 32px 28px;
    box-shadow: var(--shadow);
    border: 1px solid rgba(255, 255, 255, 0.8);
    min-height: 320px;
    display: flex;
    flex-direction: column;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    border-radius: 20px 20px 0 0;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-lg);
    border-color: rgba(16, 185, 129, 0.2);
}

.card-1::before { background: linear-gradient(90deg, #10b981, #34d399); }
.card-2::before { background: linear-gradient(90deg, #059669, #10b981); }
.card-3::before { background: linear-gradient(90deg, #047857, #059669); }
.card-4::before { background: linear-gradient(90deg, #065f46, #047857); }

.card-icon {
    width: 56px;
    height: 56px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

.card-icon .material-symbols-outlined {
    font-size: 28px;
    color: #065f46;
}

.card-1 .card-icon { background: linear-gradient(135deg, #d1fae5, #a7f3d0); }
.card-2 .card-icon { background: linear-gradient(135deg, #a7f3d0, #6ee7b7); }
.card-3 .card-icon { background: linear-gradient(135deg, #6ee7b7, #34d399); }
.card-4 .card-icon { background: linear-gradient(135deg, #34d399, #10b981); }

.card .badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
    width: fit-content;
}

.card-1 .badge { background: #d1fae5; color: #065f46; }
.card-2 .badge { background: #a7f3d0; color: #065f46; }
.card-3 .badge { background: #6ee7b7; color: #064e3b; }
.card-4 .badge { background: #34d399; color: #064e3b; }

.card h3 {
    margin: 0 0 12px 0;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--accent);
}

.card p {
    margin: 0;
    font-size: 15px;
    color: var(--muted);
    line-height: 1.7;
    flex-grow: 1;
}

.card-arrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--primary-dark);
    font-weight: 600;
    font-size: 14px;
    margin-top: 20px;
    cursor: pointer;
    transition: gap 0.2s ease;
}

.card-arrow .material-symbols-outlined {
    font-size: 18px;
}

.card:hover .card-arrow {
    gap: 12px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 60px 20px 40px;
    color: var(--muted);
    font-size: 14px;
}

.footer-brand {
    font-weight: 700;
    color: var(--primary-dark);
}

/* Responsive */
@media (max-width: 900px) {
    .stColumns > div { 
        width: 100% !important; 
        margin-bottom: 20px;
    }
    .card { 
        min-height: auto;
        padding: 28px 24px;
    }
    .hero-stats {
        gap: 32px;
    }
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display: none;}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# Hero Section
hero_html = """
<div class="hero-section">
    <div class="hero-badge">
        <span class="material-symbols-outlined">rocket_launch</span>
        Plataforma Geoespacial Completa
    </div>
    <h1 class="hero-title">
        Easy <span>GeoMax!</span>
    </h1>
    <p class="hero-subtitle">
        Simplifique suas análises geoespaciais com ferramentas poderosas de geocodificação, 
        otimização de rotas e acesso a dados abertos — tudo em uma única plataforma.
    </p>
    <div class="hero-stats">
        <div class="stat-item">
            <div class="stat-number">4+</div>
            <div class="stat-label">Ferramentas</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">100%</div>
            <div class="stat-label">Web-based</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">∞</div>
            <div class="stat-label">Possibilidades</div>
        </div>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# Section Title
section_title = """
<div class="section-title">
    <h2>Nossas Ferramentas</h2>
    <p>Escolha a solução ideal para o seu projeto geoespacial</p>
</div>
"""
st.markdown(section_title, unsafe_allow_html=True)

# Cards data com ícones do Material Symbols
descriptions = [
    {
        "title": "Easy Geocoding",
        "badge": "Geocodificação",
        "class": "card-1",
        "icon": "location_on",
        "text": "Converta listas de endereços em coordenadas geográficas utilizando provedores confiáveis como Google e ArcGIS, com integração direta para análises espaciais."
    },
    {
        "title": "Easy ReverseGeocoding",
        "badge": "Geocodificação Reversa",
        "class": "card-2",
        "icon": "sync_alt",
        "text": "Obtenha endereços detalhados a partir de coordenadas geográficas, facilitando a validação de dados espaciais e enriquecimento de bases."
    },
    {
        "title": "Easy Routes",
        "badge": "Otimização de Rotas",
        "class": "card-3",
        "icon": "route",
        "text": "Calcule trajetos otimizados entre múltiplos pontos para análises de mobilidade, planejamento logístico e comparação de alternativas."
    },
    {
        "title": "Easy Overture",
        "badge": "Dados Abertos",
        "class": "card-4",
        "icon": "map",
        "text": "Acesse e baixe dados da Overture Maps Foundation diretamente, ideais para estudos urbanos, ambientais e de infraestrutura."
    }
]

cols = st.columns(4, gap="medium")
for col, desc in zip(cols, descriptions):
    html = f"""
    <div class='card {desc['class']}'>
        <div class="card-icon">
            <span class="material-symbols-outlined">{desc['icon']}</span>
        </div>
        <div class="badge">{desc['badge']}</div>
        <h3>{desc['title']}</h3>
        <p>{desc['text']}</p>
        <div class="card-arrow">
            Acessar ferramenta
            <span class="material-symbols-outlined">arrow_forward</span>
        </div>
    </div>
    """
    col.markdown(html, unsafe_allow_html=True)

# Footer
footer_html = """
<div class="footer">
    <p>Desenvolvido pela equipe <span class="footer-brand">Easy GeoMax</span></p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
