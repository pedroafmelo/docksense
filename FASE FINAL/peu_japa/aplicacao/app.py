import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title = "DOCKSENSE",
    page_icon = "📊",
    layout = "wide"
)


c1, c2, c3 = st.columns([2, 1, 1])
col1, col2, col3 = c3.columns(3)

c1.title("People Analytics")
c3.image("/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/logodock.png",
         width = 200)
st.markdown("<h6 style= 'text-align: left; color: grey;'>Collaborator's feelings by DockSense</h6>",
            unsafe_allow_html= True)
st.markdown("<hr style= 'height: 2px; border: none; color: black; background-color: black;' />",
            unsafe_allow_html= True)

def main():
    menu()


@st.cache_data
def read_data(url):
    dados_lidos = pd.read_excel(url)
    return dados_lidos


def menu():
    selector = option_menu(
        menu_title = "",
        options = ["Home", "Data"],
        default_index = 0,
        icons = ["house", "database"],
        orientation = "horizontal",
        styles = {
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#08D8D8"},
        }
    )
    if selector == "Home":
        ...
    elif selector == "Data":
        st.write("#")
        filters()
        
     

def filters():
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
        ):  
    
        st.markdown("""<h5 style= 'text-align: center; color: grey;'
                    >Dados extraídos da plataforma Glassdoor</h5>""", unsafe_allow_html= True)
        
    c1, c2, c3 = st.columns([1, 2, 2])
    col1, col2, col3 = c3.columns(3)
    
    # Seletor de ordenamento do dataframe
    c1.write("#")
    select = c1.selectbox("Ordenamento", 
                                ["Data de inclusão (Mais recente)", "Data de inclusão (Mais antigo)", "Mais popular"],
                                index = 0)
    c2.write("#")

    # Seletor de filtro por classificacao
    multiselect = c2.multiselect("Filtro por classificação", [5, 4, 3, 2, 1], placeholder= "Escolha os filtros")
    st.write("##")

    if select == "Data de inclusão (Mais antigo)":
        dados = read_data("/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_oldest.xlsx")
        if multiselect:
            dados = dados[dados['CLASSIFICACAO'].isin(multiselect)]
            st.dataframe(dados, hide_index = True)
            col3.write("#")
            col3.download_button("Exportar arquivo",
                                "/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_oldest.xlsx",
                                file_name= "glassdoor_inclusão_antiga.xlsx")
        else:
            st.dataframe(dados, hide_index = True)
            col3.write("#")
            col3.download_button("Exportar arquivo",
                                "/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_oldest.xlsx",
                                file_name= "glassdoor_inclusão_antiga.xlsx")
    
    elif select == "Data de inclusão (Mais recente)":
        dados = read_data("/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_newest.xlsx")
        if multiselect:
            dados = dados[dados['CLASSIFICACAO'].isin(multiselect)]
            st.dataframe(dados, hide_index = True)
            col3.write("#")
            col3.download_button("Exportar arquivo",
                                "/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_newest.xlsx",
                                file_name= "glassdoor_inclusão_recente.xlsx")
        else:
            st.dataframe(dados, hide_index = True)
            col3.write("#")
            col3.download_button("Exportar arquivo",
                                "/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_newest.xlsx",
                                file_name = "glassdoor_inclusão_recente.xlsx")
        
    elif select == "Mais popular":
        dados = read_data("/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_pop.xlsx")
        if multiselect:
            dados = dados[dados['CLASSIFICACAO'].isin(multiselect)]
            st.dataframe(dados, hide_index = True)
            col3.write("#")
            col3.download_button("Exportar arquivo",
                                "/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_pop.xlsx",
                                file_name= "glassdoor_popularidade.xlsx")
        else:
            st.dataframe(dados, hide_index = True)
            col3.write("#")
            col3.download_button("Exportar arquivo",
                                "/Users/pedroafmelo/Documents/projetos/docksense/FASE FINAL/peu_japa/data/dataset_pop.xlsx",
                                file_name = "glassdoor_popularidade.xlsx")
        




if __name__ == "__main__":
    main()