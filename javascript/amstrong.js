function isArmstrong(num){
    let num_str = String(num);
    if(num_str.length < 1){
        return new Error("Invalid input number");
    }

    let sum = 0 
    for(let i of num_str){
        const value = parseInt(i) ** 3
        sum += value
    }

    return num === sum
}

function main(){
    const value = 372
    check = isArmstrong(value)

    console.log(`The value ${value} is armstrong: ${check}`)
}

main()