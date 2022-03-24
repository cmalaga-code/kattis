const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const search = (stringData) => {
    array = [];
    for (let i = 0; i < stringData.length; i ++){
        array.push(stringData[i]);
    }
    const indexValue = array.findIndex((element) => element === "a");
    return stringData.substring(indexValue);
}
  
readline.question('', inputData => {
    const solution = search(inputData);
    console.log(solution);  
    readline.close();
});