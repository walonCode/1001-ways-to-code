function isPanlindrome(word){
    let word_str = String(word)

    if (word_str.length <= 1){
        return true
    }

    word_str = word_str.split("").reverse().join("")

    if(word !== word_str){
        return false
    }

    return true
}

function main(){
    const word = "jalloh"

    check = isPanlindrome(word)

    console.log(`${word} is panlindrome: ${check}`)
}

main()