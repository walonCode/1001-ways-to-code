
const readline = require("readline")

const r1 = readline.createInterface({
    input:process.stdin,
    output:process.stdout,
})



function fizzbuzz(value){
    if (value <= 0){
        throw Error("invalid number")
    }

    for(let i = 0; i <= value; i++){
        if(i % 5 == 0 && i % 3 == 0){
            console.log(`${i}: FizzBuzz`)
        }else if(i % 5 == 0){
            console.log(`${i}: fizz`)
        }else if (i % 3 == 0){
            console.log(`${i}: Buzz`)
        }else{
            console.log(`${i}`)
        }
    }
}


function main(){
    console.log("Welcome to Fizzbuzz")
    r1.question("Enter a value: ", (value) => {
        fizzbuzz(value)
    })
}

main()