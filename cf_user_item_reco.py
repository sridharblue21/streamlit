import numpy as np
import pandas as pd
from scipy.sparse import csc_matrix, coo_matrix
from scipy.sparse.linalg import svds
from stapp import pass_song_data, pass_count_data

song_data = pass_song_data()
count_data = pass_count_data()
# drop duplicates in song data
song_data = song_data.drop(song_data[song_data.duplicated('song_id')].index)

def fn_count_data_with_song_info_df_final():
    # song and count data merge
    count_data_with_song_info_df = pd.merge(count_data, song_data, on="song_id", how="left")
    count_data_with_song_info_df = count_data_with_song_info_df.drop(columns=['Unnamed: 0'])
    counts = count_data_with_song_info_df['user_id'].value_counts()

    #Modified by Lakshminarayanan
    #Based on the above plot consider users who have played 60 times or more
    count_data_with_song_info_df_final = count_data_with_song_info_df[count_data_with_song_info_df['user_id'].isin(counts[counts >= 60].index)]
    #Modified by Lakshminarayanan
    user_song_sum_df = count_data_with_song_info_df_final[['user_id','play_count']].groupby('user_id').sum().reset_index()
    user_song_sum_df = user_song_sum_df.rename(columns={'play_count':'total_play_count'})
    count_data_with_song_info_df_final = pd.merge(count_data_with_song_info_df_final,user_song_sum_df)
    count_data_with_song_info_df_final['fractional_play_count'] = count_data_with_song_info_df_final['play_count']/count_data_with_song_info_df_final['total_play_count']
    return count_data_with_song_info_df_final


def fn_utility_matrix():
    small_set = fn_count_data_with_song_info_df_final()
    user_codes = small_set['user_id'].drop_duplicates().reset_index()
    song_codes = small_set['song_id'].drop_duplicates().reset_index()
    user_codes.rename(columns={'index':'user_index'}, inplace=True)
    song_codes.rename(columns={'index':'song_index'}, inplace=True)

    song_codes['so_index_value'] = list(song_codes.index)
    user_codes['us_index_value'] = list(user_codes.index)
    small_set = pd.merge(small_set,song_codes,how='left')
    small_set = pd.merge(small_set,user_codes,how='left')
    mat_candidate = small_set[['us_index_value','so_index_value','fractional_play_count']]
    data_array = mat_candidate['fractional_play_count'].values
    row_array = mat_candidate['us_index_value'].values
    col_array = mat_candidate['so_index_value'].values
    data_sparse = coo_matrix((data_array, (row_array, col_array)),dtype=float)
    return small_set, data_sparse


def compute_svd(urm, K):
    U, s, Vt = svds(urm, K)
    dim = (len(s), len(s))
    S = np.zeros(dim, dtype=np.float32)
    for i in range(0, len(s)):
        S[i, i] = np.sqrt(s[i])
    U = csc_matrix(U, dtype=np.float32)
    S = csc_matrix(S, dtype=np.float32)
    Vt = csc_matrix(Vt, dtype=np.float32)
    return U, S, Vt


def compute_estimated_matrix(urm, U, S, Vt, user, max_recommendation=50):
    MAX_PID = urm.shape[1]
    MAX_UID = urm.shape[0]
    rightTerm = S * Vt
    estimatedRatings = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float16)
    recomendRatings = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float16)
    prod = U[user, :] * rightTerm
    estimatedRatings[user, :] = prod.todense()
    recomendRatings[user, :] = (-estimatedRatings[user, :]).argsort()[:max_recommendation]
    return recomendRatings

small_set, data_sparse = fn_utility_matrix()
U, S, Vt = compute_svd(data_sparse, K=50)  # Picking top 50 latent features

def ui_recommendation(user_index,n):
  rank_value = 1
  rank = []
  title = []
  artist = []
  release = []
  df = pd.DataFrame()
  uTest_recommended_items = compute_estimated_matrix(data_sparse, U, S, Vt, user_index)
  iter_list = uTest_recommended_items[user_index, 0:n].flatten()
  for items in iter_list:
    song_details = small_set[small_set.so_index_value == items].drop_duplicates('so_index_value')[['title','artist_name','release']]
    rank.append(rank_value)
    title.append(list(song_details['title'])[0])
    artist.append(list(song_details['artist_name'])[0])
    release.append(list(song_details['release'])[0])
    rank_value += 1
  df['sno'] = rank
  df['title'] = title
  df['artist_name'] = artist
  df['release'] = release
  df.set_index('sno', inplace=True)
  return df
