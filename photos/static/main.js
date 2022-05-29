console.log('hello');

let clip=document.getElementById('board')
image=document.getElementById('clip')

console.log(clip)
clip.addEventListener('click' ,(e) =>{
    e.preventDefault()

    console.log('click');
    let url=image.getAttribute('src')
    
    navigator.clipboard.writeText(url)
    navigator.clipboard.readText().then(cliptext =>{
        alert(`${cliptext} copied to your clipboard`)

    })
})