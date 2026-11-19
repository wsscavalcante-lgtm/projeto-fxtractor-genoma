import streamlit as st

# Configuração básica da aba do navegador
st.set_page_config(
    page_title="Projeto FxTractor",
    page_icon="🧬",
    layout="wide",
)

# ==========================================
# TOPO DA PÁGINA (APRESENTAÇÃO)
# ==========================================
st.title("🧬 Predição Genômica de Tolerância Ambiental em Procariotos")
st.caption(
    "Disciplina: Inteligência Artificial, Ciência de Dados e Agricultura de Precisão"
)

# Imagem de destaque (usando a URL da Pexels como sugerido, e use_container_width) 

st.image("https://lh3.googleusercontent.com/rd-gg-dl/AHiVA1l21S165vILBcepkZ7zRdNNIbeSKlInxZc3tFes9Tsa3SP_ER5nGTRpYhOVZLhvIy7iIpf-q6LShJB_mwGsQoBhvu4__jCmvBdzQW0w9-AEwtGug3xM5TAog-um8eDC3G-x7vRDhZAnL0vIFWazFZvwA-zS5ZTzRygKJfpvA7nUki-5wdXdXPq570y4jYGy1afwfmM6T9H2LshB02cRigW60lRr2DhzYyOSwTa3eiBPW0nuauDDzdNX-nZtttIhtgSGJzHkImw8uN_rawB5zPY4Ac_6lSlx3qLdXdzXWHGLEf9ahyyLgawwBC7UEgWgSZC0VPUHKi46D0C-KY3F0GfNXPX3HS0gP6HFqwzcEAZJS4b-y8oQEqfzoLYqG0X8ZPFVg1C5WS4WPsh5O2cyaGQzlBwMs-h1PwAY8JNZzYuEZBFEKgVhJC67gseoPjQ5QbP1GFFk-JBffemVMK6d27BV1rKY0q807a2GZ6IIh2-uDBy371TV_ZTfv8EGyBT1PLjDncHpRyKMgDDMswgv392P5xJOxPNFRWN6wCFfCYMT9o2ZeASC-gfharzn34ZWBd4nJo5tNWx5pqmt_ovubKSGXYx3yIP1FW85R6ayT0yDobZuvf_nPsxGKNaoLc3TZr0YN-yGM5SY6txvaVppVwL85mqNc20fHunvF0_N6wRVCuhQldcpEUdCvfQDFKGDZU9UZbqwcP-4X9ccBmh4hWyCfgOY6FeANwTtPPFdtgB-xCHU0LHY8bBophG-mQ4qiAVxUvixDGzlSF-9iJWHy7YR-bfHOg69ik8dSyp31ugsM7SFfMDfC7EloyFhad9VXhQYiEAMh7z-PArgKMYlPR4HRKu_mJSI7ZqMLpot4htTaBCrwFA-Bl9MK7xw9Gbzc0PjhH57tLfO1xj1NnZts_vEMOkhIwvspphJCSRoM1fbNMdjvrWhgf7m_pwW5bRuf5hNpeG-iZgovb30UErqeRSfu_t3nDkhj8f9qUImBKhb3oT6jfaPu9RR0tTEWtb4AXJ812pKDQyWXbiE4GyCu1ZSei4NbHnHwDOk2skpt6QCyKNg9pVVpCeanW0S1iNBpoDAB_1sM69Gi6IyZmxM46QKyTVFTESbQW1JrGpMmc3yv2QmZd3GMYS5usGKDDgcee_o8CeXOK3xqZRFopAA_drj2gmcrCLUKufTM0yF2sq3VeuAEh064OIRvQucPjW009GuJDSIVQhwMJ12ff2kTV4D6FD3-5bvFy7Y1EnENGDCXWm8ozCqExxLiCBz07KIa0uYDoAOWk6NGBM4qEaZuoSLYdgs70cp6QSuTvY2cIgCBmI=s1024-rw",

        caption="Representação conceitual da predição genômica de tolerância ambiental em procariotos aplicados à soja. Crédito: Imagem gerada por Inteligência Artificial (Google Gemini), 2026.", 
        width='content')



