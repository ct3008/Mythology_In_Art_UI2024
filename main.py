from flask import Flask, render_template, request, jsonify, redirect, url_for
import datetime
import random
# import res
app = Flask(__name__)



fill_in_the_blank = [
   {"id": 0,
	"images": ["1.jpg"],
    "question": "Fill in the Blank",
	"answers": ["Athena", "Poseidon"], #names left to right,
	"hints": ["1_annotated.jpg"],
	"more_info":"Currently held in Cabinet des Médailles, Paris, this piece is dated from ca 540 - 530 B.C. \n Athena competed with Poseidon to be the patron deity of Athens, which was yet unnamed, in a version of one founding myth. They agreed that each would give the Athenians one gift and that the Athenians would choose the gift they preferred. Poseidon struck the ground with his trident and a salt water spring sprang up; this gave them a means of trade and water - Athens at its height was a significant sea power, defeating the Persian fleet at the Battle of Salamis - but the water was salty and not very good for drinking. Athena, however, offered them the first domesticated olive tree. The Athenians (or their king, Cecrops) accepted the olive tree and with it the patronage of Athena, for the olive tree brought wood, oil, and food. Robert Graves was of the opinion that 'Poseidon's attempts to take possession of certain cities are political myths' which reflect the conflict between matriarchal and patriarchal religions.", 
	"explanation_text": ["Athena: aegis (breastplate), spear, and helmet", "Poseidon: trident"],
    "answered": 0,
    "user_answers":['','']
	},
   {"id": 1,
	"images": ["2.jpg"],
    "question": "Fill in the Blank",
	"answers": ["Athena", "Herakles", "Artemis"], #names left to right,
	"hints": ["2_annotated.jpg"],
	"more_info":"This is depicts Herakles, Artemis and the Cerynitian Hind, Athenian black-figure amphora from 6th century BC. \n The Elaphos Kerynitis (Cerynitian Hind) was a golden-horned deer sacred to the goddess Artemis. Herakles was sent to fetch it as one of his twelve labours. After chasing the animal for a full year he finally captured it on Mount Artemision in Arkadia (Arcadia). The goddess Artemis complained about the treatment of her deer whose horn had broken off by the hero in the struggle. He nevertheless managed to persuade her to let him borrow it for the completion of his Labour. According to some the hind was one of five golden-horned deer gifted to Artemis by the Nymph Taygete. The other four drew the chariot of the goddess. The hind may once have been assigned a Constellation like the other beasts of Herakles' labours.", 
	"explanation_text": ["Athena: helmet", "Herakles: lion skin", "Artemis: bow and arrow"],
    "answered": 0,
    "user_answers":['','','']
	},
   {"id": 2,
	"images": ["3.jpg"],
    "question": "Fill in the Blank",
	"answers": ["Hermes", "Apollo", "Herakles", "Athena"], #names left to right,
	"hints": ["3_annotated.jpg"],
	"more_info":"Found in museum collection Antikensammlung Berlin. Originated from around 500 B.C. \n Heracles, accompanied by the gods Hermes, Apollo and Athena, is ascending to Olympus. Hermes carries a ram and the herald's wand as he looks back at Apollo. Apollo, who holds a lyre, is attired in woman's robes and veiled. A deer stands behind him. Heracles, wearing lion skin, has a club in his hand and a quiver hung over his shoulder. Behind him stands Athena holding a spear in her hand.", 
	"explanation_text": ["Hermes: caduceus and winged slippers", "Apollo: lyre", "Herakles: lionskin and bat", "Athena: spear"],
    "answered": 0,
    "user_answers":['','','','']
	}
   
]

