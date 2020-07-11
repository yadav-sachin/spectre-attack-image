const chalk = require('chalk');
const path = require('path');
const fs = require('fs');
const base64Img = require('base64-img');

const imgPath = path.join(__dirname, '/secret_img.jpg');

base64Img.base64(imgPath, (err, data) => {
    if(err)
    console.log(chalk.red.inverse('Some Error Occurred. Terminating Process --> \n\n', err));
    else{
        console.log(chalk.yellow('Processing Image ...'));
        fs.writeFileSync('../encodedImg.txt', data);
        console.log(chalk.green.inverse('Encoded Image successfully saved at "encodedImg.txt"'));
    }
    
});