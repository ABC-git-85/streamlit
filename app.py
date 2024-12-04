import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

comptes = pd.read_csv("DonneesDesComptes.csv", sep=';')

 # Préparer les données pour streamlit-authenticator
comptes = {
    "usernames": {
        row["name"]: {
            "name": row["name"],
            "password": row["password"],
            "email": row["email"],
            "role": row["role"],
        }
        for _, row in comptes.iterrows()
    }
}

# Initialiser l'authenticator
authenticator = Authenticate(
    comptes,
    cookie_name="my_app_cookie",
    key="my_app_key",
    cookie_expiry_days=30,
)

authenticator.login()

if st.session_state["authentication_status"]:
    # Navigation entre les pages
    with st.sidebar:
        authenticator.logout("Déconnexion", "sidebar")
        st.write(f"Bienvenue _{st.session_state["name"]}_")
        # Menu
        selected = option_menu(
                    menu_title=None,
                    options = ["🤩 Accueil", "😺 Les photos de mon chat"],
                    menu_icon="cast",
                    default_index=0)
        
    if selected == "🤩 Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXd5c3h6cjluNWp5OWFkbzQ0d2xkZDdmdWt3Zjd0eTlhb3BhaHB4YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SsIPF2HnLYlQnFGKsZ/giphy.webp")

    elif selected == "😺 Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat 😺")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://feelloo.com/wp-content/uploads/2019/10/jeune-chat-pexels-104827-900x598.jpeg")
        with col2:
            st.image("https://www.assuropoil.fr/wp-content/uploads/2023/07/avoir-un-chat-sante.jpg")
        with col3:
            st.image("https://franklinpetfood.com/cdn/shop/files/600X600_BENGAL_HEADER.jpg?v=1702485452&width=642")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')