import requests

with open("movie_list.txt", 'r') as f:
  movies = set(f.read().splitlines())

go = False
for movie in movies:
  if "ontheline" in movie: go=True
  if not go: continue
  cur_url = "http://www.boxofficemojo.com" + movie
  print cur_url
  r = requests.get(cur_url)
  title = movie.replace("/movies/?id=","")
  with open("mojodata/{}".format(title), 'w') as f:
    f.write(r.content)
