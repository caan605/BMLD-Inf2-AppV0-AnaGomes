import streamlit as st

pg_home = st.Page("views/home.py", title="Home")
pg_kalorien = st.Page("views/kalorien_rechner.py", title="Kalorienbedarf-Rechner")

pg = st.navigation([pg_home, pg_kalorien])
pg.run()