from flask import Flask, render_template, request, jsonify, redirect, url_for
import datetime
import random
import re
app = Flask(__name__)



fill_in_the_blank = [
   {"id": 0,
	"images": ["PoseidonAthena.jpg"],
	"answers": ["Athena", "Poseidon"], #names left to right,
	"hints": ["PoseidonAthena_annotated.jpg"],
	"more_info":"Currently held in Cabinet des Médailles, Paris, this piece is dated from ca 540 - 530 B.C.", 
	"explanation_text": ["Athena can be identified by her snake-trimmed vest, her spear, and her helmet.", "Poseidon can be identified by his trident."],
    "answered": 0,
    "user_answers":['','']
	},
   {"id": 1,
	"images": ["herakles6.jpg"],
	"answers": ["Apollo", "Herakles", "Artemis"], #names left to right,
	"hints": ["herakles6_annotated.jpg"],
	"more_info":"This is depicts Herakles, Artemis and the Cerynitian Hind, Athenian black-figure amphora from 6th century BC. The Elaphos Kerynitis (Cerynitian Hind) was a golden-horned deer sacred to the goddess Artemis. Herakles was sent to fetch it as one of his twelve labours. After chasing the animal for a full year he finally captured it on Mount Artemision in Arkadia (Arcadia). The goddess Artemis complained about the treatment of her deer whose horn had broken off by the hero in the struggle. He nevertheless managed to persuade her to let him borrow it for the completion of his Labour. According to some the hind was one of five golden-horned deer gifted to Artemis by the Nymph Taygete. The other four drew the chariot of the goddess. The hind may once have been assigned a Constellation like the other beasts of Herakles' labours.", 
	"explanation_text": ["Apollo can be seen donning similar apparel as his twin Artemis. One of them will likely have a bow", "Herakles can be identified here by the lion skin on his shoulders", "Artemis can be identified due to the bow in her hand and her twin Apollo"],
    "answered": 0,
    "user_answers":['','','']
	},
   {"id": 2,
	"images": ["HAHA.jpg"],
	"answers": ["Hermes", "Apollo", "Herakles", "Athena"], #names left to right,
	"hints": ["HAHA_annotated.jpg"],
	"more_info":"Found in museum collection Antikensammlung Berlin. Originated from around 500 B.C. Depicts the reception of Herakles into Olympus", 
	"explanation_text": ["Hermes can be identified by the caduceus he's holding and his winged slippers.", "Apollo can be identified by the lyre he's holding.", "Herakles can be identified through his lionskin pelt and bat.", "Athena can be identified through her spear."],
    "answered": 0,
    "user_answers":['','','','']
	}
   
]

drag_and_drop = [
   {"id": 0,
	"images": ["HephDion_h.jpg","HephDion_d.jpg"],
	"options": ["Dionysus","Hephaestus","Artemis", "Athena"],
	"answers": ["Hephaestus","Dionysus"], # from left to right
	"hints": ["HephDion_h_annotated.jpg","HephDion_d_annotated.jpg"],
	"more_info": "Held in the Toledo Museum of Art. Originates from 430-420 B.C. It depicts Hephaestus' retur to Olympus atop a donkey. He is led by Thionysus and a Satyriscus (child Satyr) playing a flute. \n 'Hephaistos refused to listen to any other of the gods save Dionysos - in him he reposed the fullest trust - and after making him drunk Dionysos brought him to heaven' - Pausanias, Guide to Greece 1.20.3.", 
	"explanation_text": ["Hephaestus is characterized by forging tools like his hammer and tongs.", "Dionysus can be characterized by the wine cup in his right hand, the thyrsus staff in his left hand, and the presence of a satyr near him."],
    "answered": 0,
    "user_answers":['','']
   },
   {"id": 1,
	"images": ["HAZ_z.jpg","HAZ_a.jpg","HAZ_h.jpg"],
	"options": ["Hades","Zeus", "Dionysus","Athena", "Hermes","Hephaestus"],
	"answers": ["Zeus", "Athena", "Hephaestus"], # from left to right
	"hints": ["HAZ_z_annotated.jpg","HAZ_a_annotated.jpg","HAZ_h_annotated.jpg"],
	"more_info": "", 
	"explanation_text": ["Zeus can be identified by his lightning bolt.", "Athena here can be characterized by her emergence from Zeus's head as per her myth.", "Hephaestus can be classified by his forging hammer."],
    "answered": 0,
    "user_answers":['','','']
   }
]

