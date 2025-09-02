function fact(n){
    if(n ===1 || n == 0){
        return n
    }

    return n * fact(n - 1)
}

function main(){
    value = fact(10)

    console.log(value)
}

main()