function reverse(num){
    const letterNum = String(num)
    if(letterNum.length === 1){
        return parseInt(letterNum)
    }

    const reverse = letterNum.split("").reverse().join("")

    return parseInt(reverse)
}

function main(){
    value = reverse(123)
    console.log(value)
}

main()