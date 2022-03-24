const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
  
readline.question('', numberTemperatures => {
    readline.question('', temperatures => {
        const temperaturesArray = temperatures.split(" ");
        let below_zero_count = 0;
        temperaturesArray.map((element) => {
            if (element < 0){
                below_zero_count ++;
            }
        });
        console.log(below_zero_count);
        readline.close();
    });
});