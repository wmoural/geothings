import streamlit as st

def uploader():
    return """
    <style>
    /* Container Principal */
    div[data-testid="stFileUploader"] {
        position: relative;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        background: #FAFAFA;
        padding: 2.5rem 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }

    /* Efeito de Hover */
    div[data-testid="stFileUploader"]:hover {
        border-color: #1F2937;
        background: #F9FAFB;
    }

    /* Esconde o dropzone padrao mas mantem funcional */
    section[data-testid="stFileUploaderDropzone"] {
        opacity: 0 !important;
        position: absolute !important;
        inset: 0 !important;
        z-index: 10 !important;
        cursor: pointer !important;
    }

    /* Texto Superior */
    div[data-testid="stFileUploader"]::before {
        content: "Arraste seu arquivo aqui";
        color: #6B7280;
        font-family: 'Inter', -apple-system, sans-serif;
        font-weight: 400;
        font-size: 0.95rem;
        display: block;
        margin-bottom: 1.25rem;
        position: relative;
        z-index: 1;
    }

    /* Botao Centralizado */
    div[data-testid="stFileUploader"]::after {
        content: "Selecionar arquivo";
        display: inline-block;
        background: #1F2937;
        color: #FFFFFF;
        padding: 0.625rem 1.5rem;
        border-radius: 6px;
        font-size: 0.875rem;
        font-weight: 500;
        letter-spacing: -0.01em;
        transition: background 0.2s ease;
        z-index: 1;
        position: relative;
    }

    div[data-testid="stFileUploader"]:hover::after {
        background: #374151;
    }

    /* Esconde elementos nativos */
    div[data-testid="stFileUploader"] div[role="listitem"], 
    div[data-testid="stFileUploader"] .st-emotion-cache-1ae8k9d {
        display: none !important;
    }
    
    /* Remove textos padrao do Streamlit */
    div[data-testid="stFileUploader"] *:not([role="listitem"]) {
        color: transparent !important;
        background: transparent !important;
        border: none !important;
    }
    </style>
    """
    
def uploader_depois(filename):
    if not filename: return ''
    return f"""
    <style>
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    div[data-testid="stFileUploader"] {{
        position: relative;
        border: 1px solid #D1D5DB;
        border-radius: 12px;
        background: #F9FAFB;
        padding: 2rem 1.5rem;
        text-align: center;
        animation: fadeIn 0.3s ease;
    }}

    div[data-testid="stFileUploader"]::before {{
        content: "Arquivo carregado";
        color: #1F2937;
        font-family: 'Inter', -apple-system, sans-serif;
        font-weight: 500;
        font-size: 0.95rem;
        display: block;
        margin-bottom: 0.75rem;
        position: relative;
    }}

    div[data-testid="stFileUploader"]::after {{
        content: "{filename}";
        display: inline-block;
        background: #E5E7EB;
        color: #374151;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-family: 'SF Mono', 'Fira Code', monospace;
        font-size: 0.8rem;
        position: relative;
    }}

    div[data-testid="stFileUploader"] *:not([role="listitem"]) {{
        color: transparent !important;
    }}
    </style>
    """
