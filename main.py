from flask import Flask, render_template, request, jsonify
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


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/quiz')
def quiz_home():
   return render_template('quiz.html')


@app.route('/quiz/<int:question_number>')
def quiz(question_number):
   #  start question number at 1 and just subtract 1 when accessing indices?
    if question_number < len(fill_in_the_blank):
        information = fill_in_the_blank[question_number]  # Render the first question
        if question_number > 0:
            prev_answered = fill_in_the_blank[question_number - 1]['answered']
        else:
            prev_answered = 1
        return render_template('fill_in_the_blank.html', information=information, prev_answered = prev_answered)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop)):
        information = drag_and_drop[question_number - len(fill_in_the_blank)]  # Render the first question
        if question_number > 0:
            prev_answered = drag_and_drop[question_number - len(fill_in_the_blank) - len(drag_and_drop)]['answered']
        else:
            prev_answered = 1
        return render_template('drag_and_drop.html', information=information, prev_answered = prev_answered)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics)):
        information = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop)]  # Render the first question
        if question_number > 0:
            prev_answered = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_pics.html', information=information, prev_answered = prev_answered)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics) + len(multiple_choice_text)):
        information = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]  # Render the first question
        if question_number > 0:
            prev_answered = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics) - len(multiple_choice_text)]['answered']
        else:
            prev_answered = 1
        return render_template('multiple_choice_text.html', information=information, prev_answered = prev_answered)
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

        return render_template('score.html', score=score, total_score=total_score)

@app.route('/submit_answer/<int:question_id>', methods=['POST'])
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