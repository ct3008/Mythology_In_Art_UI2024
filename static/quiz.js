$(document).ready(function () {
	const pageNum = parseInt(window.location.pathname.split('/').pop());
	// $('.buttons').css('display','block');
	// $('.learn_more').css('display','none');
	if(pageNum != 10){
		if (information.answered == 1) {
			$('.next-button').css('display', 'block');
			$('.buttons').css('display', 'none');
			$('.learn_more').css('display', 'block');
		} else {
			$('.next-button').css('display', 'none');
			$('.buttons').css('display', 'block');
			$('.learn_more').css('display', 'none');
		}
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
				$('.next-button').css('display', 'block');
				$('.buttons').css('display', 'none');
				$('.learn_more').css('display', 'block');
			} else {
				console.error('Failed to submit quiz');
			}
		})
		.catch(error => {
			console.error('Error:', error);
		});
}

function imageZoom(imgID, imgIdx, resultID) {
	var img, lens, result, cx, cy;
	img = document.querySelectorAll(imgID)[imgIdx];
	result = document.getElementById(resultID);
	/* Create lens: */
	lens = document.createElement("DIV");
	lens.setAttribute("class", "img-zoom-lens");
	/* Insert lens: */
	img.parentElement.insertBefore(lens, img);
	/* Calculate the ratio between result DIV and lens: */
	cx = result.offsetWidth / lens.offsetWidth;
	cy = result.offsetHeight / lens.offsetHeight;
	/* Set background properties for the result DIV */
	result.style.backgroundImage = "url('" + img.src + "')";
	result.style.backgroundSize = (img.width * cx) + "px " + (img.height * cy) + "px";

	/* Execute a function when someone moves the cursor over the image, or the lens: */
	lens.addEventListener("mousemove", moveLens);
	img.addEventListener("mousemove", moveLens);
	/* And also for touch screens: */
	lens.addEventListener("touchmove", moveLens);
	img.addEventListener("touchmove", moveLens);

	function moveLens(e) {
		
		var pos, x, y;
		/* Prevent any other actions that may occur when moving over the image */
		e.preventDefault();
		/* Get the cursor's x and y positions: */
		pos = getCursorPos(e);
		/* Calculate the position of the lens: */
		x = pos.x - (lens.offsetWidth / 2);
		y = pos.y - (lens.offsetHeight / 2);
		/* Prevent the lens from being positioned outside the image: */
		if (x > img.width - lens.offsetWidth) { x = img.width - lens.offsetWidth; }
		if (x < 0) { x = 0; }
		if (y > img.height - lens.offsetHeight) { y = img.height - lens.offsetHeight; }
		if (y < 0) { y = 0; }
		/* Set the position of the lens: */
		lens.style.left = x + "px";
		lens.style.top = y + "px";
		/* Set the position of the result box to follow the cursor: */
		result.style.left = (e.pageX + 10) + "px";
    	result.style.top = (e.pageY + 10) + "px";
		/* Display what the lens "sees": */
		result.style.backgroundPosition = "-" + (x * cx) + "px -" + (y * cy) + "px";
	}
	function getCursorPos(e) {
		var rect = img.getBoundingClientRect();
		var x = e.pageX - rect.left - window.scrollX;
		var y = e.pageY - rect.top - window.scrollY;
		return { x: x, y: y };
	}
}


