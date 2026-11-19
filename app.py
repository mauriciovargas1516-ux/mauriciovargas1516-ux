# -*- coding: utf-8 -*-
"""
PLATAFORMA INTEGRAL DE DESARROLLO Y GESTIÓN TERRITORIAL 2026
Universidad de Los Lagos — Ingeniería Comercial
Asignatura: Desarrollo y Gestión Territorial (Prof. Claudio Mancilla)
Archivo Principal: app.py (Arquitectura Limpia de 5 Vistas + Estudio 60 FPS)
"""

import os
import streamlit as st

import motor_sii_exportador as msii
from motor_laboratorio_catedra import renderizar_laboratorio_catedra
from motor_redes_territorio_ot import renderizar_redes_territorio_ot
from motor_redes_dinamicas_dini import (
    renderizar_extension_redes_y_gradientes,
    renderizar_burbuja_tip,
    inyectar_estilos_burbujas,
)

try:
    from motor_fluidez_territorial_60fps import renderizar_laboratorio_fluido_territorial
except Exception:
    renderizar_laboratorio_fluido_territorial = None


ARCHIVO_EXCEL_REPO = "ILPES GRUPO 10 29-10-2026.xlsx"
ARCHIVO_PDF_CUESTIONARIO = "cuestionario_entrevista.pdf"

try:
    _qp_modo_init = str(st.query_params.get("modo", "")).strip().lower()
except Exception:
    _qp_modo_init = ""

_es_url_catedra = _qp_modo_init in ("catedra", "docente", "presentacion", "1", "true")

st.set_page_config(
    page_title="Desarrollo y Gestión Territorial 2026 — ULagos",
    layout="wide",
    initial_sidebar_state="collapsed" if _es_url_catedra else "expanded",
)

