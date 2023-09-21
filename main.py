import requests
from bs4 import BeautifulSoup
import random

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")
titles = soup.find_all(name="h3", class_="title")
movies = []

for t in titles:
    title = t.getText()
    movies.append(title)

movies.reverse()

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(movie + "\n")
movie_of_today = random.choice(movies)
print("The movie for today will be: " f"{movie_of_today}")

