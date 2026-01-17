import streamlit as st

def uploader():
    return """
    <style>
    div[data-testid="stFileUploader"] {
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
        padding: 1.5rem 1rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    div[data-testid="stFileUploader"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.35);
    }
    section[data-testid="stFileUploaderDropzone"] {
        opacity: 0 !important;
        position: absolute !important;
        inset: 0 !important;
        z-index: 10 !important;
        cursor: pointer !important;
    }
    div[data-testid="stFileUploader"]::before {
        content: "Arraste seu arquivo";
        color: rgba(255,255,255,0.9);
        font-weight: 500;
        font-size: 0.95rem;
        display: block;
        margin-bottom: 0.75rem;
    }
    div[data-testid="stFileUploader"]::after {
        content: "Selecionar";
        background: rgba(255,255,255,0.95);
        color: #667EEA;
        padding: 0.5rem 1.25rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    div[data-testid="stFileUploader"] * {
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
    div[data-testid="stFileUploader"] {{
        border: 1px solid #10B981;
        border-radius: 10px;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        padding: 1.5rem 1rem;
        text-align: center;
    }}
    div[data-testid="stFileUploader"]::before {{
        content: "Arquivo carregado";
        color: rgba(255,255,255,0.95);
        font-weight: 600;
        font-size: 0.9rem;
        display: block;
        margin-bottom: 0.5rem;
    }}
    div[data-testid="stFileUploader"]::after {{
        content: "{filename}";
        background: rgba(255,255,255,0.9);
        color: #059669;
        padding: 0.4rem 1rem;
        border-radius: 5px;
        font-family: monospace;
        font-size: 0.75rem;
    }}
    div[data-testid="stFileUploader"] * {{
        color: transparent !important;
    }}
    </style>
    """
