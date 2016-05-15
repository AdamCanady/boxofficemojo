import requests, re

url = "http://www.boxofficemojo.com/yearly/chart/?page={}&view=releasedate&view2=domestic&yr={}&p=.htm"

ptrn = r'/movies/\?id=[^\.]*\.htm'

all_movies = set()

for year in range(1999,2016):
  for page in range(1,8):
    cur_url = url.format(page, year)
    print cur_url
    r = requests.get(cur_url)    

    for m in re.findall(ptrn, r.content):
      all_movies.add(m)


with open("movie_list.txt", 'w') as f:
  for m in all_movies:
    f.write("{}\n".format(m))