multiple_choice_pics = [
{
	"id": 0,
	"pic_options": ["zeus5_1.jpg", "zeus5_2.jpg", "zeus5_3.jpg"],
	"question": "Find Zeus",
	"answers": ["zeus5_1.jpg"], #0, 1, 2,... answers index of pic options
	"explanation_text": ["Zeus can be identified by his lightning bolt.", "This is Ganymedes holding an oinochoe jug.", "This is Hestia holding a flower the branch of a chaste-tree."],
	"more_info": "hello",
	"hints": ["zeus5_annotated_1.jpg","zeus5_annotated_2.jpg", "zeus5_annotated_3.jpg"],
    "answered": 0,
    "user_answers":['']
},
{
	"id": 1,
	"pic_options": ["hades_mcp1.jpg", "hades_mcp2.jpg", "hades_mcp3.jpg"],
	"question": "Find Hades",
	"answers": ["hades_mcp3.jpg"], #0, 1, 2,... answers index of pic options
	"explanation_text": ["This is Zeus with his sceptre.", "This is Apollo with bow and arrow, and laurel on his head.", "Hades can be identified by the riches and cornucopia."],
	"more_info": "hello",
	"hints": ["hades_mcp1_annotated.jpg", "hades_mcp2_annotated.jpg", "hades_mcp3_annotated.jpg"],
    "answered": 0,
    "user_answers":['']
},

]


