import { input } from "tinyinput";

class Bank {
    #Balance = 0 
    constructor(balance){
        this.#Balance = balance;
    }

    getBalance = () =>{
        console.log(this.#Balance)
    }

    async creditAccount(){
        const amount = await input("Enter the amount to be credited: ", "float")
        if(amount <= 0){
            throw Error("invalid amount")
        }
        this.#Balance += amount 
        console.log("account credited")
    }

    async withdraw(){
        const amount = await input("Enter amount to be withdrawn: ", "float")
        if(amount > this.#Balance){
            throw Error("Invalid amount to be debited");
        }

        this.#Balance - amount;
        console.log("Account debited")
    }

    async 
}

async function main(){
    const bank = new Bank(0)

    while(true){
        console.log("Welcome to the bank")
        console.log("1.Get balance")
        console.log("2.Credit Account")
        console.log("3.Withdraw from account")
        console.log("4.exit the bank")
        let choice = await input("Enter you choice: ", "int")
        
        switch(choice){
            case 1:
                bank.getBalance()
                break
            case 2:
                bank.creditAccount()
                break;
            case 3:
                bank.withdraw()
                break;
            case 4:
                console.log("exting....................")
                process.exit(0)            
        }
    }
}

main()