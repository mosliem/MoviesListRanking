import requests
import Constants

def requestRating(movie):
  
  url = "https://api.themoviedb.org/3/search/movie"

  headers = {
    "accept": "application/json",
    "Authorization": Constants.ACCESSTOKEN
   }

  PARAM = {
    "query": movie,
     "include_adults": True,
     "page": 1
   }
  request = requests.get(url, headers = headers, params = PARAM)

  data = request.json()
  
  
  movieRate = 0.0

    
  try:
    movieRate = data['results'][0]['vote_average']
  except:
    movieRate = -1
    
  return movieRate
