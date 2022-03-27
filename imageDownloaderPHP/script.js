const urlField = document.querySelectorAll('input')[0]
const urlFieldHidden = document.querySelectorAll('input')[1]
const imageArea = document.querySelector('img')
const infoArea = document.querySelector('span')
const downloadBtn = document.querySelector('button')

imageArea.addEventListener('contextmenu', e => e.preventDefault())
urlField.addEventListener('keyup', ()=>{
    const thumbUrl = urlField.value
    let isYouTube = false
    let isValid = false
    let imageID
    if(thumbUrl.startsWith("https://www.youtube.com/watch?v=")){
        isYouTube = true
        isValid = true
        imageID = thumbUrl.split('v=')[1].substring(0, 11)
    }else if(thumbUrl.startsWith('https://youtu.be/')){
        isYouTube = true
        isValid = true
        imageID = thumbUrl.split('be=')[1].substring(0, 11)
    }else if(thumbUrl.match(/\.(jpe?g|png|gif|bmp|webp)$/i)){
        isValid = true
        imageID = thumbUrl
    }else{
        infoArea.classList.add('active')
        imageArea.classList.remove('active')
        downloadBtn.disabled = true
        downloadBtn.title = 'URL field must be valid'
        imageArea.src = ''
    }
    if (isValid){
        infoArea.classList.remove('active')
        imageArea.classList.add('active')
        downloadBtn.disabled = false
        downloadBtn.title = ''
        imageArea.src = isYouTube ? `https://img.youtube.com/vi/${imageID}/maxresdefault.jpg` : imageID
        urlFieldHidden.value = isYouTube ? `https://img.youtube.com/vi/${imageID}/maxresdefault.jpg` : imageID
    }
})
