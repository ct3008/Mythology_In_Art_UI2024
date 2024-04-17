from flask import Flask, render_template, request, jsonify
import datetime
import random
app = Flask(__name__)



fill_in_the_blank = [
   {"id": 0,
	"difficulty": "easy",#hard or easy, if hard, no hints,
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus3.jpg?raw=true"],
	"answers": ["zeus", "artemis"], #names left to right,
	"hints": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOf0E92X98LAfnyTXbSBOG3TFHZsNR0oqoZSnSD7Rc4A&s"],
	"more_info":".... history of image + lore", 
	"explanation_text": ["zeus has symbols that...", "bob is short..."],
    "answered": 0,
    "user_answers":[]
	},
   {"id": 1,
	"difficulty": "easy",#hard or easy, if hard, no hints,
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus3.jpg?raw=true"],
	"answers": ["zeus"], #names left to right,
	"hints": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOf0E92X98LAfnyTXbSBOG3TFHZsNR0oqoZSnSD7Rc4A&s"],
	"more_info":".... history of image + lore", 
	"explanation_text": ["zeus has symbols that..."],
    "answered": 0,
    "user_answers":[]
	},
   {"id": 2,
	"difficulty": "easy",#hard or easy, if hard, no hints,
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus3.jpg?raw=true"],
	"answers": ["zeus"], #names left to right,
	"hints": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOf0E92X98LAfnyTXbSBOG3TFHZsNR0oqoZSnSD7Rc4A&s"],
	"more_info":".... history of image + lore", 
	"explanation_text": ["zeus has symbols that..."],
    "answered": 0,
    "user_answers":[]
	}
   
]

drag_and_drop = [
   {"id": 0,
	"difficulty":"easy",
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/athena3.jpg?raw=true","https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/herakles5.jpg?raw=true"],
	"options": ["Athena", "Herakles", "John"],
	"answers": ["Athena", "Herakles"], # from left to right
	"hints": "url_annotated",
	"more_info": ".... history of image + lore", 
	"explanation_text": ["Athena has symbols that...", "Herakles is characterized by symbols"],
    "answered": 0,
    "user_answers":[]
   },
   {"id": 1,
	"difficulty":"easy",
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/athena3.jpg?raw=true","https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/herakles5.jpg?raw=true"],
	"options": ["Athena", "Herakles", "John"],
	"answers": ["Athena", "Herakles"], # from left to right
	"hints": "url_annotated",
	"more_info": ".... history of image + lore", 
	"explanation_text": ["Athena has symbols that...", "Herakles is characterized by symbols"],
    "answered": 0,
    "user_answers":[]
   }
]

multiple_choice_pics = [
{
	"id": 0,
	"difficulty": "easy",
	"pic_options": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus1.jpg?raw=true", "https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/apollo1.jpg?raw=true", "https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/hermes1.jpg?raw=true"],
	"question": "Find Zeus",
	"answers": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus1.jpg?raw=true"], #0, 1, 2,... answers index of pic options
	"explanation_text": ["zeus has symbols that...", "hera has symbols that...", "hermes has symbols that.."],
	"more_info": ".... history of image + lore",
	"hints": ["zeus_url_annotated","hera_url_annotated", "hermes_url_annotated"],
    "answered": 0,
    "user_answers":[]
}

]


multiple_choice_text = [
{
	"id": 0,
	"difficulty": "easy",
	"image": "https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus2.jpg?raw=true",
	"options": ["Zeus", "Hera", "Hermes"],
	"question": "To which mythological figure does this piece of statue belong?",
	"answers": ["Zeus"],
	"explanation_text": ["zeus has symbols that...", "hera has symbols that...", "hermes has symbols that.."],
	"explain_pics": ["url1_zeus", "url2_hera"],
	"more_info": "....background, forklores...",
	"hints": "https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/static/zeus1.jpg?raw=true",
    "answered": 0,
    "user_answers":[]
}

]



############################
#data
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
      "description": "Apollo is the god of music, healing, and prophecy. He is associated with the transitory state between childhood and adulthood (ephebe), the muses, his sister Artemis, and killing monsters and bringing plagues. Apollo is the son of Zeus and is in charge of the oracle of Delphi.",
      "symbols": ["lyre", "laurel", "dolphin", "bow and arrow", "snake", "Often with Artemis (his twin)"],
      "data": ["apollo1.jpg","apollo2.jpg","apollo3.jpg","apollo4.jpg","apollo5.jpg","apolloArtemis.jpg","apolloAthena.jpg"]
   },
   "8": {
      "id": "8",
      "name": "Artemis",
      "description": "Artemis is the goddess of hunting, childhood and adolescence (for females), and wild animals. Shes is associated with childbirth, blood, and is also a destroyer and nurturer. She is Zeus' daughter.",
      "symbols": ["bow and arrow", "wild animals (alive and dead)", "Often with Apollo (her twin)"],
      "data": ["artemis1.jpg","artemis2.jpg","artemis3.jpg","artemis4.jpg","artemis5.jpg","apolloArtemis.jpg"]

   },
   "9": {
      "id": "9",
      "name": "Dionysus",
      "description": "Dionysus is the god of wine and of theater. He is associated with altered states of mind (from the wine) and is the youngest god. He is Zeus' son. His entourage include sailors and Maenads (crazy women).",
      "symbols": ['“exotic” animals and clothing', "wine", "Often with Maenad and Satyrs (his followers)", "vines", "grapes"],
	   "data": ["dionysus1.jpg","dionysus2.jpg","dionysus3.jpg","dionysus4.jpg","dionysus5.jpg","hephaistosDionysus.jpg"]
   },
   "10": {
      "id": "10",
      "name": "Hephaestus",
      "description": "Hephaistos is the god of craftsman (specifically hard crafts, counterbalancing Athena). He has a physical disability and is often seen being carried by a donkey after being kicked out of Mount Olympus. He is married to Aphrodite and is Hera's son.",
      "symbols": ["forging weapons", "donkey", "Often with Athena and Zeus (during Athena's birth)"],
	   "data": ["hephaistos1.jpg","hephaistos2.jpg","hephaistos3.jpg","hephaistos4.jpg","hephaistos5.jpg","hephaistosDionysus.jpg"]
   }
}

