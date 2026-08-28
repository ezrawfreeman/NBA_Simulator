import random

magic_johnson = {
    "name": "Magic Johnson",
    "teams" : ["Lakers"],
    "positions" : ["PG"],
    "pts": 19.5,
    "trb": 7.2,
    "ast": 11.2,
    "defense": 6,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Magic", "Buck"],
    "best_teammates": ["Kareem Abdul-Jabbar","Michael Cooper", "James Worthy"]
}

stephen_curry = {
    "name": "Stephen Curry",
    "teams" : ["Warriors"],
    "positions" : ["PG"],
    "pts": 24.8,
    "trb": 4.7,
    "ast": 6.3,
    "defense":6,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Steph", "Chef Curry", "The Baby-Faced Assassin"],
    "best_teammates": ["Kevin Durant", "Draymond Green", "Klay Thompson"]
}

oscar_robertson = {
    "name": "Oscar Robertson",
    "teams" : ["Kings", "Bucks"],
    "positions" : ["PG", "SG"],
    "pts": 25.7,
    "trb": 7.5,
    "ast": 9.5,
    "defense": 6.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["The Big O"],
    "best_teammates": ["Kareem Abdul-Jabbar"]
}

john_stockton = {
    "name": "John Stockton",
    "teams" : ["Jazz"],
    "positions" : ["PG"],
    "pts": 13.1,
    "trb": 2.7,
    "ast": 10.5,
    "defense": 8,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Stock", "John"],
    "best_teammates":["Karl Malone", "Jeff Hornacek"]
}

jeff_hornacek = {
    "name": "Jeff Hornacek",
    "teams": ["Jazz", "Suns"],
    "positions": ["SG"],
    "pts": 14.5,
    "trb": 3.3,
    "ast": 4.9,
    "defense": 7,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Horny"],
    "best_teammates": ["Karl Malone", "John Stockton"]
}
isiah_thomas = {
    "name": "Isiah Thomas",
    "teams" : ["Pistons"],
    "positions" : ["PG"],
    "pts": 19.2,
    "trb": 3.6,
    "ast": 9.3,
    "defense": 6,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Zeke"],
    "best_teammates": ["Joe Dumars", "Dennis Rodman", "Bil Laimbeer"]
}

chris_paul = {
    "name": "Chris Paul",
    "teams" : ["Clippers", "Pelicans", "Thunder", "Suns"],
    "positions" : ["PG"],
    "pts": 16.8,
    "trb": 4.4,
    "ast": 9.2,
    "defense": 8.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["CP3", "The Point God"],
    "best_teammates": ["Blake Griffin", "James Harden", "Devin Booker"]

}

jason_kidd = {
    "name": "Jason Kidd",
    "teams" : ["Mavericks", "Suns", "Nets"],
    "positions" : ["PG"],
    "pts": 12.6,
    "trb": 6.3,
    "ast": 8.7,
    "defense": 8.5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["J-Kidd"],
    "best_teammates": ["Dirk Nowitzki", "Shawn Marion", "Vince Carter", "Steve Nash"]
}

steve_nash = {
    "name": "Steve Nash",
    "teams" : ["Mavericks", "Suns"],
    "positions" : ["PG"],
    "pts": 14.3,
    "trb": 3.0,
    "ast": 8.5,
    "defense": 3.5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Nash"],
    "best_teammates": ["Dirk Nowitzki", "Shawn Marion", "Amar'e Stoudemire"]
    
}

bob_cousy = {
    "name": "Bob Cousy","positions" : ["PG"],
    "teams" : ["Celtics"],
    "pts": 18.4,
    "trb": 5.2,
    "ast": 7.5,
    "defense": 4.5,
    "eras": ["1950s", "1960s"],
    "nicknames": ["The Hardwood Houdini", "Cooz"],
    "best_teammates": ["Bill Russell", "Bill Sharman"]
}
bill_sharman = {
    "name": "Bill Sharman",
    "teams": ["Celtics", "Capitols"],
    "positions": ["SG"],
    "pts": 17.8,
    "trb": 3.9,
    "ast": 3.0,
    "defense": 7.5,
    "eras": ["1950s", "1960s"],
    "nicknames": ["Bullseye Bill", "Battling Bill", "Willie"],
    "best_teammates": ["Bob Cousy", "Bill Russell", "Tom Heinsohn"]
}
walt_frazier = {
    "name": "Walt Frazier", "positions" : ["PG"],
    "teams" : ["Knicks"],
    "pts": 18.9,
    "trb": 5.9,
    "ast": 6.1,
    "defense": 9.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Clyde"],
    "best_teammates": ["Willis Reed", "Earl Monroe"]
}

michael_jordan = {
    "name": "Michael Jordan",
    "teams" : ["Bulls"],
    "positions" : ["SG"],
    "pts": 30.1,
    "trb": 6.2,
    "ast": 5.3,
    "defense": 9.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["His Airness", "MJ", "Air Jordan"],
    "best_teammates": ["Scottie Pippen","Dennis Rodman", "Steve Kerr"]
}

kobe_bryant = {
    "name": "Kobe Bryant",
    "teams" : ["Lakers"],
    "positions" : ["SG"],
    "pts": 25.0,
    "trb": 5.2,
    "ast": 4.7,
    "defense": 8,
    "eras": ["1990s", "2000s", "2010s"],
    "nicknames": ["Black Mamba", "Kobe"],
    "best_teammates": ["Shaquille O'Neal","Pau Gasol"]
}

dwyane_wade = {
    "name": "Dwyane Wade",
    "teams" : ["Heat"],
    "positions" : ["SG"],
    "pts": 22.0,
    "trb": 4.7,
    "ast": 5.4,
    "defense": 8,
    "eras": ["2000s", "2010s"],
    "nicknames": ["D-Wade", "Flash"],
    "best_teammates": ["Lebron James", "Chris Bosh"]
}

jerry_west = {
    "name": "Jerry West",
    "teams" : ["Lakers"],
    "positions" : ["SG", "PG"],
    "pts": 27.0,
    "trb": 5.8,
    "ast": 6.7,
    "defense": 9,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Mr. Clutch", "The Logo"],
    "best_teammates": [ "Elgin Baylor","Wilt Chamberlain", "Gail Goodrich"]
}

gail_goodrich = {
    "name": "Gail Goodrich",
    "teams": ["Lakers", "Suns", "Jazz"],
    "positions": ["PG", "SG"],
    "pts": 18.6,
    "trb": 3.2,
    "ast": 4.7,
    "defense": 4.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Stumpy", "The Stump"],
    "best_teammates": [
        "Jerry West",
        "Wilt Chamberlain",
        "Elgin Baylor",
        "Kareem Abdul-Jabbar"
    ]
}
james_harden = {
    "name": "James Harden",
    "teams" : ["Thunder", "Rockets", "Nets"],
    "positions" : ["SG", "PG"],
    "pts": 24.0,
    "trb": 5.6,
    "ast": 7.3,
    "defense": 5.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["The Beard"],
    "best_teammates": ["Chris Paul", "Kevin Durant","Russell Westbrook", "Kyrie Irving", "Joel Embiid"]
}

clyde_drexler = {
    "name": "Clyde Drexler",
    "teams" : ["Trail Blazers", "Rockets"],
    "positions" : ["SG", "PG", "SF"],
    "pts": 20.4,
    "trb": 6.1,
    "ast": 5.6, 
    "defense": 7,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Clyde the Glide"],
    "best_teammates": ["Hakeem Olajuwan", "Charles Barkley"]
}

allen_iverson = {
    "name": "Allen Iverson",
    "teams" : ["76ers", "Nuggets"],
    "positions" : ["SG", "PG"],
    "pts": 26.7,
    "trb": 3.7,
    "ast": 6.2,
    "defense": 5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["The Answer", "AI", "Bubba Chucks"],
    "best_teammates": ["Dikembe Mutombo", "Carmelo Anthony"]
}

george_gervin = {
    "name": "George Gervin",
    "teams" : ["Spurs"],
    "positions" : ["SG", "SF"],
    "pts": 25.1,
    "trb": 5.3,
    "ast": 2.6,
    "defense": 4.5,
    "eras": ["1970s", "1980s", "ABA"],
    "nicknames": ["The Iceman", "Ice"],
    "best_teammates": ["JUlius Erving", "Artis Gilmore"]
}

reggie_miller = {
    "name": "Reggie Miller",
    "teams" : ["Pacers"],
    "positions" : ["SG"],
    "pts": 18.2,
    "trb": 3.0,
    "ast": 3.0, 
    "defense": 5,
    "eras": ["1980s", "1990s"],
     "nicknames": ["Reggie"],
     "best_teammates": ["Rik Smits", "Jalen Rose"]
}
rik_smits = {
    "name": "Rik Smits",
    "teams": ["Pacers"],
    "positions": ["C"],
    "pts": 14.8,
    "trb": 6.1,
    "ast": 1.4,
    "defense": 7.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Dunking Dutchman", "Dutch Boy in the Paint", "Dutch"],
    "best_teammates": ["Reggie Miller", "Dale Davis", "Mark Jackson"]
}
rajon_rondo = {
    "name": "Rajon Rondo",
    "teams": ["Celtics", "Pelicans", "Lakers"],
    "positions": ["PG"],
    "pts": 9.8,
    "trb": 4.5,
    "ast": 7.9,
    "defense": 8,
    "eras": ["2000s", "2010s", "2020s"],
    "nicknames": ["Playoff Rondo", "The Maestro"],
    "best_teammates": ["Paul Pierce", "Kevin Garnett", "Ray Allen", "Kobe Bryant", "Anthony Davis"]
}

ray_allen = {
    "name": "Ray Allen",
    "teams" : ["Bucks", "Sonics", "Celtics", "Heat"],
    "positions" : ["SG"],
    "pts": 18.9,
    "trb": 4.1,
    "ast": 3.4, 
    "defense": 6,
    "eras": ["1990s", "2000s", "2010s"],
    "nicknames": ["Ray Ray", "Jesus Shuttlesworth"],
    "best_teammates": ["Kevin Garnett", "Paul Pierce","Rajon Rondo","Lebron James"]
}

shorty_crapponeli = {
    "name": "Shorty Crapponeli",
    "teams" : ["Free Agent"],
    "positions" : ["SG", "PG"],
    "pts": 2.5,
    "trb": 0.3,
    "ast": 0.5,
    "defense": 4,
    "eras": ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"],
    "nicknames" : ["Crapponeli", "Stinker", "Loser McLoser", "The Worst Player on the Court", "The Crapster", "Dr. Lame", "The Midget", "Mr 5 foot 8"],
    "best_teammates": []
    
}

lebron_james = {
    "name": "LeBron James",
    "teams" : ["Cavaliers", "Heat", "Lakers"],
    "positions" : ["SG", "PG", "SF", "PF"],
    "pts": 27.0,
    "trb": 7.5,
    "ast": 7.4,
    "defense": 9,
    "eras": ["2000s", "2010s", "2020s"],
    "nicknames": ["King James", "The Chosen One", "Bron"],
    "best_teammates": []
}

