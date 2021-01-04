import streamlit as st


def artist_choice():
    artist_choice = st.multiselect("Who's your favorite artist?", ('Dwight Yoakam', 'Kings Of Leon', 'Alliance Ethnik'))
    return artist_choice


#defining a function to get the top n songs based on highest times a song is played in general and some minimum interactions (minimum number of distinct users or we can say play count) of that song
def top_played_n_songs(final_play_count, n, min_interaction=50):
    recommendations=final_play_count[final_play_count['count_play_count']>min_interaction]
    recommendations=recommendations.sort_values(by='sum_play_count', ascending=False)
    return recommendations.index[:n]

def top_rated_n_songs(song_imdb_merge, n, min_interaction=20):
    recommendations=song_imdb_merge[song_imdb_merge['numVotes']>min_interaction]
    recommendations=recommendations.sort_values(by='averageRating', ascending=False)
    return recommendations.index[:n]
