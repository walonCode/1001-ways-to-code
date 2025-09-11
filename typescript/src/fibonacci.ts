export function fibo(n:number):number{
    if(n==1 || n === 0){
        return n
    }
    return  fibo(n-1) +  fibo(n-2)
}

function main(){
    const answer = fibo(10);
    console.log(answer)
}

main()