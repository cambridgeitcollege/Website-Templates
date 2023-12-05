"use strict";

// Used to Update the Content of Options in About Section
let tablist=document.querySelectorAll(".tabs ul li");
let tabcontentlist=document.querySelectorAll(".tab-content .content");
for( let tab of tablist){
    tab.addEventListener("click",(e)=>{
        for(let classremove of tablist)
            classremove.classList.remove("active");
        for( let tabcontent of tabcontentlist)
            tabcontent.classList.remove("show-content");
        e.target.classList.add("active");
        let show=document.getElementById(""+e.target.textContent).classList.add("show-content");
    });
}

// Used to Remove Sidebar in Mobile Phone
document.querySelector(".option").addEventListener("click",function(){
    document.querySelector("nav ul").style.right="0";
})
// Used to Show Sidebar in Mobile Phone
document.querySelector("#close").addEventListener("click",function(){
    document.querySelector("nav ul").style.right="-210px";
})

//Used to Remove Preloader When Everything is Loaded
window.addEventListener("load",function(){
    document.querySelector(".preloader").style="display:none;";
})

//Typing Effect in JS
var typed = new Typed('#typed', {
    strings: ["UI/UX Designer", "Web Developer","Graphic Designer","Product Designer"],
    typeSpeed: 80,
    backSpeed:50,
    loop:true
  });