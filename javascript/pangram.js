function isPangram(word){
    let word_str = String(word)

    word_str = word_str.split("")

    const letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for(let char of letter){
        if(!word_str.includes(char)){
            return false
        }
    }

    return true
}

function main(){
    const sentences = "The quick brown fox jumps over the lazy dog"

    check = isPangram(sentences)
    console.log(`The ${sentences} is pangram: ${check}`)
}

main()