# Motor de Auditoría Automatizada GRC (AI-Powered)

## 📝 Descripción del Proyecto
Este proyecto es un Producto Mínimo Viable (MVP) diseñado para automatizar la auditoría de documentos corporativos bajo los pilares de **GRC** (Gobernanza, Riesgo y Cumplimiento). El sistema es capaz de extraer el texto de archivos PDF locales de manera segura y utilizar Inteligencia Artificial para identificar vacíos legales, riesgos operativos y faltas de cumplimiento normativo en segundos.

## 🏗️ Arquitectura del Sistema
El flujo de datos de la aplicación se compone de las siguientes capas:
1. **Extracción Local**: Utiliza `PyMuPDF` (`fitz`) para procesar el documento PDF y extraer texto plano de manera local en memoria.
2. **Seguridad de Activos**: Gestión de credenciales aisladas mediante variables de entorno (`python-dotenv`), evitando la exposición de API Keys en el código fuente.
3. **Análisis Semántico**: Integración por API con el modelo **Gemini 2.5 Flash** de Google para la evaluación lógica-normativa.

## 🛠️ Requisitos e Instalación
Para ejecutar este proyecto en un entorno local, se requiere Python 3 y la instalación de las siguientes dependencias:

```bash
pip install python-dotenv google-generativeai pymupdf