import streamlit as st
import pandas as pd
import numpy as np
import popular_reco
from load_css import local_css
import readdata

local_css('style.css')

with st.spinner('Wait for song data to load ...'):
    song_data = readdata.read_data_gdrive('song_data_with_gender.csv')
st.success('song data loaded')


with st.spinner('Wait for count data to load ...'):
    count_data = readdata.read_data_gdrive('count_data.pkl')
st.success('count data loaded')


with st.spinner('Wait for imdb_merge data to load ...'):
    song_imdb_merge = readdata.read_data_gdrive('song_only_imdb_merge.pkl')
st.success('imdb_merge data loaded')


def pass_song_data():
    return song_data


def pass_count_data():
    return count_data

def func_welcome(menu_in, level=1):
    # menu_in is menu name, level is signify if its main menu or submenu (only two level possible now)
    if level == 1:
        menu_out_msg = f"<div><span class='highlight red'>{menu_in}</span>>>>>></div>"
    elif level == 2:
        menu_out_msg = f"<div> >>>>>>>>> <span class='highlight lblue'>{menu_in}</span></div>"
    return menu_out_msg


def fn_markdown(choice1):
    #global markdown function, can be called from anywhere
    choice_out = st.markdown(f"<div><span class='highlight blue'>{choice1}</span></div>", unsafe_allow_html=True)
    return choice_out

@st.cache(persist=True)
def fn_songs_play_count():
    song_data.drop(song_data[song_data.duplicated()].index, inplace=True)  # drop duplicate song_ids
    sorted_play_counts_df = count_data.groupby(['song_id', 'play_count']).sum().sort_values(by='play_count',
                                                                                            ascending=False)
    sorted_play_counts_df.reset_index(inplace=True)
    sorted_play_counts_df.set_index('song_id',
                                    inplace=True)
    songs_play_count_df = pd.merge(sorted_play_counts_df, song_data, on='song_id')
    return songs_play_count_df

songs_play_count_df = fn_songs_play_count()


def artist_choice():  # top 20 artist by playcount
    artist_choice = songs_play_count_df[['artist_name','play_count']].groupby('artist_name').sum().sort_values(by='play_count',ascending=False)[:20]
    artist_choice = artist_choice.reset_index()
    return list(artist_choice['artist_name'].values)


def release_choice():  # top 20 releases/albums by playcount
    artist_choice = songs_play_count_df[['release','play_count']].groupby('release').sum().sort_values(by='play_count',ascending=False)[:20]
    artist_choice = artist_choice.reset_index()
    return list(artist_choice['release'].values)


@st.cache(persist=True)
def top_pop_songs(n): #top popular songs recommendation by play count
    top_count_data = count_data[count_data.play_count > 20]
    sum_play_count = songs_play_count_df.groupby('song_id').sum()['play_count']
    count_play_count = songs_play_count_df.groupby('song_id').count()['play_count']
    final_play_count = pd.DataFrame({'sum_play_count': sum_play_count, 'count_play_count': count_play_count})
    #Top n popular songs from song data for new users
    top_pop_songs_id = popular_reco.top_played_n_songs(final_play_count, n, min_interaction=50)
    title = np.unique(song_data[song_data.song_id.isin(top_pop_songs_id.index)].title.values)
    choices=np.unique(song_data[song_data.song_id.isin(top_pop_songs_id.index)].title.values)+' by '+np.unique(song_data[song_data.song_id.isin(top_pop_songs_id.index)].artist_name.values)
    top_pop_songs_title = pd.DataFrame(choices, [x for x in range(1, n+1)]).reset_index()
    top_pop_songs_title.columns = ['S.No', 'Titles']
    top_pop_songs_title.set_index('S.No', inplace=True)
    top_pop_songs_title['playCount'] = list(top_pop_songs_id.sum_play_count)
    return title, top_pop_songs_title


@st.cache(persist=True)
def top_rated_songs(n,region): #top rated songs recommendation (combining IMDb dataset)
    # min_interaction=20 is input for numVotes
    numVotes = song_imdb_merge[song_imdb_merge.region == region].groupby(['song_id'])['numVotes'].agg(['sum']).sort_values(by=['sum'],
                                                                                                   ascending=False)
    avgRating = song_imdb_merge[song_imdb_merge.region == region].groupby(['song_id'])['averageRating'].agg(['mean']).sort_values(by=['mean'],
                                                                                                          ascending=False)
    final_rating_Votes = pd.merge(numVotes.reset_index(), avgRating.reset_index(),
                                  on=['song_id']).sort_values(by='sum', ascending=False)
    final_rating_Votes.columns = ['song_id', 'numVotes', 'averageRating']
    final_rating_Votes = final_rating_Votes.set_index('song_id')

    top_rated_songs_id = popular_reco.top_rated_n_songs(final_rating_Votes, n, min_interaction=20)
    choices = song_data[song_data.song_id.isin(top_rated_songs_id.index)][['song_id','title','release','artist_name']]
    choices['S.No'] = [x for x in range(1, len(choices)+1)]
    choices.set_index('S.No', inplace=True)
    choices['Votes'] = list(top_rated_songs_id.numVotes)
    choices['Rating'] = list(top_rated_songs_id.averageRating)
    return choices
