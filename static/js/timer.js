// Required variables
var session_seconds = "00";
var session_minutes = 25;
<<<<<<< HEAD
=======
var session_count = 00;
var comenzo = false;
>>>>>>> 150fea2c06f2887bc5a5073be0b317ff85d3416e

// Audio files
var click_sound = new Audio("click.mp3");
var bell = new Audio("bell.mp3");

// Starting template for the timer
function template() {
  document.getElementById("minutes").innerHTML = session_minutes;
  document.getElementById("seconds").innerHTML = session_seconds;
}


function setTimerPomodoro(){
  session_minutes = 25;
  document.getElementById("minutes").innerHTML = session_minutes;
}

function setTimerFlowState(){
  session_minutes = 40;
  document.getElementById("minutes").innerHTML = session_minutes;
}

function start_timer() {
  click_sound.play();

  // Change the minutes and seconds to starting time
HEAD
  session_minutes = 00;
  session_seconds = 3;


  session_minutes = session_minutes -1;
  session_seconds = 59;
  session_count = 0;

  // Add the seconds and minutes to the page
  document.getElementById("minutes").innerHTML = session_minutes;
  document.getElementById("seconds").innerHTML = session_seconds;

  // Start the countdown
  var minutes_interval = setInterval(minutesTimer, 1000*session_minutes);
  var seconds_interval = setInterval(secondsTimer, 1000);
  var rest = false;


  // Functions
<<<<<<< HEAD
=======

  //Function for session counter
  function sessionsCounter() {
    session_count = 1;
    if (session_seconds <= 0) {
      if(session_minutes <= 0) {
        session_count = session_count + 1;
      }
    }
  }
>>>>>>> 150fea2c06f2887bc5a5073be0b317ff85d3416e
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
      session_minutes = session_minutes - 1;
      session_seconds = 60; 
      if (session_minutes < 0) {
        // Clears the interval i.e. stops the counter
<<<<<<< HEAD
        clearInterval(minutes_interval);
        clearInterval(seconds_interval);

        // Add the message to the html
        document.getElementById("done").innerHTML =
          "Session Completed!! Take a Break";

=======
        session_count = session_count + 1;
        document.getElementById("sessions").innerHTML = "Sesión: " + session_count;
        // Add the message to the html
        document.getElementById("done").innerHTML =
          "Sesión completada!! Toma un descanso";
>>>>>>> 150fea2c06f2887bc5a5073be0b317ff85d3416e
        // Make the html message div visible
        document.getElementById("done").classList.add("show_message");

        // PLay the bell sound to tell the end of session
        bell.play();
<<<<<<< HEAD
      }

=======

        // Cosas andres
        rest = !rest;
        if (!rest){
          session_minutes = 25;
        }
        else{
          session_minutes = 5;
        }
      } 
>>>>>>> 150fea2c06f2887bc5a5073be0b317ff85d3416e
      // Reset the session seconds to 60
    }
  }
}
<<<<<<< HEAD
=======

//Cambiar background

$('.pomodoro').on('click', function(){
  $('body').css('background-color','#041922' )
})

$('.flowState').on('click', function(){
  $('body').css('background-color','#263238' )
})
>>>>>>> 150fea2c06f2887bc5a5073be0b317ff85d3416e
