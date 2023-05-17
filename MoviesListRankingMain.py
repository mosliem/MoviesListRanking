import tkinter as tk
from tkinter import filedialog

import os 

import re 

import requests

import Constants

import movieRatingRequest as ratingReq

from datetime import datetime

from pathlib import Path

import time

def getFolderPath():
 
 folderPath = Path(input("WRITE Movies List Path \n"))
 return folderPath 

def getFolderContentNames(path):
 
 moviesName = []

 with os.scandir(path) as entries:
   for entry in entries:
     moviesName.append(entry.name)  
 return moviesName  


def filterMoviesNames(names):
   ## method 1
   moviesTitles = []

   for name in names:
    newName = re.sub("[\(\[].*?[\)\]]", " ", name)
    newName = re.sub("[-_.]"," ",name)
   
    moviesTitles.append(newName)

   # method 2
   notNeededWords = Constants.NOTNEEDEDWORDS
  
   filteredNames = []
  
   for title in moviesTitles:
     
     words = title.split()

     query = [word for word in words if word.lower() not in notNeededWords and  word.isalpha()] 

     filteredname = ' '.join(query)
     filteredNames.append(filteredname)
    
   return filteredNames


def getMoviesRatings(movies):
   
   moviesRating = {}

   animation = "|/-\\'"
   idx = 0      

   for movie in movies:
      
      ##animation
      print('getting' ,len(movies),'movies ratings', animation[idx % len(animation)], end="\r")
      idx += 1
      time.sleep(0.1)
      
      ## calling request
      rating = ratingReq.requestRating(movie)
      if rating > 0.0:
       moviesRating[movie] = rating
   
   print("Done \u2705 \n")

   return moviesRating
     

def orderMoviesRating(moviesRatings):
   sortedMoviesByRating = sorted(moviesRatings.items(),key = lambda x:x[1],reverse= True)
   return sortedMoviesByRating


def exportRatingsToFile(dirc, movieRatings):

  data = []

  for movieRating in movieRatings:
    string = movieRating[0] + " ====> " + str(movieRating[1])
    data.append(string)

  print("Exporting",len(movieRatings),"Movies Rating into txt")
   
  ## date time for file naming
  dt = datetime.now()
  tformat = dt.strftime("'%d-%m-%Y-%H-%M")

  filePath = Path(dirc)
  fileName =  'MoviesRating'+str(tformat)+'.txt'

  with open(filePath / fileName,'w') as fp:
    for d in data:
      fp.write("%s\n" % d)

 
  print("Done \u2705")
  

def main():
    
    print("WELCOME",'🎥')

    folderPath = getFolderPath()

    moviesList = getFolderContentNames(folderPath)

    filteredMoviesNameList = filterMoviesNames(moviesList)

    moviesRatings = getMoviesRatings(filteredMoviesNameList)

    sortedMoviesRating = orderMoviesRating(moviesRatings)

    filePath = input('Write a dirc to export the movies rating: ')

    exportRatingsToFile(filePath, sortedMoviesRating)




if __name__=="__main__":
    main()
