import readdata

song_bow_df = readdata.read_data_gdrive('song_data_bow_df.csv')

def top_senti_recommendation(sentiment,n):  # function that takes in sentiment as input and returns the top recommended songs
    if sentiment == 'sad':
        top_recommendation = song_bow_df[song_bow_df.sentiment_category == sentiment].sort_values(
            by=['Polarity_score'], ascending=True)[:n]
        top_recommendation = top_recommendation.sort_values(by=['artist_familiarity', 'artist_hotttnesss'], ascending=False)
    else:
        top_recommendation = song_bow_df[song_bow_df.sentiment_category == sentiment].sort_values(by=['Polarity_score','artist_familiarity','artist_hotttnesss'], ascending = False)[:n]
    top_recommendation = top_recommendation[
        ['title', 'artist_name', 'release', 'artist_familiarity', 'artist_hotttnesss', 'Polarity_score']]
    top_recommendation.columns = ['title', 'artist_name', 'release', 'familiarity', 'hotness', 'Polarity_score']
    top_recommendation.reset_index(inplace=True)
    top_recommendation.drop(columns='index', inplace = True)
    top_recommendation['sno'] = [x for x in range(1, len(top_recommendation) + 1)]
    top_recommendation.set_index('sno', inplace=True) # setting sno as index
    return top_recommendation
