import pandas as pd
import numpy as nd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

SEED = 73

# importamos nuestro dataset
df_spotify = pd.read_csv("Popular_Spotify_Songs.csv", encoding = "latin1")

# Visualizacion general de df
print(df_spotify.head)
# informacion de los tipos de datos que hay en cada columna y cuantos son
info_df = df_spotify.info()

# covertiremos variables especificas con valores categoricos a int
df_spotify["streams"] = pd.to_numeric(df_spotify["streams"], errors = "coerce")
df_spotify["in_deezer_playlists"] = pd.to_numeric(df_spotify["in_deezer_playlists"], errors="coerce")
df_spotify["in_shazam_charts"] = pd.to_numeric(df_spotify["in_shazam_charts"], errors="coerce")

# Comprobamos si hay missing values
print(df_spotify.isnull().sum())

# Eliminamos los missing values
df_spotify.dropna(subset=['streams', 'in_deezer_playlists', 'in_shazam_charts', 'key'], inplace=True)

variables_numerias =  ['streams', 'in_spotify_playlists', 'in_spotify_charts', 'in_apple_playlists', 'in_apple_charts','in_deezer_playlists', 'in_deezer_charts', 'in_shazam_charts', 'bpm', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']
