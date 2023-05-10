var wrapper = document.getElementById('wrapper');

var contact = document.getElementById("contact");

var send = document.getElementById('send');
console.log(send);

if (send != null) {
  send.onclick = function() {
    var name = document.getElementById('name-input');
    console.log(name);
    var email = document.getElementById('email-input');
    console.log(email);
    var body = document.getElementById('message-input');
    console.log(body);
    if (name.value == "" | email.value == "" | body.value == "") {
      return;
    }
    Email.send({
      SecureToken : "614f5024-41ee-472e-aa5f-0a393385f0bf",
      To : 'porterg2003@gmail.com',
      From : 'porterg2003@gmail.com',
      Subject : name.value,
      Body : body.value + "\nMy email is: " + email.value
    }).then( function() {
          contact.style.position = "absolute";
          contact.style.right = "-2000px";
          contact.style.animationName = "sendMail";
          contact.style.animationDuration = "1s";
          var message = document.createElement('p');
          message.innerHTML = "Message sent successfully";
          message.style.animationName = "slideFromRightToCenter";
          message.style.animationDuration = "2s";
          wrapper.appendChild(message);
      });
  }
}
