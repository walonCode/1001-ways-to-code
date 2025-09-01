function sumOfOdd(arr){
    if(arr.length <= 0){
        return
    }

    let sum = 0

    for (let i=0; i <= arr.length; i++){
        if (i % 2 === 1){
            sum += i
        }
    }

    return sum
}

function main(){
    const arr = [1,2,3,4,5,6]

    sum = sumOfOdd(arr)

    console.log(sum)
}

main()