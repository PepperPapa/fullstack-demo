
var el_demo1 = document.getElementById("demo1");
var res_demo1 = document.querySelector(".demo1");

var el_demo2 = document.getElementById("demo2");
var res_demo2 = document.querySelector(".demo2");

var el_demo3 = document.getElementById("demo3");
var res_demo3 = document.querySelector(".demo3");

var xhq = new XMLHttpRequest();

function handleMessage() {
  if (xhq.readyState === 4) {
    if (xhq.status === 200) {
      res_demo1.value = xhq.responseText;
    }
  }
}

el_demo1.addEventListener("click", function() {
  xhq.onreadystatechange = handleMessage;
  xhq.open("GET", "/test.py", true);
  xhq.send();
  console.log("request already sended, wait for response...");
});

el_demo2.addEventListener("click", function() {
  var img = document.createElement("img");
  img.src = "static/logo.png";
  res_demo2.appendChild(img);
});

function handleJson() {
  if (xhq.readyState === 4) {
    if (xhq.status === 200) {
      res_demo3.innerText = JSON.parse(xhq.responseText).name;
    }
  }
}

el_demo3.addEventListener("click", function() {
  xhq.onreadystatechange = handleJson;
  xhq.open("GET", "/json.py", true);
  xhq.send();
  console.log("request already sended, wait for response...");
});
