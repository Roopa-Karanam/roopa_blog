const commentForm = document.querySelector('#comment-form');

async function commentFormSubmitHandler(event) {
  // Prevent submission
  event.preventDefault();

  // Get the form action attribute (URL to post to)
  const apiUrl = commentForm.action;

  // Create a FormData instance with entered data
  const formData = new FormData(commentForm);

  // Post comment to server using AJAX
  const response = await fetch(apiUrl, {
    method: 'POST',
    body: formData,
  });

  if (response.ok) {
    // Hide the form
    commentForm.hidden = true;

    // Create a success message and display
    const successMessage = document.createElement('p');
    successMessage.textContent = 'Your comment was sent!'
    commentForm.parentNode.append(successMessage);
  } else {
    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'An error occurred. Please try again.'
    commentForm.parentNode.append(errorMessage);
  }
}

commentForm.addEventListener('submit', commentFormSubmitHandler);

function likeHandler(event) {
	event.preventDefault();
  
  // Get the element that was clicked on. It's the event
  // currentTarget property.
  const element = event.currentTarget;
  // This is an <a> tag and has a readable href property 
  const response = fetch(element.href, {
    method: 'POST',
    // Set the CSRF token header
    headers: { 'X-CSRFToken': csrftoken,
        "Content-Type": "application/x-www-form-urlencoded" },
    credentials: 'include',
    body: [],
  })
  .then(response => response.text())
  .then(function(text) {
      let num="num"+element.id;
      el = document.getElementById(num);
      el.innerText =parseInt(el.innerText) + 1;
  });  
	
}

// Select multiple classes: both like & dislike buttons
document.querySelectorAll('.likes, .dislikes')
	.forEach(function (link) {
		link.addEventListener('click', likeHandler);
	});
	