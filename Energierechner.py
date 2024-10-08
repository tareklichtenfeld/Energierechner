import streamlit as st

st.set_page_config(page_title="Der kleine Energierechner", layout="wide",
                   page_icon=":material/energy_savings_leaf:",
                   initial_sidebar_state='collapsed')

hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: visible;}
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title(":material/energy_savings_leaf: Der kleine Energierechner")
st.write("Was, KI verbraucht auch Strom? Aber wie viel denn?")


st.markdown(""
            "")
st.header("Zunächst ein paar Fragen an dich:")
ai_usage = st.slider("Wie oft nutzt du ChatGPT oder eine andere KI pro Woche, um dir Fragen beantworten zu lassen?", 1, 20, 3)
ai_questions = st.slider("Wie viele Anfragen schickst du dabei ungefähr im Schnitt?",1,10,2)

ai_weekly=ai_usage*ai_questions
ai_yearly=ai_usage*ai_questions*52
ai_energy_consumption = ai_usage*ai_questions*0.006
yearly_consumption=ai_energy_consumption*52
e_scooter_drives=yearly_consumption/0.68
zuckerverbrauch=yearly_consumption/4.5
kaffeeverbrauch=ai_energy_consumption/0.03
handyladungen=ai_energy_consumption/0.0185

st.header(f"Um mal in Relation zu setzen, wie viel Energie deine {ai_weekly} Anfragen pro Woche benötigen, hier ein paar kurze Vergleiche:")
with st.expander("In Kaffeetassen"):
    st.write(f"Das sind ganze {int(round(kaffeeverbrauch,0))} heiße Tassen Kaffee pro Woche, die du mit der Energie zubereiten könntest. ")
with st.expander("In Handyladungen"):
    st.write(f"Du hättest dein Handy mit der dafür benötigten Energie {int(round(handyladungen,0))} mal laden können - alleine in dieser Woche.")
with st.expander("In E-Scooter-Fahrten nach Steinfurt"):
    st.write(f"Wow, wenn du damit so weitermachst, hättest du für den gleichen Strombedarf stattdessen in diesem Jahr auch {int(round(e_scooter_drives,0))} mal mit dem E-Scooter von Münster in die Bereichsbibliothekt Steinfurt und zurück fahren können, um dir dort die Fragen aus Büchern zu beantworten.")
with st.expander("Läufst du lieber?"):
    st.write(f"Statt so ein Sprachmodell zu fragen hättest du übers Jahr verteilt auch {round(zuckerverbrauch,2)} kg Zucker essen können, die enthalten nämlich so viel Energie wie für deine {ai_yearly} Anfragen benötigt wird, und pushen dich sicher ein paar mal beim Longrun zur Bib in Steinfurt, wo du dann selbst recherchieren kannst.")
    st.write("Aber wahrscheinlich hast du das sowieso gemacht :D")
st.markdown(""
            "")
with st.popover("Was bedeutet das jetzt?"):
    st.write("Der Betrieb der Rechenzentren für Large Language Models hat einen enormen Strombedarf. Solange der Strom dafür nicht nur aus erneuerbaren Energiequellen stammt, trägt die Nutzung von KI-Tools zur Verstärkung des Treibhauseffekts durch den damit verbundenen CO2-Ausstoß bei.")



with st.sidebar.expander("Quellen"):
    st.link_button("Energieverbrauch von LLMs","https://www.scinexx.de/news/technik/wie-viel-strom-braucht-der-ki-boom/")
    st.link_button("Entwicklung im Energieverbrauch","https://www.tagesschau.de/wirtschaft/digitales/ki-energie-strom-verbrauch-klimaschutz-100.html")
with st.sidebar.expander("Annahmen"):
    st.write(":material/storage: Energieverbrauch von LLMs: 6 Wh/Anfrage")
    st.write(":material/phone_iphone: Kapazität eines Handyakkus: 5000 mAh bei 3.7 V")
    st.write(":material/nutrition: Energiegehalt von Zucker: 4.5 kWh/kg")
    st.write(":material/local_cafe: Energiebedarf der Zubereitung von Kaffee: 0.03 kWh/Tasse")