larry_bird = {
    "name": "Larry Bird",
    "teams" : ["Celtics"],
    "positions" : ["SF", "PF"],
    "pts": 24.3,
    "trb": 10.0,
    "ast": 6.3,
    "defense": 8,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Larry Legend", "The Hick from French Lick"],
    "best_teammates": []
}
muggsy_bogues = {
    "name": "Muggsy Bogues",
    "teams": ["Hornets", "Raptors"],
    "positions": ["PG"],
    "pts": 7.7,
    "trb": 2.6,
    "ast": 7.6,
    "defense": 7.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Muggsy"],
    "best_teammates": []
}
chris_bosh = {
    "name": "Chris Bosh",
    "teams": ["Raptors", "Heat"],
    "positions": ["PF", "C"],
    "pts": 19.2,
    "trb": 8.5,
    "ast": 2.0,
    "defense": 8,
    "eras": ["2000s", "2010s"],
    "nicknames": ["CB4", "Bosh"],
    "best_teammates": []
}
vince_carter = {
    "name": "Vince Carter",
    "teams": ["Raptors", "Nets"],
    "positions": ["SG", "SF"],
    "pts": 16.7,
    "trb": 4.3,
    "ast": 3.1,
    "defense": 6.5,
    "eras": ["1990s", "2000s", "2010s"],
    "nicknames": ["Vinsanity", "Half Man Half Amazing", "Air Canada", "VC"],
    "best_teammates": []
}
kyle_lowry = {
    "name": "Kyle Lowry",
    "teams": ["Raptors", "Rockets", "Heat"],
    "positions": ["PG"],
    "pts": 14.3,
    "trb": 4.3,
    "ast": 6.2,
    "defense": 8,
    "eras": ["2000s", "2010s", "2020s"],
    "nicknames": ["K-Low", "Lowry"],
    "best_teammates": []
}
paul_pierce = {
    "name": "Paul Pierce",
    "teams": ["Celtics"],
    "positions": ["SF", "SG"],
    "pts": 19.7,
    "trb": 5.6,
    "ast": 3.5,
    "defense": 6,
    "eras": [ "2000s", "2010s"],
    "nicknames": ["The Truth"],
    "best_teammates": []
}
devin_booker = {
    "name": "Devin Booker",
    "teams": ["Suns"],
    "positions": ["SG"],
    "pts": 24.3,
    "trb": 4.0,
    "ast": 5.0,
    "defense": 5.5,
    "eras": ["2010s", "2020s"],
    "nicknames" : ["D-Book"],
    "best_teammates": []
}
jimmy_butler = {
    "name": "Jimmy Butler",
    "teams": ["Bulls", "Timberwolves", "76ers", "Heat"],
    "positions": ["SG", "SF"],
    "pts": 18.3,
    "trb": 5.3,
    "ast": 4.3,
    "defense": 8,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Jimmy Buckets", "Playoff Jimmy"],
    "best_teammates": []
}
alex_caruso = {
    "name": "Alex Caruso",
    "teams": ["Lakers", "Bulls", "Thunder"],
    "positions": ["PG", "SG"],
    "pts": 6.8,
    "trb": 2.9,
    "ast": 2.9,
    "defense": 9,
    "eras": ["2020s"],
    "nicknames": ["Bald Mamba", "Carushow"],
    "best_teammates": []
}
anthony_edwards = {
    "name": "Anthony Edwards",
    "teams": ["Timberwolves"],
    "positions": ["SG", "SF"],
    "pts": 23.0,
    "trb": 5.2,
    "ast": 4.5,
    "defense": 7,
    "eras": ["2020s"],
    "nicknames": ["Ant-Man"],
    "best_teammates": []
}
karl_anthony_towns = {
    "name": "Karl-Anthony Towns",
    "teams": ["Timberwolves"],
    "positions": ["C", "PF"],
    "pts": 22.9,
    "trb": 10.4,
    "ast": 3.0,
    "defense": 6,
    "eras": ["2010s", "2020s"],
    "nicknames": ["KAT", "The Big KAT"],
    "best_teammates": []
}
joel_embiid = {
    "name": "Joel Embiid",
    "teams": ["76ers"],
    "positions": ["C"],
    "pts": 27.7,
    "trb": 11.0,
    "ast": 3.5,
    "defense": 8.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["The Process", "JoJo"],
    "best_teammates": []
}
paul_george = {
    "name": "Paul George",
    "teams": ["Pacers", "Thunder", "Clippers"],
    "positions": ["SG", "SF"],
    "pts": 19.5,
    "trb": 6.4,
    "ast": 3.7,
    "defense": 8.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["PG-13", "Playoff P", "Young Trece", "Pandemic P"],
    "best_teammates": []
}
klay_thompson = {
    "name": "Klay Thompson",
    "teams": ["Warriors"],
    "positions": ["SG", "SF"],
    "pts": 19.6,
    "trb": 3.5,
    "ast": 2.3,
    "defense": 8,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Splash Brother", "Game 6 Klay", "Killa Klay", "Kaptain Klay"],
    "best_teammates": []
}
draymond_green = {
    "name": "Draymond Green",
    "teams": ["Warriors"],
    "positions": ["PF", "C"],
    "pts": 8.7,
    "trb": 7.0,
    "ast": 5.6,
    "defense": 10,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Dray", "The Dancing Bear", "Triple Single"],
    "best_teammates": []
}
robert_horry = {
    "name": "Robert Horry",
    "teams": ["Rockets", "Lakers", "Spurs"],
    "positions": ["PF", "SF"],
    "pts": 7.0,
    "trb": 4.8,
    "ast": 2.1,
    "defense": 7,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Big Shot Bob"],
    "best_teammates": []
}
james_worthy = {
    "name": "James Worthy",
    "teams": ["Lakers"],
    "positions": ["SF", "PF"],
    "pts": 17.6,
    "trb": 5.1,
    "ast": 3.0,
    "defense": 7.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Big Game James"],
    "best_teammates": []
}

dwight_howard = {
    "name": "Dwight Howard",
    "teams": ["Magic", "Lakers"],
    "positions": ["C"],
    "pts": 15.7,
    "trb": 11.8,
    "ast": 1.4,
    "defense": 9.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Superman", "D-12"],
    "best_teammates": []
}
kyrie_irving = {
    "name": "Kyrie Irving",
    "teams": ["Cavaliers", "Celtics", "Nets", "Mavericks"],
    "positions": ["PG", "SG"],
    "pts": 23.7,
    "trb": 4.1,
    "ast": 5.6,
    "defense": 5.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Uncle Drew", "Kai"],
    "best_teammates": []
}
damian_lillard = {
    "name": "Damian Lillard",
    "teams": ["Trail Blazers", "Bucks"],
    "positions": ["PG"],
    "pts": 25.1,
    "trb": 4.2,
    "ast": 6.7,
    "defense": 5.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Dame D.O.L.L.A.", "Dame Time"],
    "best_teammates": []
}
pau_gasol = {
    "name": "Pau Gasol",
    "teams": ["Grizzlies", "Lakers"],
    "positions": ["PF", "C"],
    "pts": 17.0,
    "trb": 9.2,
    "ast": 3.2,
    "defense": 7,
    "eras": ["2000s", "2010s"],
    "nicknames": ["The Spaniard"],
    "best_teammates": []
}
marc_gasol = {
    "name": "Marc Gasol",
    "teams": ["Grizzlies", "Raptors", "Lakers"],
    "positions": ["C"],
    "pts": 14.0,
    "trb": 7.4,
    "ast": 3.4,
    "defense": 9,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Big Spain"],
    "best_teammates": []
}
brook_lopez = {
    "name": "Brook Lopez",
    "teams": ["Nets", "Bucks"],
    "positions": ["C"],
    "pts": 16.1,
    "trb": 5.2,
    "ast": 1.4,
    "defense": 8.5,
    "eras": ["2000s", "2010s", "2020s"],
    "nicknames": ["Splash Mountain"],
    "best_teammates": []
}
robin_lopez = {
    "name": "Robin Lopez",
    "teams": ["Suns", "Trail Blazers", "Bulls", "Bucks"],
    "positions": ["C"],
    "pts": 8.5,
    "trb": 4.8,
    "ast": 0.8,
    "defense": 7,
    "eras": ["2000s", "2010s", "2020s"],
    "nicknames": ["RoLo"],
    "best_teammates": []
}
shawn_marion = {
    "name": "Shawn Marion",
    "teams": ["Suns", "Mavericks"],
    "positions": ["SF", "PF"],
    "pts": 15.2,
    "trb": 8.7,
    "ast": 1.9,
    "defense": 8.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["The Matrix"],
    "best_teammates": []
}
tracy_mcgrady = {
    "name": "Tracy McGrady",
    "teams": ["Raptors", "Magic", "Rockets"],
    "positions": ["SG", "SF"],
    "pts": 19.6,
    "trb": 5.6,
    "ast": 4.4,
    "defense": 6.5,
    "eras": [ "2000s"],
    "nicknames": ["T-Mac"],
    "best_teammates": []
}
yao_ming = {
    "name": "Yao Ming",
    "teams": ["Rockets"],
    "positions": ["C"],
    "pts": 19.0,
    "trb": 9.2,
    "ast": 1.6,
    "defense": 7.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["The Ming Dynasty"],
    "best_teammates": []
}
donovan_mitchell = {
    "name": "Donovan Mitchell",
    "teams": ["Jazz", "Cavaliers"],
    "positions": ["SG", "PG"],
    "pts": 24.8,
    "trb": 4.3,
    "ast": 4.8,
    "defense": 6.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Spida"],
    "best_teammates": []
}
kevin_love = {
    "name": "Kevin Love",
    "teams": ["Cavaliers", "Timberwolves"],
    "positions": ["PF", "C"],
    "pts": 16.0,
    "trb": 9.9,
    "ast": 2.4,
    "defense": 5.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["K-Love"],
    "best_teammates": []
}
alonzo_mourning = {
    "name": "Alonzo Mourning",
    "teams": ["Hornets", "Heat"],
    "positions": ["C"],
    "pts": 17.1,
    "trb": 8.5,
    "ast": 1.1,
    "defense": 9.5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Zo"],
    "best_teammates": []
}
gary_payton = {
    "name": "Gary Payton",
    "teams": ["Sonics"],
    "positions": ["PG"],
    "pts": 16.3,
    "trb": 3.9,
    "ast": 6.7,
    "defense": 10,
    "eras": ["1990s", "2000s"],
    "nicknames": ["The Glove"],
    "best_teammates": []
}
detlef_schrempf = {
    "name": "Detlef Schrempf",
    "teams": ["Sonics"],
    "positions": ["SF", "PF"],
    "pts": 13.9,
    "trb": 6.2,
    "ast": 3.4,
    "defense": 6,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Det the Threat", "The Grand Teuton"],
    "best_teammates": []
}
derrick_rose = {
    "name": "Derrick Rose",
    "teams": ["Bulls"],
    "positions": ["PG"],
    "pts": 17.4,
    "trb": 3.2,
    "ast": 5.2,
    "defense": 5.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["D-Rose"],
    "best_teammates": []
}
jeremy_lin = {
    "name": "Jeremy Lin",
    "teams": ["Knicks"],
    "positions": ["PG"],
    "pts": 11.6,
    "trb": 2.8,
    "ast": 4.3,
    "defense": 5.5,
    "eras": ["2010s"],
    "nicknames": ["Linsanity"],
    "best_teammates": []
}
russell_westbrook = {
    "name": "Russell Westbrook",
    "teams": ["Thunder", "Wizards"],
    "positions": ["PG"],
    "pts": 21.7,
    "trb": 7.1,
    "ast": 8.1,
    "defense": 6,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Brodie", "Russ", "Mr. Triple-Double"],
    "best_teammates": []
}
andrew_wiggins = {
    "name": "Andrew Wiggins",
    "teams": ["Timberwolves"],
    "positions": ["SF"],
    "pts": 18.5,
    "trb": 4.8,
    "ast": 2.3,
    "defense": 7,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Maple Jordan", "The Wigginator"],
    "best_teammates": []
}
nick_young = {
    "name": "Nick Young",
    "teams": ["Lakers"],
    "positions": ["SG", "SF"],
    "pts": 11.4,
    "trb": 2.0,
    "ast": 1.0,
    "defense": 4,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Swaggy P", "Bean Burrito"],
    "best_teammates": []
}
dennis_johnson = {
    "name": "Dennis Johnson",
    "teams": ["Celtics", "Sonics"],
    "positions": ["PG", "SG"],
    "pts": 14.1,
    "trb": 3.9,
    "ast": 5.0,
    "defense": 9,
    "eras": ["1970s", "1980s"],
    "nicknames": ["DJ"],
    "best_teammates": []
}
willis_reed = {
    "name": "Willis Reed",
    "teams": ["Knicks"],
    "positions": ["PF", "C"],
    "pts": 18.7,
    "trb": 12.9,
    "ast": 1.8,
    "defense": 8.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["The Captain"],
    "best_teammates": []
}
dave_cowens = {
    "name": "Dave Cowens",
    "teams": ["Celtics"],
    "positions": ["C"],
    "pts": 17.6,
    "trb": 13.6,
    "ast": 3.8,
    "defense": 8,
    "eras": ["1970s", "1980s"],
    "nicknames": ["The Whistler"],
    "best_teammates": []
}
alex_english = {
    "name": "Alex English",
    "teams": ["Nuggets"],
    "positions": ["SF"],
    "pts": 21.5,
    "trb": 5.5,
    "ast": 3.6,
    "defense": 5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Blade", "Mr. Silky Smooth", "Mr. Nugget"],
    "best_teammates": []
}
paul_arizin = {
    "name": "Paul Arizin",
    "teams": ["Warriors"],
    "positions": ["SF"],
    "pts": 22.8,
    "trb": 8.6,
    "ast": 2.3,
    "defense": 6,
    "eras": ["1950s", "1960s"],
    "nicknames": ["Pitchin' Paul"],
    "best_teammates": []
}
george_mikan = {
    "name": "George Mikan",
    "teams": ["Lakers"],
    "positions": ["C"],
    "pts": 23.1,
    "trb": 13.4,
    "ast": 2.8,
    "defense": 8,
    "eras": ["1950s"],
    "nicknames": ["Mr. Basketball"],
    "best_teammates": []
}
chris_webber = {
    "name": "Chris Webber",
    "teams": ["Kings"],
    "positions": ["PF", "C"],
    "pts": 20.7,
    "trb": 9.8,
    "ast": 4.2,
    "defense": 7,
    "eras": ["1990s", "2000s"],
    "nicknames": ["C-Webb"],
    "best_teammates": []
}
manu_ginobili = {
    "name": "Manu Ginobili",
    "teams": ["Spurs"],
    "positions": ["SG"],
    "pts": 13.3,
    "trb": 3.5,
    "ast": 3.8,
    "defense": 8,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Manu", "Manudona"],
    "best_teammates": []
}
tony_parker = {
    "name": "Tony Parker",
    "teams": ["Spurs"],
    "positions": ["PG"],
    "pts": 15.5,
    "trb": 2.7,
    "ast": 5.6,
    "defense": 6.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["TP"],
    "best_teammates": []
}
shawn_kemp = {
    "name": "Shawn Kemp",
    "teams": ["Sonics", "Cavaliers"],
    "positions": ["PF"],
    "pts": 14.6,
    "trb": 8.4,
    "ast": 1.6,
    "defense": 7,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Reign Man", "Dr Dunkenstein"],
    "best_teammates": []
}
kevin_durant = {
    "name": "Kevin Durant",
    "teams" : ["Thunder", "Warriors", "Nets", "Suns"],
    "positions" : ["SF", "PF", "SG"],
    "pts": 27.3,
    "trb": 6.7,
    "ast": 4.4,
    "defense":8,
    "eras": ["2010s", "2020s"],
    "nicknames": ["KD", "Slim Reaper", "Durantula"],
    "best_teammates": []
}

