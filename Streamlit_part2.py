import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Liste des datasets de Seaborn
datasets = {
    'tips' : sns.load_dataset(https://datasets.imdbws.com/name.basics.tsv.gz),
    'iris' : sns.load_dataset("iris"),
    'penguins' : sns.load_dataset("penguins"),
    'flights' : sns.load_dataset("flights"),
    'diamonds' : sns.load_dataset("diamonds"),
    'titanic' : sns.load_dataset("titanic"),
    'exercise' : sns.load_dataset("exercise"),
    'mpg' : sns.load_dataset("mpg"),
    'planets' : sns.load_dataset("planets"),
}

# Titre de la page
st.title("Manipulation de données et création de graphiques")

#### TABLEAU #### 

# Création de la première liste déroulante pour choisir un dataset
dataset_name = st.selectbox('Quel dataset veux-tu utiliser ?', list(datasets.keys()))
# Affichage du dataset
dataset = datasets[dataset_name]
st.dataframe(dataset)

#### GRAPHIQUE ####

# Liste les en-têtes de colonne
nom_colonnes = dataset.columns.tolist()
# Choisir la valeur de x parmi les en-têtes de colonne
x = st.selectbox('Choisissez la colonne X', nom_colonnes)
# Choisir la valeur de y parmi les en-têtes de colonne
y = st.selectbox('Choisissez la colonne Y', nom_colonnes)

# Création de la deuxième liste déroulante pour choisir un type de graphique
graph = st.selectbox('Quel graphique veux-tu utiliser ?', ['scatter_chart', 'bart_chart', 'line_chart'])
# Création du graphique
if graph == 'scatter_chart':
    fig = px.scatter(dataset, x=x, y=y)
elif graph == 'bart_chart':
    fig = px.bar(dataset, x=x, y=y)
elif graph == 'line_chart':
    fig = px.line(dataset, x=x, y=y)
st.plotly_chart(fig)

#### MATRICE DE CORRELATION ####

matrice_correlation = st.checkbox('Afficher la matrice de corrélation')

if matrice_correlation:
    # Extraction des colonnes x et y sélectionnées
    selected_dataset = dataset[[x, y]]
    # Vérifier que les valeurs sélectionnées soient des valeurs numériques pour calculer la corrélation
    if dataset[x].dtype in ['float64', 'int64'] and dataset[y].dtype in ['float64', 'int64']:
        # Calcul de la correlation
        correlation = selected_dataset.corr()
        # Création du graphique
        fig = plt.figure()
        sns.heatmap(correlation)
        plt.title('Ma matrice de corrélation')
        st.pyplot(fig)
    else:
        st.error('Les colonnes sélectionnées doivent être de type numérique (float ou int) pour calculer une corrélation.')
else:
    st.write("")