const students = document.querySelectorAll('.students')
const pjtIframe = document.querySelector('#pjtIframe')
const appNameInput = document.querySelector('#appNameInput')
const pjtIframeUrl = document.querySelector('#iframeUrl')

let appName = 'community'
appNameInput.addEventListener('change', (e)=>{
  pjtIframe.src = pjtIframe.src.replace(appName, e.target.value)
  appName = e.target.value
})

students.forEach((student)=>{
  const baseUrl = 'http://127.0.0.1'
  const portNum = student.dataset.port

  student.addEventListener('click', ()=>{
    pjtIframe.src = `${baseUrl}:${portNum}/${appName}`
    pjtIframeUrl.href = pjtIframe.src
    active = document.querySelector('.active')
    if (active){
      active.className = active.className.replace('active', '')
    }
    student.classList.add('active')

  })
})
