$(document).ready(function(){
	// $('.buttons').css('display','block');
	// $('.learn_more').css('display','none');
	if(information.answered == 1){	
		$('.buttons').css('display','none');
		$('.learn_more').css('display','block');
	}else{
		$('.buttons').css('display','block');
		$('.learn_more').css('display','none');
	}
	

})

    
function submitQuiz() {
	let formData = {
	    user_answers: information.user_answers
	};
	console.log(formData)

	fetch(`/update_information/${information.id}/${questionType}`, {
	    method: 'POST',
	    headers: {
		'Content-Type': 'application/json'
	    },
	    body: JSON.stringify(formData)
	})
	.then(response => {
	    if (response.ok) {
		console.log('Quiz submitted successfully');
		$('.next-button').css('display','block');
		$('.buttons').css('display','none');
		$('.learn_more').css('display','block');
	    } else {
		console.error('Failed to submit quiz');
	    }
	})
	.catch(error => {
	    console.error('Error:', error);
	});
    }