drag_and_drop = [
   {"id": 0,
    "question": "Drag the Correct Name to Each Image",
	"images": ["4.jpg","4.2.jpg"],
	"options": ["Dionysus","Hephaistos","Artemis", "Athena"],
	"answers": ["Hephaistos","Dionysus"], # from left to right
	"hints": ["4_annotated.jpg","4.2_annotated.jpg"],
	"more_info": "Held in the Toledo Museum of Art. Originates from 430-420 B.C. \n It depicts Hephaistos' return to Olympus atop a donkey. He is led by Thionysus and a Satyriscus (child Satyr) playing a flute. \n 'Hephaistos refused to listen to any other of the gods save Dionysos - in him he reposed the fullest trust - and after making him drunk Dionysos brought him to heaven' - Pausanias, Guide to Greece 1.20.3.", 
	"explanation_text": ["Hephaistos: hammer, tongs (forging tools), and donkey", "Dionysus: wine cup, thyrsus staff, and satyr"],
    "answered": 0,
    "user_answers":['','']
   },
   {"id": 1,
    "question": "Drag the Correct Name to Each Image",
	"images": ["5.jpg","5.1.jpg","5.2.jpg"],
	"options": ["Hades","Zeus", "Dionysus","Athena", "Hermes","Hephaistos"],
	"answers": ["Zeus", "Athena", "Hephaistos"], # from left to right
	"hints": ["5_annotated.jpg","5.1_annotated.jpg","5.2_annotated.jpg"],
	"more_info": "Held in the British Museum in London. Dates ca. 555 - 550 B.C. \n Hephaistos births Athena from the skull of Zeus with the blow of an axe. The king of the gods is seated on a throne decorated with the head of a swan and brandishes a lightning-bolt in his outstretched hand. Athena springs forth from his head, born ready-equipped with a shield. Hephaistos waves a hand, imitating an Eileithyia (birth-goddess), and holds a double-headed axe or mallet. He wears a short workman's chiton and boots.", 
	"explanation_text": ["Zeus: lightning bolt", "Athena: emerging from Zeus' head", "Hephaistos: forging hammer."],
    "answered": 0,
    "user_answers":['','','']
   }
]

multiple_choice_pics = [
{
	"id": 0,
	"pic_options": ["6.jpg", "6.1.jpg", "6.2.jpg"],
	"question": "Find Zeus",
	"answers": ["6.jpg"], #0, 1, 2,... answers index of pic options
	"explanation_text": ["Zeus can be identified by his lightning bolt and scepter.", "This is Ganymedes holding an oinochoe jug.", "This is Hestia holding a flower the branch of a chaste-tree."],
	"more_info": "The painting is from a kylix, a type of Greek drinking cup, is displayed at the National Archaeological Museum of Tarquinia and holds the catalogue number RC6848. It's part of the Attic Red Figure pottery style and is believed to be the work of Oltos, an artist from the Archaic period of ancient Greece. The cup's detailed red images against a black backdrop are typical of this style and era, capturing a piece of history in its design.",
	"hints": ["6_annotated_1.jpg","6_annotated_2.jpg", "6_annotated_3.jpg"],
    "answered": 0,
    "user_answers":['']
},
{
	"id": 1,
	"pic_options": ["7.jpg", "7.1.jpg", "7.2.jpg"],
	"question": "Find Hades",
	"answers": ["7.2.jpg"], #0, 1, 2,... answers index of pic options
	"explanation_text": ["This is Zeus with his scepter.", "This is Apollo with bow and arrow, and laurel on his head.", "Hades can be identified by the riches and cornucopia."],
	"more_info": "The painting with Hades is on a jar called pelike in The National Archaeological Museum in Athens, with the identification number Athens 16346. It features the red-figure pottery style and is thought to have been painted by the Orestes Painter, a known artist from ancient Greece's Classical period. The exact date it was made isn't recorded, but its style reflects that era's art.",
	"hints": ["7_annotated.jpg", "7.1_annotated.jpg", "7.2_annotated.jpg"],
    "answered": 0,
    "user_answers":['']
},

]


