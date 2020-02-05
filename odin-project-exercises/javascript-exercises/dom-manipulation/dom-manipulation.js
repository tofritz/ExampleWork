const container = document.querySelector("#container");

const redPara = document.createElement("p");
redPara.textContent = "Hey I'm red!";
redPara.style.color = "red";
container.appendChild(redPara);

const blueHeader = document.createElement("h3");
blueHeader.textContent = "I'm a blue h3!";
blueHeader.style.color = "blue";
container.appendChild(blueHeader);

const newDiv = document.createElement("div");
newDiv.style.borderColor = "black";
newDiv.style.backgroundColor = "pink";

const newHeader = document.createElement("h1");
newHeader.textContent = "I'm in a div";
const newPara = document.createElement("p");
newPara.textContent = "ME TOO!";

newDiv.appendChild(newHeader);
newDiv.appendChild(newPara);
container.appendChild(newDiv);

const button = document.querySelector("#btn");
button.addEventListener("click", function(e) {
  e.target.style.background = "blue";
});
