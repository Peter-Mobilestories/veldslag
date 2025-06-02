import streamlit as st
import random

# --- Pagina-instellingen ---
st.set_page_config(page_title="De Slag om Slot Haneburg", page_icon="🏰")

# --- Middeleeuwse styling met CSS ---
st.markdown("""
    <style>
    /* Achtergrondkleur (perkamentachtig) */
    .stApp {
        background-color: #f8f1da;
        color: #3e2d1c;
    }

    /* Middeleeuws lettertype */
    @import url('https://fonts.googleapis.com/css2?family=IM+Fell+English&display=swap');

    html, body, [class*="css"] {
        font-family: 'IM Fell English', serif;
    }

    /* Titel opmaak */
    h1 {
        text-align: center;
        font-size: 3em;
        color: #4a2e0f;
        text-shadow: 1px 1px #d2b48c;
        margin-bottom: 0.5em;
    }

    /* Vraagbox styling */
    .vraagbox {
        background-color: rgba(255, 255, 255, 0.75);
        padding: 1.2em;
        border-radius: 10px;
        border: 2px solid #5b3c1e;
        box-shadow: 4px 4px 12px rgba(0,0,0,0.2);
    }

    /* Hintbox styling */
    .hintbox {
        background-color: #f2e4ca;
        padding: 0.7em;
        border-left: 5px solid #9c6d3c;
        margin-top: 1em;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# --- Titel & inleiding ---
st.title("🏰 De Slag om Slot Haneburg")

st.markdown("""
In het **Jaar des Hoenders 1284** trekken de edele Chickkies ten strijde tegen de duistere machten van Drakenrust. 
Verken het slagveld, beantwoord raadselachtige vragen, en ontdek waar de kroon verborgen ligt...  
""")

# --- Vragen en logica ---
vragen = [
    {"coord": "A1", "vraag": "Welke fabelachtige draak heeft meerdere hoofden?", "antwoord": "Hydra"},
    {"coord": "B2", "vraag": "Wat droeg een ridderes tijdens een magisch duel?", "antwoord": "Spreukmantel"},
    {"coord": "C3", "vraag": "Hoeveel poten heeft een kip?", "antwoord": "2"},
    {"coord": "D4", "vraag": "Wat kraait 's ochtends en denkt dat hij de zon oproept?", "antwoord": "Haan"},
    {"coord": "E5", "vraag": "Hoe noemt men het zwaard van een edele krijgster?", "antwoord": "Lichtbrenger"},
]

geraakt_vakken = ["A1", "C3", "E5"]
bezochte_vakken = []

# --- Interactieveld ---
st.markdown("### 🔍 Kies uw veld, edele zuster:")
vak = st.text_input("📍 Voer een veld in (bijv. B2):").upper().strip()

if vak:
    vraag_data = next((v for v in vragen if v["coord"] == vak), None)
    if vraag_data:
        if vak in bezochte_vakken:
            st.warning("⚠️ Dit veld werd reeds onderzocht, waarde krijgster.")
        else:
            with st.container():
                st.markdown(f"<div class='vraagbox'><b>📜 Vraag:</b><br>{vraag_data['vraag']}</div>", unsafe_allow_html=True)
                antwoord = st.text_input("✒️ Uw antwoord:", key=vak)
                if antwoord:
                    if antwoord.strip().lower() == vraag_data["antwoord"].lower():
                        st.success("✅ Juist beantwoord, wijze zuster!")
                        if vak in geraakt_vakken:
                            st.markdown("<div class='hintbox'>🔥 Geraakt! Een vijandelijke eenheid werd verslagen!</div>", unsafe_allow_html=True)
                            st.markdown("<div class='hintbox'>🧭 Hint: Men fluistert dat de kroon zich westelijk van rij F bevindt…</div>", unsafe_allow_html=True)
                        else:
                            st.info("📜 Geen vijand hier, slechts kippenveren en modder...")
                        bezochte_vakken.append(vak)
                    else:
                        st.error("❌ Helaas, dat is niet wat de oude kronieken vermelden.")
    else:
        st.error("⛔ Dit veld komt niet voor in de kronieken van Haneburg.")
