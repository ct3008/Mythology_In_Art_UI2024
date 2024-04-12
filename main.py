from flask import Flask, render_template
import datetime
app = Flask(__name__)

figures = {
   "1": {
      "id": "1",
      "name": "Zeus",
      "description": "Zeus is the ruler of the cosmos. He is related to right and wrong, justice, political wisdom, law, kingship, and oaths, in addition to physical, social and mental powers. Zeus is married to Hera.",
      "symbols": ["lightning bolt", "sceptre", "eagle"],
      "data": ["/static/zeus1.jpg", "/static/zeus2.jpg", "/static/zeus3.jpg", "/static/zeus4.jpg", "/static/zeus5.jpg", "athenaZeusHephaistos.jpg"]
   },
   "2": {
      "id": "2",
      "name": "Poseidon",
      "description": "Poseidon is the ruler of the sea. He is related to earthquakes, horses, seas, ships, and physical stability. Poseidon is married to Amphitrite.",
      "symbols": ["trident", "horses", "sea creatures"],
      "data": ["/static/poseidon1.jpg", "/static/poseidon2.jpg", "/static/poseidon3.jpg", "/static/poseidon4.jpg", "/static/poseidon5.jpg"]
   },
   "3": {
      "id": "3",
      "name": "Hades",
      "description": "Hades is the ruler of the Underworld. He is he is seen as a figure of earth fertility and riches. Hades is married to Persephone.",
      "symbols": ["scepter", "cornucopia", "riches", "Often shown with Persephone or Kerberos"],
      "data": ["/static/hades1.jpg", "/static/hades2.jpg", "/static/hades3.jpg", "/static/hades4.jpg", "/static/hades5.jpg"]
   },
   "4": {
      "id": "4",
      "name": "Athena",
      "description": "Athena is the goddess of wisdom, war, and weaving (soft crafts). She's in charge of the rational and tactical sides of war. Athena is the daughter of Zeus and often helps heroes in their quests.",
      "symbols": ["aegis (breastplate)", "helmet", "shield", "spear"],
      "data": ["/static/athena1.jpg", "/static/athena2.jpg", "/static/athena3.jpg", "/static/athena4.jpg", "/static/athena5.jpg", "/static/athenaZeusHephaistos.jpg", "/static/heraklesAthena.jpg", "/static/mainAthenaJason.jpg"],
   },
   "5": {
      "id": "5",
      "name": "Hermes",
      "description": "Hermes is the god of crossing boundaries (figuratively and literally) and is the son of Zeus. He is associated with transitions and changes, and is the messenger and trickster god. Hermes also assists with the transition between life and death (takes people to the Underworld).",
      "symbols": ["caduceus (wand/sceptre)", "traveler's cap (petasos)", "winged sandals"],
      "data": ["/static/hermes1.jpg", "/static/hermes2.jpg", "/static/hermes3.jpg", "/static/hermes4.jpg", "/static/hermes5.jpg"],
   },
   "6": {
      "id": "6",
      "name": "Herakles",
      "description": "Herakles is known to be the greatest of all heroes. He is Zeus' son, and exceptional at birth. Herakles is famous for his 12 labors and is the only hero to be immortalized in the Olympus.",
      "symbols": ["lion skin", "bat", "Often shown fighting monsters"],
      "data": ["/static/herakles1.jpg", "/static/herakles2.jpg", "/static/herakles3.jpg", "/static/herakles4.jpg", "/static/herakles5.jpg", "/static/heraklesAthena.jpg"],
   },
   "7": {
      "id": "7",
      "name": "Apollo",
      "description": "description",
      "symbols": "symbols",
      "data": []
   },
   "8": {
      "id": "8",
      "name": "Artemis",
      "description": "description",
      "symbols": "symbols",
      "data": []
   },
   "9": {
      "id": "9",
      "name": "Dionysus",
      "description": "description",
      "symbols": "symbols",
      "data": []
   },
   "10": {
      "id": "10",
      "name": "Hephaestus",
      "description": "description",
      "symbols": "symbols",
      "data": []
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