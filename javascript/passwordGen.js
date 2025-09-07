function generate(length){

    const letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    const symbols = ['@','!','$','%','^','&','*','(', ')','_','+']
    const numbers = ['1','2','3','4','5','6','7','8','9','0']

    const allchar = letters + symbols + numbers


    //still having an issue with the random value in js
    let password = ""
    for(let i =0; i <= length; i++){
        password += allchar[Math.floor(Math.random() * 2)]
    }

    return password
}

function main(){
    password = generate(10);
    console.log(password)
}

main()