julius_erving = {
    "name": "Julius Erving",
    "teams" : ["Nets", "76ers"],
    "positions" : ["SG", "SF"],
    "pts": 22.0,
    "trb": 6.7,
    "ast": 3.9,
    "defense": 8.5,
    "eras": ["1970s", "1980s", "ABA"],
    "nicknames": ["Dr. J"],
    "best_teammates": []
}

kawhi_leonard = {
    "name": "Kawhi Leonard",
    "teams" : ["Spurs", "Raptors", "Clippers"],
    "positions" : ["SG", "SF", "PF"],
    "pts": 19.6,
    "trb": 6.4,
    "ast": 3.0,
    "defense": 9.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["The Klaw"],
    "best_teammates": []
}

elgin_baylor = {
    "name": "Elgin Baylor",
    "teams" : ["Lakers"],
    "positions" : ["SF"],
    "pts": 27.4,
    "trb": 13.5,
    "ast": 4.3,
    "defense": 6.5,
    "eras": ["1960s"],
    "nicknames": ["Elgin"]
}

scottie_pippen = {
    "name": "Scottie Pippen",
    "teams" : ["Bulls", "Trail Blazers"],
    "positions" : ["SF"],
    "pts": 16.1,
    "trb": 6.4,
    "ast": 5.2,
    "defense": 9.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Pip", "Scottie"],
    "best_teammates": []
}

john_havlicek = {
    "name": "John Havlicek",
    "teams" : ["Celtics"],
    "positions" : ["SG", "SF"],
    "pts": 20.8,
    "trb": 6.3,
    "ast": 4.8,
    "defense": 9,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Hondo"],
    "best_teammates": []
}

rick_barry = {
    "name": "Rick Barry",
    "teams" : ["Warriors"],
    "positions" : ["SF"],
    "pts": 23.2,
    "trb": 6.5,
    "ast": 3.9,
    "defense": 6.5,
    "eras": ["1960s", "1970s", "ABA"],
    "nicknames": ["The Miami Greyhound"],
    "best_teammates": []
}

dominique_wilkins = {
    "name": "Dominique Wilkins",
    "teams" : ["Hawks"],
    "positions" : ["SF"],
    "pts": 24.8,
    "trb": 6.7,
    "ast": 2.5,
    "defense": 5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Human Highlight Film"]
}

tim_duncan = {
    "name": "Tim Duncan",
    "teams" : ["Spurs"],
    "positions" : ["PF", "C"],
    "pts": 19.0,
    "trb": 10.8,
    "ast": 3.0,
    "defense": 9.5,
    "eras": ["1990s", "2000s", "2010s"],
    "nicknames": ["The Big Fundamental"],
    "best_teammates": []
}

karl_malone = {
    "name": "Karl Malone",
    "teams" : ["Jazz"],
    "positions" : ["PF"],
    "pts": 25.0,
    "trb": 10.1,
    "ast": 3.6, 
    "defense": 7.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Mailman"],
    "best_teammates": []
}

kevin_garnett = {
    "name": "Kevin Garnett",
    "teams" : ["Timberwolves", "Celtics"],
    "positions" : ["PF", "C"],
    "pts": 17.8,
    "trb": 10.0,
    "ast": 3.7,
    "defense": 9,
    "eras": ["1990s", "2000s", "2010s"],
    "nicknames": ["KG", "The Big Ticket"],
    "best_teammates": []
}

dirk_nowitzki = {
    "name": "Dirk Nowitzki",
    "teams" : ["Mavericks"],
    "positions" : ["PF"],
    "pts": 20.7,
    "trb": 7.5,
    "ast": 2.4,
    "defense": 5,
    "eras": ["1990s", "2000s", "2010s"],
    "nicknames": ["Dirk", "The Diggler", "The Dunking Deutshman"],
    "best_teammates": []
}

giannis_antetokounmpo = {
    "name": "Giannis Antetokounmpo",
    "teams" : ["Bucks"],
    "positions" : ["SF", "PF"],
    "pts": 24.0,
    "trb": 9.9,
    "ast": 5.0, 
    "defense": 9,
    "eras": ["2010s", "2020s"],
    "nicknames": ["The Greek Freak"],
    "best_teammates": []
}

charles_barkley = {
    "name": "Charles Barkley",
    "teams" : ["76ers", "Suns"],
    "positions" : ["PF"],
    "pts": 22.1,
    "trb": 11.7,
    "ast": 3.9,
    "defense" : 4.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Sir Charles", "The Round Mound of Rebound"],
    "best_teammates": []
}

bob_pettit = {
    "name": "Bob Pettit",
    "teams" : ["Hawks"],
    "positions" : ["PF", "C"],
    "pts": 26.4,
    "trb": 16.2,
    "ast": 3.0,
    "defense": 7.5,
    "eras": ["1950s", "1960s"],
    "nicknames": ["Big Blue", "Dixie Dandy"],
    "best_teammates": []
}

anthony_davis = {
    "name": "Anthony Davis",
    "teams" : ["Pelicans", "Lakers"],
    "positions" : ["PF", "C"],
    "pts": 24.0,
    "trb": 10.7,
    "ast": 2.5,
    "defense": 9,
    "eras": ["2010s", "2020s"],
    "nicknames": ["AD", "The Brow"],
    "best_teammates": []
}

kevin_mchale = {
    "name": "Kevin McHale",
    "teams" : ["Celtics"],
    "positions" : ["PF", "C"],
    "pts": 17.9,
    "trb": 7.3,
    "ast": 1.7,
    "defense": 8.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Black Hole", "The Torture Chamber"],
    "best_teammates": []
}

elvin_hayes = {
    "name": "Elvin Hayes",
    "teams" : ["Rockets", "Wizards"],
    "positions" : ["PF", "C"],
    "pts": 21.0,
    "trb": 12.5,
    "ast": 1.8,
    "defense": 7.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["The Big E", "The Bionic Man"],
    "best_teammates": []
    
}

kareem_abdul_jabbar = {
    "name": "Kareem Abdul-Jabbar",
    "teams" : ["Bucks", "Lakers"],
    "positions" : ["C"],
    "pts": 24.6,
    "trb": 11.2,
    "ast": 3.6,
    "defense": 8,
    "eras": [ "1970s", "1980s"],
    "nicknames": ["Cap"],
    "best_teammates": []
}

bill_russell = {
    "name": "Bill Russell",
    "teams" : ["Celtics"],
    "positions" : [ "C"],
    "pts": 15.1,
    "trb": 22.5,
    "ast": 4.3,
    "defense": 9.5,
    "eras": ["1950s", "1960s"],
    "nicknames": ["The Secretary of Defense", "Mr. 11 Rings"],
    "best_teammates": []
}

wilt_chamberlain = {
    "name": "Wilt Chamberlain",
    "teams" : ["Warriors", "76ers", "Lakers"],
    "positions" : ["C"],
    "pts": 30.1,
    "trb": 22.9,
    "ast": 4.4,
    "defense": 9.5,
    "eras": ["1950s", "1960s", "1970s"],
    "nicknames": ["Wilt the Stilt", "The Big Dipper"],
    "best_teammates": []
}

hakeem_olajuwon = {
    "name": "Hakeem Olajuwon",
    "teams" : ["Rockets"],
    "positions" : ["C"],
    "pts": 21.8,
    "trb": 11.1,
    "ast": 2.5,
    "defense": 10,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Dream"],
    "best_teammates": []
}

shaquille_oneal = {
    "name": "Shaquille O'Neal",
    "teams" : ["Magic", "Lakers", "Heat"],
    "positions" : ["C"],
    "pts": 23.7,
    "trb": 10.9,
    "ast": 2.5,
    "defense": 8,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Shaq", "The Diesel", "Superman", "The Big Aristotle"],
    "best_teammates": []
}

nikola_jokic = {
    "name": "Nikola Jokic",
    "teams" : ["Nuggets"],
    "positions" : ["C"],
    "pts": 21.2,
    "trb": 10.9,
    "ast": 7.0,
    "defense": 6.5,
    "eras": ["2020s"],
    "nicknames": ["The Joker"],
    "best_teammates": []

}

moses_malone = {
    "name": "Moses Malone",
    "teams" : ["Rockets", "76ers", "Wizards", "Hawks"],
    "positions" : ["PF", "C"],
    "pts": 20.6,
    "trb": 12.2,
    "ast": 1.4, 
    "defense": 6,
    "eras": ["1970s", "1980s", "ABA"],
    "nicknames": ["The Chairman of the Boards", "Big Mo"],
    "best_teammates": []
}

david_robinson = {
    "name": "David Robinson",
    "teams" : ["Spurs"],
    "positions" : ["C"],
    "pts": 21.1,
    "trb": 10.6,
    "ast": 2.5,
    "defense": 9.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Admiral"],
    "best_teammates": []
}

patrick_ewing = {
    "name": "Patrick Ewing",
    "teams" : ["Knicks"],
    "positions" : ["C"],
    "pts": 21.0,
    "trb": 9.8,
    "ast": 1.9,
    "defense": 8.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Big Pat"],
    "best_teammates": []
}

bill_walton = {
    "name": "Bill Walton",
    "teams" : ["Trail Blazers", "Celtics"],
    "positions" : ["C"],
    "pts": 13.3,
    "trb": 10.5,
    "ast": 3.4,
    "defense": 9,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Big Red", "Grateful Red", "The Red Baron"],
    "best_teammates": []
}

shai_gilgeousalexander = {
    "name": "Shai Gilgeous-Alexander",
    "teams" : ["Thunder"],
    "positions" : ["PG", "SG"],
    "pts": 25.3,
    "trb": 4.7,
    "ast": 5.3,
    "defense": 7,
    "eras" : ["2020s"],
    "nicknames" : ["SGA", "The Free Throw Merchant"],
    "best_teammates": []
    
}

victor_wembanyama = {
    "name": "Victor Wembanyama",
    "teams" : ["Spurs"],
    "positions" : ["C", "PF"],
    "pts": 23.4,
    "trb": 11.0,
    "ast": 3.5,
    "defense": 11,
    "eras": ["2020s"],
    "nicknames" : ["Wemby", "The Alien"],
    "best_teammates": []
}

luka_doncic = {
    "name": "Luka Doncic",
    "teams" : ["Mavericks", "Lakers"],
    "positions" : ["PG", "SG"],
    "pts": 29.2,
    "trb": 8.5,
    "ast": 8.2,
    "defense": 5,
    "eras": ["2020s"],
    "nicknames" : ["Luka Magic", "The Don"],
    "best_teammates": []
}

cade_cunningham = {
    "name": "Cade Cunningham",
    "teams" : ["Pistons"],
    "positions" : ["PG", "SG"],
    "pts": 22.5,
    "trb": 5.4,
    "ast": 8.0,
    "defense": 6.5,
    "eras": ["2020s"],
    "nicknames" : ["MotorCade", "Deuce"],
    "best_teammates": []
}

jayson_tatum = {
    "name": "Jayson Tatum",
    "teams" : ["Celtics"],
    "positions" : ["SF", "PF"],
    "pts": 23.5,
    "trb": 7.4,
    "ast": 3.9,
    "defense": 8,
    "eras": ["2020s", "2010s"],
    "nicknames" : ["JT", "Taco Jay", "The Anomaly"],
    "best_teammates": []
}

jaylen_brown = {
    "name": "Jaylen Brown",
    "teams" : ["Celtics"],
    "positions" : ["SG", "SF"],
    "pts": 20.0,
    "trb": 5.5,
    "ast": 2.9,
    "defense": 7.5,
    "eras": ["2020s", "2010s"],
    "nicknames" : ["JB", "Juice", "Gravedigger", "Young Beard"],
    "best_teammates": []
}

