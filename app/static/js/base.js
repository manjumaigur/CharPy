var text_feed = document.getElementById('text_feed');
var signal_info = document.getElementById('signal_info');
var detectionFlag = 0;

// function startDetection() {
//   detectionFlag = 1;
//   requestText();
// }

// function stopDetection() {
//   detectionFlag = 0;
//   requestText();
// }

// function requestText(){
//   if(detectionFlag) {
//     $.ajax({
//       type: 'GET',
//       url: "http://localhost:5000/text_feed",
//     }).done(function (data) {
//       if (data.success) {
//         text_feed.innerHTML = data.text_detected;
//         setTimeout(requestText, 500);
//       }
//     });
//   }
// }

function send_signal(){
  $.ajax({
    type: 'GET',
    url: "http://localhost:5000/send_signal",
  }).done(function (data) {
    if (data.success) {
      signal_info.innerHTML = "Signals sent";
    }
  });  
}