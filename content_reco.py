import readdata
import pandas as pd
from gensim import corpora

song_data_with_genre1 = readdata.read_data_gdrive('song_data_with_genre.pkl')
song_bowdf1 = readdata.read_data_gdrive('song_data_bow_df.csv')

# load pickle files for genre search
processed_corpus = readdata.read_data_gdrive('processed_corpus.pkl', type = 'joblib')
index = readdata.read_data_gdrive('gensim_sparse_similarities.pkl', type = 'joblib')
tfidf = readdata.read_data_gdrive('gensim_tfidf_model.pkl', type = 'joblib')
dictionary = corpora.Dictionary(processed_corpus)
#######################################################
# load pickle files Lyrics search
lyrics_processed_corpus = readdata.read_data_gdrive('lyrics_processed_corpus.pkl', type = 'joblib')
lyrics_index = readdata.read_data_gdrive('lyrics_gensim_sparse_similarities.pkl', type = 'joblib')
lyrics_tfidf = readdata.read_data_gdrive('lyrics_gensim_tfidf_model.pkl', type = 'joblib')
lyrics_dictionary = corpora.Dictionary(lyrics_processed_corpus)

def text_recommendations(title):  # function that takes in song title as input and returns the top 10 recommended songs
    reco = []
    doc_l = []
    score_l = []
    song_data_with_genre = song_data_with_genre1
    song_data_with_genre.genre = song_data_with_genre.genre.astype('object')
    song_data_with_genre.release = song_data_with_genre.release.astype('object')
    song_data_with_genre = song_data_with_genre[['title', 'artist_name', 'release','genre','year']]
    query_document = title.lower().split() # assign search title
    query_bow = dictionary.doc2bow(query_document)
    sims = index[tfidf[query_bow]] # index from Sparse Similarities, and tfidf is from gensim model

    for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
        doc_l.append(document_number)
        score_l.append(score)

    recommended_songs_idx_score = pd.DataFrame(score_l, doc_l).head(10) # top 10 title recommendations
    recommended_songs_idx_score = recommended_songs_idx_score.reset_index()
    recommended_songs_idx_score.columns = ['index', 'score']
    recommended_songs_idx_score.set_index('index', inplace=True)

    # song titles with top score recommended based on the content searched by user
    for idx in recommended_songs_idx_score.index:
        dict_reco = dict(song_data_with_genre.loc[idx][['title', 'artist_name', 'release','genre','year']])
        reco.append(dict_reco)
    recommended_songs = pd.DataFrame(reco)
    recommended_songs['score'] = list(recommended_songs_idx_score.score.values)
    recommended_songs['sno'] = [x for x in range(1, len(recommended_songs) + 1)]
    recommended_songs.set_index('sno', inplace=True) # setting sno as index
    return recommended_songs


def lyrics_recommendations(title):  # function that takes in song title as input and returns the top 10 recommended songs
    reco = []
    doc_l = []
    score_l = []
    song_bowdf = song_bowdf1
    song_bowdf = song_bowdf[['title', 'artist_name', 'release','genre','year']]
    lyrics_query_document = title.lower().split() # assign search title
    lyrics_query_bow = dictionary.doc2bow(lyrics_query_document)
    sims = lyrics_index[lyrics_tfidf[lyrics_query_bow]] # index from Sparse Similarities, and tfidf is from gensim model

    for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
        doc_l.append(document_number)
        score_l.append(score)

    recommended_songs_idx_score = pd.DataFrame(score_l, doc_l).head(10) # top 10 title recommendations
    recommended_songs_idx_score = recommended_songs_idx_score.reset_index()
    recommended_songs_idx_score.columns = ['index', 'score']
    recommended_songs_idx_score.set_index('index', inplace=True)

    # song titles with top score recommended based on the content searched by user
    for idx in recommended_songs_idx_score.index:
        dict_reco = dict(song_bowdf.loc[idx][['title', 'artist_name', 'release','genre','year']])
        reco.append(dict_reco)
    recommended_songs = pd.DataFrame(reco)
    recommended_songs['score'] = list(recommended_songs_idx_score.score.values)
    recommended_songs['sno'] = [x for x in range(1, len(recommended_songs) + 1)]
    recommended_songs.set_index('sno', inplace=True) # setting sno as index
    return recommended_songs
