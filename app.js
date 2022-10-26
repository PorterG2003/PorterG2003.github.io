var contact = document.getElementById("contact")

send.onclick = function() {
  var name = document.getElementById('name-input');
  console.log(name);
  var email = document.getElementById('email-input');
  console.log(email);
  var body = document.getElementById('message-input');
  console.log(body);
  var send = document.getElementById('send');
	Email.send({
    SecureToken : "614f5024-41ee-472e-aa5f-0a393385f0bf",
    To : 'porterg2003@gmail.com',
    From : 'porterg2003@gmail.com',
    Subject : name.value,
    Body : body.value + "\nMy email is: " + email.value
  }).then( function() {
        name.style.display = "none";
        email.style.display = "none";
        body.style.display = "none";
        send.style.display = "none";
        var message = document.createElement('p');
        message.innerHTML = "Message sent successfully";
        contact.appendChild(message);
    });
}
