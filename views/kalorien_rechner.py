import streamlit as st
from functions.kalorienbedarf import calculate_calories

st.title("🍽️ Kalorienbedarf-Rechner")

with st.form("kalorien_form"):
    age = st.number_input("Alter (Jahre)", min_value=0, max_value=120, value=25)
    height = st.number_input("Größe (cm)", min_value=50, max_value=250, value=170)
    weight = st.number_input("Gewicht (kg)", min_value=10, max_value=300, value=70)
    gender = st.selectbox("Geschlecht", ["m", "w"])
    activity = st.selectbox("Aktivitätslevel", ["Keine", "Leicht", "Mäßig", "Aktiv", "Sehr aktiv"])
    goal = st.selectbox("Ziel", ["Abnehmen", "Halten", "Zunehmen"])
    submit = st.form_submit_button("📊 Berechnen")

if submit:
    bmr, tdee = calculate_calories(age, height, weight, gender, activity)
    st.session_state.bmr = bmr
    st.session_state.tdee = tdee
    st.session_state.goal = goal

if "bmr" in st.session_state:
    st.success("✅ Berechnung abgeschlossen!")
    st.metric("Grundumsatz (BMR)", f"{st.session_state.bmr:.0f} kcal/Tag")
    st.metric("Gesamtbedarf (TDEE)", f"{st.session_state.tdee:.0f} kcal/Tag")
    st.subheader(f"Ziel: {st.session_state.goal}")
    
    if st.session_state.goal == "Abnehmen":
        st.info("💡 Reduziere deine Kalorien um ~500 kcal/Tag")
    elif st.session_state.goal == "Zunehmen":
        st.info("💡 Erhöhe deine Kalorien um ~500 kcal/Tag")
    else:
        st.info("💡 Halte dich am errechneten Bedarf")
    
    st.balloons()