jalen_brunson = {
    "name": "Jalen Brunson",
    "teams" : ["Mavericks", "Knicks"],
    "positions" : ["PG", "SG"],
    "pts": 26,
    "trb": 3.3,
    "ast": 6.8,
    "defense": 4,
    "eras": ["2020s"],
    "nicknames" : ["Captain Clutch", "The Brunson Burner"],
    "best_teammates": []
}
bob_mcadoo = {
    "name": "Bob McAdoo",
    "teams": ["Clippers"],
    "positions": ["PF", "C"],
    "pts": 22.1,
    "trb": 9.4,
    "ast": 2.3,
    "defense": 6,
    "eras": ["1970s", "1980s"],
    "nicknames" : ["Doo", "Mac"],
    "best_teammates": []
}
robert_parish = {
    "name": "Robert Parish",
    "teams": ["Celtics", "Warriors"],
    "positions": ["C"],
    "pts": 14.5,
    "trb": 9.1,
    "ast": 1.4,
    "defense": 8,
    "eras": ["1970s", "1980s", "1990s"],
    "nicknames" : ["The Chief"],
    "best_teammates": []
}
ben_wallace = {
    "name": "Ben Wallace",
    "teams": ["Pistons", "Magic"],
    "positions": ["C", "PF"],
    "pts": 5.7,
    "trb": 9.6,
    "ast": 1.3,
    "defense": 10,
    "eras": ["2000s", "2010s"],
    "nicknames" : ["Big Ben"],
    "best_teammates": []
}
jermaine_oneal = {
    "name": "Jermaine O'Neal",
    "teams": ["Pacers", "Trail Blazers", "Heat"],
    "positions": ["PF", "C"],
    "pts": 18.6,
    "trb": 9.6,
    "ast": 2.7,
    "defense": 8,
    "eras": ["2000s", "2010s"],
    "nicknames" : ["J.O."],
    "best_teammates": []
}
amare_stoudemire = {
    "name": "Amar'e Stoudemire",
    "teams": ["Suns", "Knicks"],
    "positions": ["PF", "C"],
    "pts": 18.9,
    "trb": 7.8,
    "ast": 1.2,
    "defense": 5.5,
    "eras": ["2000s", "2010s"],
    "nicknames" : ["STAT"],
    "best_teammates": []
}
john_starks = {
    "name": "John Starks",
    "teams": ["Knicks"],
    "positions": ["SG"],
    "pts": 12.5,
    "trb": 2.5,
    "ast": 3.6,
    "defense": 7,
    "eras": ["1990s", "2000s"],
    "nicknames" : ["Starsky"],
    "best_teammates": []
}
deron_williams = {
    "name": "Deron Williams",
    "teams": ["Jazz", "Nets", "Mavericks"],
    "positions": ["PG"],
    "pts": 16.3,
    "trb": 3.1,
    "ast": 8.1,
    "defense": 6.5,
    "eras": ["2000s", "2010s"],
    "nicknames" : ["D-Will"],
    "best_teammates": []
}
dennis_rodman = {
    "name": "Dennis Rodman",
    "teams": ["Pistons", "Bulls", "Spurs"],
    "positions": ["SF", "PF"],
    "pts": 7.3,
    "trb": 13.1,
    "ast": 1.8,
    "defense": 10,
    "eras": ["1980s", "1990s"],
    "nicknames" : ["The Worm", "Dennis the Menace"],
    "best_teammates": []
}
trae_young = {
    "name": "Trae Young",
    "teams": ["Hawks"],
    "positions": ["PG"],
    "pts": 25.3,
    "trb": 3.5,
    "ast": 9.3,
    "defense": 3.5,
    "eras": [ "2020s"],
    "nicknames" : ["Ice Trae"],
    "best_teammates": []
}
al_horford = {
    "name": "Al Horford",
    "teams": ["Hawks", "Celtics", "76ers"],
    "positions": ["PF", "C"],
    "pts": 13.9,
    "trb": 8.2,
    "ast": 3.2,
    "defense": 8,
    "eras": ["2000s", "2010s", "2020s"],
    "nicknames" : ["Big Al", "Big-Game Al", "The Godfather"],
    "best_teammates": []
}
dikembe_mutombo = {
    "name": "Dikembe Mutombo",
    "teams": ["Nuggets", "Hawks", "76ers"],
    "positions": ["C"],
    "pts": 9.8,
    "trb": 10.3,
    "ast": 1.0,
    "defense": 10,
    "eras": ["1990s", "2000s"],
    "nicknames" : ["Mt. Mutombo", "The Wag"],
    "best_teammates": []
}
rudy_gobert = {
    "name": "Rudy Gobert",
    "teams": ["Jazz", "Timberwolves"],
    "positions": ["C"],
    "pts": 12.5,
    "trb": 11.7,
    "ast": 1.3,
    "defense": 10,
    "eras": ["2010s", "2020s"],
    "nicknames" : ["The Stifle Tower", "The French Rejection"],
    "best_teammates": []
}
chris_andersen = {
    "name": "Chris Andersen",
    "teams": ["Nuggets", "Heat"],
    "positions": ["PF", "C"],
    "pts": 5.4,
    "trb": 5.0,
    "ast": 0.5,
    "defense": 8,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Birdman"],
    "best_teammates": []
}
carmelo_anthony = {
    "name": "Carmelo Anthony",
    "teams": ["Nuggets", "Knicks"],
    "positions": ["SF", "PF"],
    "pts": 22.5,
    "trb": 6.2,
    "ast": 2.7,
    "defense": 5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Melo", "Hoodie Melo"],
    "best_teammates": []
}
harrison_barnes = {
    "name": "Harrison Barnes",
    "teams": ["Warriors", "Mavericks", "Kings", "Spurs"],
    "positions": ["SF", "PF"],
    "pts": 13.7,
    "trb": 4.9,
    "ast": 1.8,
    "defense": 6,
    "eras": ["2010s", "2020s"],
    "nicknames": ["The Black Falcon"],
    "best_teammates": []
}
gus_williams = {
    "name": "Gus Williams",
    "teams": ["Sonics"],
    "positions": ["PG"],
    "pts": 19.0,
    "trb": 3.5,
    "ast": 6.0,
    "defense": 7.0,
    "eras": ["1970s", "1980s"],
    "nicknames": ["The Wizard"],
    "best_teammates": []
    
}
fred_brown = {
    "name": "Fred Brown",
    "teams": ["Sonics"],
    "positions": ["SG"],
    "pts": 14.6,
    "trb": 2.7,
    "ast": 3.3,
    "defense": 6.0,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Downtown Freddie Brown", "Downtown"],
    "best_teammates": []
    
}
rashard_lewis = {
    "name": "Rashard Lewis",
    "teams": ["Sonics", "Magic"],
    "positions": ["SF", "PF"],
    "pts": 16.3,
    "trb": 5.7,
    "ast": 2.3,
    "defense": 6.0,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Sweet Lew", "Rashard"],
    "player_type": "NBA",
    "best_teammates": []
}
jack_sikma = {
    "name": "Jack Sikma",
    "teams": ["Sonics", "Bucks"],
    "positions": ["C"],
    "pts": 15.6,
    "trb": 9.8,
    "ast": 3.2,
    "defense": 7.0,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Sikko"],
    "best_teammates": []
}
spencer_haywood = {
    "name": "Spencer Haywood",
    "teams": ["Sonics", "Knicks", "Lakers", "Wizards"],
    "positions": ["PF", "C"],
    "pts": 20.3,
    "trb": 10.3,
    "ast": 1.8,
    "defense": 6.0,
    "eras": ["1960s", "1970s", "ABA"],
    "nicknames": ["The Stallion", "Wood", "Driftwood"],
    "best_teammates": []
}
bob_rule = {
    "name": "Bob Rule",
    "teams": ["Sonics"],
    "positions": ["PF", "C"],
    "pts": 18.7,
    "trb": 9.5,
    "ast": 2.0,
    "defense": 5.0,
    "eras": ["1960s", "1970s"],
    "nicknames": ["The Axe"],
    "best_teammates": []
}
lenny_wilkens = {
    "name": "Lenny Wilkens",
    "teams": ["Hawks", "Sonics"],
    "positions": ["PG"],
    "pts": 16.5,
    "trb": 4.5,
    "ast": 7.4,
    "defense": 7.0,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Sweetie Cakes", "Sweetwater"],
    "player_type": "NBA",
    "best_teammates": []
}
lou_hudson = {
    "name": "Lou Hudson",
    "teams": ["Hawks"],
    "positions": ["SG"],
    "pts": 20.2,
    "trb": 4.4,
    "ast": 2.7,
    "defense": 6.0,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Sweet Lou"],
    "player_type": "NBA",
    "best_teammates": []
}
pete_maravich = {
    "name": "Pete Maravich",
    "teams": ["Hawks", "Jazz"],
    "positions": ["PG", "SG"],
    "pts": 24.2,
    "trb": 4.2,
    "ast": 5.4,
    "defense": 3.5,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Pistol Pete", "The Pistol"],
    "player_type": "NBA",
    "best_teammates": []
}
joe_johnson = {
    "name": "Joe Johnson",
    "teams": ["Hawks", "Nets"],
    "positions": ["SG", "SF"],
    "pts": 16.2,
    "trb": 4.0,
    "ast": 3.9,
    "defense": 6.0,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Iso Joe"],
    "player_type": "NBA",
    "best_teammates": []
}
cliff_hagan = {
    "name": "Cliff Hagan",
    "teams": ["Hawks"],
    "positions": ["SF", "PF"],
    "pts": 18.0,
    "trb": 6.9,
    "ast": 3.0,
    "defense": 7.5,
    "eras": ["1950s", "1960s"],
    "nicknames": [
        "Hag",
        "The Kentucky Colonel"
    ],
    "player_type": "NBA",
    "best_teammates": []
}
buck_williams = {
    "name": "Buck Williams",
    "teams": ["Nets", "Trail Blazers"],
    "positions": ["PF", "C"],
    "pts": 12.8,
    "trb": 10.0,
    "ast": 1.3,
    "defense": 8.7,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Buck"],
    "player_type": "NBA",
    "best_teammates": []
}
kenyon_martin = {
    "name": "Kenyon Martin",
    "teams": ["Nets"],
    "positions": ["PF"],
    "pts": 12.3,
    "trb": 6.8,
    "ast": 1.9,
    "defense": 8.4,
    "eras": ["2000s", "2010s"],
    "nicknames": ["K-Mart"],
    "player_type": "NBA",
    "best_teammates": []
}
kemba_walker = {
    "name": "Kemba Walker",
    "teams": ["Hornets"],
    "positions": ["PG"],
    "pts": 19.3,
    "trb": 3.8,
    "ast": 5.3,
    "defense": 5.5,
    "eras": ["2010s"],
    "nicknames": ["Kemba", "Cardiac Kemba"],
    "best_teammates": []
}
lamelo_ball = {
    "name": "LaMelo Ball",
    "teams": ["Hornets"],
    "positions": ["PG", "SG"],
    "pts": 21.0,
    "trb": 6.0,
    "ast": 7.4,
    "defense": 4.8,
    "eras": ["2020s"],
    "nicknames": ["Melo", "LaMelo"],
    "best_teammates": []
}
dell_curry = {
    "name": "Dell Curry",
    "teams": ["Hornets"],
    "positions": ["SG"],
    "pts": 14.8,
    "trb": 2.9,
    "ast": 2.3,
    "defense": 5.2,
    "eras": ["1990s"],
    "nicknames": ["Dell", "Poppa Dell", "Steph's Dad"],
    "best_teammates": []
}
larry_johnson = {
    "name": "Larry Johnson",
    "teams": ["Hornets"],
    "positions": ["PF", "SF"],
    "pts": 16.2,
    "trb": 7.5,
    "ast": 3.3,
    "defense": 6.8,
    "eras": ["1990s"],
    "nicknames": ["LJ", "Grandmama"],
    "best_teammates": []
}
glen_rice = {
    "name": "Glen Rice",
    "teams": ["Hornets"],
    "positions": ["SF"],
    "pts": 18.3,
    "trb": 4.4,
    "ast": 2.2,
    "defense": 5.5,
    "eras": ["1990s"],
    "nicknames": ["G-Money", "Rice"],
    "best_teammates": []
}
al_jefferson = {
    "name": "Al Jefferson",
    "teams": ["Hornets"],
    "positions": ["C"],
    "pts": 15.7,
    "trb": 8.4,
    "ast": 1.5,
    "defense": 5.8,
    "eras": ["2010s"],
    "nicknames": ["Big Al"],
    "best_teammates": []
}
gerald_wallace = {
    "name": "Gerald Wallace",
    "teams": ["Hornets"],
    "positions": ["SF"],
    "pts": 14.4,
    "trb": 5.7,
    "ast": 2.5,
    "defense": 8.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Crash"],
    "best_teammates": []
}
kirk_hinrich = {
    "name": "Kirk Hinrich",
    "teams": ["Bulls"],
    "positions": ["PG", "SG"],
    "pts": 11.9,
    "trb": 3.4,
    "ast": 5.0,
    "defense": 7.8,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Captain Kirk"],
    "best_teammates": []
}
zach_lavine = {
    "name": "Zach LaVine",
    "teams": ["Bulls"],
    "positions": ["SG", "SF"],
    "pts": 23.3,
    "trb": 4.6,
    "ast": 4.5,
    "defense": 4.5,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Zach Attack"],
    "best_teammates": []
}
horace_grant = {
    "name": "Horace Grant",
    "teams": ["Bulls"],
    "positions": ["PF"],
    "pts": 12.6,
    "trb": 8.6,
    "ast": 2.3,
    "defense": 8.0,
    "eras": ["1990s"],
    "nicknames": ["The General", "Goggles Grant"],
    "best_teammates": []
}
artis_gilmore = {
    "name": "Artis Gilmore",
    "teams": ["Bulls"],
    "positions": ["C"],
    "pts": 19.8,
    "trb": 11.8,
    "ast": 2.0,
    "defense": 8.8,
    "eras": ["1970s", "1980s", "ABA"],
    "nicknames": ["The A-Train"],
    "best_teammates": []
}
joakim_noah = {
    "name": "Joakim Noah",
    "teams": ["Bulls"],
    "positions": ["C"],
    "pts": 9.3,
    "trb": 9.4,
    "ast": 3.0,
    "defense": 9.0,
    "eras": ["2010s"],
    "nicknames": ["Sticks", "Stick Stickity", "French Toast"],
    "best_teammates": []
}
luc_longley = {
    "name": "Luc Longley",
    "teams": ["Bulls"],
    "positions": ["C"],
    "pts": 7.2,
    "trb": 4.9,
    "ast": 1.9,
    "defense": 7.0,
    "eras": ["1990s"],
    "nicknames": ["Luuuuuc"],
    "best_teammates": []
}
steve_kerr = {
    "name": "Steve Kerr",
    "teams": ["Bulls", "Spurs"],
    "positions": ["PG", "SG"],
    "pts": 8.2,
    "trb": 1.8,
    "ast": 1.9,
    "defense": 5.0,
    "eras": ["1990s"],
    "nicknames": ["Steve", "The Future Warriors Coach"],
    "best_teammates": []
}
toni_kukoc = {
    "name": "Toni Kukoč",
    "teams": ["Bulls"],
    "positions": ["SF", "PF"],
    "pts": 11.6,
    "trb": 4.2,
    "ast": 3.7,
    "defense": 5.5,
    "eras": ["1990s"],
    "nicknames": ["The Croatian Sensation", "Kuki", "The Waiter", "The Pink Panther"],
    "best_teammates": []
}
mark_price = {
    "name": "Mark Price",
    "teams": ["Cavaliers"],
    "positions": ["PG"],
    "pts": 15.2,
    "trb": 2.6,
    "ast": 6.7,
    "defense": 6.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The OK Kid"],
    "best_teammates": []
}
brad_daugherty = {
    "name": "Brad Daugherty",
    "teams": ["Cavaliers"],
    "positions": ["C"],
    "pts": 19.0,
    "trb": 9.5,
    "ast": 3.7,
    "defense": 6.0,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Big Train", "El Gato Grande", "Big Dukie"],
    "best_teammates": []
}
larry_nance = {
    "name": "Larry Nance",
    "teams": ["Cavaliers", "Suns"],
    "positions": ["PF", "SF"],
    "pts": 17.1,
    "trb": 8.1,
    "ast": 2.6,
    "defense": 8.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The High Flyer", "The High-Ayatolla of Slamola", "Little Hawk", "Mr. Slambassador"],
    "best_teammates": []
}
zydrunas_ilgauskas = {
    "name": "Zydrunas Ilgauskas",
    "teams": ["Cavaliers"],
    "positions": ["C"],
    "pts": 13.8,
    "trb": 7.7,
    "ast": 1.2,
    "defense": 6.5,
    "eras": ["2000s"],
    "nicknames": ["Big Z"],
    "best_teammates": []
}
anderson_varejao = {
    "name": "Anderson Varejão",
    "teams": ["Cavaliers"],
    "positions": ["C", "PF"],
    "pts": 7.6,
    "trb": 7.5,
    "ast": 1.2,
    "defense": 7.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Wild Thing"],
    "best_teammates": []
}
michael_finley = {
    "name": "Michael Finley",
    "teams": ["Mavericks"],
    "positions": ["SG", "SF"],
    "pts": 19.2,
    "trb": 5.1,
    "ast": 3.7,
    "defense": 6.5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Fin", "Fin Dawg"],
    "best_teammates": []
}
tyson_chandler = {
    "name": "Tyson Chandler",
    "teams": ["Mavericks", "Knicks"],
    "positions": ["C"],
    "pts": 11.1,
    "trb": 9.1,
    "ast": 1.1,
    "defense": 9.0,
    "eras": ["2000s", "2010s"],
    "nicknames": ["T-Chan", "TC"],
    "best_teammates": []
}
shawn_bradley = {
    "name": "Shawn Bradley",
    "teams": ["Mavericks"],
    "positions": ["C"],
    "pts": 8.1,
    "trb": 6.3,
    "ast": 0.7,
    "defense": 8.5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["The Stormin' Mormon"],
    "best_teammates": []
}
fat_lever = {
    "name": "Fat Lever",
    "teams": ["Nuggets"],
    "positions": ["PG", "SG"],
    "pts": 13.9,
    "trb": 6.0,
    "ast": 7.5,
    "defense": 7.5,
    "eras": ["1980s"],
    "nicknames": ["Fat"],
    "best_teammates": []
}
david_thompson = {
    "name": "David Thompson",
    "teams": ["Nuggets"],
    "positions": ["SG", "SF"],
    "pts": 22.7,
    "trb": 4.1,
    "ast": 3.2,
    "defense": 7.0,
    "eras": ["1970s", "1980s", "ABA"],
    "nicknames": ["Skywalker"],
    "best_teammates": []
}
dan_issel = {
    "name": "Dan Issel",
    "teams": ["Nuggets"],
    "positions": ["PF", "C"],
    "pts": 22.6,
    "trb": 9.1,
    "ast": 2.5,
    "defense": 6.5,
    "eras": ["1970s", "1980s", "ABA"],
    "nicknames": ["The Horse"],
    "best_teammates": []
}
marcus_camby = {
    "name": "Marcus Camby",
    "teams": ["Nuggets", "Knicks"],
    "positions": ["C"],
    "pts": 9.6,
    "trb": 9.8,
    "ast": 1.9,
    "defense": 8.5,
    "eras": ["2000s"],
    "nicknames": ["The Cambyman"],
    "best_teammates": []
}
joe_dumars = {
    "name": "Joe Dumars",
    "teams": ["Pistons"],
    "positions": ["SG", "PG"],
    "pts": 16.1,
    "trb": 2.2,
    "ast": 4.5,
    "defense": 9.0,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Joe D", "Broadway Joe"],
    "best_teammates": []
}
rip_hamilton = {
    "name": "Richard Hamilton",
    "teams": ["Pistons"],
    "positions": ["SG"],
    "pts": 17.1,
    "trb": 3.1,
    "ast": 3.1,
    "defense": 7.0,
    "eras": ["2000s"],
    "nicknames": ["Rip"],
    "best_teammates": []
}
tayshaun_prince = {
    "name": "Tayshaun Prince",
    "teams": ["Pistons"],
    "positions": ["SF"],
    "pts": 11.1,
    "trb": 4.3,
    "ast": 2.8,
    "defense": 9.0,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Tay", "The Palace Prince"],
    "best_teammates": []
}
bill_laimbeer = {
    "name": "Bill Laimbeer",
    "teams": ["Pistons"],
    "positions": ["C", "PF"],
    "pts": 12.9,
    "trb": 9.7,
    "ast": 2.0,
    "defense": 8.0,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Asshole", "The Bad Boy"],
    "best_teammates": []
}
bob_lanier = {
    "name": "Bob Lanier",
    "teams": ["Pistons"],
    "positions": ["C"],
    "pts": 20.1,
    "trb": 10.1,
    "ast": 3.1,
    "defense": 7.5,
    "eras": ["1970s"],
    "nicknames": ["The Big Dobber","Dobber", "Bob a Dob"],
    "best_teammates": []
}
andre_drummond = {
    "name": "Andre Drummond",
    "teams": ["Pistons"],
    "positions": ["C"],
    "pts": 14.4,
    "trb": 13.9,
    "ast": 1.5,
    "defense": 7.5,
    "eras": ["2010s"],
    "nicknames": ["The Big Penguin"],
    "best_teammates": []
}
blake_griffin = {
    "name": "Blake Griffin",
    "teams": ["Clippers", "Pistons"],
    "positions": ["PF"],
    "pts": 19.0,
    "trb": 8.0,
    "ast": 4.0,
    "defense": 6.5,
    "eras": ["2010s"],
    "nicknames": ["Poster Child", "Blake the Quake"],
    "best_teammates": []
}
nate_thurmond = {
    "name": "Nate Thurmond",
    "teams": ["Warriors"],
    "positions": ["C", "PF"],
    "pts": 15.0,
    "trb": 15.0,
    "ast": 2.7,
    "defense": 9.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Nate the Great"],
    "best_teammates": []
}
chris_mullin = {
    "name": "Chris Mullin",
    "teams": ["Warriors"],
    "positions": ["SF", "SG"],
    "pts": 18.2,
    "trb": 4.1,
    "ast": 3.5,
    "defense": 4.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Mullet", "The Silent Assassin"],
    "best_teammates": []
}
tim_hardaway = {
    "name": "Tim Hardaway",
    "teams": ["Warriors", "Heat"],
    "positions": ["PG"],
    "pts": 17.7,
    "trb": 3.3,
    "ast": 8.2,
    "defense": 6.0,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Tim Bug", "UTEP Two-Step"],
    "best_teammates": []
}
mitch_richmond = {
    "name": "Mitch Richmond",
    "teams": ["Warriors", "Kings"],
    "positions": ["SG", "SF"],
    "pts": 21.0,
    "trb": 3.9,
    "ast": 3.5,
    "defense": 6.5,
    "eras": ["1980s", "1990s", "2000s"],
    "nicknames": ["The Rock", "Hammer"],
    "best_teammates": []
}
andre_iguodala = {
    "name": "Andre Iguodala",
    "teams": ["Warriors", "76ers"],
    "positions": ["SF", "SG"],
    "pts": 11.3,
    "trb": 4.9,
    "ast": 4.2,
    "defense": 8.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Iggy", "Dre"],
    "best_teammates": []
}
ralph_sampson = {
    "name": "Ralph Sampson",
    "teams": ["Rockets"],
    "positions": ["PF", "C"],
    "pts": 15.4,
    "trb": 8.8,
    "ast": 2.7,
    "defense": 7.5,
    "eras": ["1980s"],
    "nicknames": ["The Skyscraper"],
    "best_teammates": []
}
calvin_murphy = {
    "name": "Calvin Murphy",
    "teams": ["Rockets"],
    "positions": ["PG", "SG"],
    "pts": 17.9,
    "trb": 2.1,
    "ast": 4.4,
    "defense": 5.5,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Mighty Mouse", "The Pocket Rocket"],
    "best_teammates": []
    
}
rik_smits = {
    "name": "Rik Smits",
    "teams": ["Pacers"],
    "positions": ["C"],
    "pts": 14.8,
    "trb": 6.1,
    "ast": 1.4,
    "defense": 7.0,
    "eras": ["1980s", "1990s"],
    "nicknames": ["The Dunking Dutchman"],
    "best_teammates": []
}
mark_jackson = {
    "name": "Mark Jackson",
    "teams": ["Pacers", "Knicks"],
    "positions": ["PG"],
    "pts": 9.6,
    "trb": 3.8,
    "ast": 8.0,
    "defense": 4,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Action Jackson"],
    "best_teammates": []
}
george_mcginnis = {
    "name": "George McGinnis",
    "teams": ["Pacers", "76ers"],
    "positions": ["PF", "SF"],
    "pts": 17.2,
    "trb": 9.8,
    "ast": 3.8,
    "defense": 5.0,
    "eras": ["1970s", "ABA"],
    "nicknames": ["Big Mac"],
    "best_teammates": []
}
mel_daniels = {
    "name": "Mel Daniels",
    "teams": ["Pacers"],
    "positions": ["C"],
    "pts": 18.4,
    "trb": 14.9,
    "ast": 1.6,
    "defense": 8.5,
    "eras": ["1960s", "1970s", "ABA"],
    "nicknames": ["The Gentle Giant", "Big Mel"],
    "best_teammates": []
}
roger_brown = {
    "name": "Roger Brown",
    "teams": ["Pacers"],
    "positions": ["SF", "SG"],
    "pts": 17.4,
    "trb": 6.0,
    "ast": 3.5,
    "defense": 6,
    "eras": ["1960s", "1970s", "ABA"],
    "nicknames": ["The Rajah"],
    "best_teammates": []
}
tyrese_haliburton = {
    "name": "Tyrese Haliburton",
    "teams": ["Pacers"],
    "positions": ["PG"],
    "pts": 17.5,
    "trb": 3.5,
    "ast": 8.7,
    "defense": 5.0,
    "eras": ["2020s"],
    "nicknames": ["Hali" , "The Haliban", "Haliburger"],
    "best_teammates": []
}
deandre_jordan = {
    "name": "DeAndre Jordan",
    "teams": ["Clippers"],
    "positions": ["C"],
    "pts": 11.4,
    "trb": 10.9,
    "ast": 1.0,
    "defense": 7.5,
    "eras": ["2010s"],
    "nicknames": ["DJ", "DeAndre the Giant"],
    "best_teammates": []
}
elton_brand = {
    "name": "Elton Brand",
    "teams": ["Clippers", "Bulls"],
    "positions": ["PF", "C"],
    "pts": 20.1,
    "trb": 10.0,
    "ast": 2.5,
    "defense": 7.5,
    "eras": ["2000s"],
    "nicknames": ["EB", "Old School Chevy"],
    "best_teammates": []
}
danny_manning = {
    "name": "Danny Manning",
    "teams": ["Clippers"],
    "positions": ["PF", "SF"],
    "pts": 14.0,
    "trb": 5.2,
    "ast": 2.3,
    "defense": 6.0,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Danny"],
    "best_teammates": []
}
world_free = {
    "name": "World B. Free",
    "teams": ["Clippers"],
    "positions": ["PG", "SG"],
    "pts": 20.3,
    "trb": 2.7,
    "ast": 3.7,
    "defense": 5.5,
    "eras": ["1970s", "1980s"],
    "nicknames": ["All World", "Rainbow Jumper"],
    "best_teammates": []
}
jamaal_wilkes = {
    "name": "Jamaal Wilkes",
    "teams": ["Lakers", "Warriors"],
    "positions": ["SF"],
    "pts": 17.7,
    "trb": 6.2,
    "ast": 2.5,
    "defense": 7.5,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Silk"],
    "best_teammates": []
}
byron_scott = {
    "name": "Byron Scott",
    "teams": ["Lakers"],
    "positions": ["SG"],
    "pts": 14.1,
    "trb": 2.8,
    "ast": 2.5,
    "defense": 6.5,
    "eras": ["1980s", "1990s"],
    "nicknames": ["Lord Byron", "Baby B."],
    "best_teammates": []
}
michael_cooper = {
    "name": "Michael Cooper",
    "teams": ["Lakers"],
    "positions": ["SG", "PG"],
    "pts": 8.9,
    "trb": 4.2,
    "ast": 4.2,
    "defense": 9.0,
    "eras": ["1980s"],
    "nicknames": ["Coop"],
    "best_teammates": []
}
kurt_rambis = {
    "name": "Kurt Rambis",
    "teams": ["Lakers"],
    "positions": ["PF"],
    "pts": 5.2,
    "trb": 5.6,
    "ast": 1.4,
    "defense": 7.5,
    "eras": ["1980s"],
    "nicknames": ["Goggles", "Rambo"],
    "best_teammates": []
}
mike_conley = {
    "name": "Mike Conley",
    "teams": ["Grizzlies"],
    "positions": ["PG"],
    "pts": 14.3,
    "trb": 3.0,
    "ast": 5.7,
    "defense": 7.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Money Mike", "Grit-n-Grind"],
    "best_teammates": []
}
zach_randolph = {
    "name": "Zach Randolph",
    "teams": ["Grizzlies", "Trail Blazers"],
    "positions": ["PF"],
    "pts": 16.6,
    "trb": 9.1,
    "ast": 1.8,
    "defense": 5.5,
    "eras": ["2000s", "2010s"],
    "nicknames": ["Z-Bo"],
    "best_teammates": []
}
tony_allen = {
    "name": "Tony Allen",
    "teams": ["Grizzlies"],
    "positions": ["SG", "SF"],
    "pts": 8.1,
    "trb": 4.0,
    "ast": 1.3,
    "defense": 10.0,
    "eras": ["2000s", "2010s"],
    "nicknames": ["The Grindfather"],
    "best_teammates": []
}
shareef_abdur_rahim = {
    "name": "Shareef Abdur-Rahim",
    "teams": ["Grizzlies", "Hawks"],
    "positions": ["PF", "SF"],
    "pts": 18.1,
    "trb": 7.5,
    "ast": 2.5,
    "defense": 5.0,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Reef"],
    "best_teammates": []
}
bryant_reeves = {
    "name": "Bryant Reeves",
    "teams": ["Grizzlies"],
    "positions": ["C"],
    "pts": 12.5,
    "trb": 6.9,
    "ast": 1.2,
    "defense": 4.5,
    "eras": ["1990s"],
    "nicknames": ["Big Country"],
    "best_teammates": []
}
udonis_haslem = {
    "name": "Udonis Haslem",
    "teams": ["Heat"],
    "positions": ["PF", "C"],
    "pts": 7.5,
    "trb": 6.6,
    "ast": 0.8,
    "defense": 7.5,
    "eras": ["2000s"],
    "nicknames": ["UD", "Mr. 305"],
    "best_teammates": []
}
bam_adebayo = {
    "name": "Bam Adebayo",
    "teams": ["Heat"],
    "positions": ["C", "PF"],
    "pts": 19.4,
    "trb": 9.6,
    "ast": 3.5,
    "defense": 9.0,
    "eras": [ "2020s"],
    "nicknames": ["Bam", "Mr. 83 Points"],
    "best_teammates": []
}
john_wall = {
    "name": "John Wall",
    "teams": ["Wizards"],
    "positions": ["PG"],
    "pts": 19.0,
    "trb": 4.3,
    "ast": 9.2,
    "defense": 8.0,
    "eras": ["2010s"],
    "nicknames": ["The Kentucky Kid", "Optimus Dime"],
    "best_teammates": []
}
bradley_beal = {
    "name": "Bradley Beal",
    "teams": ["Wizards", "Suns"],
    "positions": ["SG"],
    "pts": 21.5,
    "trb": 4.1,
    "ast": 4.3,
    "defense": 5.5,
    "eras": ["2010s"],
    "nicknames": ["Real Deal Beal"],
    "best_teammates": []
}
wes_unseld = {
    "name": "Wes Unseld",
    "teams": ["Wizards"],
    "positions": ["C"],
    "pts": 10.8,
    "trb": 14.0,
    "ast": 3.9,
    "defense": 9.7,
    "eras": ["1960s", "1970s"],
    "nicknames": ["The Incredible Hulk", "The Wide U", "The Oak Tree"],
    "best_teammates": []
}
penny_hardaway= {
    "name": "Penny Hardaway",
    "teams": ["Magic"],
    "positions": ["PG", "SG"],
    "pts": 15.2,
    "trb": 4.5,
    "ast": 5.0,
    "defense": 8.2,
    "eras": ["1990s"],
    "nicknames": ["Penny", "Lil' Penny"],
    "best_teammates": []
}
adrian_dantley = {
    "name": "Adrian Dantley",
    "teams": ["Jazz", "Pistons"],
    "positions": ["SF"],
    "pts": 24.3,
    "trb": 5.7,
    "ast": 3.0,
    "defense": 6.8,
    "eras": ["1970s", "1980s"],
    "nicknames": ["AD", "The Teacher"],
    "best_teammates": []
}
serge_ibaka = {
    "name": "Serge Ibaka",
    "teams": ["Thunder", "Raptors"],
    "positions": ["PF", "C"],
    "pts": 12.0,
    "trb": 7.1,
    "ast": 0.8,
    "defense": 9.5,
    "eras": ["2010s"],
    "nicknames": ["Air Congo", "Iblocka"],
    "best_teammates": []
}
chet_holmgren = {
    "name": "Chet Holmgren",
    "teams": ["Thunder"],
    "positions": ["PF", "C"],
    "pts": 17.0,
    "trb": 8.5,
    "ast": 2.8,
    "defense": 9.0,
    "eras": ["2020s"],
    "nicknames": ["The Unicorn", "Slim"],
    "best_teammates": []
}
zion_williamson = {
    "name": "Zion Williamson",
    "teams": ["Pelicans"],
    "positions": ["PF"],
    "pts": 24.7,
    "trb": 6.6,
    "ast": 4.3,
    "defense": 6.8,
    "eras": ["2020s"],
    "nicknames": ["Zanos", "Mount Zion"],
    "best_teammates": []
}
jrue_holiday = {
    "name": "Jrue Holiday",
    "teams": ["76ers", "Pelicans", "Bucks"],
    "positions": ["PG", "SG"],
    "pts": 16.0,
    "trb": 4.2,
    "ast": 6.2,
    "defense": 9.6,
    "eras": ["2010s", "2020s"],
    "nicknames": ["Jrue", "The Locksmith"],
    "best_teammates": []
}
tyreke_evans = {
    "name": "Tyreke Evans",
    "teams": ["Kings", "Pelicans", "Grizzlies", "Pacers"],
    "positions": ["PG", "SG", "SF"],
    "pts": 15.7,
    "trb": 4.8,
    "ast": 4.8,
    "defense": 5,
    "eras": ["2010s"],
    "nicknames": ["Reke", "T-Rex"],
    "best_teammates": []
}
brandon_ingram = {
    "name": "Brandon Ingram",
    "teams": ["Lakers", "Pelicans"],
    "positions": ["SF", "SG"],
    "pts": 20.0,
    "trb": 5.2,
    "ast": 4.3,
    "defense": 5.8,
    "eras": ["2010s", "2020s"],
    "nicknames": ["BI", "Slim Reefer"],
    "best_teammates": []
}
dave_bing = {
    "name": "Dave Bing",
    "teams": ["Pistons", "Wizards"],
    "positions": ["PG"],
    "pts": 20.3,
    "trb": 3.8,
    "ast": 6.0,
    "defense": 6.2,
    "eras": ["1960s", "1970s"],
    "nicknames": ["Duke", "Bingo"],
    "best_teammates": []
}
sam_jones = {
    "name": "Sam Jones",
    "teams": ["Celtics"],
    "positions": ["SG"],
    "pts": 17.7,
    "trb": 4.9,
    "ast": 2.5,
    "defense": 8.0,
    "eras": ["1950s", "1960s"],
    "nicknames": ["Mr. Clutch"],
    "best_teammates": []
}
nate_archibald = {
    "name": "Nate Archibald",
    "teams": ["Kings", "Celtics"],
    "positions": ["PG"],
    "pts": 18.8,
    "trb": 2.3,
    "ast": 7.4,
    "defense": 7.0,
    "eras": ["1970s", "1980s"],
    "nicknames": ["Tiny"],
    "best_teammates": []
}
jalen_rose = {
    "name": "Jalen Rose",
    "teams": ["Pacers", "Bulls"],
    "positions": ["PG", "SG", "SF"],
    "pts": 14.3,
    "trb": 3.5,
    "ast": 3.8,
    "defense": 4.5,
    "eras": ["1990s", "2000s"],
    "nicknames": ["Jinx"],
    "best_teammates": ["Reggie Miller", "Rik Smits", "Dale Davis"],
    "best_teammates": []
}
earl_monroe= {
    "name": "Earl Monroe",
    "teams": ["Wizards", "Knicks"],
    "positions": ["PG", "SG"],
    "pts": 18.8,
    "trb": 3.0,
    "ast": 3.9,
    "defense": 7.5,
    "eras": ["1960s", "1970s"],
    "nicknames": ["The Pearl", "Black Jesus"],
    "best_teammates": []
}
louie_dampier = {
    "name": "Louie Dampier",
    "teams": ["Colonels"],
    "positions": ["PG", "SG"],
    "pts": 18.5,
    "trb": 2.6,
    "ast": 4.8,
    "defense": 5.5,
    "eras": ["ABA", "1960s", "1970s"],
    "nicknames": ["Little Louie"],
    "best_teammates": []
}
freddie_lewis = {
    "name": "Freddie Lewis",
    "teams": ["Pacers"],
    "positions": ["PG", "SG"],
    "pts": 17.1,
    "trb": 2.7,
    "ast": 4.9,
    "defense": 6.5,
    "eras": ["ABA", "1960s", "1970s"],
    "nicknames": ["Freddie"],
    "best_teammates": []
}
billy_cunningham = {
    "name": "Billy Cunningham",
    "teams": ["76ers", "Carolina Cougars"],
    "positions": ["SF", "PF"],
    "pts": 21.2,
    "trb": 10.4,
    "ast": 4.3,
    "defense": 7.5,
    "eras": ["ABA", "1960s", "1970s"],
    "nicknames": ["The Kangaroo Kid"],
    "best_teammates": []
}
bobby_jones = {
    "name": "Bobby Jones",
    "teams": ["Nuggets", "76ers"],
    "positions": ["PF", "SF"],
    "pts": 11.2,
    "trb": 8.3,
    "ast": 3.2,
    "defense": 9.5,
    "eras": ["ABA", "1970s", "1980s"],
    "nicknames": ["The Secretary of Defense"],
    "best_teammates": ["Julius Erving", "Moses Malone", "Maurice Cheeks", "Andrew Toney"]
}
connie_hawkins = {
    "name": "Connie Hawkins",
    "teams": ["Pittsburgh Pipers", "Minnesota Pipers"],
    "positions": ["SF", "PF"],
    "pts": 26.8,
    "trb": 13.5,
    "ast": 4.1,
    "defense": 8.0,
    "eras": ["ABA", "1960s", "1970s"],
    "nicknames": ["The Hawk"],
    "best_teammates": ["Gail Goodrich", "Jerry West"]
}
billy_paultz = {
    "name": "Billy Paultz",
    "teams": ["Nets", "Spurs"],
    "positions": ["C", "PF"],
    "pts": 13.8,
    "trb": 10.2,
    "ast": 2.3,
    "defense": 8.5,
    "eras": ["ABA", "1970s", "1980s"],
    "nicknames": ["The Whopper"],
    "best_teammates": ["Julius Erving", "Rick Barry"]
}
maurice_cheeks = {
    "name": "Maurice Cheeks",
    "teams": ["76ers"],
    "positions": ["PG"],
    "pts": 11.1,
    "trb": 2.8,
    "ast": 6.7,
    "defense": 8.5,
    "eras": ["1970s", "1980s", "1990s"],
    "nicknames": ["Little Mo", "Mo"],
    "best_teammates": [
        "Julius Erving",
        "Moses Malone",
        "Andrew Toney",
        "Bobby Jones"
    ]
}
ron_boone = {
    "name": "Ron Boone",
    "teams": ["Utah Stars", "Los Angeles Stars"],
    "positions": ["SG", "PG"],
    "pts": 18.6,
    "trb": 5.0,
    "ast": 5.0,
    "defense": 7.0,
    "eras": ["ABA", "1960s", "1970s"],
    "nicknames": ["The Silver Fox"],
    "best_teammates": ["Adrian Dantley", 'Moses Malone']
}
andrew_toney = {
    "name": "Andrew Toney",
    "teams": ["76ers"],
    "positions": ["SG"],
    "pts": 15.9,
    "trb": 2.2,
    "ast": 4.2,
    "defense": 4.0,
    "eras": ["1980s"],
    "nicknames": ["The Boston Strangler"],
    "best_teammates": [
        "Julius Erving",
        "Moses Malone",
        "Maurice Cheeks",
        "Bobby Jones"
    ]
}
players = [
    andrew_toney,
    maurice_cheeks, 
    gail_goodrich,
    rajon_rondo,
    ron_boone,
    billy_paultz,
    connie_hawkins,
    bobby_jones,
    billy_cunningham,
    freddie_lewis,
    louie_dampier,
    earl_monroe,
    nate_archibald,
    sam_jones,
    dave_bing,
    brandon_ingram,
    tyreke_evans,
    jrue_holiday, 
    zion_williamson, 
    serge_ibaka,
    chet_holmgren,
    adrian_dantley,
    penny_hardaway,
    wes_unseld,
    bradley_beal,
    john_wall,
    bam_adebayo,
    udonis_haslem,
    bryant_reeves,
    shareef_abdur_rahim,
    tony_allen,
    zach_randolph,
    mike_conley,
    kurt_rambis,
    michael_cooper,
    byron_scott,
    jamaal_wilkes,
    world_free,
    danny_manning,
    elton_brand,
    deandre_jordan,
    tyrese_haliburton, 
    roger_brown,
    mel_daniels,
    george_mcginnis,
    mark_jackson,
    rik_smits,
    calvin_murphy,
    ralph_sampson,
    mitch_richmond,
    tim_hardaway,
    chris_mullin,
    nate_thurmond,
    blake_griffin,
    andre_drummond,
    bob_lanier,
    bill_laimbeer,
    tayshaun_prince,
    rip_hamilton,
    joe_dumars,
    marcus_camby,
    dan_issel,
    david_thompson,
    fat_lever,
    shawn_bradley,
    tyson_chandler,
    michael_finley,
    anderson_varejao,
    zydrunas_ilgauskas,
    larry_nance,
    brad_daugherty,
    mark_price,
    luc_longley,
    joakim_noah,
    artis_gilmore,
    horace_grant,
    zach_lavine,
    kirk_hinrich,
    gerald_wallace,
    al_jefferson,
    glen_rice,
    larry_johnson,
    dell_curry,
    lamelo_ball,
    kemba_walker,
    kenyon_martin,
    buck_williams,
    cliff_hagan,
    pete_maravich,
    lou_hudson,
    lenny_wilkens,
    bob_rule,
    spencer_haywood,
    jack_sikma,
    rashard_lewis,
    fred_brown,
    gus_williams,
    magic_johnson,
    stephen_curry,
    oscar_robertson,
    john_stockton,
    isiah_thomas,
    chris_paul,
    jason_kidd,
    steve_nash,
    bob_cousy,
    walt_frazier,
    michael_jordan,
    kobe_bryant,
    dwyane_wade,
    jerry_west,
    james_harden,
    clyde_drexler,
    allen_iverson,
    george_gervin,
    reggie_miller,
    ray_allen,
    shorty_crapponeli,
    lebron_james,
    larry_bird,
    muggsy_bogues,
    chris_bosh,
    vince_carter,
    kyle_lowry,
    paul_pierce,
    devin_booker,
    jimmy_butler,
    alex_caruso,
    anthony_edwards,
    karl_anthony_towns,
    joel_embiid,
    paul_george,
    klay_thompson,
    draymond_green,
    robert_horry,
    james_worthy,
    dwight_howard,
    kyrie_irving,
    damian_lillard,
    pau_gasol,
    marc_gasol,
    brook_lopez,
    robin_lopez,
    shawn_marion,
    tracy_mcgrady,
    yao_ming,
    donovan_mitchell,
    kevin_love,
    alonzo_mourning,
    gary_payton,
    detlef_schrempf,
    derrick_rose,
    jeremy_lin,
    russell_westbrook,
    andrew_wiggins,
    nick_young,
    dennis_johnson,
    willis_reed,
    rik_smits,
    jalen_rose,
    dave_cowens,
    alex_english,
    paul_arizin,
    george_mikan,
    chris_webber,
    manu_ginobili,
    tony_parker,
    shawn_kemp,
    kevin_durant,
    julius_erving,
    kawhi_leonard,
    elgin_baylor,
    scottie_pippen,
    john_havlicek,
    rick_barry,
    dominique_wilkins,
    tim_duncan,
    karl_malone,
    kevin_garnett,
    dirk_nowitzki,
    giannis_antetokounmpo,
    charles_barkley,
    bob_pettit,
    anthony_davis,
    kevin_mchale,
    elvin_hayes,
    kareem_abdul_jabbar,
    bill_russell,
    wilt_chamberlain,
    hakeem_olajuwon,
    shaquille_oneal,
    nikola_jokic,
    moses_malone,
    david_robinson,
    patrick_ewing,
    bill_walton,
    shai_gilgeousalexander,
    victor_wembanyama,
    luka_doncic,
    cade_cunningham,
    jayson_tatum,
    jaylen_brown,
    jalen_brunson,
    bob_mcadoo,
    robert_parish,
    ben_wallace,
    bill_sharman,
    jeff_hornacek,
    jermaine_oneal,
    amare_stoudemire,
    john_starks,
    deron_williams,
    dennis_rodman,
    trae_young,
    al_horford,
    dikembe_mutombo,
    rudy_gobert,
    chris_andersen,
    carmelo_anthony,
    harrison_barnes
]
franchises = [
    "Sonics",
    "Hawks",
    "Celtics",
    "Nets",
    "Hornets",
    "Bulls",
    "Cavaliers",
    "Mavericks",
    "Nuggets",
    "Pistons",
    "Warriors",
    "Rockets",
    "Pacers",
    "Clippers",
    "Lakers",
    "Grizzlies",
    "Heat",
    "Bucks",
    "Timberwolves",
    "Pelicans",
    "Knicks",
    "Thunder",
    "Magic",
    "76ers",
    "Suns",
    "Trail Blazers",
    "Kings",
    "Spurs",
    "Raptors",
    "Jazz",
    "Wizards"
]
positions = ["PG", "SG", "SF", "PF", "C"]

