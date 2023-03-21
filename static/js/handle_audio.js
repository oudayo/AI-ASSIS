
var isRecording = false;
const recordButton = document.querySelector('.record');
const audioPlayer = document.querySelector('.audio-player');

let mediaRecorder;
let chunks = [];

recordButton.addEventListener('click', () => {
  //cas lowl eli recording deja yemchi

  if (isRecording){
    mediaRecorder.stop();
    recordButton.innerHTML = 'start';
    isRecording = false;
  }
  else {
    //cas theni howa el etat initial, maaneha mafamech recording kaaed ysir
    navigator.mediaDevices.getUserMedia({ audio: true })
    .then((stream) => {
      mediaRecorder = new MediaRecorder(stream, {
          mimeType: 'audio/webm;codecs=pcm'
          });
      mediaRecorder.start();

      const audioChunks = [];
      chunks = []
      mediaRecorder.addEventListener("dataavailable", (event) => {
        audioChunks.push(event.data);
      });

      mediaRecorder.addEventListener("stop", () => {
        const audioBlob = new Blob(audioChunks, {type: 'audio/mp3'});
        chunks = [audioBlob];


        if (chunks.length) {
    
    const audioBlob = new Blob(chunks, { type: 'audio/mp3' });
    const formData = new FormData();
    formData.append('audio', audioBlob, 'r.mp3');
    fetch('http://127.0.0.1:8000/upload_audio/', {
      method: 'POST',
      
      body: formData
    })
      .then(response => 
        response.json()
      )
      .then(async data => {
        console.log(data.link)
      //if the answer contains a link, open it 
      if (data.link) window.open(data.link);

        let binary = atob(data.audio);
        let blob = new Blob([binary], {
          type: 'audio/mp3'
        });
        let blobUrl = URL.createObjectURL(blob);

        audioPlayer.src = "data:audio/mp3;base64,"+ data.audio;
        audioPlayer.addEventListener('play', () => console.log('ready'));
        audioPlayer.play();

       
      })
      .catch(error => console.error(error));
  }
        
      });

    });
    recordButton.innerHTML = 'stop';
    isRecording = true;
  }


});
