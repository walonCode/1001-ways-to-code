function sumOfEven(arr){
    if(arr.length <= 0){
        return
    }

    let sum = 0

    for (let i=0; i <= arr.length; i++){
        if (i % 2 === 0){
            sum += i
        }
    }

    return sum
}

function main(){
    const arr = [1,2,3,4,5,6]

    sum = sumOfEven(arr)

    console.log(sum)
}

main()