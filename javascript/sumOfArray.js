function sum(arr){
    if(arr.length <= 0){
        return
    }

    let sum = 0

    for(let i of arr){
        sum += i
    }
    return sum
}



function main(){
    const arr = [1,2,3,4,5,6]

    sum = sum(arr)

    console.log(sum)
}

main()