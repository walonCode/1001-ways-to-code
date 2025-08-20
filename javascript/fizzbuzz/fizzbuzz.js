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

function input(question){
    return new Promise(resolve => r1.question(question, answer => {
        r1.close()
        resolve(answer)
    }))
}


async function main(){
    console.log("Welcome to Fizzbuzz")
    const value = await input("Enter a value: ")
    fizzbuzz(value)
}

main()
