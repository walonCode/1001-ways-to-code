//fibo with recursion
fn fibo(n:i32) -> i32 {
    if n == 0 || n == 1 {
        return n;
    }
    
    return fibo(n - 1) + fibo(n - 2);
}

//fibo with loops


fn main(){
    //finding the fibonacci of any value 
    
    let value = fibo(10);
    
    println!("The fibo value of 10 is: {value}");

}