const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
  
readline.question('', inputData => {
    const [a, b, c] = inputData.split(" ");
    console.log((a*b)*c);
    readline.close();
});