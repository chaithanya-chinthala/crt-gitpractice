 const id = document.getElementById("btn1")
btn1.addEventListener("mousedown", function(){
    btn1.style.boxShadow = "10px 10px 10px pink";
})

btn1.addEventListener("mouseup", function(){
    btn1.style.boxShadow = "";
})
