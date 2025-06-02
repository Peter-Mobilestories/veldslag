import streamlit as st
import time

st.set_page_config(page_title="De Slag om Slot Haneburg", page_icon="🏰")

if 'gevonden_vakken' not in st.session_state:
    st.session_state.gevonden_vakken = []
if 'gevonden_troepen' not in st.session_state:
    st.session_state.gevonden_troepen = []
if 'gegeven_adressen' not in st.session_state:
    st.session_state.gegeven_adressen = []
if 'wacht_tot' not in st.session_state:
    st.session_state.wacht_tot = 0

formatie = [
    ['E3', 'E4', 'E5', 'E6'],
    ['F1', 'F2'],
    ['B5', 'B6'],
    ['A3', 'B3', 'C3']
]

adressen = [
    ("Esso het Anker", "A2, 6121 PE Born"),
    ("Tankpool 24", "Eijsden Knuvelkes, 6245 LZ Eijsden"),
    ("E40 Aire de Tignee Sud", "4632 Soumagne, België"),
    ("Rue du Parc 2", "4950 Waimes, België")
]

vraag_data = {
    "A1": {"type": "opdracht", "tekst": "Maak een katapult van elastiek en lepels en schiet een marshmallow.", "codewoord": "kelk"},
    "A2": {"type": "vraag", "tekst": "Wat was de taak van een hofnar?\nA) De koning verdedigen\nB) Grappen maken en de koning vermaken\nC) Het kasteel schoonmaken", "antwoord": "B"},
    "A3": {"type": "opdracht", "tekst": "Vorm samen een menselijk schild.", "codewoord": "rondetafel"},
    "A4": {"type": "opdracht", "tekst": "Verzin een monster dat jullie onderweg tegenkomen en beschrijf hoe jullie het verslaan.", "codewoord": "Draak"},
    "A5": {"type": "opdracht", "tekst": "Spreek 1 minuut als een dronken nar.", "codewoord": "Jeanne"},
    "A6": {"type": "opdracht", "tekst": "Doe een zwaardgevecht met onzichtbare wapens in slow motion.", "codewoord": "Prinseserwt"},
    "B1": {"type": "vraag", "tekst": "Wat was de functie van een donjon in een kasteel?\nA) Wijnkelder\nB) Hoofdtoren/verdediging\nC) Feestzaal", "antwoord": "B"},
    "B2": {"type": "opdracht", "tekst": "Maak een vlag voor jouw team.", "codewoord": "Joris"},
    "B3": {"type": "vraag", "tekst": "Wat droeg een ridder als bescherming (6 letters)?", "antwoord": "harnas"},
    "B4": {"type": "opdracht", "tekst": "Als jij koning(in) was, wat zou je eerste wet zijn? Deze wet moet je team het hele weekend volgen.", "codewoord": "hofnar"},
    "B5": {"type": "consequentie", "tekst": "Je loopt in een hinderlaag van de tegenpartij.", "wacht": 120},
    "B6": {"type": "opdracht", "tekst": "Voer een middeleeuwse ridderceremonie uit en sla iemand tot ridder met een tak.", "codewoord": "hekserij"},
    "C1": {"type": "vraag", "tekst": "Wat is een banier?\nA) Een paard\nB) Een strijdkreet\nC) Een vlag met een symbool van een ridder of familie", "antwoord": "C"},
    "C2": {"type": "opdracht", "tekst": "Vertel in 20 seconden het verhaal van je eerste drakengevecht.", "codewoord": ""},
    "C3": {"type": "consequentie", "tekst": "De rivier is te diep – je loopt 2 minuten vertraging op.", "wacht": 120},
    "C4": {"type": "opdracht", "tekst": "Voer een zwaardgevecht met dropveters in slow motion.", "codewoord": "slot"},
    "C5": {"type": "consequentie", "tekst": "Je leger verdwaalt in het moeras – je mag 3 minuten geen nieuwe locatie aanvallen.", "wacht": 180},
    "C6": {"type": "opdracht", "tekst": "Maak een kasteel van wat je om je heen vindt.", "codewoord": ""},
    "D1": {"type": "opdracht", "tekst": "Bedenk een toverspreuk van 4 woorden en gebruik hem met beweging.", "codewoord": ""},
    "D2": {"type": "consequentie", "tekst": "Je moet je terugtrekken – je mag gedurende twee minuten geen nieuwe locatie aanvallen.", "wacht": 120},
    "D3": {"type": "vraag", "tekst": "Lang steekwapen, vaak gebruikt op paarden (4 letters)", "antwoord": "lans"},
    "D4": {"type": "consequentie", "tekst": "Je hebt het rantsoen van de tegenpartij gevonden – ga direct door.", "wacht": 0},
    "D5": {"type": "vraag", "tekst": "Wat was een heraut?\nA) Een kok\nB) Een boodschapper die aankondigingen deed\nC) Een soldaat", "antwoord": "B"},
    "D6": {"type": "opdracht", "tekst": "Maak een schild.", "codewoord": "prins"},
    "E1": {"type": "opdracht", "tekst": "Kruip 15 meter over het gras alsof je gewond bent in de strijd.", "codewoord": "pijlenboog"},
    "E2": {"type": "vraag", "tekst": "Wat is een pelgrim?\nA) Iemand die op reis ging om religieuze redenen\nB) Een roofridder\nC) Een koopman met kamelen", "antwoord": "A"},
    "E3": {"type": "vraag", "tekst": "Vuurspuwend wezen in veel sagen (5 letters)", "antwoord": "draak"},
    "E4": {"type": "vraag", "tekst": "Welke taal werd vaak gebruikt in officiële documenten in de middeleeuwen?\nA) Frans\nB) Nederlands\nC) Latijn", "antwoord": "C"},
    "E5": {"type": "opdracht", "tekst": "Verzin een middeleeuwse bijnaam voor al je groepsleden.", "codewoord": "schild"},
    "E6": {"type": "opdracht", "tekst": "Maak een helm van aluminiumfolie.", "codewoord": "veldslag"},
    "F1": {"type": "consequentie", "tekst": "Je wapens zijn verdwenen; gebruik bij de volgende opdracht alleen je linkerhand.", "wacht": 0},
    "F2": {"type": "consequentie", "tekst": "Herhaal je eerder bedachte eerste wet als koning(in).", "wacht": 0},
    "F3": {"type": "consequentie", "tekst": "Geheime kaart ontvangen – je hoeft geen opdracht te doen.", "wacht": 0},
    "F4": {"type": "vraag", "tekst": "Wat is de functie van een banier?", "antwoord": "vlag met symbool van een ridder of familie"},
    "F5": {"type": "consequentie", "tekst": "Geheime kaart ontvangen – je hoeft geen opdracht te doen.", "wacht": 0},
    "F6": {"type": "consequentie", "tekst": "De brug is ingestort! Wacht 1 minuut.", "wacht": 60},
}

