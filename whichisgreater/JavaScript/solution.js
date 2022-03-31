const readline = require('readline');

const read = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

read.question("", (data) => {
    const integerArray = data.split(" ")
    if (integerArray[0] > integerArray[1]) {
        console.log(1)
    } else {
        console.log(0)
    }
    read.close();
});