def create_average_player(position):
    first_names = [
    "Ezra",
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Joseph",
    "Thomas",
    "Charles",
    "Christopher",
    "Daniel",
    "Matthew",
    "Anthony",
    "Donald",
    "Mark",
    "Paul",
    "Steven",
    "Andrew",
    "Kenneth",
    "George",
    "Joshua",
    "Kevin",
    "Brian",
    "Edward",
    "Samir",
    "Zadek"
    ]
    last_names = [
    "Ghoshal",
    "Freeman",
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
    "Lee",
    "Perez",
    "Thompson",
    "White",
    "Harris"
    ]
    name = random.choice(first_names) + " (RP) " + random.choice(last_names)
 
    return {
        "name": name,
        "teams": [random.choice(random_team_names)],
        "positions": [position],
        "pts": round(random.uniform(10.0, 20.0), 1),
        "trb": round(random.uniform(3.0, 8.0), 1),
        "ast": round(random.uniform(2.0, 6.0), 1),
        "defense": round(random.uniform(3.5, 7.0), 1),
        "eras": ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"],
        "nicknames": [name.split()[0]]
    }

def create_all_star_player(position):
    first_names = [
    "Ace",
    "Action",
    "Big",
    "Bird",
    "Blaze",
    "Boom",
    "Bones",
    "Boss",
    "Buck",
    "Bullet",
    "Whiz Kid",
    "Buckets",
    "Champ",
    "Chief",
    "Crash",
    "Dash",
    "Dizzy",
    "Doc",
    "Dollar",
    "Duke",
    "Flash",
    "Fly",
    "Frost",
    "Hammer",
    "Hawk",
    "Ice",
    "Jet",
    "Jinx",
    "King",
    "Knuckles",
    "Lightning",
    "Magic",
    "Major",
    "Mojo",
    "Nitro",
    "Prime",
    "Prince",
    "Rocket",
    "Scooter",
    "Shadow",
    "Shooter",
    "Showtime",
    "Slam",
    "Smooth",
    "Snake",
    "Sonny",
    "Speedy",
    "Sporty",
    "Stretch",
    "Superfly",
    "Tank",
    "Tex",
    "Thunder",
    "Trigger",
    "Turbo",
    "Whisper",
    "Wild",
    "Zeke"
]
    last_names = [
    "Ghoshal",
    "Freeman",
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
    "Lee",
    "Perez",
    "Thompson",
    "White",
    "Harris"
    ]
    name =  random.choice(first_names) + " (AS) " + random.choice(last_names)
    return {
    "name": name,
    "teams": [random.choice(franchises)],
    "positions": [position],
    "pts": round(random.uniform(15.0, 25.0), 1),
    "trb": round(random.uniform(6.0, 12.0), 1),
    "ast": round(random.uniform(5.0, 10.0), 1),
    "defense": round(random.uniform(3.5, 7.0), 1),
    "eras": ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"],
    "nicknames": [name.split()[0]]
    }

        
