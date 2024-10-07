import streamlit as st

st.set_page_config(page_title="Der kleine Energierechner", layout="wide",
                   page_icon=":material/energy_savings_leaf:")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title(":material/energy_savings_leaf: Der kleine Energierechner")
st.write("Dieses Tool hilft dir eventuell dabei, Energiemengen aus deinem Alltag in Relation zu setzen.")


st.markdown(""
            "")
st.header("Zunächst ein paar Fragen:")
backofen = st.slider("Wie oft hast du in der letzten Woche den Backofen genutzt?", 1, 10, 3)
st.slider("")

