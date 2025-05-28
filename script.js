function goFullscreen() {
  document.documentElement.requestFullscreen();
}

const clockElem = document.getElementById("clock");
const player = document.getElementById("player");
const songList = [
  "songs/song1.mp3",
  "songs/song2.mp3"
];

function updateClock() {
  const now = new Date().toLocaleString("en-US", {
    timeZone: "Asia/Kolkata",
    hour12: false
  });
  const [date, time] = now.split(", ");
  const ms = new Date().getMilliseconds().toString().padStart(3, '0');
  clockElem.innerText = `${time}:${ms}`;
  requestAnimationFrame(updateClock);
}

function startTimer() {
  const duration = parseInt(document.getElementById("timerInput").value);
  if (isNaN(duration) || duration <= 0) return alert("Enter valid seconds");

  playMusic();
  setTimeout(() => {
    stopMusic();
    alert("Timer Finished!");
  }, duration * 1000);
}

function playMusic() {
  const song = songList[Math.floor(Math.random() * songList.length)];
  player.src = song;
  player.play();
  player.onended = playMusic;
}

function stopMusic() {
  player.pause();
  player.currentTime = 0;
  player.onended = null;
}

updateClock();
