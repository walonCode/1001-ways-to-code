function interest(amount, rate, year){
    if(!amount || !rate || !year){
        return new Error("Invalid inputs")
    }

    const interest = (amount * rate * year) / 100

    return interest
}

function main(){
    interest = interest(1000, 3.5, 3);
    console.log(`The interest is: ${interest}`)
}

main()