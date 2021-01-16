import pathlib
import streamlit as st

def staticpath():
    STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
    return STREAMLIT_STATIC_PATH

def datapath(file):
    data_path={
        'gender_classify.pkl': 'https://drive.google.com/file/d/1W-nfgJq5uYQ9qfz-xJTuvs9zGBKILcw9/view?usp=sharing',
               'gensim_sparse_similarities.pkl': 'https://drive.google.com/file/d/1kUZccv741saMZCtjkeLaqvyXQdo0lm_p/view?usp=sharing',
               'gensim_tfidf_model.pkl': 'https://drive.google.com/file/d/13AQ1UXusKC5YM69S-T9rf7fy9TqfeaKe/view?usp=sharing',
               'lyrics_gensim_sparse_similarities.pkl': 'https://drive.google.com/file/d/1nBaBo13mMP8Mulb8m_T011VN1NW1dtB9/view?usp=sharing',
               'lyrics_gensim_tfidf_model.pkl': 'https://drive.google.com/file/d/1VA5AknuqPKRbzSzUCkluQjLi4x3e57IU/view?usp=sharing',
               'lyrics_processed_corpus.pkl': 'https://drive.google.com/file/d/1zyd9Juu2mvaSlOpY08FIBLuH3Z7u6Rit/view?usp=sharing',
               'processed_corpus.pkl': 'https://drive.google.com/file/d/1EisIQHDUo-9LGNUiQty4bnh_tJevKoWw/view?usp=sharing',
               'song_data_with_genre.pkl': 'https://drive.google.com/file/d/1Yy9LIMc1qfpzUEVuL-7AAtaGUGSlu5vI/view?usp=sharing',
               'song_only_imdb_merge.pkl': 'https://drive.google.com/file/d/1nRuS7slV5GqbLN5oggt_aop4-eitu8mv/view?usp=sharing',
               'count_data.csv': 'https://drive.google.com/file/d/1Bg9tYJslW60Aur6DSmRyYtEmlr4NlJJs/view?usp=sharing',
               'count_data.pkl': 'https://drive.google.com/file/d/1xmWrj3bCemUSpklMT-8abocUKrcuw2CX/view?usp=sharing',
               'song_data_with_gender.csv': 'https://drive.google.com/file/d/1Y0dplEjPdN45GS0rpP7PNJAMp7L3Gq7u/view?usp=sharing',
               'song_data.csv': 'https://drive.google.com/file/d/13hyZ-u-wS7sr9zzgluE7ybiiNngI7eVZ/view?usp=sharing',
               'song_data_bow_df.csv':'https://drive.google.com/file/d/19yzVwLr1iiAHdjXvd_VuV5-Hfz85MS4X/view?usp=sharing'
    }
    return data_path[file]
