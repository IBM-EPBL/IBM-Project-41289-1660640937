let canvas = document.getElementById("canvass");
canvas.height = 280;
canvas.width = 280;
var boundings = canvas.getBoundingClientRect();

var drawing = false;
let ctx = canvas.getContext("2d");
ctx.fillStyle = "black";
ctx.fillRect(0, 0, canvas.width, canvas.height);
var boundings = canvas.getBoundingClientRect();
var clear_btn = document.getElementById('clear-btn');
var predict_btn = document.getElementById('predict-btn');
var result_space = document.getElementById('result');
let classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

window.addEventListener("load", () => {
    loadModel();
})

async function loadModel() {
    model = undefined;
    model = await tf.loadLayersModel("./model/mnistJSModel/model.json");
    console.log("model loaded")
}



function clear() {
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    result_space.innerText = " ";
}

function start(e) {
    drawing = true;
    draw(e);
}

function stop() {
    drawing = false;
    ctx.beginPath();

}

function draw(e) {
    if (!drawing) {
        return
    }
    ctx.lineWidth = 8;
    ctx.lineCap = "round";
    ctx.lineTo(e.clientX - boundings.left, e.clientY - boundings.top);
    ctx.strokeStyle = "white";
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - boundings.left, e.clientY - boundings.top);
}

function preprocessCanvas(image) {
    let tensor = tf.browser.fromPixels(image)
        .resizeNearestNeighbor([28, 28])
        .mean(2)
        .expandDims(2)
        .expandDims()
        .toFloat();
    return tensor.div(255.0)

}

async function predcit() {
    html2canvas(document.getElementById("canvass"))
        .then((img) => {

            let predictions = model.predict(preprocessCanvas(img)).data()
            predictions.then(function(res) {
                let results = Array.from(res);
                ans = classes[results.indexOf(Math.max(...results))]
                console.log(results);
                if (results[ans] > 0.2) { result_space.innerText = String(ans); } else { result_space.innerHTML = '<h6 style="width:100%;height:100%">&#128565;</h6>'; }
            })
        })
}


canvas.addEventListener("mousedown", start);
canvas.addEventListener("mousemove", draw);
canvas.addEventListener("mouseup", stop)
clear_btn.addEventListener('click', clear);
predict_btn.addEventListener('click', predcit);