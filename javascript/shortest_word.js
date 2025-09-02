function shortest(sentence) {
    if (!sentence || sentence.length === 0) {
        return null;
    }

    let words = sentence.split(" ");

    let shortestWord = words[0];

    for (let i = 1; i < words.length; i++) {
        if (words[i].length < shortestWord.length) {
            shortestWord = words[i];
        }
    }

    return shortestWord;
}

function main() {
    const sentence = "Walon is sometimes crazy, but a geek he is not";
    const word = shortest(sentence);
    console.log(word);
}

main();
