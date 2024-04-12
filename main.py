from flask import Flask, render_template
import datetime
app = Flask(__name__)

figures = {
   "1": {
      "id": "1",
      "name": "Zeus",
      "description": "Zeus is the ruler of the cosmos. He is related to right and wrong, justice, political wisdom, law, kingship, and oaths, in addition to physical, social and mental powers. Zeus is married to Hera.",
      "symbols": ["lightning bolt", "sceptre", "eagle"],
      "data": ["zeus1.jpg", "zeus2.jpg", "zeus3.jpg", "zeus4.jpg", "zeus5.jpg", "athenaZeusHephaistos.jpg"]
   },
   "2": {
      "id": "2",
      "name": "Poseidon",
      "description": "Poseidon is the ruler of the sea. He is related to earthquakes, horses, seas, ships, and physical stability. Poseidon is married to Amphitrite.",
      "symbols": ["trident", "horses", "sea creatures"],
      "data": ["poseidon1.jpg", "poseidon2.jpg", "poseidon3.jpg", "poseidon4.jpg", "poseidon5.jpg"]
   },
   "3": {
      "id": "3",
      "name": "Hades",
      "description": "Hades is the ruler of the Underworld. He is he is seen as a figure of earth fertility and riches. Hades is married to Persephone.",
      "symbols": ["scepter", "cornucopia", "riches", "Often shown with Persephone or Kerberos"],
      "data": ["hades1.jpg", "hades2.jpg", "hades3.jpg", "hades4.jpg", "hades5.jpg"]
   },
   "4": {
      "id": "4",
      "name": "Athena",
      "description": "Athena is the goddess of wisdom, war, and weaving (soft crafts). She's in charge of the rational and tactical sides of war. Athena is the daughter of Zeus and often helps heroes in their quests.",
      "symbols": ["aegis (breastplate)", "helmet", "shield", "spear"],
      "data": ["athena1.jpg", "athena2.jpg", "athena3.jpg", "athena4.jpg", "athena5.jpg", "athenaZeusHephaistos.jpg", "heraklesAthena.jpg", "mainAthenaJason.jpg"],
   },
   "5": {
      "id": "5",
      "name": "Hermes",
      "description": "Hermes is the god of crossing boundaries (figuratively and literally) and is the son of Zeus. He is associated with transitions and changes, and is the messenger and trickster god. Hermes also assists with the transition between life and death (takes people to the Underworld).",
      "symbols": ["caduceus (wand/sceptre)", "traveler's cap (petasos)", "winged sandals"],
      "data": ["hermes1.jpg", "hermes2.jpg", "hermes3.jpg", "hermes4.jpg", "hermes5.jpg"],
   },
   "6": {
      "id": "6",
      "name": "Herakles",
      "description": "Herakles is known to be the greatest of all heroes. He is Zeus' son, and exceptional at birth. Herakles is famous for his 12 labors and is the only hero to be immortalized in the Olympus.",
      "symbols": ["lion skin", "bat", "Often shown fighting monsters"],
      "data": ["herakles1.jpg", "herakles2.jpg", "herakles3.jpg", "herakles4.jpg", "herakles5.jpg", "heraklesAthena.jpg"],
   },
   "7": {
      "id": "7",
      "name": "Apollo",
      "description": "description",
      "symbols": "symbols",
      "data": ["apollo1.jpg","apollo2.jpg","apollo3.jpg","apollo4.jpg","apollo5.jpg","apolloArtemis.jpg","apolloAthena.jpg"]
   },
   "8": {
      "id": "8",
      "name": "Artemis",
      "description": "description",
      "symbols": "symbols",
	  "data": ["artemis1.jpg","artemis2.jpg","artemis3.jpg","artemis4.jpg","artemis5.jpg","apolloArtemis.jpg"]

   },
   "9": {
      "id": "9",
      "name": "Dionysus",
      "description": "description",
      "symbols": "symbols",
	  "data": ["dionysus1.jpg","dionysus2.jpg","dionysus3.jpg","dionysus4.jpg","dionysus5.jpg","hephaistosDionysus.jpg"]
   },
   "10": {
      "id": "10",
      "name": "Hephaestus",
      "description": "description",
      "symbols": "symbols",
	  "data": ["hephaistos1.jpg","hephaistos2.jpg","hephaistos3.jpg","hephaistos4.jpg","hephaistos5.jpg","hephaistosDionysus.jpg"]
   }
}


#ask: reset for a new user

#time stamp for each page
user_progress = {}

#sequence of pages visited
user_sequence = []

@app.route('/')
def home():
   user_sequence.append("home")
   user_progress["home"] = datetime.datetime.now()
   print(user_sequence)
   return render_template('home.html', figures=figures)

@app.route('/learn')
def contents():
	user_sequence.append("learn")
	user_progress["learn"] = datetime.datetime.now()
	return render_template('contents.html', figures=figures)

@app.route('/learn/<id>')
def learn(id):
	user_sequence.append("learn/"+id)
	user_progress["learn/"+id] = datetime.datetime.now()
	return render_template('learn.html', figures=figures, figure=figures[id])

if __name__ == '__main__':
   app.run(debug = True)