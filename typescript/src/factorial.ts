function fact(n:number):number{
    if(n==1 || n==0){
        return n;
    }

    return fact(n-1) + fact(n-2)
}

const answer = fact(10)

console.log(answer)