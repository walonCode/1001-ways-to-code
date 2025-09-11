function reverse_list(list:Array<number>):Array<number>{
    if(list.length <= 1){
        return list
    }

    let reverse = list.reverse()

    return reverse
}

const list = [2,1,4,2,4,3,7,8,5,6,4,0,1]
const reverse = reverse_list(list)

console.log(`The reverse of the list is ${reverse}`)