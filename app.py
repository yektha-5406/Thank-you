<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thank You </title>

<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background:#6a5acd;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .card {
        background: white;
        padding: 40px;
        border-radius: 25px;
        width: 350px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        animation: fadeIn 1s ease;
    }

    h1 {
        color: #6a5acd;
        margin-bottom: 10px;
    }

    p {
        font-size: 16px;
        color: #444;
    }

    button {
        margin-top: 20px;
        padding: 12px 25px;
        border: none;
        border-radius: 25px;
        background: #6a5acd;
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
    }

    button:hover {
        background: #483d8b;
        transform: scale(1.05);
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }

    .hidden {
        display: none;
    }
</style>
</head>

<body>

<div class="card">
    <h1>Hey 😊</h1>
    <p id="text">I have something to tell you...</p>
    <button onclick="nextStep()">Click Me</button>
</div>

<script>
let step = 0;

function nextStep() {
    const text = document.getElementById("text");

    if(step === 0) {
        text.innerHTML = "You really helped me a lot 💡";
    }
    else if(step === 1) {
        text.innerHTML = "Because of you, I learned how to create an app 😄.I'll always remember u";
    }
    else if(step === 2) {
        text.innerHTML = "<b>THANK YOU 💖 for teaching me how to create an App!</b>";
        confettiEffect();
    }

    step++;
}

function confettiEffect() {
    for(let i=0; i<100; i++) {
        let conf = document.createElement("div");
        conf.style.position = "fixed";
        conf.style.width = "8px";
        conf.style.height = "8px";
        conf.style.background = "#" + Math.floor(Math.random()*16777215).toString(16);
        conf.style.top = "-10px";
        conf.style.left = Math.random()*100 + "vw";
        conf.style.opacity = 0.8;
        conf.style.borderRadius = "50%";
        conf.style.transition = "top 2s linear";

        document.body.appendChild(conf);

        setTimeout(() => {
            conf.style.top = "100vh";
        }, 10);

        setTimeout(() => {
            conf.remove();
        }, 2000);
    }
}
</script>

</body>
</html>
