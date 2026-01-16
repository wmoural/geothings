import streamlit as st

def uploader():
    return """
    <style>
    /* Container Principal */
    div[data-testid="stFileUploader"] {
        position: relative;
        border: 2px dashed #D1D5DB;
        border-radius: 16px;
        background: linear-gradient(145deg, #ffffff, #f3f4f6);
        padding: 2.5rem 1rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    /* Efeito de Hover */
    div[data-testid="stFileUploader"]:hover {
        border-color: #3B82F6;
        background: #F0F7FF;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.2);
    }

    /* Esconde o dropzone padrão mas mantém funcional */
    section[data-testid="stFileUploaderDropzone"] {
        opacity: 0 !important;
        position: absolute !important;
        inset: 0 !important;
        z-index: 10 !important;
        cursor: pointer !important;
    }

    /* Texto Superior (Instrução) */
    div[data-testid="stFileUploader"]::before {
        content: "✨ Arraste seu arquivo aqui";
        color: #4B5563;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 1.1rem;
        display: block;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }

    /* Botão Centralizado */
    div[data-testid="stFileUploader"]::after {
        content: "Procurar no Computador";
        display: inline-block;
        background: linear-gradient(90deg, #3B82F6 0%, #2563EB 100%);
        color: #FFFFFF;
        padding: 0.75rem 1.8rem;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.025em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
        z-index: 1;
        position: relative;
    }

    /* Esconde elementos nativos poluídos */
    div[data-testid="stFileUploader"] div[role="listitem"], 
    div[data-testid="stFileUploader"] .st-emotion-cache-1ae8k9d {
        display: none !important;
    }
    
    /* Remove textos padrão do Streamlit */
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
    @keyframes slideUp {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    div[data-testid="stFileUploader"] {{
        position: relative;
        border: 2px solid #10B981;
        border-radius: 16px;
        background: #ECFDF5;
        padding: 2rem 1rem;
        text-align: center;
        animation: slideUp 0.4s ease-out;
    }}

    div[data-testid="stFileUploader"]::before {{
        content: "✅ Arquivo pronto!";
        color: #065F46;
        font-weight: 700;
        font-size: 1.1rem;
        display: block;
        margin-bottom: 0.8rem;
        position: relative;
    }}

    div[data-testid="stFileUploader"]::after {{
        content: "{filename}";
        display: inline-block;
        background: #10B981;
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 8px;
        font-family: monospace;
        font-size: 0.85rem;
        position: relative;
    }}

    /* Estilização extra para o estado de sucesso */
    div[data-testid="stFileUploader"] *:not([role="listitem"]) {{
        color: transparent !important;
    }}
    </style>
    """
