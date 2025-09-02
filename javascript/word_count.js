function count(word){
    if(word.length <= 1){
        return
    }

    let count = String(word)

    count = count.split(" ")

    return count.length
}

function main(){
    const words = "My name is walon"
    count = count(words)

    console.log(count)

}

main()