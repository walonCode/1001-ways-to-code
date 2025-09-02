function count_vowel(sentences){
    if(sentences.length <= 1){
        return
    }

    const vowel = ['a', 'e','i','o', 'u']
    let word  = String(sentences)

    word = word.toLowerCase

    let count = 0

    for (let i of sentences){
        if(vowel.includes(i)){
            count += 1
        }
    }

    return count
}

function main(){
    const sentences = "Hello"
    count = count_vowel(sentences)

    console.log(count)
}

main()