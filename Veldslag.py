import streamlit as st
import random

# --- Veldslaggegevens ---
vragen = [
    {"coord": "A1", "vraag": "Welke fabelachtige draak heeft meerdere hoofden?", "antwoord": "Hydra"},
    {"coord": "B2", "vraag": "Wat droeg een ridderes tijdens een magisch duel?", "antwoord": "Spreukmantel"},
    {"coord": "C3", "vraag": "Hoeveel poten heeft een kip?", "antwoord": "2"},
    {"coord": "D4", "vraag": "Wat kraait 's ochtends en denkt dat hij de zon oproept?", "antwoord": "Haan"},
]

geraakt_vakken = ["A1", "C3"]
bezochte_vakken = set()

# --- Streamlit UI ---
st.title("🐔 Veldslag der Chickkies – Het Jaar des Hoenders")

vak = st.text_input("📍 Voer een veld in (bijv. B2):").upper().strip()

if vak:
    vraag_data = next((v for v in vragen if v["coord"] == vak), None)
    if vraag_data:
        if vak in bezochte_vakken:
            st.warning("⚠️ Dit veld heb je al bezocht!")
        else:
            st.write("📜 Vraag:")
            st.write(vraag_data["vraag"])
            antwoord = st.text_input("Jouw antwoord:", key=vak)
            if antwoord:
                if antwoord.strip().lower() == vraag_data["antwoord"].lower():
                    st.success("✅ Correct!")
                    if vak in geraakt_vakken:
                        st.success("🔥 Geraakt! Je hebt een troep geraakt!")
                        st.info("Hint: De kroon is ten westen van kolom G...")
                    else:
                        st.info("❌ Maar hier stond niemand...")
                    bezochte_vakken.add(vak)
                else:
                    st.error("❌ Onjuist antwoord.")
    else:
        st.error("⛔ Onbekend vak of hier ligt niets verborgen.")