figures_list = []
for v in figures.values():
    figures_list.append(v['name'])

#TODO: Each image has an associated explanation and list of symbols that appear
# (for 'hint', 'learn more', and correct/incorrect answers)

#############################
#generate 10 questions of varying type and content
questions = []
used_images = []

#track user answers and progress
score = 0
current_question = 0 #prevent users from jumping ahead in the quiz
user_answers = []

def gen_fill_in_the_blank():
    correct_answer = random.choice(figures_list)
    #get an unused image
    image = correct_answer.lower() + "1.jpg" #1 for now
    second_option = random.choice(list(set(figures_list) - set([correct_answer])))
    ret = {
        "id": 0,
        "type": "fill_in_the_blank",
        "images":[image],
        "hints":[], #'get 'hint' from image dictionary
        "explanation_text":["text"], #get 'explanation' from image dictionary
        "answers":[correct_answer, second_option],
        "answered":0,
        "user_answers":[]
    }
    return ret

question_types = [gen_fill_in_the_blank]
def generate_questions():
    for i in range(5):
       new_question = random.choice(question_types)()
       new_question["id"] = str(i)
       questions.append(new_question)
    return questions
        

questions = generate_questions()



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
	return render_template('learn.html', figures=figures,  figure=figures[id])

@app.route('/quiz')
def quiz_home():
   return render_template('quiz.html', figures=figures)

#combine all question types
@app.route('/quiz2/<id>')
def quiz2(id):
    question = questions[int(id)]
    if (int(id) < len(questions)):
        return render_template(question['type']+'.html', figures=figures, information=question, prev_answered = (current_question >= int(id)))
    else:
        return render_template('score.html', figures=figures, score=score, total_score=len(questions))


@app.route('/quiz/<int:question_number>')
def quiz(question_number):
   #  start question number at 1 and just subtract 1 when accessing indices?
    if question_number < len(fill_in_the_blank):
        information = fill_in_the_blank[question_number]  # Render the first question
        if question_number > 0:
            prev_answered = fill_in_the_blank[question_number - 1]['answered']
        else:
            prev_answered = 1
        return render_template('fill_in_the_blank.html', figures=figures, information=information, prev_answered = prev_answered)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop)):
        information = drag_and_drop[question_number - len(fill_in_the_blank)]  # Render the first question
        if question_number > 0:
            prev_answered = drag_and_drop[question_number - len(fill_in_the_blank) - len(drag_and_drop)]['answered']
        else:
            prev_answered = 1
        return render_template('drag_and_drop.html', figures=figures, information=information, prev_answered = prev_answered)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics)):
        information = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop)]  # Render the first question
        if question_number > 0:
            prev_answered = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_pics.html', figures=figures, information=information, prev_answered = prev_answered)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics) + len(multiple_choice_text)):
        information = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]  # Render the first question
        if question_number > 0:
            prev_answered = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics) - len(multiple_choice_text)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_text.html', figures=figures, information=information, prev_answered = prev_answered)
    else:
        score = 0
        total_score = 0
        score_1, total_score_1 = find_score(fill_in_the_blank)
        score += score_1
        total_score += total_score_1
        
        score_2, total_score_2 = find_score(drag_and_drop)
        score += score_2
        total_score += total_score_2
        
        score_3, total_score_3 = find_score(multiple_choice_pics)
        score += score_3
        total_score += total_score_3
        
        score_4, total_score_4 = find_score(multiple_choice_text)
        score += score_4
        total_score += total_score_4

        return render_template('score.html', figures=figures, score=score, total_score=total_score)

@app.route('/submit_answer2/<int:question_id>', methods=['POST'])
def submit_answer(question_id):
    # pass for sake of test
    pass

@app.route('/update_information/<int:id>/<string:questionType>', methods=['POST'])
def update_information(id, questionType):
    data = request.json
    if questionType == 'fitb':
        information = fill_in_the_blank[id]
    elif questionType == 'dd':
        information = drag_and_drop[id]
    elif questionType == 'mcp':
        information = multiple_choice_pics[id]
    elif questionType == 'mct':
        information = multiple_choice_text[id]
    information['user_answers'] = data['user_answers']
    # print(data)
    information['answered'] = 1
    
    # data = request.json  # Get data sent from the client
    # Update the information list based on the received data, pageNum, and questionType
    # Logic to update the information list...
    return jsonify({'message': 'Information updated successfully'})

def find_score(list):
    score = 0
    total_score = 0
    for item in list:
        print(item)
        for idx, answer in enumerate(item['answers']):
            if item['user_answers'][idx].lower() == answer.lower():
                # print("____________INCREASE SCORE________________________________________________________________")
                score += 1
            total_score += 1
    return score, total_score
    


if __name__ == '__main__':
   app.run(debug = True)