random_cities = [
    "Fightin'",
    "Terrible",
    "Amazng",
    "Stupendous",
    "Seattle",
    "Tampa",
    "San Diego",
    "St. Louis",
    "Baltimore",
    "Charlotte",
    "Pittsburgh",
    "Portland",
    "Las Vegas",
    "Austin",
    "Cincinnati",
    "Kansas City",
    "Columbus",
    "Indianapolis",
    "Orlando",
    "San Antonio",
    "Virginia Beach",
    "Nashville",
    "Jacksonville",
    "Raleigh",
    "Richmond",
    "Milwaukee",
    "Louisville",
    "New Orleans",
    "Memphis",
    "Buffalo",
    "Rochester",
    "Hartford",
    "Providence",
    "Birmingham",
    "Oklahoma City",
    "Norfolk",
    "Greensboro",
    "Albuquerque",
    "Tucson",
    "Fresno",
    "Bakersfield",
    "Honolulu",
    "Omaha",
    "Tulsa",
    "Wichita",
    "Boise",
    "Colorado Springs",
    "Spokane",
    "Little Rock",
    "Des Moines",
    "Madison",
    "Syracuse",
    "Dayton",
    "Toledo",
    "Harrisburg",
    "Scranton",
    "Grand Rapids",
    "Knoxville",
    "Chattanooga",
    "Lexington",
    "Wilmington",
    "Charleston",
    "Savannah",
    "Augusta",
    "Huntsville",
    "Mobile",
    "Jackson",
    "Lubbock",
    "El Paso",
    "Corpus Christi",
    "McAllen",
    "Baton Rouge",
    "Lafayette",
    "Shreveport",
    "Fort Myers",
    "Lakeland",
    "Sarasota",
    "Daytona Beach",
    "Cape Coral",
    "Palm Bay",
    "Pensacola",
    "Anchorage",
    "Salt Lake City",
    "Reno",
    "Stockton",
    "Modesto",
    "Santa Barbara",
    "Oxnard",
    "Eugene",
    "Salem",
    "Vancouver",
    "Montreal",
    "Calgary",
    "Edmonton",
    "Ottawa",
    "Winnipeg",
    "Quebec City",
    "Hamilton",
    "Kitchener",
    "London",
    "Halifax",
    "Windsor",
    "Louisa",
    "Mexico City",
    "Skowhegan",
    "Charlottesville",
    "Goochland",
    "Tokyo",
    "Mumbai",
    "Delhi",
    "Shanghai",
    "Beijing",
    "Guangzhou",
    "Shenzhen",
    "Hong Kong",
    "Singapore",
    "Seoul",
    "Bangkok",
    "Jakarta",
    "Manila",
    "Ho Chi Minh City",
    "Hanoi",
    "Kuala Lumpur",
    "Dhaka",
    "Karachi",
    "Lahore",
    "Colombo",

    "London",
    "Paris",
    "Berlin",
    "Madrid",
    "Rome",
    "Milan",
    "Barcelona",
    "Amsterdam",
    "Brussels",
    "Vienna",
    "Prague",
    "Budapest",
    "Warsaw",
    "Athens",
    "Lisbon",
    "Dublin",
    "Copenhagen",
    "Stockholm",
    "Oslo",
    "Helsinki",
    "Zurich",
    "Geneva",
    "Munich",
    "Frankfurt",
    "Istanbul",
    "Moscow",
    "Kyiv",
    "Porto",
    

    "Cairo",
    "Lagos",
    "Johannesburg",
    "Cape Town",
    "Nairobi",
    "Addis Ababa",
    "Casablanca",
    "Accra",
    "Abuja",
    "Dakar",
    "Dar es Salaam",
    "Kampala",
    "Timbuktu",
    "Big Bend",
    "Leningrad",
    "São Paulo",
    "Rio de Janeiro",
    "Buenos Aires",
    "Lima",
    "Bogotá",
    "Santiago",
    "Caracas",
    "Quito",
    "Montevideo",
    "Asunción",
    "La Paz",
    "Panama City",
    "Cuzco",

    "Mexico City",
    "Guadalajara",
    "Monterrey",
    "Havana",
    "Santo Domingo",
    "San José",
    "Guatemala City",

    "Dubai",
    "Abu Dhabi",
    "Doha",
    "Riyadh",
    "Jeddah",
    "Djibouti",
    "Beirut",
    "Tehran",
    "Baghdad",
    "Guatemala City",
    "Pyongyang",
    "Sydney",
    "Melbourne",
    "Brisbane",
    "Perth",
    "Auckland",
    "Wellington",
    "Interplanetary",

    "Montreal",
    "Vancouver",
    "Calgary",
    "Ottawa",
    "Whitehorse",
    "Greenland",
    "Outer Mongolia",
    "Cabo Verde",
    "Wabash",
    "Walla Walla",
    "Goochland",
    "Capitol City",
    "Springfield",
    "Intergalactic",
    "Space",
    "Extraterrestrial",
    "Florida",
    "Northern Maine",
    "Yukon",
    "North Korea",
    "Soviet",
    "Fightin'",
    "Killer",
    "Mighty",
    "Unstoppable",
    "Deadly",
    "Psychedelic",
    "Gruesome",
    "Home Town",
    "Gryffindor",
    "Slytherin",
    "Ravenclaw",
    "Hufflepuff",
    "Fearsome",
    "Greenland",
    "East Timor"

]

