function max(num){
    let num_string = String(num)
    if(num_string.length <= 1){
        return parseInt(num_string)
    }

    num_string = num_string.split("")
    let max = num_string[0]
    
    for(let i = 1; i <= num_string.length; i++){
        if(parseInt(num_string[i]) > max){
            max = num_string[i]
        }
    }

    return parseInt(max)
}

function main(){
    max = max(1578)

    console.log(`Max is: ${max}`)
}

main()