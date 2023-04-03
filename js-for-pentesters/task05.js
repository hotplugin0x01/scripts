// https://pentesteracademylab.appspot.com/lab/webapp/jfp/5

// Objectives:
//     Remove the Form and add a notification "Website is Down! Please visit SecurityTube.net"

var h = document.createElement('h1');
h.innerText = 'Website is Down! Please visit SecurityTube.net';

var form = document.forms[0];
form.parentNode.appendChild(h);
form.parentNode.removeChild(form);
