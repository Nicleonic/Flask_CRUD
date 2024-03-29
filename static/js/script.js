(() => {
    'use strict'


let pswrd = document.getElementById('pswrd');
let viewerBtn = document.getElementById('viewerBtn');


document.getElementById('modalbtn').addEventListener('click', (e)=>{
    console.log("Modal was clicked")
})


viewerBtn.addEventListener("click", (e)=>{
    // console.log(e.target)
    if(pswrd.type === 'password'){
        pswrd.setAttribute('type', 'text');
        viewerBtn.classList.add('hide');
    }else{
        pswrd.setAttribute('type', 'password');
        viewerBtn.classList.remove('hide');
    }
})



// ====================== Listing Students

let suppr = document.getElementById("clear");
let modif = document.getElementById("update");

suppr.addEventListener("click",function (e) {
    alert("Voulez-vous vraiment supprimer?");
    console.log("suppr clicked")
})




})