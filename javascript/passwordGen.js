function generate(length) {
    const letters = 'abcdefghijklmnopqrstuvwxyz'.split('');
    const symbols = ['@','!','$','%','^','&','*','(', ')','_','+'];
    const numbers = '0123456789'.split('');

    const allchar = letters.concat(symbols, numbers);

    let password = "";
    for(let i = 0; i < length; i++){
        const value = Math.floor(Math.random() * allchar.length);
        password += allchar[value];
    }

    return password;
}

function main(){
    const password = generate(10);
    console.log(password);
}

main();
