import pandas as pd
import numpy as nd
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

# Comenzamos con la limpieza de datos
print(df_spotify.isnull().sum())

for art in df_spotify["artist(s)_name"]:
    print(art)
