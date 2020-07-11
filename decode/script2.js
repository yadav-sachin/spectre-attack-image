const chalk = require('chalk');
const base64Img = require('base64-img');
const fs = require('fs');

fs.readFile('../spectre_output.txt', 'utf-8', (err, data) => {
    if (err)
        console.log(chalk.red('Error reading the Spectre Output file'));
    else {
        base64Img.img(data, '../', 'secret_img', (err, filepath) => {
            if (err)
                console.log(chalk.red('File cannot be Parsed, err'));
            else
                console.log(chalk.green('Output Saved at ', filepath));
        });
    }
});