random_team_names = [
    "Spice",
    "Flatworms",
    "Hammerheads",
    "Dumpster Divers",
    "Lounge Lizards",
    "Proleteariat",
    "Lions",
    "Serpents",
    "Badgers",
    "Ravens",
    "Boot-Lickers",
    "Jack-Booted Thugs",
    "Rednecks",
    "Blizzard",
    "Toddlers",
    "Shag",
    "Horde",
    "Beef",
    "By-Products",
    "Bubbles",
    "Salsa",
    "Invaders",
    "Mosquitoes",
    "Potatoes",
    "Celery",
    "Wasteland",
    "Rapids",
    "Wipers of Other People's Bottoms",
    "Koalas",
    "Dust Devils",
    "Munchkins",
    "Gelatinous Cubes",
    "Almish",
    "Chowder",
    "Digglers",
    "Coal Miners",
    "Corndoggers",
    "Horny Toads",
    "Lard",
    "Meat Stix",
    "Pulse",
    "Groin-Grabbers",
    "Grampaws",
    "Leaping Lizards",
    "Spotted Lanternflies",
    "Flood",
    "Wildfire",
    "Earthquake"
    "Tsunami",
    "Kaiju",
    "Plague",
    "Locusts",
    "Fighting Artichokes",
    "Yard Goats",
    "Whistle-Pigs",
    "Manglers",
    "Meat-Packers",
    "Dental Assistants",
    "Cornholers",
    "Hot Rats",
    "Mildew",
    "Tomatillos",
    "Kangaroo Rats",
    "Naked Mole Rats",
    "Axolotls",
    "Jellyfish",
    "Thorn Devils",
    "Intestines",
    "Biscuits-n-Gravy",
    "Hummingbirds",
    "Ballers",
    "Sports-Ballers",
    "Sno-Cones",
    "Calamari",
    "Sap-Suckers",
    "Nudists",
    "Spekkhogger",
    "Schadenfreude",
    "Burritos Mojados",
    "Sushi",
    "Cheese Eaters",
    "Jellyfish",
    "Killer Whales",
    "Liver Lovers",
    "Buttkickers",
    "Crudites",
    "Hot Diggety Doggetys",
    "Bobbleheads",
    "Cornflowers",
    "Bucketheads",
    "Lawn Chairs",
    "Roadrunners",
    "Moon Dogs",
    "Fireflies",
    "Thunderbirds",
    "Turnips",
    "Sasquatches",
    "Pickles",
    "Comets",
    "Wombats",
    "Marmots",
    "Jackalopes",
    "Raccoons",
    "Tater Tots",
    "Banjoes",
    "Goose Eggs",
    "Mudcats",
    "Hot Dogs",
    "Croutons",
    "Whirlwinds",
    "Road Hogs",
    "Nighthawks",
    "Potholes",
    "Grasshoppers",
    "Mosquitoes",
    "Bees Knees",
    "Lumberjacks",
    "Sidewinders",
    "Possums",
    "Yard Gnomes",
    "Watermelons",
    "Moonshiners",
    "Sourdoughs",
    "Porcupines",
    "Hooligans",
    "Flapjacks",
    "Rutabagas",
    "Fiddlers",
    "Corkscrews",
    "Paper Tigers",
    "Space Cadets",
    "Swamp Gas",
    "Gravy Boats",
    "Lava Lamps",
    "Windbreakers",
    "Free Radicals",
    "Oddballs",
    "Troublemakers",
    "Muckrakers",
    "Huckleberries",
    "Bumblebees",
    "Platypuses",
    "Walruses",
    "Narwhals",
    "Dust Devils",
    "Quicksand",
    "Barnacles",
    "Sundials",
    "Firecrackers",
    "Loose Cannons",
    "Paperclips",
    "Cinderblocks",
    "Waffle Irons",
    "Wheelbarrows",
    "Lawnmowers",
    "Boondoggles",
    "Brouhahas",
    "Kerfuffles",
    "Shenanigans",
    "Ruckuses",
    "Hullabaloos",
    "Whippersnappers",
    "Ballyhoos",
    "Hobnobs",
    "Dingbats",
    "Goofballs",
    "Noodlers",
    "Sasquatchers",
    "Pancakes",
    "Meatballs",
    "Spatulas",
    "Toasters",
    "Shopping Carts",
    "Traffic Cones",
    "Rubber Ducks",
    "Tin Foils",
    "Couch Potatoes",
    "Velcro",
    "Staplers",
    "Leftovers",
    "Misfits",
    "Question Marks",
    "Underachievers",
    "Wild Cards",
    "Whoops",
    "Dudes",
    "Nose Pickers",
    "Rednecks",
    "Bong Rippers",
    "Cowpies",
    "Dingoes",
    "Elephant Seals",
    "Headbangers",
    "Walleyes",
    "Crudites",
    "Tastee Freez",
    "Hobgoblins",
    "Iguanas",
    "Kissin' Cousins",
    "Liver Lovers",
    "Mayonnaise",
    "Noodle-oos",
    "Flying Squirrels",
    "Banana Slugs",
    "Sea Otters",
    "Communists"
    "Lobsters",
    "Hillbillies",
    "Granite",
    "Stoners",
    "Puritans",
    "Roosters",
    "Crust Punks",
    "Cheesecake",
    "Day Trippers",
    "Vagabonds",
    "Disease",
    "Horsemen of the Apocalypse",
    "Sinkholes",
    "Executioners",
    "Beachcombers",
    "Jelly",
    "Sea Cucumbers",
    "Pangolins",
    "Vichyssoise",
    "Greco-Romans",
    "Barbarians",
    "Druids",
    "Manatees",
    "Amphibians",
    "Poison Dart Tree Frogs",
    "Disaster Squad",
    "Benchwarmers",
    "Bad News Bears",
    "Orb",
    "Accountants",
    "Jesters",
    "Rapscallions",
    "Orphans",
    "Dictators",
    "Frostbite",
    "Lumberjacks",
    "Virus",
    "Chowder",
    "Jarheads",
    "Cake-Sniffers"
    
]

