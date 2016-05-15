# import ucsv as csv
import csv, datetime

all_movies = {}
# read all movies
r = csv.DictReader(open("all_movies.csv","r"))
for m in r:
  all_movies[m["Title"]] = m

nominees = []
# read only nominees/winners
r2 = csv.DictReader(open("movie_data_extra_clean.csv","r"))
for m in r2:
  nominees.append(m)
for nominee in nominees:
  title = nominee["Title"]
  if title in all_movies:
    all_movies[title]["Win"] = nominee["Win"]
    all_movies[title]["Oscar"] = 1

for movie in all_movies:
  if "Win" not in all_movies[movie]:
    all_movies[movie]["Win"] = 0
  if "Oscar" not in all_movies[movie]:
    all_movies[movie]["Oscar"] = 0

  if str(all_movies[movie]["Win"]) == "0" and str(all_movies[movie]["Oscar"]) == "1":
    all_movies[movie]["Nom"] = "1"
  else:
    all_movies[movie]["Nom"] = "0"

    # R
    # PG-13
    # PG
    # G
    # Unrated
    # NC-17


  if all_movies[movie]["Rating"] == "R":
    all_movies[movie]["R"] = "1"
  else:
    all_movies[movie]["R"] = "0"

  if all_movies[movie]["Rating"] == "PG-13":
    all_movies[movie]["PG13"] = "1"
  else:
    all_movies[movie]["PG13"] = "0"

  if all_movies[movie]["Rating"] == "PG":
    all_movies[movie]["PG"] = "1"
  else:
    all_movies[movie]["PG"] = "0"

  if all_movies[movie]["Rating"] == "G":
    all_movies[movie]["G"] = "1"
  else:
    all_movies[movie]["G"] = "0"

  if all_movies[movie]["Rating"] == "Unrated":
    all_movies[movie]["Unrated"] = "1"
  else:
    all_movies[movie]["Unrated"] = "0"

  if all_movies[movie]["Rating"] == "NC-17":
    all_movies[movie]["NC17"] = "1"
  else:
    all_movies[movie]["NC17"] = "0"


  all_movies[movie]["ProductionBudget"] = all_movies[movie]["ProductionBudget"].replace(",","").replace("$","")
  if "N/A" in all_movies[movie]["ProductionBudget"]: continue
  if float(all_movies[movie]["ProductionBudget"]) < 100:
    all_movies[movie]["ProductionBudget"] = int(float(all_movies[movie]["ProductionBudget"]) * 1000000)



  # Parse datetime
  # d = datetime.datetime.strptime("%B %d, %Y", all_movies[movie]["ReleaseDate"])
  # q1 = datetime.datetime(d.year, 0,0)
  # q2 = datetime.datetime(d.year, 4, 0)
  # q3 = datetime.datetime(d.year, 7, 0)
  # q4 = datetime.datetime(d.year, 10, 0)

  if any([i in all_movies[movie]["ReleaseDate"] for i in ["January", "February", "March"]]):
    all_movies[movie]["Q1"] = "1"
  else:
    all_movies[movie]["Q1"] = "0"

  if any([i in all_movies[movie]["ReleaseDate"] for i in ["April", "May", "June"]]):
    all_movies[movie]["Q2"] = "1"
  else:
    all_movies[movie]["Q2"] = "0"

  if any([i in all_movies[movie]["ReleaseDate"] for i in ["July", "August", "September"]]):
    all_movies[movie]["Q3"] = "1"
  else:
    all_movies[movie]["Q3"] = "0"

  if any([i in all_movies[movie]["ReleaseDate"] for i in ["October", "November", "December"]]):
    all_movies[movie]["Q4"] = "1"
  else:
    all_movies[movie]["Q4"] = "0"


# write everything
headers = set()
for movie in all_movies:
  for key in all_movies[movie]:
    headers.add(key)
print headers

w = csv.DictWriter(open("movie_data_extra_clean_combined.csv",'w'), fieldnames=headers)
w.writeheader()
for movie in all_movies:
  if all_movies[movie]["ProductionBudget"] == "N/A": continue
  w.writerow(all_movies[movie])
