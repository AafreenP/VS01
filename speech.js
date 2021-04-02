var SpeechRecognition = window.webkitSpeechRecognition;
  
var recognition = new SpeechRecognition();
 
var Textbox = $('#textbox');
var instructions = $('instructions');
 
var Content = '';
 
recognition.continuous = true;
//===================================

recognition.interimResults = true;

var final_transcript='';

function startButton(event) {
  final_transcript = '';
  recognition.lang = select_dialect.value;
  recognition.start();
}

recognition.onresult = function(event) {
  var interim_transcript = '';

  for (var i = event.resultIndex; i < event.results.length; ++i) {
    if (event.results[i].isFinal) {
      final_transcript += event.results[i][0].transcript;
      Textbox.val(final_transcript);
    } else {
      interim_transcript += event.results[i][0].transcript;
      Textbox.val(interim_transcript);
    }
  }
  final_transcript = capitalize(final_transcript);
  final_span.innerHTML = linebreak(final_transcript);
  interim_span.innerHTML = linebreak(interim_transcript);
};

recognition.onstart = function() { 
  instructions.text('Voice recognition is ON.');
}
 
recognition.onspeechend = function() {
  instructions.text('No activity.');
}
 
recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    instructions.text('Try again.');  
  }
}
 
$('#start-btn').on('click', function(e) {
  if (Content.length) {
    Content += ' ';
  }
  recognition.start();
});
 
Textbox.on('input', function() {
  Content = $(this).val();
})
