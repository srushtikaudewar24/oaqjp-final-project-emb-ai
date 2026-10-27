// Connect the IBM starter UI to the Flask emotionDetector endpoint.
function RunSentimentAnalysis() {
  const textToAnalyze = document.getElementById('textToAnalyze').value;
  const output = document.getElementById('system_response');
  output.textContent = 'Analyzing...';
  const request = new XMLHttpRequest();
  request.onreadystatechange = function () {
    if (request.readyState === 4) {
      output.textContent = request.responseText ||
        (request.status === 0 ? 'Could not connect to the server.' : 'Unable to analyze the text.');
    }
  };
  request.open('GET', '/emotionDetector?textToAnalyze=' + encodeURIComponent(textToAnalyze), true);
  request.send();
}
