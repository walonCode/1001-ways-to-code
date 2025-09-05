function checkCard(num){
    let num_str = String(num)
    if(num_str < 16){
        return
    }

    num_str = num_str.split("").reverse().join("")

    let total = 0
    for(let i of num_str){
        let n  = parseInt(i)
        if (i % 2 === 1){
            n *= 2
            if (n > 9){
                n -= 9
            } 
        }
        total += n
    }

    return total % 10 === 0
}


function main(){
    const card = '4567567845353456'
    const check = checkCard(card)

    console.log(`This card ${card} is valid?: ${check}`)
}

main()