multiple_choice_text = [ 
{
    "id": 0,
	"image": "hermes3.jpg",
	"options": ["Hermes", "Apollo", "Dionysus"],
	"question": "To which mythological figure does this piece of art belong?",
	"answers": ["Hermes"],
	"explanation_text": ["Hermes can be identified by his traveler's cap and winged sandals.", "Apollo can be identified by lyre, bow and arrow.", "Dionysus can be indentified by “exotic” animals and clothing, wines, vines and grapes."],
	"more_info": "....background, forklores...",
	"hints": "hermes3_annotated.jpg",
    "answered": 0,
    "user_answers":['']
},
{
    "id": 1,
	"image": "artemis1.jpg",
	"options": ["Athena", "Zeus", "Artemis"],
	"question": "To which mythological figure does this piece of art belong?",
	"answers": ["Artemis"],
	"explanation_text": ["Athena can be identified by breastplate, helmet, shield and spear.", "Zeus can be identified by his lightning bolt and sceptre.", "Artemis can be identified by her bow and arrow."],
	"more_info": "....background, forklores...",
	"hints": "artemis1_annotated.jpg",
    "answered": 0,
    "user_answers":['']
},
{
    "id": 2,
	"image": "dionysus6.jpg",
	"options": ["Poseidon", "Dionysus", "Hephaestus"],
	"question": "To which mythological figure does this piece of art belong?",
	"answers": ["Dionysus"],
	"explanation_text": ["Poseidon can be identified by trident and horses.", "Dionysus can be identified by vines, maenad and satyrs (his followers).", "Hephaestus can be identified by forging weapons and donkey."],
	"more_info": "....background, forklores...",
	"hints": "dionysus6_annotated.jpg",
    "answered": 0,
    "user_answers":['']
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
      "symbols": ['“Exotic” animals and clothing', "wine", "Often with Maenad and Satyrs (his followers)", "vines", "grapes", "thyrsus"],
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

# figures_list = []
# for v in figures.values():
#     figures_list.append(v['name'])

#TODO: Each image has an associated explanation and list of symbols that appear
# (for 'hint', 'learn more', and correct/incorrect answers)

#############################
#generate 10 questions of varying type and content
# questions = []
# used_images = []
# all_images = [
#     { 
#         "name": "zeus1.jpg",
#         "symbols":[], #symbols that appear in this image
#         "learn_more":"" #description of the myth in the image
#     }
# ]
# all_images = ["zeus1.jpg", ""]

#track user answers and progress
# score = 0
# current_question = 0 #prevent users from jumping ahead in the quiz
# user_answers = []

# def gen_fill_in_the_blank():
#     #choose a god and an unused image
#     while True:
#         image = random.choice(all_images)
#         if (image not in used_images):
#             break

#     # if any(image in i for i in figures_list):
#     #     correct_answers = s
#     correct_answers = []
#     # second_option = random.choice(list(set(figures_list) - set([correct_answer])))
#     ret = {
#         "id": 0,
#         "type": "fill_in_the_blank",
#         "images":[image],
#         "hints":[], #'get 'hint' from symbols list in image dictionary
#         "explanation_text":["text"], #get 'explanation' from symbols list in image dictionary
#         "answers": correct_answers,
#         "answered":0,
#         "user_answers":[]
#     }
#     return ret

# question_types = [gen_fill_in_the_blank]
# def generate_questions():
#     for i in range(5):
#        new_question = random.choice(question_types)()
#        new_question["id"] = str(i)
#        questions.append(new_question)
#     return questions
        

# questions = generate_questions()



#ask: reset for a new user

#time stamp for each page
user_progress = {}

#sequence of pages visited
user_sequence = []

#holds the history of scores of the user
all_scores = []

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

# @app.route('/quiz')
# def quiz_home():
#    return render_template('quiz.html', figures=figures)

# #combine all question types
# @app.route('/quiz2/<id>')
# def quiz2(id):
#     question = questions[int(id)]
#     if (int(id) < len(questions)):
#         return render_template(question['type']+'.html', figures=figures, information=question, prev_answered = (current_question >= int(id)))
#     else:
#         return render_template('score.html', figures=figures, score=score, total_score=len(questions))


@app.route('/quiz/<int:question_number>')
def quiz(question_number):
   #  start question number at 1 and just subtract 1 when accessing indices?
    if question_number < len(fill_in_the_blank):
        information = fill_in_the_blank[question_number]  # Render the first question
        if question_number > 0:
            prev_answered = fill_in_the_blank[question_number - 1]['answered']
        else:
            prev_answered = 1
        return render_template('fill_in_the_blank.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop)):
        information = drag_and_drop[question_number - len(fill_in_the_blank)]  # Render the first question
        if question_number > 0:
            prev_answered = drag_and_drop[question_number - len(fill_in_the_blank) - len(drag_and_drop)]['answered']
        else:
            prev_answered = 1
        return render_template('drag_and_drop.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics)):
        information = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop)]  # Render the first question
        if question_number > 0:
            prev_answered = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_pics.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics) + len(multiple_choice_text)):
        information = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]  # Render the first question
        if question_number > 0:
            prev_answered = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics) - len(multiple_choice_text)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_text.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    else:
        score, total_score = calc_score()

        return render_template('score.html', figures=figures, score=score, total_score=total_score, all_scores=all_scores[::-1])

@app.route('/submit_answer/<int:question_id>', methods=['POST'])
def submit_answer(question_id):
    # pass for sake of test
    pass

@app.route('/restart_quiz')
def restart_quiz():
    # Restart quiz
    score, _ = calc_score()
    all_scores.append(score)
    for question in fill_in_the_blank:
        question['answered'] = 0
        for i, _ in enumerate(question['user_answers']):
            question['user_answers'][i] = ''
    for question in drag_and_drop:
        question['answered'] = 0
        for i, _ in enumerate(question['user_answers']):
            question['user_answers'][i] = ''
    for question in multiple_choice_pics:
        question['answered'] = 0
        for i, _ in enumerate(question['user_answers']):
            question['user_answers'][i] = ''
    for question in multiple_choice_text:
        question['answered'] = 0
        for i, _ in enumerate(question['user_answers']):
            question['user_answers'][i] = ''
    return redirect(url_for('quiz', question_number=0))

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
        for idx, answer in enumerate(item['answers']):
            if item['user_answers'][idx].lower() == answer.lower():
                # print("____________INCREASE SCORE________________________________________________________________")
                score += 1
            total_score += 1
    return score, total_score

def calc_score():
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

    return score, total_score
    


if __name__ == '__main__':
   app.run(debug = True)