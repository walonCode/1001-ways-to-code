function fibo(n:number):number{
    if(n==1 || n === 0){
        return n
    }
    return n * fibo(n-1)
}

function main(){
    const answer = fibo(10);
    console.log(answer)
}

main()