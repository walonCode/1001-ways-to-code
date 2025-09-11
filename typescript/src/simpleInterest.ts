const simpleInterest = (principle:number, rate:number, year:number):number => {
    if(principle === 0 || rate === 0 || year === 0){
        return 0
    }

    const interest:number = (principle * year * rate) / 100

    return interest
}


const principle = 1000;
const rate = 3;
const year = 2;

const interest = simpleInterest(principle,rate,year)

console.log(`Simple interest on this payment is: ${interest}`)