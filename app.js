const {exec} = require("child_process");
const express = require("express")

const app = express()
app.use(express.static('public'))

var analyze = function () {
    exec('python3 diabetes.py', (err, stdout, stderr) => {
        if(err) {
            throw err;
        }

        if(stdout.includes('Done')) {
            console.log('Done');
            exec('ls', (err, stdout, stderr) => {
                console.log(stdout);
            })
        }
        console.log('stderr: ', stderr);
    })
}

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
})

app.get('/analyze', (req, res) => {
    analyze();
    res.sendFile(__dirname + '/index.html');
})

app.listen(4433, () => console.log('Started server'))
