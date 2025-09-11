function reverse_num(n:number):number{
    let num_str:string = String(n)
    if(num_str.length <= 1){
        return n
    }

    num_str = num_str.split("").reverse().join("")

    return parseInt(num_str)
}

const number = 134;
const num_reversed = reverse_num(number)

console.log(`reverse of the above number is: ${num_reversed}`)