function longestWord(sentences){
    let sentence_str = String(sentences)
    sentence_str = sentence_str.split(" ")

    let word = sentence_str[0]

    for(let i of sentence_str){
        if(i.length > word.length){
            word = i
        }
    }

    return word
}

function main(){
    const sentence = "Walon is a good and bad person"

    word = longestWord(sentence)

    console.log(`The longest word in the "${sentence}" is: ${word}`)
}

main()