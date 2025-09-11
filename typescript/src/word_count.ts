function word_count(sentence:string):number {
    let word_list = sentence.split(" ")
    if (word_list.length <= 1){
        return 1
    }

    return word_list.length

}

const sentence = "Walon is crazy and is also a good person";
const count = word_count(sentence)

console.log(`Number of word in the sentence are: ${count}`)