st.info(
    "**Resumo do Projeto:** Uso de aprendizado de máquina sobre características genômicas de "
    "13.554 procariotos para predizer preferências de salinidade, temperatura, oxigênio e pH — "
    "acelerando a descoberta de bioinsumos para soja, solos salinizados e regiões de clima extremo."
)

# Números principais em 4 colunas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Genomas analisados", "13.554", "Bactérias e arqueias")
col2.metric("Variáveis genômicas", "~152.343", "COGs, ncRNAs, k-mers, AA")
col3.metric("Condições avaliadas", "4", "Sal, Temp., pH e O₂")
col4.metric("Banco de fenótipos", "BacDive", "Dados públicos")

st.divider()

# ==========================================
# CONTEÚDO ORGANIZADO EM ABAS
# ==========================================
aba1, aba2, aba3, aba4 = st.tabs([
    "🌱 Problema e Lacuna",
    "🧪 Dados e Genômica",
    "🤖 IA e Validação",
    "📋 Hipóteses e Equipe",
])

# --- ABA 1: PROBLEMA E LACUNA ---
with aba1:
    st.subheader("Por que esta pesquisa é necessária?")
    st.write(
        "Definir as condições em que uma bactéria sobrevive depende hoje de ensaios de cultivo "
        "lentos, caros e de baixo rendimento. Isso atrasa o desenvolvimento de inoculantes para a soja "
        "frente ao aquecimento global, seca e solos de clima extremo."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.warning(
            "**Calor (45 °C)**\n\n"
            "Foram triados 73 isolados para encontrar apenas 1 linhagem tolerante a 45 °C, "
            "que elevou a parte aérea da soja em 17,8% (Shaffique et al., 2024)."
        )
    with c2:
        st.warning(
            "**Frio (4 °C a 15 °C)**\n\n"
            "De 454 rizóbios avaliados, só 33 cresceram a 4 °C (Yuan et al., 2020). Em outro estudo, "
            "foram 5 ciclos de 7 dias para isolar bactérias que elevaram a produtividade em 21,94% (Yan et al., 2025)."
        )
    with c3:
        st.warning(
            "**Calor + Seca**\n\n"
            "A coinoculação de rizóbios e endófitos adaptados aumentou em 36,2% a massa de grãos "
            "por planta sob estresse térmico e hídrico (Shevchuk et al., 2025)."
        )

    st.subheader("Qual é a lacuna científica?")
    st.success(
        "Estudos agronômicos ainda se limitam ao gene 16S rRNA, e modelos computacionais anteriores "
        "quase não exploraram os **RNAs não codificantes (ncRNAs)**. O FxTractor usa o genoma completo "
        "para prever a tolerância ambiental **antes mesmo de levar o isolado à placa de Petri**."
    )

# --- ABA 2: DADOS E GENÔMICA ---
with aba2:
    st.subheader("As 4 camadas genômicas extraídas")
    st.write(
        "Os genomas completos (NCBI, BV-BRC e IMG) são filtrados com CheckM (completude > 90% e "
        "contaminação ≤ 5%) e cruzados com os registros de cultivo do BacDive."
    )

    tabela_camadas = [
        {"Camada": "COGs (eggNOG)", "Variáveis": "20.141", "Função biológica": "Transportadores, chaperonas e enzimas"},
        {"Camada": "ncRNAs (Rfam)", "Variáveis": "1.110", "Função biológica": "Regulação rápida sob estresse (ex.: SRP, anti-hemB)"},
        {"Camada": "k-mers (k=9)", "Variáveis": "131.072", "Função biológica": "Assinatura de composição do DNA"},
        {"Camada": "Aminoácidos", "Variáveis": "20", "Função biológica": "Estabilidade e solubilidade das proteínas"},
    ]
    st.table(tabela_camadas)

    st.subheader("Simulador simples: o que escolher na prática?")
    escolha = st.radio(
        "Qual é o foco da aplicação?",
        ["Prever rápido com baixo custo computacional", "Explicar o mecanismo genético da tolerância"],
    )

    if escolha == "Prever rápido com baixo custo computacional":
        st.info(
            "**Recomendação:** Usar a frequência dos **20 aminoácidos** (ou **k-mers**) com um "
            "**modelo linear simples**. Exige poucos MB de memória e entrega alto poder preditivo."
        )
    else:
        st.info(
            "**Recomendação:** Usar **COGs** e **ncRNAs** com **modelo linear + SHAP**. "
            "Exige mais memória (~26 GB para COGs), mas mostra exatamente quais genes explicam a adaptação."
        )

# --- ABA 3: IA E VALIDAÇÃO ---
with aba3:
    st.subheader("Estratégia de Machine Learning")
    st.write(
        "Como o número de variáveis é muito maior que o de amostras (p ≫ n), o pipeline aplica "
        "filtro de variância, agrupamento por correlação de Spearman e eliminação recursiva (RFE)."
    )

    tabela_modelos = [
        {"Modelo": "Regressão Linear / Logística", "Destaque": "Rápido e fácil de interpretar biologicamente"},
        {"Modelo": "SVM (Linear, Polinomial, RBF)", "Destaque": "Excelente desempenho com muitas variáveis"},
        {"Modelo": "Random Forest", "Destaque": "Captura interações não lineares entre variáveis"},
        {"Modelo": "k-NN", "Destaque": "Baseado em similaridade (atenção ao parentesco filogenético)"},
    ]
    st.table(tabela_modelos)

    st.subheader("Como evitamos erros e garantimos confiança?")
    st.markdown(
        """
        - **Prevenção de *Data Leakage*:** A divisão entre treino e teste é feita por **taxonomia**
          (gênero/família) e não de forma aleatória, evitando que o modelo apenas "decore" parentesco evolutivo.
        - **Métricas agronômicas:** **F1-score** na classificação e **RMSE + R²** na regressão
          (erro na unidade real, como ±2 °C ou ±0,5% de NaCl).
        - **Explicabilidade (SHAP):** Mostra quais genes e ncRNAs aumentam ou reduzem a tolerância.
        - **Validação externa:** Teste final em um isolado inédito fora do treino (*Limnochorda* sp. EGM147).
        """
    )

# --- ABA 4: HIPÓTESES, EQUIPE E CONTATO ---
with aba4:
    st.subheader("Pré-registro Científico")
    col_h1, col_h0 = st.columns(2)
    with col_h1:
        st.success(
            "**Resultados Esperados (H₁)**\n\n"
            "Modelos com desempenho superior a preditores triviais e variáveis prioritárias no SHAP "
            "ligadas a mecanismos reais (chaperonas, solutos compatíveis como betaína e ncRNAs reguladores)."
        )
    with col_h0:
        st.error(
            "**Critério de Refutação (H₀)**\n\n"
            "A hipótese não será sustentada se o F1 ficar próximo de 0,50, o R² próximo de 0, "
            "ou se as variáveis mais importantes forem apenas ruído sem relação biológica."
        )

    st.divider()
    st.subheader("Equipe Responsável")
    st.write(
        "- **Carlos Antonio da Silva Santos**\n"
        "- **Leonardo Quirino de Oliveira**\n"
        "- **Wendson Soares da Silva Cavalcante**"
    )

    with st.expander("📚 Ver referências principais"):
        st.write(
            "1. Shaffique et al. (2024) — *BMC Plant Biology*\n"
            "2. Shevchuk et al. (2025) — *Microbiological Journal*\n"
            "3. Walter Costa et al. ([2025]) — Manuscrito (FxTractor)\n"
            "4. Yan et al. (2025) — *Agronomy*\n"
            "5. Yuan et al. (2020) — *Microbes and Environments*"
        )