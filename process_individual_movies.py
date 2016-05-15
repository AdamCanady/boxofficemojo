import os, re, csv

production_budget_pattern = r"Production Budget: <b>([^<]*)</b>"
release_date_pattern = r"""Release Date: <b><nobr><a href="[^"]*">([^<]*)</a>"""
title_pattern = r"""<font face="Verdana" size="6"><b>([^<]*)</b>"""
gross_domestic_pattern = r"Domestic Total Gross: <b>([^<]*)</b>"
release_length_pattern = r"(\d{1,3}) days / \d{1,3} weeks"
num_theaters_pattern = r"<td>&nbsp;([\d,]{1,6}) theaters"
rating_pattern = r"MPAA Rating: <b>([^<]*)</b>"
running_time_pattern = r"Runtime: <b>(\d{1}) hrs\. (\d{2}) min\."

e = open("all_movies.csv", "w")
w = csv.writer(e)

w.writerow(["Title", "ReleaseDate", "ProductionBudget", "TotalBoxOffice", "ReleaseLength", "NumTheaters", "Rating", "Runtime"])

for movie in os.listdir("mojodata"):
  with open("mojodata/{}".format(movie),'r') as f:
    m = f.read().replace("&amp;", "&")

  production_budget = re.findall(production_budget_pattern, m)
  release_date = re.findall(release_date_pattern, m)
  title = re.findall(title_pattern, m)
  gross_domestic = re.findall(gross_domestic_pattern, m)
  release_length = re.findall(release_length_pattern, m)
  num_theaters = re.findall(num_theaters_pattern, m)
  rating = re.findall(rating_pattern, m)
  running_time = re.findall(running_time_pattern, m)

  if title and \
   release_date and \
   production_budget and \
   gross_domestic and \
   release_length and \
   num_theaters and \
   rating and \
   running_time:
    if "million" in production_budget[0]:
      production_budget[0] = production_budget[0].replace(" million","000000").replace("$", "")

    running_time_mins = str(int(running_time[0][0]) * 60 + int(running_time[0][1]))

    gross_domestic[0] = gross_domestic[0].replace("$","").replace(",","")
    w.writerow([title[0], 
      release_date[0], 
      production_budget[0], 
      gross_domestic[0], 
      release_length[0], 
      num_theaters[0].replace(",",""), 
      rating[0], 
      running_time_mins])

