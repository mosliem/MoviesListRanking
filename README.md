# MoviesListRanking
- Python script for ranking movies saved on local storage by its rating 

## Description 
- It ranks a list of Movies saved on local storage. By only using the directory of the files, it extracts the names of the movies. 
TMDB API for getting The ratings, it exports a txt file with Movies and its rating


#### Python packages needed to install 
      pip install request 
  
#### How to run 
- Account to get an access token from https://developer.themoviedb.org/reference/intro/getting-started 
- Set your access token on Constants.py

       ACCESSTOKEN = Your access token
- Change the pattern of getting the absolute movie name from its file by changing the values of  NOTNEEDEDWORDS list on Constants.py
<br>

<p align="center">

<img src="https://github.com/mosliem/MoviesListRanking/blob/main/IMG-20230529-WA0016.jpg" />

</p>
- Run the script 
                      
       python3 MoviesListRankingMain.py

#### Results 
a txt file containing movies names with its rating

<img src="https://github.com/mosliem/MoviesListRanking/blob/main/IMG-20230529-WA0017.jpg" />


