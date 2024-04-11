from flask import Flask, render_template
app = Flask(__name__)




fill_in_the_blank = [
   {"id": 0,
	"difficulty": "easy",#hard or easy, if hard, no hints,
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/data/zeus3.jpg?raw=true"],
	"answers": ["zeus"], #names left to right,
	"hints": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOf0E92X98LAfnyTXbSBOG3TFHZsNR0oqoZSnSD7Rc4A&s"],
	"more_info":".... history of image + lore", 
	"explanation_text": ["zeus has symbols that..."]
	},
   {"id": 1,
	"difficulty": "easy",#hard or easy, if hard, no hints,
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/data/zeus3.jpg?raw=true"],
	"answers": ["zeus"], #names left to right,
	"hints": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOf0E92X98LAfnyTXbSBOG3TFHZsNR0oqoZSnSD7Rc4A&s"],
	"more_info":".... history of image + lore", 
	"explanation_text": ["zeus has symbols that..."]
	},
   {"id": 2,
	"difficulty": "easy",#hard or easy, if hard, no hints,
	"images": ["https://github.com/ct3008/Mythology_In_Art_UI2024/blob/main/data/zeus3.jpg?raw=true"],
	"answers": ["zeus"], #names left to right,
	"hints": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOf0E92X98LAfnyTXbSBOG3TFHZsNR0oqoZSnSD7Rc4A&s"],
	"more_info":".... history of image + lore", 
	"explanation_text": ["zeus has symbols that..."]
	}
   
]

drag_and_drop = [
   {"id": 0,
	"difficulty":"easy",
	"image": "url",
	"options": ["option1", "option2", "option3"],
	"answers": ["name1", "name2", "name3"], # from left to right
	"hints": "url_annotated",
	"more_info": ".... history of image + lore", 
	"explanation_text": ["zeus has symbols that...", "other is characterized by symbols", ...],
   },
   {"id": 1,
	"difficulty":"easy",
	"image": "url",
	"options": ["option1", "option2", "option3"],
	"answers": ["name1", "name2", "name3"], # from left to right
	"hints": "url_annotated",
	"more_info": ".... history of image + lore", 
	"explanation_text": ["zeus has symbols that...", "other is characterized by symbols", ...],
   }
]

multiple_choice_pics = [
{
	"id": 0,
	"difficulty": "easy",
	"pic_options": ["zeus_url", "hera_url", "hermes_url"],
	"question": "Find Zeus",
	"answer": "0", #0, 1, 2,... answers index of pic options
	"explanation_text": ["zeus has symbols that...", "hera has symbols that...", "hermes has symbols that.."],
	"more_info": ".... history of image + lore",
	"hints": ["zeus_url_annotated","hera_url_annotated", "hermes_url_annotated"],
}

]


multiple_choice_text = [
{
	"id": 0,
	"difficulty": "easy",
	"image": "url",
	"options": ["zeus", "hera", "hermes"],
	"question": "......",
	"answer": "zeus",
	"explanation_text": ["zeus has symbols that...", "hera has symbols that...", "hermes has symbols that.."],
	"explain_pics": ["url1_zeus", "url2_hera"],
	"more_info": "....background, forklores...",
	"hints": "url_annotated",
}

]

score = 0

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/quiz/<int:question_number>')
def quiz(question_number):
   #  start question number at 1 and just subtract 1 when accessing indices?
    if question_number < len(fill_in_the_blank):
        information = fill_in_the_blank[question_number]  # Render the first question
        return render_template('fill_in_the_blank.html', information=information)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop)):
        information = drag_and_drop[question_number - len(fill_in_the_blank)]  # Render the first question
        return render_template('drag_and_drop.html', information=information)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics)):
        information = multiple_choice_pics[question_number - len(fill_in_the_blank) - len(drag_and_drop)]  # Render the first question
        return render_template('multiple_choice_pics.html', information=information)
    elif question_number < (len(fill_in_the_blank) + len(drag_and_drop) + len(multiple_choice_pics) + len(multiple_choice_text)):
        information = multiple_choice_text[question_number - len(fill_in_the_blank) - len(drag_and_drop) - len(multiple_choice_pics)]  # Render the first question
        return render_template('multiple_choice_text.html', information=information)
    else:
        return render_template('score.html', score=score)



if __name__ == '__main__':
   app.run(debug = True)