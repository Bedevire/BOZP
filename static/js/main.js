console.log('Hello from script.js')

const appUrl = "http://127.0.0.1:5000/"

async function sendQuery(){
    let query = document.getElementById('txtQuery').value;

    fetch(appUrl + "answer/" + query)
        .then( (response) => {
            content = response.text();
            return content;
        } )
        .then( (data) => {
            console.log("Response is " + data);
            document.getElementById('parResponse').textContent = data;
        });
}

