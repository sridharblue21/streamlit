# following have been done in this streamlitapp

This is a recommendation engine to help improve customer experience in searching top songs from MSD.
In addition to MSD this has rating data from IMDb which give us average ratings and number of votes, akas data which gives us region, language and title as the key features.
These datasets will help us with a different dimension of rating other than play count to create popularity, content or collaborative based filtering

Objective:
Use transactional user data to develop a recommendation system that can be adopted by online music subscription services like Spotify, Saavn

-created streamlit app with login authentication, 
-added html message styling through style sheets
-modularised the code for easy maintainability.
-used @st.cache to cache data generated using random function
-to use this change path of data files to point to you data location in appconfig.py