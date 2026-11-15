# Mauricio Alejandro Vargas Ortega
**Ingeniería Comercial | Desarrollador Python — FinOps, Automatización de Procesos y Modelamiento Cuantitativo**  
Universidad de Los Lagos — Osorno, Chile  
[Perfil de LinkedIn](https://www.linkedin.com/in/mauricio-vargas-ortega/)

Desarrollo de motores de cálculo financiero, pipelines de automatización empresarial en la nube (Google Cloud Platform / Linux), administración programática multi-repositorio, auditoría tributaria electrónica (SII) y plataformas analíticas interactivas de soporte a la toma de decisiones.

---

## I. Plataformas Interactivas en Vivo (Streamlit Cloud)

Acceso directo a los sistemas desplegados en producción y su impacto operativo frente al flujo manual tradicional:

| Sistema / Módulo | Área de Aplicación y Capacidades | Mejora vs. Flujo Manual | Código Fuente | Plataforma Web |
| :--- | :--- | :---: | :--- | :--- |
| **Super Hub y Central de Mando GitHub** | Extractor multi-repositorio en RAM (volcado total, firmas AST y partición en tomos), CMS remoto por lotes vía GitHub REST API (`About`, `Topics`, `requirements.txt`, `README.md` y despliegue masivo) y lectura quirúrgica HTTP Byte-Range sobre respaldos `.zip` en Google Drive API con visor PDF.js. | **99,8%** (`450x` más rápido) | [github-context-extractor](https://github.com/mauriciovargas1516-ux/github-context-extractor) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-334155?style=flat-square&logo=streamlit&logoColor=white)](https://app-context-extractor-cl8x5kwfdodzvmx7m3vean.streamlit.app/) |
| **Simulador de Finanzas Avanzadas** | Evaluación de activos reales, estructura de capital (CAPM/WACC), FCL, FCI, amortización francesa, sensibilidad multiescenario y simulación de Monte Carlo (hasta 50.000 iteraciones) con exportación a Excel de 6 hojas con fórmulas vivas. | **99,4%** (`163x` más rápido) | [FINANZAS-AVANZADAS-2026](https://github.com/mauriciovargas1516-ux/FINANZAS-AVANZADAS-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-107C41?style=flat-square&logo=streamlit&logoColor=white)](https://finanzas-avanzadas-2026-nxvqzsfrrtgu9e92javcli.streamlit.app/) |
| **Suite de Evaluación de Proyectos** | Formulación y evaluación privada, social y ambiental bajo normativa SNI / MIDESO 2026 (precios sociales, microeconomía de Fontaine, Matriz de Leopold, Marco Lógico) con compilación automática en 1 clic de informe Word institucional, PDF y libros Excel dinámicos en `.zip`. | **99,6%** (`230x` más rápido) | [PROYECTOS-2026](https://github.com/mauriciovargas1516-ux/PROYECTOS-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-1E3A8A?style=flat-square&logo=streamlit&logoColor=white)](https://proyectos-2026-ubfvxgpqmpp5z7dn6wlnn3.streamlit.app/) |
| **Suite de Gestión Tributaria** | Normativa del Código Tributario, simulador de Rentas (1ª y 2ª Categoría LIR), liquidación de IVA / proporcionalidad y remanente UTM F29 (DL 825 / Ley 21.420) y analítica del Plan de Gestión de Cumplimiento Tributario (PGCT 2026 SII). | **99,3%** (`144x` más rápido) | [GESTION-TRIBUTARIA-2026](https://github.com/mauriciovargas1516-ux/GESTION-TRIBUTARIA-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-0F172A?style=flat-square&logo=streamlit&logoColor=white)](https://gestion-tributaria-2026-avecwdhabftj7rjnx5knmb.streamlit.app/) |
| **Motor de Análisis Territorial** | Plataforma de 8 módulos: técnicas de análisis regional SII (ILPES / Shift & Share MADE), convergencia econométrica REAT, movilidad de Quah, redes empresariales animadas (Dini 2010 / UCINET / Boisier ELITE) y ordenamiento territorial (Rondinelli, Guttman y PROT en 97 comunas). | **99,4%** (`180x` más rápido) | [DESARROLLO-Y-GESTION-TERRITORIAL-2026](https://github.com/mauriciovargas1516-ux/DESARROLLO-Y-GESTION-TERRITORIAL-2026) | [![Abrir Sistema](https://img.shields.io/badge/STREAMLIT_APP-ABRIR_SISTEMA-0284C7?style=flat-square&logo=streamlit&logoColor=white)](https://desarrollo-y-gestion-territorial-2026-ec6keylhsgra88s77bkl6f.streamlit.app/) |

---

## II. Motores de Automatización Empresarial, FinOps e Ingeniería (Python)

| Repositorio | Arquitectura y Función Operativa | Impacto Operativo | Stack Principal |
| :--- | :--- | :---: | :--- |
| **[insumaes-woocommerce-automation](https://github.com/mauriciovargas1516-ux/insumaes-woocommerce-automation)** | ERP Omnicanal en la nube (42 funciones activas): sincronización delta cada 3s de inventario y precios entre WooCommerce y Mercado Libre, CRM B2B en SQLite (~204 ciudades y 445 cotizaciones), traspasador multicanal (Mercado Libre, Falabella, Paris, Lider, Shopify) y auditoría de márgenes. | **630 hrs/año ahorradas** (`95,3%` mejora) | `Python` `GCP VM` `SQLite` `REST APIs` |
| **[motor-planos-sec-te1-chile](https://github.com/mauriciovargas1516-ux/motor-planos-sec-te1-chile)** | Motor paramétrico para generación automatizada de planos eléctricos interiores y rurales en AutoCAD (`.dxf`), cuadros de cargas nativos, cálculo de caída de tensión y clasificación normativa TE1 (D.S. N° 92/83) ante la SEC. | **98,5% reducción** tiempo dibujo CAD | `Python` `ezdxf` `Streamlit` `Tkinter` |
| **[motor-auditor-dte-finops](https://github.com/mauriciovargas1516-ux/motor-auditor-dte-finops)** | Pipeline de auditoría forense para Cuentas por Pagar (AP) y Cuentas por Cobrar (AR): extracción vectorial de PDFs, validación de RUT/Folio ante el SII y bloqueo preventivo de pagos duplicados con exportación estructurada a Excel. | **99,6% velocidad** auditoría DTE | `Python` `pdfplumber` `Pandas` `Regex` |
| **[motor-conciliador-chile](https://github.com/mauriciovargas1516-ux/motor-conciliador-chile)** | Sistema de conciliación bancaria corporativa en 3 fases (agrupación de lotes, cruce exacto por RUT/monto y emparejamiento difuso) con detección automática de cabeceras y reportes de excepciones en Excel. | **99,2% reducción** cruce cartolas | `Python` `Pandas` `TheFuzz` `OpenPyXL` |
| **[moodle-hybrid-scraper](https://github.com/mauriciovargas1516-ux/moodle-hybrid-scraper)** | Extractor documental de arquitectura híbrida: autenticación en formularios dinámicos mediante captura de sesión y descarga masiva de alta velocidad por peticiones HTTP directas. | **99,0% ahorro** descarga masiva | `Python` `Selenium` `Requests` `BS4` |

---

## III. Stack Técnico

* **Lenguajes y Entornos:** Python 3, R (REAT / R Markdown), SQL (SQLite), Bash / Cron (Linux Debian/Ubuntu).
* **Librerías de Ingeniería, Datos y Documentación:** Pandas, NumPy, SciPy, NumPy-Financial, Plotly, Matplotlib, NetworkX, OpenPyXL, python-docx, pypdf, pdfplumber, BeautifulSoup4, TheFuzz, ezdxf.
* **Infraestructura, APIs y Despliegue:** Google Cloud Platform (Compute Engine / IAM / Google Drive API), Streamlit Cloud, Git / GitHub REST API, Integración con APIs REST (WooCommerce, Mercado Libre, Dropbox).
