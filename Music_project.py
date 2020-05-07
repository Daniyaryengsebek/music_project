import pandas as pd
df = pd.read_csv('/downloads/music_project.csv')
df.set_axis(['user_id', 'track_name', 'artist_name', 'genre_name', 'city', 'time', 'weekday'], axis = 'columns', inplace = True)

df['track_name'] = df['track_name'].fillna('unknown')

df['artist_name'] = df['artist_name'].fillna('unknown')

df.dropna(subset = ['genre_name'], inplace = True)

df=df.drop_duplicates().reset_index(drop = True)

genres_list = df['genre_name'].unique()
#print(genres_list)

def find_genre(genre_name):
    i = 0
    for element in genres_list:
        if element == genre_name:
            i += 1
    return i

def find_hip_hop(df,wrong):
    df['genre_name'] = df['genre_name'].replace(wrong, 'hiphop')
    number_of_errors = df[df['genre_name'] == wrong]['genre_name'].count()
    return number_of_errors

find_hip_hop(df, 'hip')
#print(find_hip_hop)

df.groupby('city')['genre_name'].count

df.groupby('weekday')['genre_name'].count

def number_tracks(df,day,city):
    track_list = df[(df['weekday'] == day) & (df['city'] == city)]
    track_list_count = track_list['genre_name'].count()
    return track_list_count


header = ['city', 'monday', 'wednesday', 'friday']
data_by_days = [
    ['Moscow', 15347, 10865, 15680],
    ['Saint-Petersburg', 5519, 6913, 5802],
]
table = pd.DataFrame(data = data_by_days, columns = header)
#print(table)

moscow_general = df[df['city'] == 'Moscow']
#print(moscow_general)

spb_general = df[df['city'] == 'Saint-Petersburg']
#print(spb_general)

def genre_weekday(df, day, time1, time2):
    genre_list = df[(df['weekday'] == day) & (df['time'] > time1) & (df['time'] < time2)]
    genre_list_sorted = genre_list.groupby('genre_name')['genre_name'].count().head(10)
    return genre_list_sorted

genre_weekday(moscow_general, 'Monday', '07:00:00', '11:00:00')
genre_weekday(spb_general, 'Monday', '07:00:00', '11:00:00')
genre_weekday(moscow_general, 'Friday', '17:00:00', '23:00:00')
genre_weekday(spb_general, 'Friday', '17:00:00', '23:00:00')

#print(genre_weekday)

moscow_genres = moscow_general.groupby('genre_name')['genre_name'].count().sort_values(ascending = False)

print(moscow_genres.head(10))

spb_genres = spb_general.groupby('genre_name')['genre_name'].count().sort_values(ascending = False)

print(spb_genres.head(10))
