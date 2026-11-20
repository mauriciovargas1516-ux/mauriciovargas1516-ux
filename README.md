# ERP Omnicanal Insumaes Cloud — Arquitectura y Caso de Producción

**Sistema en Producción (Código Privado) | Tienda en Vivo:** [www.insumaes.cl](https://www.insumaes.cl)  
**Alcance:** 42 funciones operativas | 2.509 ítems sincronizados (WooCommerce + Mercado Libre) | CRM B2B SQLite | Arquitectura UI/UX CSS3

Sistema de automatización empresarial desplegado sobre Google Cloud Platform (Linux VM) para sincronizar inventario en tiempo real, resguardar márgenes comerciales, estructurar catálogo técnico e-commerce y consolidar inteligencia comercial B2B a partir de múltiples fuentes de datos.

---

## 1. Impacto Operativo Medido (Flujo Manual vs. Arquitectura Cloud)

La automatización de procesos recurrentes alcanza una mejora consolidada de eficiencia del **95,3%** (**21,2x más rápido**), equivalente a **52,5 horas ahorradas al mes** y **630,0 horas al año** (**75,0 jornadas laborales completas**):

| Proceso Operativo / Comercial | Volumen Activo | Manual vs. Cloud | Ahorro (Mes / Año) | Mejora (Velocidad) |
| :--- | :--- | :---: | :---: | :---: |
| **1. Sincronización Stock y Precios (Woo + ML)** | 2.509 ítems (550 cambios/mes) | 23,8 hrs vs. **0,9 hrs** | **22,9 hrs/mes** (274,8 hrs/año) | **96,2% (26,4x)** |
| **2. Emisión y Cruce de Cotizaciones B2B** | 141 cot/mes (445 en SQL) | 18,8 hrs vs. **1,2 hrs** | **17,6 hrs/mes** (211,2 hrs/año) | **93,6% (15,7x)** |
| **3. Estandarización HTML/CSS y Auto-Linker ISO** | 752 fichas vinculadas | 7,5 hrs vs. **0,2 hrs** | **7,3 hrs/mes** (87,6 hrs/año) | **97,3% (37,5x)** |
| **4. Estandarización de Fotos (800x720) y Categorías** | 1.727 prods (100 ajustes/mes) | 5,0 hrs vs. **0,3 hrs** | **4,7 hrs/mes** (56,4 hrs/año) | **94,0% (16,7x)** |
| **TOTAL OPERACIÓN CONTINUA** | **2.509 ítems + CRM B2B** | **55,1 hrs vs. 2,6 hrs** | **52,5 hrs/mes (630,0 hrs/año)** | **95,3% (21,2x)** |

### Eficiencia en Procesos Masivos por Lote y Expansión Omnicanal

| Proceso Masivo de Catálogo o Analítica Comercial | Tiempo Manual | Tiempo Cloud | Mejora (Multiplicador) |
| :--- | :---: | :---: | :---: |
| **Vinculación bidireccional de venta cruzada en 752 fichas técnicas** | 43,9 horas | **4,0 minutos** | **99,8% (658,5x)** |
| **Consolidación de cartera nacional (~204 ciudades) en SQLite** | 18,0 horas | **1,8 minutos** | **99,8% (600,0x)** |
| **Consulta 360 de cliente, RUT, historial y cotizaciones** | 15,0 minutos | **0,01 segundos (SQL)** | **99,9% (90.000x)** |
| **Auditoría de márgenes líquidos y diferencias de precio (782 ítems ML vs. Web)** | 19,5 horas | **3,0 segundos** | **99,9% (23.400x)** |
| **Transformación de catálogo (1.500 SKUs activos) para 5 canales externos** | 772,7 horas | **2,3 horas** | **99,7% (336,0x)** |

---

## 2. Arquitectura del Sistema por Capas

El ecosistema opera de forma modular en 5 capas de ingeniería backend más una capa de arquitectura front-end e-commerce:

| Capa del Sistema | Responsabilidad Técnica |
| :--- | :--- |
| **1. Núcleo de Control y Telemetría** | Panel centralizado en consola con 42 funciones, interruptores en caliente sin reinicio, telemetría de latencia API en tiempo real, bitácoras separadas por canal y envío automatizado de reportes ejecutivos. |
| **2. Motor Delta 24/7 y Reglas de Precisión** | Demonio residente en RAM que monitorea cambios en la planilla maestra cada 3 segundos e inyecta únicamente deltas en 0,35 a 1,08 segundos. Incluye colchón configurable de inventario, cortafuegos anti-errores de precio (bloqueo en 0,01s), emparejamiento tolerante a formatos de SKU/código y lógica de paquetes/cajas cerradas. |
| **3. Suite WooCommerce y Arquitectura UI/UX** | Administración masiva vía REST API: vinculación cruzada de compatibilidad ISO (752 fichas), estandarización automatizada de imágenes (800x720 px), ajuste porcentual de precios con ofertas tachadas y reversión instantánea. Incluye arquitectura **CSS3 modular** desplegada en producción sobre `insumaes.cl` (mega-menú industrial responsive, grilla de tarjetas con micro-interacciones, árbol jerárquico de categorías en 3 niveles y extracción programática de respaldo estético en Python). |
| **4. Integración Mercado Libre & POS** | Sincronización de inventario sobre 782 publicaciones con candado de protección de precios, entorno piloto de pruebas unitarias, instantáneas de respaldo/restauración masiva, terminal compatible con pistola lectora de códigos de barra (EAN/SKU) y generador PDF vectorial de etiquetas Code128. |
| **5. CRM SQLite B2B y Trampolín Multicanal** | Base relacional SQLite en modo solo lectura que indexa 445 cotizaciones B2B y cartera comercial de ~204 ciudades. Incluye auditor de márgenes líquidos (descontando comisiones y logística), detector de brechas entre canales y exportador universal estructurado para Mercado Libre, marketplaces de retail y Shopify. |

---

## 3. Stack Técnico

- **Backend y Automatización:** Python 3, Pandas, NumPy, OpenPyXL, Pillow (PIL), SQLite3, ThreadPoolExecutor, Bash / Cron.
- **Infraestructura y APIs:** Google Cloud Platform (Compute Engine Linux VM), WooCommerce REST API v3, Mercado Libre API (OAuth2), Dropbox API, SMTP.
- **Front-End E-Commerce:** HTML5, CSS3 modular (Grid, Flexbox, variables, transiciones y micro-animaciones sin sobrecarga JS), WordPress / WooCommerce / Elementor.

---

## 4. Confidencialidad

El código fuente operativo, los archivos de configuración, las credenciales de integración y las bases de datos comerciales residen en un repositorio privado de producción. La operación e interfaz pública resultante pueden verificarse directamente en [https://www.insumaes.cl](https://www.insumaes.cl).
