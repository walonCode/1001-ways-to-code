import { input } from "tinyinput";

function fizzBuzz(value){
    for(let i=0; i <= value; i++){
        if (i % 3 === 0 && i % 5 === 0){
            console.log(`${i}: FizzBuzz`)
        }else if(i % 5 === 0){
            console.log(`${i}: Fizz`)
        }else{
            console.log(`${i}: Buzz`)
        }
    }
}


async function main(){
    const value = await input("Enter a value: ", "string")

    fizzBuzz(value)
}

main()