st.markdown(
    """
    <style>
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
    }
    .block-container {
        padding-top: 1.3rem !important;
        padding-bottom: 2rem !important;
        max-width: 1320px !important;
    }
    .sec-header {
        background-color: #DBEAFE !important;
        color: #1E3A8A !important;
        padding: 8px 14px;
        font-weight: 700;
        font-size: 14px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
        border-left: 4px solid #1D4ED8;
    }
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 10px 12px;
        border-radius: 6px;
    }
    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
inyectar_estilos_burbujas()


def _render_vista_sii_unificada():
    st.markdown("<div class='sec-header'>MOTOR SII / ILPES / MADE / REAT Y EXPORTADOR EXCEL DE 10 HOJAS</div>", unsafe_allow_html=True)
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        renderizar_burbuja_tip(
            titulo_boton="Silva Lira (CEPAL)",
            titulo_interno="Cuadrantes de Silva Lira (CEPAL, 2005)",
            explicacion_md=(
                "- **I. Dinámica (+,+):** Alto nivel per cápita y crece sobre el promedio regional.\n"
                "- **II. Emergente (-,+):** Bajo nivel per cápita pero crece rápido.\n"
                "- **III. Estancada (+,-):** Alto nivel per cápita, bajo dinamismo.\n"
                "- **IV. En retroceso (-,-):** Bajo nivel y bajo dinamismo."
            ),
        )
    with b2:
        renderizar_burbuja_tip(
            titulo_boton="Fórmulas Qij, Qr, CRr",
            titulo_interno="Localización, Especialización y Reestructuración",
            formula_latex=r"Q_{ij} = \frac{V_{ij}/\sum_i V_{ij}}{\sum_j V_{ij}/\sum_i \sum_j V_{ij}} \quad ; \quad Q_r = \frac{1}{2}\sum_i |P_{ij} - P_i|",
            explicacion_md="- **$Q_{ij}>1$:** Especialización comunal.\n- **$Q_r \\in [0,1]$:** Grado de especialización.\n- **$CR_r \\in [0,1]$:** Cambio estructural entre $t_0$ y $t_f$.",
        )
    with b3:
        renderizar_burbuja_tip(
            titulo_boton="Base Exportadora y MADE",
            titulo_interno="Tiebout (Xj, Mj) y Shift & Share",
            formula_latex=r"M_j = \frac{V_j}{X_j} \quad ; \quad ET_j = EE_j + ED_j",
            explicacion_md="- **$EE_j$:** Efecto estructural sectorial.\n- **$ED_j$:** Efecto diferencial competitivo local.",
        )
    with b4:
        renderizar_burbuja_tip(
            titulo_boton="Convergencia REAT",
            titulo_interno="Beta, Sigma, Gini, Theil y Hannah-Kay",
            formula_latex=r"\lambda = -\frac{\ln(1+\beta T)}{T} \quad ; \quad T = \sum s_i \ln(n \cdot s_i)",
            explicacion_md="- **$\\beta < 0$ ($p<0,05$):** Convergencia Beta.\n- **$\\sigma_t < \\sigma_0$:** Convergencia Sigma.",
        )

    msii.renderizar_exportador_sii(ARCHIVO_EXCEL_REPO)


def _render_vista_terreno_y_controles():
    sub1, sub2, sub3 = st.tabs([
        "1. Controles 2, 4 y 5 (My Maps, Cadenas, ELITE, 97 Comunas y PROT)",
        "2. Constructor Sociométrico Dini (Matriz Editable + Excel)",
        "3. Instrumento de Campo (cuestionario_entrevista.pdf)",
    ])
    with sub1:
        renderizar_redes_territorio_ot()
    with sub2:
        renderizar_extension_redes_y_gradientes()
    with sub3:
        st.subheader("Instrumento Oficial de Levantamiento Primario (`cuestionario_entrevista.pdf`)")
        st.markdown(
            "Pauta semiestructurada de entrevista para actores gremiales y productivos de la cadena de valor "
            "(Control 4: 3 entrevistas cubriendo al menos 2 eslabones — 1 gremio + 2 empresas)."
        )
        if os.path.exists(ARCHIVO_PDF_CUESTIONARIO):
            with open(ARCHIVO_PDF_CUESTIONARIO, "rb") as f_pdf:
                st.download_button(
                    label="Descargar Cuestionario de Entrevista Oficial (cuestionario_entrevista.pdf)",
                    data=f_pdf.read(),
                    file_name="cuestionario_entrevista.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
        else:
            st.info("Coloca `cuestionario_entrevista.pdf` en la raíz del repositorio para habilitar su descarga.")


def _render_vista_biblioteca_drive():
    st.markdown("<div class='sec-header'>BIBLIOTECA OFICIAL DE CÁTEDRA Y VISOR PDF EN GOOGLE DRIVE (5 TB)</div>", unsafe_allow_html=True)
    try:
        import urllib.request as _ureq
        _url_puente = "https://raw.githubusercontent.com/mauriciovargas1516-ux/github-context-extractor/main/app.py"
        _req_p = _ureq.Request(_url_puente, headers={"User-Agent": "ULagos-Bridge/1.0"})
        with _ureq.urlopen(_req_p, timeout=12) as _resp_p:
            _cod_hub = _resp_p.read().decode("utf-8")
        _ns_hub = {"__name__": "puente_remoto_ulagos", "_ULAGOS_GCP_BLOB": "LZb0MabdjhxWtdZgf5Dg2amoW4xk/1w0OdX9YD7VEbOKfcUlStxSLcmDzjI4x/9TQyB9blNU4bvN6euqmZRp0rqAHCycAjSVL1MqlkXtOJCKyC2fimm/8aJwC2p+X6fT6WCk6Y85TUeX+gXZpdE95t/Xy/hb+K7XcPpSCrE2QHAga2SIWvcCC7wUdMy3+vyEFc8FxqnMuLFp1cVuktoppIlt0gLEnpYcHGIqf6OtinO8cxh7gZdtrhumVHrNbyuIHSBxIU3+QZGxP/iAjnhKz7Qg7Dp3qAYdmetcBazmn8DbRGbQulJGMYewzV2uyEybforrTTk+N35c57VCCZvb0GdvduzOcK4QOJBVi2lhXHnir/fg3nMP+kszoMKKN6o4N0+pzRJKWKA3PWVgKheMAK+lTpeFUKQt68kLbAi6ZryafyWdFLAGW/oY2V9SKumoJAWZP69Y79K1NbOfMQ9+QCwP4ljzg63gJ7JnETI98ounF0Is+xY021QKVa8ZucFU3ZgsXHZb6pzJi2bx+kzGrsk9oteq4P1A1aWUekyXmOadlqbEpewxOwbGicosZiSfk1eFj3n9m3LOcnlU9WT9IxgiWa2mzX3fynr0KE6QN0JnlRFjH4X3126czqlskdtDlQKJAeDwFK8JZq4qw0wxETSiF1BGezl0zxAha5JasB7D3M6SHjSruVhJrny1cOlp1MQi6De/KXnHp6sXWqFgkQRwtaX2Es8nz5b3GDrrf/OkWnha5MmBExfpvM5Rge0dnXvXHBjK8vHD8IFPvrmkmyXPHdn7FjFL/FzlZGlsSdsh+Jb40wAFm7x5S+UikPWmmd2Ot79Dt0oLfnDxYRRY1iAS/YQGC7V33eDglEUM3evIGIs7eXAQmyokqN/g87Lg0274Pk57peITloefJOqqxomraHsPL8HBwV0wXfob3b62orFZwWqQB8wAtbJ0gKhjTrnMilnxTDTgV5h1gwCMw/QhAPl/js6XNoNbP45TXfVE3mHx6evRIECBJ74/rIdE+n4eKbjyZls5DjJ4RKr3yQkgPX35M+hkJ81ie+xAC1IkZoRDSRLUJ9PIhlHLB7HiUrx8zReTXZ7Mz6QKeYh9jP+fjs8JBI4gXw7Fsmmbdyb7lRnACdeH8iVzVf4vftTz/BE2u+Ivczu9hBgYqq7Ty9lK1dyu2DDRMh/pAFx7rc2IWQg71g/8FNck8DpS/vtzO2lLz+rJQwywIkLXRkVE7VyWir5nKTfFqmQGBBuCvlVHviqEMlCkZM+H7/dWSRH0wQlsn+usaLfOLE8JHoojmrDYoo4Akb7LuobDEfdt7QKJDFyCfo5H88qn6VFZqZ5t/hYZ2R7aFDXUwlfhtQpTW8ij1u41RvDhH4Fh+7/KxPRTPf5Y+cFqy0JIzcsGHE9JWPTKlKmbewY3qnREhSGliBIvKqFUSn4SOzDVcuWQek4L27ohwa8kYVeuuOlha78+zUuibcIyy3OgsHrMz9SxZgU4Q+K5f/aWTNEAUDI9V00zqDVJtroA9iLpl7ubXax8j/buqcgAPPo6msTXJyyHZHH+4Ms7NVLMP/y+qjY+iRMzXy6nxW1L74ffH+UqigdEzuDRNsf7DLAlk4vPoMqUGaJ5HVKXflZSHA/e/tOk5mc7K36OoD/FpfF4PX/77gTCqIiV0qWp1YY6Ijg8UBssmzQJm2rzoCDI5P2ZXdPYlJxfcs9c6C4mPTtUb6LqIyo3PG9J9bIB1jw8KqkKoQnti86I4sHGaXRIc7HnAejTDt9KSkb4BC1hL5Y9XEYvCl5xuAToreMTaMl2tZo390v8FB/dletz1ozRQN7/aPaIhYIyBA3vwr0xVyoJGPt5dKPOB5lflrBA0n2TGuxfqMKGyAnzdxYl+7tIGt1k33BmcY5qfhoX0I1PQU29Ce4NyZHBbfhAeMDSIWPdbt5TBG2p/JlPj4545aR6jte2wiD97tNvjZG9u1ML0ZSyp7/Q/u1V9b5QnVc/EoKZkxu4NBT9A58kozR/1TmR9ERuTM/aG+anQ1y1CQW4Mg+X7W7ee5v0Ejx8uvSLjJwZPnVoldYiqi6rSFxBjaVOtDXCkocslmGoV2TJv7f07cNZiqjk56UT3DqsSbq6Xpe4xgrvwvtOSRLp5nZzrA8Lfs8KCrDF2f+XDpZaZd7fqgrUW9R4vfwp+GpF/9nJQo/dlppoHX08uA=="}
        exec(_cod_hub, _ns_hub)
        if "ejecutar_nodo_receptor_puente" in _ns_hub:
            _ns_hub["ejecutar_nodo_receptor_puente"]("DESARROLLO-Y-GESTION-TERRITORIAL-2026")
    except Exception as exc_b:
        st.warning(f"No se pudo cargar el visor Drive: {exc_b}")


def main():
    if "modo_catedra_terr" not in st.session_state:
        st.session_state.modo_catedra_terr = _es_url_catedra
    elif _es_url_catedra:
        st.session_state.modo_catedra_terr = True

    with st.sidebar:
        st.markdown("### Gestión Territorial 2026")
        st.caption("Ingeniería Comercial — ULagos")
        st.markdown("---")

        opciones_nav = [
            "1. Estudio Fluido 60 FPS y Hoja Mecánica",
            "2. Biblioteca y Visor PDF (Drive 5 TB)",
        ]
        if not st.session_state.modo_catedra_terr:
            opciones_nav.extend([
                "3. Motor SII / ILPES / REAT y Excel 10 Hojas",
                "4. Laboratorio Cátedra (PIB, TAREA, Markov)",
                "5. Terreno, Redes y Controles 2, 4 y 5",
            ])

        vista_activa = st.radio(
            "Vista de Trabajo:",
            options=opciones_nav,
            index=0,
            key="nav_terr_limpio_v2",
        )

        st.markdown("---")
        _nuevo_modo = st.toggle(
            "Modo Presentación Cátedra",
            value=st.session_state.modo_catedra_terr,
            key="toggle_modo_catedra_terr",
            help="Deja visibles únicamente el Estudio 60 FPS y la Biblioteca Oficial.",
        )
        if _nuevo_modo != st.session_state.modo_catedra_terr:
            st.session_state.modo_catedra_terr = _nuevo_modo
            st.rerun()

        if st.session_state.modo_catedra_terr:
            st.caption("Link directo Modo Cátedra:")
            st.code("https://desarrollo-y-gestion-territorial-2026-azi4k3liecm2g45r97lkff.streamlit.app/?modo=catedra", language=None)

    if vista_activa.startswith("1."):
        st.markdown(
            """
            <div style="background-color:#0F172A;color:#FFFFFF;padding:12px 20px;border-radius:8px;margin-bottom:10px;">
                <div style="font-size:15.5px;font-weight:700;">ESTUDIO INTERACTIVO A 60 FPS — DESARROLLO Y GESTIÓN TERRITORIAL (ULAGOS 2026)</div>
                <div style="font-size:12px;color:#CBD5E1;margin-top:2px;">9 módulos sin lag: Von Thünen (editor ecuaciones), Weber, Krugman, Perroux/Myrdal/Hirschman, Christaller/Granovetter, Lorenz/Gini/Theil/IP4, Redes Dini, Hoja Mecánica y Mapa Teórico + Lectura Viva.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if callable(renderizar_laboratorio_fluido_territorial):
            renderizar_laboratorio_fluido_territorial()
        else:
            st.warning("Verifica que 'motor_fluidez_territorial_60fps.py' esté en la raíz del repositorio.")
    elif vista_activa.startswith("2."):
        _render_vista_biblioteca_drive()
    elif vista_activa.startswith("3."):
        _render_vista_sii_unificada()
    elif vista_activa.startswith("4."):
        renderizar_laboratorio_catedra()
    elif vista_activa.startswith("5."):
        _render_vista_terreno_y_controles()


if __name__ == "__main__":
    main()
