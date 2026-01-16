import streamlit as st
import streamlit.components.v1 as components

# Configurando página
st.set_page_config(page_title='geothings!', layout='wide', page_icon=':material/public:')

# --- CSS PERSONALIZADO ---
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0');

/* Fundo Verde Pastel Simples */
[data-testid="stAppViewContainer"] {
    background-color: #f0fdf4; /* Tom verde pastel bem suave */
}

body {
    font-family: 'Inter', sans-serif;
}

/* Hero Modernizado */
.main-header {
    text-align: center;
    padding: 80px 20px 60px;
}

.title-logo {
    font-size: 4rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -2px;
    margin-bottom: 10px;
}

.title-logo span {
    color: #10b981;
}

.subtitle-hero {
    font-size: 1.2rem;
    color: #64748b;
    max-width: 600px;
    margin: 0 auto;
    font-weight: 400;
}

/* Grid de Cards */
.card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(16, 185, 129, 0.1);
    border-radius: 24px;
    padding: 40px 30px;
    text-align: center;
    transition: all 0.4s ease;
    height: 100%;
}

.card:hover {
    transform: translateY(-10px);
    background: white;
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    border-color: #10b981;
}

.icon-wrapper {
    background: #ecfdf5;
    width: 60px;
    height: 60px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 24px;
}

.icon-wrapper .material-symbols-outlined {
    color: #10b981;
    font-size: 32px;
}

.card h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 16px;
}

.card p {
    font-size: 0.95rem;
    color: #64748b;
    line-height: 1.6;
}

/* Esconder elementos padrão do Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("""
<div class="main-header">
    <h1 class="title-logo">geo<span>things!</span></h1>
</div>
""", unsafe_allow_html=True)

# --- CARDS DATA ---
tools = [
    {
        "title": "Easy Geocoding",
        "icon": "location_on",
        "text": "Converta endereços em coordenadas geográficas com precisão industrial."
    },
    {
        "title": "Easy Reverse",
        "icon": "sync_alt",
        "text": "Descubra o endereço exato a partir de qualquer ponto no mapa."
    },
    {
        "title": "Easy Routes",
        "icon": "route",
        "text": "Otimize trajetos complexos e economize tempo e recursos logísticos."
    },
    {
        "title": "Easy Overture",
        "icon": "map",
        "text": "Explore bilhões de dados abertos da fundação Overture Maps."
    }
]

# --- RENDERIZAÇÃO DOS CARDS ---
cols = st.columns(len(tools), gap="large")

for col, tool in zip(cols, tools):
    with col:
        html_card = f"""
        <div class="card">
            <div class="icon-wrapper">
                <span class="material-symbols-outlined">{tool['icon']}</span>
            </div>
            <h3>{tool['title']}</h3>
            <p>{tool['text']}</p>
        </div>
        """
        st.markdown(html_card, unsafe_allow_html=True)

# Espaçador inferior
st.markdown("<br><br><br>", unsafe_allow_html=True)