st.title("🏰 De Slag om Slot Haneburg")
st.markdown("Voer een veld in (bijv. A1-F6):")
vak = st.text_input("📍 Veld").upper().strip()

nu = time.time()
if st.session_state.wacht_tot > nu:
    resterend = int(st.session_state.wacht_tot - nu)
    st.warning(f"⏳ Je moet nog {resterend} seconden wachten voordat je verder mag.")
    st.stop()

if vak:
    if vak in st.session_state.gevonden_vakken:
        st.info("📌 Dit veld is al onderzocht.")
    elif vak not in vraag_data:
        st.error("❌ Onbekend veld. Gebruik A1 t/m F6.")
    else:
        item = vraag_data[vak]
        st.markdown(f"### 🧾 Opdracht voor {vak}:")
        st.write(item['tekst'])

        if item['type'] == 'vraag':
            antwoord = st.text_input("📝 Antwoord:")
            if antwoord:
                if antwoord.strip().lower() == item['antwoord'].lower():
                    st.success("✅ Correct beantwoord!")
                    st.session_state.gevonden_vakken.append(vak)
                else:
                    st.error("❌ Onjuist antwoord.")

        elif item['type'] == 'opdracht':
            codewoord = st.text_input("🔐 Voer het ontvangen codewoord in:")
            if codewoord:
                if codewoord.strip().lower() == item['codewoord'].lower():
                    st.success("✅ Correct codewoord!")
                    st.session_state.gevonden_vakken.append(vak)
                else:
                    st.error("❌ Onjuist codewoord.")

        elif item['type'] == 'consequentie':
            wachttijd = item.get('wacht', 60)
            st.warning(f"⚠️ {item['tekst']}")
            if wachttijd > 0:
                st.session_state.wacht_tot = time.time() + wachttijd
                st.stop()
            else:
                st.session_state.gevonden_vakken.append(vak)

        geraakt = False
        for troep in formatie:
            if vak in troep:
                geraakt = True
                st.success("🎯 RAAK!")
                troep_id = tuple(troep)
                if all(v in st.session_state.gevonden_vakken for v in troep):
                    if troep_id not in st.session_state.gevonden_troepen:
                        idx = len(st.session_state.gevonden_troepen)
                        if idx < len(adressen):
                            naam, adres = adressen[idx]
                            st.balloons()
                            st.success(f"💥 Troepenmacht vernietigd! Hint {idx+1}: {naam}, {adres}")
                            st.session_state.gevonden_troepen.append(troep_id)
                            st.session_state.gegeven_adressen.append(adres)
                break
        if not geraakt:
            st.info("💨 MIS!")

st.markdown("---")
st.markdown(f"### 📍 Gevonden vakken: {', '.join(st.session_state.gevonden_vakken)}")