multiple_choice_text = [ 
{
    "id": 0,
	"image": "8.jpg",
	"options": ["Hermes", "Apollo", "Dionysus"],
	"question": "To which mythological figure does this piece of art belong?",
	"answers": ["Hermes"],
	"explanation_text": ["Hermes can be identified by his traveler's cap, winged sandals, and caduceus (wand/scepter).", "Apollo can be identified by lyre, bow and arrow.", "Dionysus can be indentified by “exotic” animals and clothing, wines, vines and grapes."],
	"more_info": "This painting piece of the god Hermes are on the inside of a Kylie, a type of Ancient Greek cup. It's decorated with a festive scene on the outside and was made in Athens by potter Pamphaios and painter Ambrosios Painter around 510 BC. The cup, found in Vulci, is now in the Munich State Collection of Antiquities, inventory number 2614. It's made of clay and mentioned in a book on red-figure vase painters by John D. Beazley.",
	"hints": "8_annotated.jpg",
    "answered": 0,
    "user_answers":['']
},
{
    "id": 1,
	"image": "9.jpg",
	"options": ["Athena", "Zeus", "Artemis"],
	"question": "To which mythological figure does this piece of art belong?",
	"answers": ["Artemis"],
	"explanation_text": ["Athena can be identified by breastplate, helmet, shield and spear.", "Zeus can be identified by his lightning bolt and scepter.", "Artemis can be identified by her bow and arrow."],
	"more_info": "The painting of Artemis is on a bell krater, a type of ancient Greek vase for mixing wine and water, housed in the Museum of Fine Arts, Boston, under the catalogue number Boston 10.185. Made around 470 B.C., it features the Attic red-figure style and is known as the name vase of the Pan Painter, a celebrated artist of the Early Classical period. This piece highlights the artistic and cultural achievements of ancient Greece.",
	"hints": "9_annotated.jpg",
    "answered": 0,
    "user_answers":['']
},
{
    "id": 2,
	"image": "10.jpg",
	"options": ["Poseidon", "Dionysus", "Hephaistos"],
	"question": "To which mythological figure does this piece of art belong?",
	"answers": ["Dionysus"],
	"explanation_text": ["Poseidon can be identified by trident and horses.", "Dionysus can be identified by vines, maenad and satyrs (his followers).", "Hephaistos can be identified by forging weapons and donkey."],
	"more_info": "This piece is attributed to the painter Makron and can be found within the Antikensammlung Berlin museum collection in catalog number Berlin F2290. It depicts Dionysus crowned with a wreath of ivy and holding a fruiting grapevine in one hand and thyrsos (pine-cone tipped staff) in the other. He is accompanied by a Satyr playing a double-flute.",
	"hints": "10_annotated.jpg",
    "answered": 0,
    "user_answers":['']
}

]



