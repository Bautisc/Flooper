// Required variables
var session_seconds = "00";
var session_minutes = 25;
var session_count = 00;

// Audio files
var click_sound = new Audio("static/mp3/click.mp3");
var bell = new Audio("../static/mp3/bell.mp3");

// Starting template for the timer
function template() {
  document.getElementById("minutes").innerHTML = session_minutes;
  document.getElementById("seconds").innerHTML = session_seconds;
  document.getElementById("sessions").innerHTML = session_count;
}

function start_timer() {
  click_sound.play();

  // Change the minutes and seconds to starting time
  session_minutes = 00;
<<<<<<< HEAD
  session_seconds = 03;
=======
  session_seconds = 01;
>>>>>>> 3481897de3e25fcfd5d35e49d9e18e8e46af20e8
  session_count = 4;
  // Add the seconds and minutes to the page
  document.getElementById("minutes").innerHTML = session_minutes;
  document.getElementById("seconds").innerHTML = session_seconds;
  document.getElementById("sessions").innerHTML = "Sesión: " + session_count;
  // Start the countdown
  var minutes_interval = setInterval(minutesTimer, 60000);
  var seconds_interval = setInterval(secondsTimer, 1000);

  // Functions

  //Function for session counter
  function sessionsCounter() {
    session_count = 1;
    if (session_seconds <= 0) {
      if(session_minutes <= 0) {
        session_count = session_count - 1;
      }
    }
  }
  // Function for minute counter
  function minutesTimer() {
    session_minutes = session_minutes - 1;
    document.getElementById("minutes").innerHTML = session_minutes;
  }
  // Function for second counter
  function secondsTimer() {
    session_seconds = session_seconds - 1;
    document.getElementById("seconds").innerHTML = session_seconds;

    // Check if the seconds and minutes counter has reached 0
    // If reached 0 then end the session
    if (session_seconds <= 0) {
      if (session_minutes <= 0) {
        // Clears the interval i.e. stops the counter
        clearInterval(minutes_interval);
        clearInterval(seconds_interval);
        session_count = session_count -1;
        document.getElementById("sessions").innerHTML = "Sesión: " + session_count;
        // Add the message to the html
        document.getElementById("done").innerHTML =
          "Sesión completada!! Toma un descanso";

        // Make the html message div visible
        document.getElementById("done").classList.add("show_message");
        // PLay the bell sound to tell the end of session
        bell.play();
      } 
      // Reset the session seconds to 60
      session_seconds = 60;
    }
  }
}