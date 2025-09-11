export function fact(n:number):number{
    if(n==1 || n==0){
        return n;
    }

    return n * fact(n-1)
}

const answer = fact(10)

console.log(answer)