############################
#data
figures = {
    "1": {
      "id": "1",
      "name": "Apollo",
      "description": "Apollo is the god of music, healing, and prophecy. He is associated with the transitory state between childhood and adulthood (ephebe), the muses, his sister Artemis, and killing monsters and bringing plagues. Apollo is the son of Zeus and is in charge of the oracle of Delphi.",
      "symbols": ["lyre", "laurel", "dolphin", "bow and arrow", "snake", "Often with Artemis (his twin)"],
      "data": ["apollo1.jpg","apollo2.jpg","apollo3.jpg","apollo4.jpg","apollo5.jpg","apolloArtemis.jpg","apolloAthena.jpg"]
   },
   "2": {
      "id": "2",
      "name": "Artemis",
      "description": "Artemis is the goddess of hunting, childhood and adolescence (for females), and wild animals. She is associated with childbirth, blood, and is also a destroyer and nurturer. She is Zeus' daughter.",
      "symbols": ["bow and arrow", "wild animals (alive and dead)", "Often with Apollo (her twin)"],
      "data": ["artemis2.jpg", "artemis5.jpg", "artemis1.jpg", "artemis3.jpg", "artemis4.jpg", "apolloArtemis.jpg"]

   },
   "3": {
      "id": "3",
      "name": "Athena",
      "description": "Athena is the goddess of wisdom, war, and weaving (soft crafts). She's in charge of the rational and tactical sides of war. Athena is the daughter of Zeus and often helps heroes in their quests.",
      "symbols": ["aegis (breastplate)", "helmet", "shield", "spear"],
      "data": ["athena3.jpg", "athena5.jpg", "athena1.jpg", "athena2.jpg", "athena4.jpg", "athenaZeusHephaistos.jpg", "heraklesAthena.jpg", "mainAthenaJason.jpg"],
   },
   "4": {
      "id": "4",
      "name": "Dionysus",
      "description": "Dionysus is the god of wine and of theater. He is associated with altered states of mind (from the wine) and is the youngest god. He is Zeus' son. His entourage include sailors and Maenads (crazy women).",
      "symbols": ['“Exotic” animals and clothing', "wine", "Often with Maenad and Satyrs (his followers)", "vines", "grapes"],
	   "data": ["dionysus1.jpg", "dionysus4.jpg", "dionysus2.jpg", "dionysus3.jpg", "dionysus5.jpg", "hephaistosDionysus.jpg"]
     
   },
   "5": {
      "id": "5",
      "name": "Hades",
      "description": "Hades is the ruler of the Underworld. He is seen as a figure of earth fertility and riches. Hades is married to Persephone.",
      "symbols": ["scepter", "cornucopia", "riches", "Often shown with Persephone or Kerberos"],
      "data": ["hades2.jpg", "hades5.jpg", "hades1.jpg", "hades3.jpg", "hades4.jpg"]
   },
   "6": {
      "id": "6",
      "name": "Hephaistos",
      "description": "Hephaistos is the god of craftsman (specifically hard crafts, counterbalancing Athena). He has a physical disability and is often seen being carried by a donkey after being kicked out of Mount Olympus. He is married to Aphrodite and is Hera's son.",
      "symbols": ["forging weapons", "donkey", "Often with Athena and Zeus (during Athena's birth)"],
	   "data": ["hephaistos1.jpg","hephaistos2.jpg","hephaistos3.jpg","hephaistos4.jpg","hephaistos5.jpg","hephaistosDionysus.jpg"]
   },
   "7": {
      "id": "7",
      "name": "Herakles",
      "description": "Herakles is known to be the greatest of all heroes. He is Zeus' son, and exceptional at birth. Herakles is famous for his 12 labors and is the only hero to be immortalized in the Olympus.",
      "symbols": ["lion skin", "bat", "Often shown fighting monsters"],
      "data": ["herakles1.jpg", "herakles5.jpg", "herakles2.jpg", "herakles3.jpg", "herakles4.jpg", "heraklesAthena.jpg"],
   },
   "8": {
      "id": "8",
      "name": "Hermes",
      "description": "Hermes is the god of crossing boundaries (figuratively and literally) and is the son of Zeus. He is associated with transitions and changes, and is the messenger and trickster god. Hermes also assists with the transition between life and death (takes people to the Underworld).",
      "symbols": ["caduceus (wand/scepter)", "petasos (traveler's cap)", "winged sandals"],
      "data": ["hermes1.jpg", "hermes2.jpg", "hermes3.jpg", "hermes4.jpg", "hermes5.jpg"],
   },
   "9": {
      "id": "9",
      "name": "Poseidon",
      "description": "Poseidon is the ruler of the sea. He is related to earthquakes, horses, seas, ships, and physical stability. Poseidon is married to Amphitrite.",
      "symbols": ["trident", "horses", "sea creatures"],
      "data": ["poseidon1.jpg", "poseidon5.jpg", "poseidon2.jpg", "poseidon3.jpg", "poseidon4.jpg"]
   },
   "10": {
      "id": "10",
      "name": "Zeus",
      "description": "Zeus is the ruler of the cosmos. He is related to right and wrong, justice, political wisdom, law, kingship, and oaths, in addition to physical, social and mental powers. Zeus is married to Hera.",
      "symbols": ["lightning bolt", "scepter", "eagle"],
      "data": ["zeus1.jpg", "zeus3.jpg", "zeus2.jpg", "zeus4.jpg", "zeus5.jpg", "athenaZeusHephaistos.jpg"]
   }
}

