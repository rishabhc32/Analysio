const {exec} = require("child_process");

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
