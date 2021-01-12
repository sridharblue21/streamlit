import readdata
import pandas as pd
from gensim import corpora, similarities
import pickle
import joblib

# load pickle files
processed_corpus = pickle.load( open( "processed_corpus.pkl", "rb" ) )
bow_corpus = pickle.load( open( "bow_corpus.pkl", "rb" ) )

# gensim_tfidf_model => models.TfidfModel()
tfidf = joblib.load('gensim_tfidf_model.pkl')

dictionary = corpora.Dictionary(processed_corpus)


def recommendations(title):  # function that takes in song title as input and returns the top 10 recommended songs
    reco = []
    doc_l = []
    score_l = []
    song_data_with_genre = readdata.read_song_genre()
    song_data_with_genre = song_data_with_genre.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'tid'])
    # Compute similarity against a corpus of documents by storing the sparse index matrix in memory.
    index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=len(dictionary.token2id))
    query_document = title.lower().split()
    query_bow = dictionary.doc2bow(query_document)
    sims = index[tfidf[query_bow]]

    for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
        doc_l.append(document_number)
        score_l.append(score)

    recommended_songs_idx_score = pd.DataFrame(score_l, doc_l).head(10)
    recommended_songs_idx_score = recommended_songs_idx_score.reset_index()
    recommended_songs_idx_score.columns = ['index', 'score']
    recommended_songs_idx_score.set_index('index', inplace=True)

    # song recommendations based on content searched
    for idx in recommended_songs_idx_score.index:
        dict_reco = dict(song_data_with_genre.loc[idx][['title', 'artist_name']])
        reco.append(dict_reco)
    recommended_songs = pd.DataFrame(reco)
    return recommended_songs
