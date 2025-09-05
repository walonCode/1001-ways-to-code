function sum(num){
    let num_str = String(num)
    if (num_str.length <= 1) {
        return num
    }

    let sum = 0
    for(let i of num_str){
        sum += parseInt(i)
    }

    return sum
}

function main(){
    const value = 1234
    sum = sum(value)

    console.log(`Sum of ${value} is: ${sum}`)
}

main()