def random_team_name():
    return random.choice(random_cities) + " " + random.choice(random_team_names)

all_actions = [

# Scoring
"drains a three",
"hits a corner three",
"buries a step-back jumper",
"knocks down a mid-range jumper",
"sinks a turnaround jumper",
"finishes with a smooth layup",
"throws down a thunderous dunk",
"slams home a one-handed jam",
"tips in the miss",
"banks in a runner",
"hits a fadeaway",
"converts the and-one",
"makes both free throws",
"splits the free throws",
"hits a floater in the lane",
"finishes through contact",
"elevates for a powerful dunk",
"hits a pull-up jumper",
"connects from deep",
"knocks down a baseline jumper",

# Misses
"misses a contested three",
"comes up short on a jumper",
"bricks a three",
"misses an easy layup",
"can't finish at the rim",
"has a shot blocked",
"misses both free throws",
"rattles out a jumper",
"airballs a three",
"misses a fadeaway",

# Passing
"finds an open teammate",
"threads a perfect bounce pass",
"throws a no-look pass",
"fires a cross-court pass",
"drops a perfect alley-oop pass",
"sets up a teammate for an easy basket",
"whips a pass into the post",
"finds the cutter",
"kicks it out for three",
"delivers a beautiful assist",

# Rebounding
"grabs the offensive rebound",
"pulls down the defensive rebound",
"snatches the rebound in traffic",
"tips the rebound to a teammate",
"boxes out perfectly",
"wins the rebounding battle",
"cleans the glass",

# Defense
"blocks the shot",
"rejects the layup",
"comes up with a steal",
"jumps the passing lane",
"forces a turnover",
"draws an offensive foul",
"plays outstanding defense",
"ties up the ball for a jump ball",
"strips the ball clean",
"contests the shot perfectly",

# Turnovers
"throws the ball away",
"steps out of bounds",
"travels",
"commits an offensive foul",
"loses the handle",
"throws an errant pass",
"gets called for double dribble",
"is called for carrying",

# Fouls
"commits a hard foul",
"picks up a reach-in foul",
"is called for a blocking foul",
"commits a shooting foul",
"gets whistled for an illegal screen",
"picks up a loose-ball foul",

# Hustle / Miscellaneous
"dives on the floor for the loose ball",
"hustles after the long rebound",
"saves the ball from going out of bounds",
"wins the jump ball",
"draws a charge",
"gets the crowd on its feet",
"fires up the bench",
"celebrates after the big play",
"calls for the ball",
"takes over the game"

]
scoring_actions = [
    "drains a three from the parking lot",
    "hits a half-court heave at the buzzer",
    "catches fire and scores three straight baskets",
    "splits the defense and finishes at the rim",
    "pulls up from the logo and buries it",
    "drives through traffic for an impossible layup",
    "rises over the defense for a thunderous dunk",
    "hits a step-back three with a defender in his face",
    "gets to the rim and finishes through contact",
    "knocks down a jumper from the top of the key",
    "puts the defender on skates and scores",
    "banks one in from an impossible angle",
    "buries a contested jumper at the buzzer",
    "takes over the game with back-to-back buckets",
    "launches a ridiculous three and somehow knocks it down"
]

rebound_actions = [
    "rips down a rebound in traffic",
    "skywalks above everyone for the rebound",
    "snatches the rebound with one hand",
    "bulldozes through the paint for an offensive rebound",
    "grabs the rebound over two defenders",
    "tips the ball to himself and comes down with it",
    "crashes the boards and comes away with the ball",
    "pulls down a huge offensive rebound",
    "outmuscles everyone underneath the basket",
    "snatches a rebound at the peak of the jump",
    "battles through three players for the rebound",
    "grabs the rebound and immediately starts the fast break"
]

assist_actions = [
    "threads a pass through traffic for an easy basket",
    "fires a laser across the court for an open three",
    "finds a teammate cutting to the basket",
    "throws a perfect alley-oop",
    "delivers a no-look pass for an easy bucket",
    "whips a pass through a tiny opening in the defense",
    "finds the open man in the corner",
    "throws a full-court pass for an easy score",
    "drops a perfect dime into the paint",
    "splits the defense with a brilliant pass",
    "draws two defenders and finds the open shooter",
    "delivers a behind-the-back pass for a basket"
]

defense_actions = [
    "swats the ball into the third row",
    "blocks a shot at the rim",
    "strips the ball cleanly from the ball handler",
    "takes a charge that shakes the building",
    "picks the shooter's pocket",
    "rejects a dunk attempt at the rim",
    "snuffs out a fast break all by himself",
    "forces a terrible shot with suffocating defense",
    "comes flying out of nowhere for the block",
    "intercepts the pass and starts the break",
    "locks down the opposing star",
    "swats the shot off the backboard",
    "tips the ball away at the last possible second",
    "makes the defensive play of the game",
    "sends the ball into the cheap seats"
]