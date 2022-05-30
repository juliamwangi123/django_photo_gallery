console.log('hello');

let clip=document.getElementById('board') //button to click when copying
image=document.getElementById('clip') // get the image 

console.log(clip)
clip.addEventListener('click' ,(e) =>{
    e.preventDefault()

    let url=image.getAttribute('src') //get the image attribute url 
    
    navigator.clipboard.writeText(url) //write the url to clipboard
    navigator.clipboard.readText().then(cliptext =>{    //read the clipboard content
        alert(`${cliptext} copied to your clipboard`)

    })
})