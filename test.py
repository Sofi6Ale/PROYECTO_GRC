import os
import fitz  # <-- Esta es la librería PyMuPDF para leer el PDF
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Configuración de Seguridad
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: Clave no encontrada en el archivo .env")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    print("✅ Sistema GRC listo y conectado con Gemini 2.5 Flash.")

    # 2. Función base de auditoría
    def realizar_auditoria(texto_pdf):
        prompt = f"""
        Eres un auditor Senior de GRC (Gobernanza, Riesgo y Cumplimiento). 
        Analiza el siguiente texto extraído de un documento de la empresa.
        Identifica posibles riesgos, faltas de cumplimiento o ambigüedades.
        
        Texto del documento:
        {texto_pdf}
        """
        response = model.generate_content(prompt)
        return response.text

    # 3. NUEVO: Lógica para abrir y leer el PDF
    # Definimos la ruta donde está tu archivo
    ruta_pdf = os.path.join("documentos", "politica_prueba.pdf")

    print(f"🔍 Intentando abrir el archivo: {ruta_pdf}...")

    if not os.path.exists(ruta_pdf):
        print(f"❌ Error: No encontré el archivo '{ruta_pdf}'. Revisa el nombre o la carpeta.")
    else:
        try:
            # Abrimos el PDF con PyMuPDF
            documento = fitz.open(ruta_pdf)
            texto_extraido = ""

            # Recorremos cada página y extraemos su texto
            for pagina in documento:
                texto_extraido += pagina.get_text()

            print("📖 Texto extraído con éxito. Enviando a la IA para auditoría...")
            print("⏳ Procesando... (esto puede tomar unos segundos)")

            # Enviamos el texto acumulado a la función de Gemini
            resultado_auditoria = realizar_auditoria(texto_extraido)

            print("\n================ 🚨 INFORME DE AUDITORÍA GRC 🚨 ================")
            print(resultado_auditoria)
            print("================================================================")

        except Exception as e:
            print(f"❌ Ocurrió un error al procesar el PDF: {e}")