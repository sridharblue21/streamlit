# Dhwani App has been developed using streamlitapp

Dhwani is a top songs recommendation engine to help improve customer experience in searching top songs from MSD.
In addition to MSD this has rating data from IMDb which give us average ratings and number of votes, akas data which gives us region, language and title as the key features.
These datasets will help us with a different dimension of rating other than play count to create popularity, content or collaborative based filtering

Objective:
Use transactional user data to develop a recommendation system that can be adopted by online music subscription services like Spotify, Saavn

-created streamlit app with login authentication, 
-added html message styling through style sheets
-modularised the code for easy maintainability.
-used @st.cache to cache data generated using random function
-to use this change path of data files to point to you data location in appconfig.py

Demo video: https://drive.google.com/file/d/1V0IISlYKb7dC_B0bNjQGqsB3OxjkfTuC/view?usp=sharing

Installation procedure:
- Requires Python 3.6 and above (pre-requisite)
- Install PyCharm
- Inside PyCharm venv (virtual environment) pip install the following packages in addition to default python packages such as pandas, numpy
- pip install streamlit
- pip install gensim
- pip install PIL
- pip install scipy
- pip install joblib
- pip install pickle
- pip install urllib
- pip install requests

Run Streamlit inside PyCharm (venv)
- streamlit run main.py

Login as Lachu/MIT@123. Allow datasets to load into memory, this takes about 3-5 minutes. Hurray! You are all set to use the app. Welcome to Dhwani - A million melodies!
