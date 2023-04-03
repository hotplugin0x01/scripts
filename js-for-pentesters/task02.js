// https://pentesteracademylab.appspot.com/lab/webapp/jfp/2

// Objectives:
//     Change all the Links on this page to "http://PentesterAcademy/topics"


const as = document.getElementsByTagName('a'); 
for (let i=0; i < as.length; i++) {
    as[i].href = 'http://PentesterAcademy/topics';
    as[i].textContent = as[i].textContent + ' (Changed)';
}