function reverse(arr){
    if(arr.length === 1){
        return arr
    }

    const reverse = arr.slice().reverse()

    return reverse
}

function main(){
    const arr = [1,2,3,4,5,6]
    
    value = reverse(arr)
    console.log(value)
}

main()