all_images = {
    "zeus1.jpg": {
        "symbols":{
            "lightning bolt":[70,80],
            "scepter":[35,90]
        }
    },
    "zeus3.jpg": {
        "symbols":{
            "lightning bolt":[20,90],
            "eagle":[80,80]
        }
    },
    "poseidon1.jpg": {
        "symbols":{
            "trident":[60,90],
            "sea creatures":[20,30]
        }
    },
    "poseidon5.jpg": {
        "symbols":{
            "trident":[60,50],
            "sea creatures":[35,45]
        }
    },  
    "hades2.jpg": {
        "symbols":{
            "cornucopia":[40,60],
            "Persephone":[75,60],
            "scepter":[60,60],
            '"riches"':[50,50],
        }
    }, 
    "hades5.jpg": {
        "symbols":{
            "scepter":[72,60],
            "Persephone":[30,50],
        }
    }, 
    "athena3.jpg": {
        "symbols":{
            "shield":[33,20],
            "spear":[65,85],
            "helmet":[45,80],
            "aegis":[53,60],

        }
    }, 
    "athena5.jpg": {
        "symbols":{
            "helmet":[47,90],
            "aegis":[48,67],
        }
    },
    "hermes1.jpg": {
        "symbols":{
            "petasos":[35,80],
            "caduceus":[35,53],
            "winged sandals":[28,10]
        }
    },
    "hermes2.jpg": {
        "symbols":{
            "petasos":[60,95],
            "caduceus":[40,73],
            "winged sandals":[46,8]
        }
    },
    "herakles1.jpg": {
        "symbols":{
            "lion skin":[55,70],
            "bat":[65,65]
        }
    },
    "herakles5.jpg": {
        "symbols":{
            "lion skin":[35,30],
            "bat":[60,70]
        }
    },
    "apollo1.jpg": {
        "symbols":{
            "lyre":[60,70],
            "animals":[68,30],
        }
    },
    "apollo2.jpg": {
        "symbols":{
            "lyre":[50,50],
            "laurel":[50,90],
            "bow and arrow":[85,90]
        }
    },
    "artemis2.jpg": {
        "symbols":{
            "wild animals":[30,26],
            "bow and arrow":[70, 70],
        }
    },
    "artemis5.jpg": {
        "symbols":{
            "wild animals":[35,20],
            "bow and arrow":[40,73],
        }
    },
    "dionysus1.jpg": {
        "symbols":{
            '"exotic" animals':[32,50],
            "vines":[50,80],
        }
    },
    "dionysus4.jpg": {
        "symbols":{
            '"exotic" animals':[54,40],
            "vines":[30,44],
            '"exotic" clothing':[40,30],
            "satyr":[20,50],
            "maenad":[73,30],
        }
    },
    "hephaistos1.jpg": {
        "symbols":{
            "forged weapons":[53,70],
            "donkey":[65,40],
        }
    },
    "hephaistos2.jpg": {
        "symbols":{
            "forging weapons":[70,40]
        }
    },
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
dates = []

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
	return render_template('learn.html', figures=figures,  figure=figures[id], images=all_images)

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
        information = fill_in_the_blank[question_number]
        if question_number > 0:
            prev_answered = fill_in_the_blank[question_number - 1]['answered']
        else:
            prev_answered = 1
        return render_template('fill_in_the_blank.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop)):
        information = drag_and_drop[question_number - len(fill_in_the_blank)]
        if question_number > 0:
            prev_answered = drag_and_drop[question_number - len(fill_in_the_blank) - len(drag_and_drop)]['answered']
        else:
            prev_answered = 1
        return render_template('drag_and_drop.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics)):
        information = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop)]
        if question_number > 0:
            prev_answered = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_pics.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics) + len(multiple_choice_text)):
        information = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]
        if question_number > 0:
            prev_answered = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics) - len(multiple_choice_text)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_text.html', figures=figures, information=information, prev_answered=prev_answered, question_id=question_number)
    else:
        score, total_score = calc_score()
        combined_data = list(zip(all_scores[::-1], dates[::-1]))
        return render_template('score.html', figures=figures, score=score, total_score=total_score, combined_data=combined_data)

@app.route('/submit_answer/<int:question_id>', methods=['POST'])
def submit_answer(question_id):
    # pass for sake of test
    pass

@app.route('/restart_quiz')
def restart_quiz():
    # restart quiz
    score, _ = calc_score()
    all_scores.append(score)
    formatted_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dates.append(formatted_date)
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