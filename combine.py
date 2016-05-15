import ucsv as csv
import json

r = csv.DictReader(open("movie_data.csv"))

movies = {}

for row in r:
  fname = "moviejson/{}.json".format(row["Title"])
  print fname
  with open(fname) as f:
    extra_data = json.loads(f.read())

  row.update(extra_data)

  movies[row["Title"]] = row

headers = set()
for movie in movies:
  for key in movies[movie]:
    headers.add(key)

print movies[movies.keys()[0]].keys()
w = csv.DictWriter(open("movie_data_extra.csv","w"), fieldnames=headers)
# w.writeheader()
for movie in movies:
  print movie
  w.writerow(movies[movie])
