// https://pentesteracademylab.appspot.com/lab/webapp/jfp/4

// Objectives:
//     Add a new form field called "ATM PIN"


const atm = document.createElement('input');
atm.type = 'text';
atm.name = 'atm-pin';
atm.placeholder = 'ATM PIN';
atm.classList.add('input-block-level');

const form = document.forms[0];
const email = document.forms[0].elements[0];
form.insertBefore(atm, email);