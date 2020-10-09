const students = document.querySelectorAll('.students')
const pjtIframe = document.querySelector('#pjtIframe')
const appNameInput = document.querySelector('#appNameInput')
const pjtIframeUrl = document.querySelector('#iframeUrl')
const readmeToggle = document.querySelector('#readme')

let appName = 'community'
let presentStudent = ''
let presentStudentPort = ''
let isReadmeState = false
const baseUrl = 'http://127.0.0.1'
const mainPort = window.location.port
const pjtName = window.location.href.split('/')[3]

appNameInput.addEventListener('change', (e)=>{
  pjtIframe.src = pjtIframe.src.replace(appName, e.target.value)
  appName = e.target.value
})

students.forEach((student)=>{  
  student.addEventListener('click', ()=>{
    presentStudentPort = student.dataset.port
    presentStudent = student.dataset.name
    if (isReadmeState) {
      pjtIframe.src = `${baseUrl}:${mainPort}/${pjtName}/readme/${presentStudent}/`
      pjtIframeUrl.href = pjtIframe.src
    }
    else {
      pjtIframe.src = `${baseUrl}:${presentStudentPort}/${appName}`
      pjtIframeUrl.href = pjtIframe.src
    }
    active = document.querySelector('.active')
    if (active){
      active.className = active.className.replace('active', '')
    }
    student.classList.add('active')

  })
})

readmeToggle.addEventListener('change', ()=>{
  isReadmeState = !isReadmeState
  if (!presentStudent) {
    return
  }
  if (isReadmeState) {
    pjtIframe.src = `${baseUrl}:${mainPort}/${pjtName}/readme/${presentStudent}/`
    pjtIframeUrl.href = pjtIframe.src
  } else{
    pjtIframe.src = `${baseUrl}:${presentStudentPort}/${appName}`
    pjtIframeUrl.href = pjtIframe.src
  }
})
