import readdata
import pandas as pd
from gensim import corpora, similarities
import pickle
import joblib

# load pickle files
processed_corpus = pickle.load( open( "processed_corpus.pkl", "rb" ) )
index = joblib.load("gensim_sparse_similarities.pkl")
# gensim_tfidf_model => models.TfidfModel()
tfidf = joblib.load('gensim_tfidf_model.pkl')

dictionary = corpora.Dictionary(processed_corpus)


def recommendations(title):  # function that takes in song title as input and returns the top 10 recommended songs
    reco = []
    doc_l = []
    score_l = []
    song_data_with_genre = readdata.read_song_genre()
    song_data_with_genre = song_data_with_genre[['title', 'artist_name', 'release','genre','year','artist_gender']]
    #song_data_with_genre = song_data_with_genre.drop_duplicates(song_data_with_genre.duplicated(subset=['title', 'artist_name', 'genre', 'release']))
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
