const timers = {};
const audio = new Audio('static/media/alarm.mp3');

function startTimer(timerId) {
    const existingTimer = timers[timerId];
    if (existingTimer) {
        resumeTimer(timerId)
        return;
    }

    const initialMinutes = parseInt(document.getElementById(`initialMinutes${timerId}`).innerText) || 0;
    const initialSeconds = parseInt(document.getElementById(`initialSeconds${timerId}`).innerText) || 0;

    const totalSeconds = initialMinutes * 60 + initialSeconds;

    const timer = {
        timer: setInterval(() => updateITimer(timerId), 1000),
        isTimerRunning: true,
        hours: 0,
        minutes: initialMinutes,
        seconds: initialSeconds,
        totalSeconds: totalSeconds,
        progressBar: document.getElementById(`progressBar${timerId}`),
        startButton: document.getElementById(`startButton${timerId}`),
        pauseButton: document.getElementById(`pauseButton${timerId}`),
    };

    timers[timerId] = timer;

    setProgressBarDuration(timerId, totalSeconds);
    updateITimerDisplay(timerId);

    timer.startButton.classList.add("disabled");
}

function setProgressBarDuration(timerId, duration) {
    const progressBar = timers[timerId].progressBar;
    progressBar.style.setProperty('--duration', duration + 's');
}

function updateITimer(timerId) {
    let timer = timers[timerId];

    // Check if the timer is running
    if (timer.isTimerRunning) {
        timer.seconds--;

        if (timer.seconds < 0) {
            timer.seconds = 59;
            timer.minutes--;

            if (timer.minutes < 0) {
                timer.minutes = 59;
                timer.hours--;

                if (timer.hours < 0) {
                    clearInterval(timer.timer);
                    timerComplete(timerId);
                    timer.isTimerRunning = false;
                    return;
                }
            }
        }

        updateITimerDisplay(timerId);
        updateProgressBar(timerId);
    }
}

function updateProgressBar(timerId) {
    let timer = timers[timerId];

    // Check if the timer is still running
    if (timer.isTimerRunning) {
        let remainingSeconds = timer.hours * 3600 + timer.minutes * 60 + timer.seconds;
        let progressPercentage = ((timer.totalSeconds - remainingSeconds) / timer.totalSeconds) * 100;

        timer.progressBar.style.width = `${progressPercentage}%`;
    }
}

function resetProgressBar(timer) {
    timer.progressBar.style.width = '0%';
}


function pauseITimer(timerId) {
    const timer = timers[timerId];

    if (timer.isTimerRunning) {
        clearInterval(timer.timer);
        timer.isTimerRunning = false;
        timer.startButton.textContent = "Resume";
        timer.startButton.classList.remove("disabled");
        timer.pauseButton.classList.add("disabled");
    }
}

function resumeTimer(timerId) {
    const timer = timers[timerId];

    if (!timer.isTimerRunning) {
        timer.timer = setInterval(() => updateITimer(timerId), 1000);
        timer.isTimerRunning = true;

        timer.startButton.textContent = "Start"
        timer.startButton.classList.add("disabled");

        timer.pauseButton.classList.remove("disabled");
    }
}

function resetTimer(timerId) {
    const timerIdInput = document.querySelector(`input.timerId[value='${timerId}']`);
    const initialMinutes = parseInt(document.getElementById(`initialMinutes${timerId}`).innerText) || 0;
    const initialSeconds = parseInt(document.getElementById(`initialSeconds${timerId}`).innerText) || 0;

    let timer = timers[timerId];
    clearInterval(timer.timer);
    timer.isTimerRunning = false;
    timer.seconds = initialSeconds;
    timer.hours = 0;
    timer.minutes = initialMinutes;
    timer.startButton.textContent = "Start";
    timer.startButton.classList.remove('disabled');
    timer.pauseButton.classList.remove('disabled');
    updateITimerDisplay(timerId);
    resetProgressBar(timer);
}

function timerComplete(timerId) {
    audio.play();
    resetTimer(timerId);
}

function updateITimerDisplay(timerId) {
    let timer = timers[timerId];
    const formattedHours = padTime(timer.hours);
    const formattedMinutes = padTime(timer.minutes);
    const formattedSeconds = padTime(timer.seconds);

    document.getElementById(`hours${timerId}`).innerText = formattedHours;
    document.getElementById(`minutes${timerId}`).innerText = formattedMinutes;
    document.getElementById(`seconds${timerId}`).innerText = formattedSeconds;
}

function padTime(time) {
    return (time < 10) ? `0${time}` : time;
}
