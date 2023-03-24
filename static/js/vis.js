// partie audio wave
var audioCtx;
var audioElement;
var audioSrc;
var analyser;
var canvas = document.getElementById("waveform");
var canvasCtx = canvas.getContext("2d");
var freqData;
canvasCtx.fillStyle = "#808080";
canvasCtx.fillRect(0, 0, canvas.width, canvas.height);
canvasCtx.lineWidth = 2;
canvasCtx.strokeStyle = "#ffffff";

function renderFrame() {
  requestAnimationFrame(renderFrame);
  var freqData = new Uint8Array(analyser.frequencyBinCount);
  analyser.getByteFrequencyData(freqData);
  canvasCtx.fillStyle = "#808080";
  canvasCtx.fillRect(0, 0, canvas.width, canvas.height);
  canvasCtx.lineWidth = 2;
  canvasCtx.strokeStyle = "#ffffff";
  canvasCtx.beginPath();
  var sliceWidth = (canvas.width * 1.0) / freqData.length;
  var x = 0;
  var centerY = canvas.height / 2;
  var centerX = canvas.width / 3;

  for (var i = 0; i < freqData.length; i++) {
    var v = freqData[i] / 128.0;
    var y = (v * canvas.height) / 3.5;
    if (i === 0) {
      canvasCtx.moveTo(centerX + x, centerY + y); // move to center y-position
    } else {
      canvasCtx.lineTo(centerX + x, centerY + y); // add center y-position to each point
    }
    x += sliceWidth;
  }
  //canvasCtx.lineTo(centerX, centerY); // connect the last point to the center y-position
  canvasCtx.stroke();
}

const recordButtonn = document.querySelector(".record");
recordButtonn.addEventListener(
  "click",
  () => {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    audioElement = document.getElementById("audio");
    audioSrc = audioCtx.createMediaElementSource(audioElement);
    analyser = audioCtx.createAnalyser();

    // Bind our analyser to the media element source.
    audioSrc.connect(analyser);
    audioSrc.connect(audioCtx.destination);

    // Set initial state of waveform to straight line in the middle
    freqData = new Uint8Array(analyser.frequencyBinCount);
    freqData.fill(128);

    renderFrame();
  },
  { once: true }
);
//end audiowave

//end audiowave