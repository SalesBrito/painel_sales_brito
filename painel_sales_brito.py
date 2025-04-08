import streamlit as st
from datetime import datetime
import pandas as pd
import calendar

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Painel @sales_brito", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #0D1117;
            color: #C9D1D9;
            font-family: monospace;
        }
        .stApp {
            background-color: #0D1117;
        }
        .logo-custom {
            font-size: 24px;
            color: #00FFAA;
            font-weight: bold;
            text-align: center;
        }
        .rodape {
            font-size: 12px;
            color: #999;
            text-align: center;
            margin-top: 20px;
        }
        .calendar-box {
            border: 1px solid #00FFAA;
            padding: 10px;
            border-radius: 10px;
            background-color: #161B22;
            margin-bottom: 20px;
        }
        .logo-img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80px;
            border-radius: 50%;
        }
    </style>
""", unsafe_allow_html=True)

# FUNÇÃO DE LOGIN
def login():
    st.title("🔐 Painel @sales_brito - Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username == "sales_brito" and password == "PMGO2025!":
            st.session_state["logado"] = True
        else:
            st.error("Usuário ou senha incorretos.")

# FUNÇÃO PRINCIPAL DO PAINEL
def painel():
    if st.button("Sair", key="logout"):
        st.session_state.clear()
        st.experimental_rerun()

    st.image("https://avatars.githubusercontent.com/u/139248535?v=4", use_column_width=False, width=100, caption="@sales_brito")

    st.markdown("""
        <div class='logo-custom'>👨‍💻 Painel Pessoal - @sales_brito</div>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "📚 Estudos (PMGO)", "💰 Investimentos", "🔐 Senhas", "📷 Fotos",
        "📝 Anotações", "✅ Tarefas", "🌦️ Clima", "📎 Atalhos",
        "🏦 Contas Bancárias", "📤 Uploads", "🗂️ Arquivos",
        "💼 Currículo e Portfólio"
    ])

    # 1 - ESTUDOS
    with tabs[0]:
        st.subheader("📚 Cronograma de Estudos - PMGO")

        if "cronograma_df" not in st.session_state:
            st.session_state.cronograma_df = pd.DataFrame({
                "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
                "Matéria": ["Português", "Legislação", "Informática", "Direitos Humanos", "Redação", "RLM", "Revisão"],
                "Tempo (h)": [2, 2, 2, 2, 1.5, 1.5, 2]
            })

        st.data_editor(st.session_state.cronograma_df, use_container_width=True, num_rows="dynamic")

        st.markdown("### 📊 Planilha de Questões (editável)")
        if "questoes_df" not in st.session_state:
            st.session_state.questoes_df = pd.DataFrame({
                "Matéria": ["Português", "Legislação", "Informática", "Direitos Humanos"],
                "Resolvidas": [30, 20, 15, 10],
                "Acertos": [25, 18, 12, 8],
                "% Acerto": [83, 90, 80, 80]
            })
        st.data_editor(st.session_state.questoes_df, use_container_width=True, num_rows="dynamic")

    # 2 - INVESTIMENTOS
    with tabs[1]:
        st.subheader("💰 Plano de Investimento com R$100/mês")
        st.markdown("""
        ### 📈 Estratégia de Investimento Inicial
        - **Meta**: Crescer patrimônio com aportes mensais de R$100
        - **Perfil**: Iniciante/Moderado

        ### 💸 Alocação Mensal (Exemplo Atualizado):
        - **R$ 40** – Tesouro Direto IPCA+ (longo prazo, proteção inflação)
        - **R$ 30** – Fundo de ações (ex: Itaú Ações Consumo ou Trend Ações)
        - **R$ 20** – Renda fixa de liquidez diária (Reserva de Emergência - Nubank, PicPay)
        - **R$ 10** – Criptomoedas (via PIX no Mercado Bitcoin ou Binance)

        ### 🎯 Meta final: Comprar moto à vista com R$10.000
        """)

        if "investimentos_df" not in st.session_state:
            st.session_state.investimentos_df = pd.DataFrame({
                "Mês": ["Abril", "Maio", "Junho"],
                "Tesouro IPCA": [40, 40, 40],
                "Ações": [30, 30, 30],
                "Renda Fixa": [20, 20, 20],
                "Criptos": [10, 10, 10]
            })

        st.data_editor(st.session_state.investimentos_df, use_container_width=True, num_rows="dynamic")

    # 3 - SENHAS
    with tabs[2]:
        st.subheader("🔐 Cofre de Senhas Seguras")
        if "senhas_df" not in st.session_state:
            st.session_state.senhas_df = pd.DataFrame({
                "Categoria": ["E-mail", "Banco", "Instagram", "Cofre"],
                "Serviço": ["Gmail", "Caixa", "@salesbrito_", "Cofre Principal"],
                "Usuário": ["salesbrito080@gmail.com", "123456-7", "salesbrito_", "admin"],
                "Senha": ["minhaSenha123", "bancoSenha456", "instaSenha789", "senhaCofre@2025"]
            })

        st.data_editor(st.session_state.senhas_df, use_container_width=True, num_rows="dynamic")

    # 6 - TAREFAS
    with tabs[5]:
        st.subheader("✅ Tarefas e Atividades")

        if "tarefas_df" not in st.session_state:
            st.session_state.tarefas_df = pd.DataFrame({
                "Data": ["2025-04-08", "2025-04-12"],
                "Atividade": ["Revisar Direito Penal", "Exercício físico semanal"],
                "Status": ["Pendente", "Pendente"]
            })

        st.data_editor(st.session_state.tarefas_df, use_container_width=True, num_rows="dynamic")

    # 9 - CONTAS BANCÁRIAS
    with tabs[8]:
        st.subheader("🏦 Minhas Contas Bancárias")

        if "contas_df" not in st.session_state:
            st.session_state.contas_df = pd.DataFrame({
                "Banco": ["Nubank", "Caixa", "Banco do Brasil"],
                "Agência": ["0001", "1234", "5678"],
                "Conta": ["123456-7", "987654-3", "112233-4"],
                "Tipo": ["Conta Corrente", "Poupança", "Conta Corrente"],
                "Saldo Atual (R$)": [1000.00, 250.00, 500.00]
            })

        st.data_editor(st.session_state.contas_df, use_container_width=True, num_rows="dynamic")

    # 12 - CURRÍCULO E PORTFÓLIO
    with tabs[11]:
        st.subheader("💼 Currículo e Portfólio Profissional")

        st.markdown("### 📄 Currículo em PDF")
        st.markdown("- [Visualizar Currículo Profissional](https://drive.google.com/file/d/1WTQZ5KnQ8LUnv38OaS0lwONMHR7dV_GM/view?usp=sharing)")

        st.markdown("### 🌐 Portfólio Online")
        st.markdown("- [Portfólio - Visual Hacker/Tech](https://salesbrito.vercel.app)")

        st.markdown("### 📦 Projetos e Repositórios")
        st.markdown("- [GitHub: @salesbrito](https://github.com/salesbrito)")
        st.markdown("- [Joguinhos Hacker (brincadeira)](https://joguinhosales.netlify.app)")

        st.markdown("### 📝 Informações Profissionais")
        st.markdown("""
        - 👨‍🎓 **Formação:** Tecnologia da Informação (Estácio - 2025)
        - 🛡️ **Experiência:** Vigilante, Segurança de Eventos/Shopping, Frentista
        - 💡 **Habilidades:** Python, Suporte Técnico, Monitoramento, Excel Avançado
        - 🎯 **Meta Profissional:** Unir TI e Segurança | Aprovado na PMGO
        """)

    # RODAPÉ
    st.markdown("""
        <div class='rodape'>
        © 2025 Marcos Vinicius Sales de Brito | Painel @sales_brito<br>
        Desenvolvido com ❤ por @sales_brito | Estilo Hacker | Meta: Comprar moto à vista!
        </div>
    """, unsafe_allow_html=True)

# EXECUÇÃO DO APLICATIVO
if "logado" not in st.session_state:
    login()
else:
    painel()