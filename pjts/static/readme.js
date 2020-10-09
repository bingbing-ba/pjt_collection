const converter = new showdown.Converter()
converter.setFlavor('github')
const container = document.getElementById('container')
const origin = document.getElementById('origin')
const htmlreadme = converter.makeHtml(origin.innerText)
container.innerHTML = htmlreadme
