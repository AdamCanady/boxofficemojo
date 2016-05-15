import requests

movies = '''American Sniper
Zero Dark Thirty
The Dresser
Letters from Iwo Jima
Dangerous Liaisons
Amour
There Will Be Blood
Selma
Extremely Loud & Incredibly Close
In the Name of the Father
Million Dollar Baby
Her (2013)
Howards End
Silver Linings Playbook
The Crying Game
Gandhi
The Cider House Rules
Nebraska
Chocolat
Platoon
The Killing Fields
My Left Foot
Shine
Frost/Nixon
The Imitation Game
Hope and Glory
Mississippi Burning
Secrets & Lies
The Reader
The Artist
Sideways
Moonstruck
A Passage to India
The King's Speech
In the Bedroom
The Hours
Chicago
Whiplash
Driving Miss Daisy
Slumdog Millionaire
Gosford Park
Shakespeare in Love
127 Hours
Crouching Tiger, Hidden Dragon
Rain Man
Capote
The Aviator
Good Will Hunting
The Pianist
Sense and Sensibility
The Color Purple
Atonement
Brokeback Mountain
The Descendants
Philomena
Schindler's List
Working Girl
Dallas Buyers Club
The Mission
The Last Emperor
Life Is Beautiful
Juno
The Queen
Finding Neverland
Traffic
Scent of a Woman
Babel
Tootsie
The Shawshank Redemption
Django Unchained
The Wolf of Wall Street
American Hustle
L.A. Confidential
The English Patient
Birdman
Les Miserables (2012)
Il Postino
Titanic
The Right Stuff
American Beauty
The Accidental Tourist
An Education
Mystic River
Born on the Fourth of July
A Beautiful Mind
Milk
The Verdict
As Good as It Gets
The Theory of Everything
Broadcast News
Elizabeth 
The Piano
Awakenings
No Country for Old Men
Lost in Translation
Terms of Endearment
12 Years a Slave
Good Night, and Good Luck.
Michael Clayton
Out of Africa
The Fighter
Black Swan
Lincoln
Hugo
Bugsy
Dances with Wolves
Pulp Fiction
Amadeus
Life of Pi
True Grit
Children of a Lesser God
Avatar
The Prince of Tides
The Curious Case of Benjamin Button
The Thin Red Line
JFK
Argo
Jerry Maguire
Beauty and the Beast
Munich
A Room with a View
The Hurt Locker
The Full Monty
Kiss of the Spider Woman
Up in the Air
The Green Mile
The Remains of the Day
A Few Good Men
Beasts of the Southern Wild
Quiz Show
Gangs of New York
Braveheart
The Lord of the Rings: The Fellowship of the Ring
War Horse
Master and Commander: The Far Side of the World
The Departed
Unforgiven
Babe
Saving Private Ryan
The Lord of the Rings: The Return of the King
Places in the Heart
The Big Chill
The Insider
Goodfellas
Fatal Attraction
Gravity
Forrest Gump
The Blind Side
The Godfather Part III
Precious: Based on the Novel "Push" by Sapphire
The Sixth Sense
The Lord of the Rings: The Two Towers
Boyhood
Winter's Bone
E.T.: The Extra-Terrestrial
Ray
The Fugitive
A Soldier's Story
Captain Phillips
The Social Network
Ghost
Fargo
Midnight in Paris
Little Miss Sunshine
Moulin Rouge!
Gladiator
Moneyball
The Help
Seabiscuit
The Silence of the Lambs
Toy Story 3
Inglourious Basterds
The Kids Are All Right
Prizzi's Honor
District 9
Missing
Inception
The Grand Budapest Hotel
Witness
A Serious Man
Crash
Erin Brockovich
Up
Dead Poets Society
Tender Mercies
The Tree of Life
Field of Dreams
Apollo 13
Hannah and Her Sisters
Four Weddings and a Funeral
'''.splitlines()


for movie in movies:
  params = {
    "t": movie,
    "plot": "full",
    "r": "json"
  }

  response = requests.get("http://www.omdbapi.com/", params=params)
  print response.status_code, len(response.content), movie
  with open("moviejson/{}.json".format(movie.replace("/","---")), 'w') as f:
    f.write(response.content)
