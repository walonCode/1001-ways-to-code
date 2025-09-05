function average(...num){
    if(num.length <= 1){
        return num
    }

    let sum = 0

    for(let i of num){
        sum += i
    }

    return sum / num.length
}

function main(){
    average = average(1,2,3,4,5,6)

    console.log(`Average is: ${average}`)
}

main()