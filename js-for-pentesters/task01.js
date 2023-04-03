// https://pentesteracademylab.appspot.com/lab/webapp/jfp/1

// Objectives:
//     Modify the text "Modify me" to "Modified you"
//     Modify the text "Find me" to "Found you"


document.getElementsByTagName('h1')[0].textContent='Found you!';
document.getElementsByClassName('form-signin-heading')[0].textContent='Modified you!';