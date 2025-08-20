const input = require("./input")

class Bank {
    #Balance;
    constructor(balance){
        this.#Balance = balance;
    }

    getBalance = () =>{
        console.log(this.#Balance)
    }

    async creditAccount(){
        const amount = await input("Enter the amount to be credited: ")
        if(amount <= 0){
            throw Error("invalid amount")
        }
        this.#Balance += amount 
        console.log("account credited")
    }

    async withdraw(){
        const amount = await input("Enter amount to be withdrawn: ")
        if(amount > this.#Balance){
            throw Error("Invalid amount to be debited");
        }

        this.#Balance - amount;
        console.log("Account debited")
    }
}

async function main(){
    const Walon = new Bank(500)
    Walon.creditAccount()
    Walon.withdraw()
    Walon.getBalance()
}

main()