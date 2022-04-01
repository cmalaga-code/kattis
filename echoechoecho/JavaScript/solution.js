const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('', (word) => {
    const solution = word + " "
    console.log(solution.repeat(3))
    readline.close();
})