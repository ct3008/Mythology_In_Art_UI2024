from flask import Flask, render_template
app = Flask(__name__)

figures = {"1": {
   "id": "1",
   "name": "Zeus",
   "description": "zeus description",
   "symbols": "symbols for zeus",
   "data": ["/static/zeus1.jpg"]
},
"2": {
   "id": "2",
   "name": "Poseidon",
   "description": "description",
   "symbols": "symbols",
   "data": []
},
"3": {
   "id": "3",
   "name": "Hades",
   "description": "description",
   "symbols": "symbols",
   "data": []
},
"4": {
   "id": "4",
   "name": "Athena",
   "description": "description",
   "symbols": "symbols",
   "data": []
},
"5": {
   "id": "5",
   "name": "Hermes",
   "description": "description",
   "symbols": "symbols",
   "data": []
},
"6": {
   "id": "6",
   "name": "Herakles",
   "description": "description",
   "symbols": "symbols",
   "data": []
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
}}


#		
@app.route('/')
def home():
   return render_template('home.html', figures=figures)

@app.route('/learn')
def contents():
   return render_template('contents.html', figures=figures)

@app.route('/learn/<id>')
def learn(id):
   return render_template('learn.html', figures=figures, figure=figures[id])

if __name__ == '__main__':
   app.run(debug = True)