import streamlit as st


password = st.text_input("Enter the password to access the app:", type="password")
if password == st.secrets["app_password"]:
    st.success("Access granted!")
# config de la page
    st.set_page_config(
        page_title="Loan aproval Prediction",
        page_icon="🚀",
        layout="wide"
    )

    # titre 
    st.title("Loan Approval Prediction App 🚀")
    st.markdown("## About this App")

    # contenu
    st.write("Bienvenue dans l'application de prédiction d'approbation de prêt. ")

else:
    st.error("Access denied")
    st.stop()