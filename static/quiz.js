$(document).ready(function () {

	$('.buttons').css('display', 'block');
	$('.learn_more').css('display', 'none');

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

function imageZoom(imgID, resultID) {
	var img, lens, result, cx, cy;
	img = document.getElementById(imgID);
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
		/* Display what the lens "sees": */
		result.style.backgroundPosition = "-" + (x * cx) + "px -" + (y * cy) + "px";
	}
	function getCursorPos(e) {
		var a, x = 0, y = 0;
		e = e || window.event;
		/* Get the x and y positions of the image: */
		a = img.getBoundingClientRect();
		/* Calculate the cursor's x and y coordinates, relative to the image: */
		x = e.pageX - a.left;
		y = e.pageY - a.top;
		/* Consider any page scrolling: */
		x = x - window.pageXOffset;
		y = y - window.pageYOffset;
		return { x: x, y: y };
	}
}

// $('.product-img--main')
//         // tile mouse actions
//         .on('mouseover', function(){
//           $(this).children('.product-img--main__image').css({'transform': 'scale('+ $(this).attr('data-scale') +')'});
//         })
//         .on('mouseout', function(){
//           $(this).children('.product-img--main__image').css({'transform': 'scale(1)'});
//         })
//         .on('mousemove', function(e){
//           $(this).children('.product-img--main__image').css({'transform-origin': ((e.pageX - $(this).offset().left) / $(this).width()) * 100 + '% ' + ((e.pageY - $(this).offset().top) / $(this).height()) * 100 +'%'});
//         })
//         // tiles set up
//         .each(function(){
//           $(this)
//             // add a image container
//             .append('<div class="product-img--main__image"></div>')
//             // set up a background image for each tile based on data-image attribute
//             .children('.product-img--main__image').css({'background-image': 'url('+ $(this).attr('data-image') +')'});
//         });
