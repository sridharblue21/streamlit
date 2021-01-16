import stapp
import user_list


def insert_user_choice(name, choice, flag):  # insert users artist_choice value in userdf against username record
    userdf = user_list.user_list()
    if choice and flag=='A':
        sel_user_rec=userdf[userdf.name.isin([name])]
        name_delta = sel_user_rec.name.values
        userdf.loc[userdf[userdf['name'] == name_delta[0]].index, 'artist_choice'] = ''  # resetting NaN value to empty string
        userdf.loc[userdf[userdf['name'] == name_delta[0]].index, 'artist_choice'] = [choice]
        userdf.to_csv('userdf.csv', mode='w')
        return 'success'
    elif choice and flag == 'R':
        sel_user_rec=userdf[userdf.name.isin([name])]
        name_delta = sel_user_rec.name.values
        userdf.loc[userdf[userdf['name'] == name_delta[0]].index, 'release_choice'] = ''  # resetting NaN value to empty string
        userdf.loc[userdf[userdf['name'] == name_delta[0]].index, 'release_choice'] = [choice]
        userdf.to_csv('userdf.csv', mode='w')
        return 'success'
    else:
        return 'failure'


def artist_choice():  # top 20 artist by playcount
    songs_play_count_df = stapp.fn_songs_play_count()
    artist_choice = songs_play_count_df[['artist_name','play_count']].groupby('artist_name').sum().sort_values(by='play_count',ascending=False)[:20]
    artist_choice = artist_choice.reset_index()
    return list(artist_choice['artist_name'].values)


def release_choice():  # top 20 releases/albums by playcount
    songs_play_count_df = stapp.fn_songs_play_count()
    artist_choice = songs_play_count_df[['release','play_count']].groupby('release').sum().sort_values(by='play_count',ascending=False)[:20]
    artist_choice = artist_choice.reset_index()
    return list(artist_choice['release'].values)


#defining a function to get the top n songs based on highest times a song is played in general and some minimum interactions (minimum number of distinct users or we can say play count) of that song
def top_played_n_songs(final_play_count, n, min_interaction=50):
    recommendations=final_play_count[final_play_count['count_play_count']>min_interaction]
    recommendations=recommendations.sort_values(by='sum_play_count', ascending=False)
    return recommendations[:n]

def top_rated_n_songs(song_imdb_merge, n, min_interaction=20):
    recommendations=song_imdb_merge[song_imdb_merge['numVotes']>min_interaction]
    recommendations=recommendations.sort_values(by=['numVotes', 'averageRating'], ascending=False)
    return recommendations[:n]
