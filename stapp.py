import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
import pandas as pd
import numpy as np
import popular_reco
from load_css import local_css
import readdata

local_css('style.css')


def func_welcome(menu_in,level=1): # menu_in is menu name, level is signify if its main menu or submenu (only two level possible now)
    if level==1:
        menu_out_msg = f"<div><span class='highlight red'>{menu_in}</span>>>>>></div>"
    elif level==2:
        menu_out_msg = f"<div> >>>>>>>>> <span class='highlight lblue'>{menu_in}</span></div>"
    return menu_out_msg

def fn_markdown(choice1): #global markdown function, can be called from anywhere
    choice_out=st.markdown(f"<div><span class='highlight blue'>{choice1}</span></div>",unsafe_allow_html=True)
    return choice_out

def fn_songs_play_count():
    song_data = readdata.read_song()
    count_data = readdata.read_count()

    sorted_play_counts_df = count_data.groupby(['song_id', 'play_count']).sum().sort_values(by='play_count',
                                                                                            ascending=False)
    sorted_play_counts_df.reset_index(inplace=True)
    sorted_play_counts_df.set_index('song_id',
                                    inplace=True)  # making song_id index of the df, this is required to merge with song_data df

    # Sorted in descending order of play_count to see the top play counts first
    songs_play_count_df = pd.merge(sorted_play_counts_df, song_data, on='song_id')
    return songs_play_count_df,song_data,count_data

def top_pop_songs(n): #top popular songs recommendation by playcount
    songs_play_count_df, song_data, count_data = fn_songs_play_count()
    top_count_data = count_data[count_data.play_count > 20]

    sum_play_count = songs_play_count_df.groupby('song_id').sum()['play_count']
    count_play_count = songs_play_count_df.groupby('song_id').count()['play_count']
    final_play_count = pd.DataFrame({'sum_play_count': sum_play_count, 'count_play_count': count_play_count})
    #Top n popular songs from song data for new users
    top_pop_songs_id=list(popular_reco.top_played_n_songs(final_play_count, n, min_interaction=50))
    choices=np.unique(song_data[song_data.song_id.isin(top_pop_songs_id)].title.values)+' by '+np.unique(song_data[song_data.song_id.isin(top_pop_songs_id)].artist_name.values)
    top_pop_songs_title=pd.DataFrame(choices,[x for x in range(1,n+1)]).reset_index()
    top_pop_songs_title.columns=['S.No','Titles']
    top_pop_songs_title.set_index('S.No',inplace=True)
    return top_pop_songs_title

def top_rated_songs(n): #top rated songs recommendation (combining IMDb dataset)
    df_akas_data = readdata.read_akas()
    df_rating_data = readdata.read_rating()
    songs_play_count_df, song_data, count_data = fn_songs_play_count()
    imdb_merge = pd.merge(df_akas_data, df_rating_data, left_on='titleId', right_on='tconst')
    imdb_merge = imdb_merge[imdb_merge.ordering == 1]  # filtering further to remove duplicate titles
    song_imdb_merge = pd.merge(songs_play_count_df, imdb_merge, left_on='title',
                               right_on='title')  # Song data and IMDb rating data merged
    song_imdb_merge.set_index('song_id', inplace=True)
    top_rated_songs_id=list(popular_reco.top_rated_n_songs(song_imdb_merge, n, min_interaction=20))  #min_interaction=20 is input for numVotes
    choices=np.unique(song_data[song_data.song_id.isin(top_rated_songs_id)].title.values)+' by '+np.unique(song_data[song_data.song_id.isin(top_rated_songs_id)].artist_name.values)
    top_rated_songs_title=pd.DataFrame(choices,[x for x in range(1,n+1)]).reset_index()
    top_rated_songs_title.columns=['S.No','Titles']
    top_rated_songs_title.set_index('S.No',inplace=True)
    return top_rated_songs_title
