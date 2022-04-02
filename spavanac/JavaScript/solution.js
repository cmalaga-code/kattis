const readline = require("readline");
const rl = readline.createInterface({ 
    input: process.stdin, 
    output : process.stdout
});

const conversion = (t) => {
    let timeArray = t.split(" ");
    if (parseInt(timeArray[1]) < 45){
        if (parseInt(timeArray[0]) === 0) {
            remainder = 45 - parseInt(timeArray[1]);
            newMinute = 60 - remainder;
            newHour = 23;
            console.log(newHour, newMinute);
        } else {
            remainder = 45 - parseInt(timeArray[1]);
            newMinute = 60 - remainder;
            newHour = timeArray[0] - 1;
            console.log(newHour, newMinute);
        }
    } else {
        newMinute = parseInt(timeArray[1]) - 45;
        console.log(timeArray[0], newMinute);
    }
}

rl.question('', (input) => {
    solution = conversion(input);
    rl.close();
});
