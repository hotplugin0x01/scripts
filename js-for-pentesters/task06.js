// https://pentesteracademylab.appspot.com/lab/webapp/jfp/6

// Objectives:
    // Capture all Mouse Clicks and Redirect to http://PentesterAcademy.com

document.body.addEventListener('click', function () {
    location.href = 'http://pentesteracademy.com';
}, true) 