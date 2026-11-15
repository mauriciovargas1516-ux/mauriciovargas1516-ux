# Mauricio Alejandro Vargas Ortega
**Ingeniería Comercial | Desarrollador Python — FinOps, Automatización de Procesos y Modelamiento Cuantitativo**  
Universidad de Los Lagos — Osorno, Chile  
[Perfil de LinkedIn](https://www.linkedin.com/in/mauricio-vargas-ortega/)

Desarrollo de motores de cálculo financiero, pipelines de automatización empresarial en la nube (Google Cloud Platform / Linux), administración programática multi-repositorio, auditoría tributaria electrónica (SII) y plataformas analíticas interactivas de soporte a la toma de decisiones.

---

## I. Plataformas Interactivas en Vivo (Streamlit Cloud)

Acceso directo a los sistemas desplegados en producción y su impacto en horas frente al flujo manual tradicional:

| Sistema / Módulo | Área de Aplicación | Manual vs. Cloud | Mejora | Código Fuente | Plataforma Web |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **Super Hub y Central de Mando GitHub** | Extractor multi-repositorio en RAM (volcado total, firmas AST y tomos), CMS remoto por lotes vía GitHub REST API (`About`, `requirements.txt`, `README.md`, despliegue masivo) y lectura HTTP Byte-Range sobre Google Drive API con visor PDF.js. | **7,5 hrs** vs. **1 min** | **99,8%** (`450x`) | [github-context-extractor](https://github.com/mauriciovargas1516-ux/github-context-extractor) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-334155?style=flat-square&logo=streamlit&logoColor=white)](https://app-context-extractor-cl8x5kwfdodzvmx7m3vean.streamlit.app/) |
| **Suite de Evaluación de Proyectos** | Formulación y evaluación privada, social y ambiental bajo normativa SNI / MIDESO 2026 (precios sociales, microeconomía de Fontaine, Matriz de Leopold, Marco Lógico) con compilación en 1 clic de Word, PDF y libros Excel dinámicos en `.zip`. | **46,0 hrs** vs. **12 min** | **99,6%** (`230x`) | [PROYECTOS-2026](https://github.com/mauriciovargas1516-ux/PROYECTOS-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-1E3A8A?style=flat-square&logo=streamlit&logoColor=white)](https://app-context-extractor-cl8x5kwfdodzvmx7m3vean.streamlit.app/) |
| **Simulador de Finanzas Avanzadas** | Evaluación de activos reales, estructura de capital (CAPM/WACC), FCL, FCI, amortización francesa, sensibilidad multiescenario y simulación de Monte Carlo (50.000 iteraciones) con exportación a Excel de 6 hojas con fórmulas vivas. | **24,5 hrs** vs. **9 min** | **99,4%** (`163x`) | [FINANZAS-AVANZADAS-2026](https://github.com/mauriciovargas1516-ux/FINANZAS-AVANZADAS-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-107C41?style=flat-square&logo=streamlit&logoColor=white)](https://finanzas-avanzadas-2026-nxvqzsfrrtgu9e92javcli.streamlit.app/) |
| **Motor de Análisis Territorial** | Plataforma de 8 módulos: técnicas de análisis regional SII (ILPES / Shift & Share MADE), convergencia econométrica REAT, movilidad de Quah, redes empresariales animadas (Dini 2010 / UCINET / ELITE) y ordenamiento territorial (97 comunas). | **18,0 hrs** vs. **6 min** | **99,4%** (`180x`) | [DESARROLLO-Y-GESTION-TERRITORIAL-2026](https://github.com/mauriciovargas1516-ux/DESARROLLO-Y-GESTION-TERRITORIAL-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-0284C7?style=flat-square&logo=streamlit&logoColor=white)](https://app-context-extractor-cl8x5kwfdodzvmx7m3vean.streamlit.app/) |
| **Suite de Gestión Tributaria** | Normativa Código Tributario, simulador de Rentas (1ª y 2ª Categoría LIR), liquidación de IVA / proporcionalidad y remanente UTM F29 (DL 825 / Ley 21.420) y analítica del Plan de Gestión de Cumplimiento Tributario (PGCT 2026 SII). | **11,5 hrs** vs. **5 min** | **99,3%** (`144x`) | [GESTION-TRIBUTARIA-2026](https://github.com/mauriciovargas1516-ux/GESTION-TRIBUTARIA-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-0F172A?style=flat-square&logo=streamlit&logoColor=white)](https://app-context-extractor-cl8x5kwfdodzvmx7m3vean.streamlit.app/) |

---

## II. Motores de Automatización Empresarial, FinOps e Ingeniería (Python)

| Repositorio | Arquitectura y Función Operativa | Impacto Operativo (Horas / Mejora) | Stack Principal |
| :--- | :--- | :---: | :--- |
| **[insumaes-woocommerce-automation](https://github.com/mauriciovargas1516-ux/insumaes-woocommerce-automation)** | ERP Omnicanal en la nube (42 funciones activas): sincronización delta cada 3s de inventario y precios entre WooCommerce y Mercado Libre, CRM B2B en SQLite (~204 ciudades y 445 cotizaciones), traspasador multicanal (Mercado Libre, Falabella, Paris, Lider, Shopify) y auditoría de márgenes. | **55,1 hrs vs. 2,6 hrs/mes**<br>**630 hrs/año ahorradas** (`95,3%`) | `Python` `GCP VM` `SQLite` `REST APIs` |
| **[motor-planos-sec-te1-chile](https://github.com/mauriciovargas1516-ux/motor-planos-sec-te1-chile)** | Motor paramétrico para generación automatizada de planos eléctricos interiores y rurales en AutoCAD (`.dxf`), cuadros de cargas nativos, cálculo de caída de tensión y clasificación normativa TE1 (D.S. N° 92/83) ante la SEC. | **98,5% reducción**<br>tiempo dibujo CAD | `Python` `ezdxf` `Streamlit` `Tkinter` |
| **[motor-auditor-dte-finops](https://github.com/mauriciovargas1516-ux/motor-auditor-dte-finops)** | Pipeline de auditoría forense para Cuentas por Pagar (AP) y Cuentas por Cobrar (AR): extracción vectorial de PDFs, validación de RUT/Folio ante el SII y bloqueo preventivo de pagos duplicados con exportación estructurada a Excel. | **99,6% velocidad**<br>auditoría masiva DTE | `Python` `pdfplumber` `Pandas` `Regex` |
| **[motor-conciliador-chile](https://github.com/mauriciovargas1516-ux/motor-conciliador-chile)** | Sistema de conciliación bancaria corporativa en 3 fases (agrupación de lotes, cruce exacto por RUT/monto y emparejamiento difuso) con detección automática de cabeceras y reportes de excepciones en Excel. | **99,2% reducción**<br>cruce de cartolas | `Python` `Pandas` `TheFuzz` `OpenPyXL` |
| **[moodle-hybrid-scraper](https://github.com/mauriciovargas1516-ux/moodle-hybrid-scraper)** | Extractor documental de arquitectura híbrida: autenticación en formularios dinámicos mediante captura de sesión y descarga masiva de alta velocidad por peticiones HTTP directas. | **99,0% ahorro**<br>descarga masiva | `Python` `Selenium` `Requests` `BS4` |

---

## III. Stack Técnico

* **Lenguajes y Entornos:** Python 3, R (REAT / R Markdown), SQL (SQLite), Bash / Cron (Linux Debian/Ubuntu).
* **Librerías de Ingeniería, Datos y Documentación:** Pandas, NumPy, SciPy, NumPy-Financial, Plotly, Matplotlib, NetworkX, OpenPyXL, python-docx, pypdf, pdfplumber, BeautifulSoup4, TheFuzz, ezdxf.
* **Infraestructura, APIs y Despliegue:** Google Cloud Platform (Compute Engine / IAM / Google Drive API), Streamlit Cloud, Git / GitHub REST API, Integración con APIs REST (WooCommerce, Mercado Libre, Dropbox).
