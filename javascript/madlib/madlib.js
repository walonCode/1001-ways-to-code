import { input } from "tinyinput"

async function main(){
    const noun = await input("Enter a noun: ", "string")
    const verb = await input("Enter a verb: ", "string")
    const adjective = await input("Enter an adjective: ", "string")

    console.log(`The ${noun} was given a choice to do ${verb} in a way that is ${adjective}`)
}

main()