import streamlit as st
import pandas as pd
import seaborn as sns
import math

# Chargement du dataset "taxis"
taxis_df = sns.load_dataset("taxis")
# Liste les valeurs uniques de la colonne pickup_borough 
pickup_borough_list = taxis_df['pickup_borough'].unique()
# Tri de la liste par ordre alphabétique
# La liste contient des NaN => on veut le mettre à la fin de la liste
pickup_borough_list_sorted = sorted(pickup_borough_list, key=lambda x: (isinstance(x, float) and math.isnan(x), x)) # Si False alors valeur ajouté en premier dans la liste. Si True alors valeur ajouté à la fin 

st.title("Bienvenue sur le site web d'Amandine")

arrondissement = st.selectbox("Indiquez votre arrondissement de récupération", pickup_borough_list_sorted)

st.write("Tu as choisi : " + str(arrondissement))

if arrondissement == 'Brooklyn':
    st.image("https://www.terre.tv/wp-content/uploads/2022/05/brooklyn-new-york-1024x632.jpg")
elif arrondissement == 'Bronx':
    st.image("https://photo620x400.mnstatic.com/fdd552b53deea69a647a6ffcca9ed153/bronx-.jpg")
elif arrondissement == 'Queens':
    st.image("https://media.routard.com/image/50/8/pont-de-queensboro-entre-manhattan-et-long-island-city.1614508.w630.jpg")
elif arrondissement == 'Manhattan':
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/Luchtfoto_van_Lower_Manhattan.jpg")
else:
    st.image("https://images.pexels.com/photos/5428836/pexels-photo-5428836.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")