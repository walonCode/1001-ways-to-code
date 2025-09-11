const sumOfOdd = (list:number[]):number => {
    if(list.length <= 1){
        return list[0];
    }

    let sum = 0;

    for(let i of list){
        if (i % 2 === 1){
            sum += i;
        }
    }

    return sum
}

const list_ = [1,2,3,4,5,6];
const value = sumOfOdd(list_)

console.log(`Sum of the even number is: ${value}`);