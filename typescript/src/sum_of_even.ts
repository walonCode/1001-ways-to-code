const sumOfEven = (list:number[]):number => {
    if(list.length <= 1){
        return list[0];
    }

    let sum = 0;

    for(let i of list){
        if (i % 2 === 0){
            sum += i;
        }
    }

    return sum
}

const list_arr = [1,2,3,4,5,6];
const sum = sumOfEven(list_arr)

console.log(`Sum of the even number is: ${sum}`);