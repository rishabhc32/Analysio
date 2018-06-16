const {exec} = require("child_process");

exec('python3 diabetes.py', (err, stdout, stderr) => {
    if(err) {
        throw err;
    }

    if(stdout.includes('Done')) {
        console.log('Done');
    }
    console.log('stderr: ', stderr);
})
