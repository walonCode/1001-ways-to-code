class Calculator {
    #VALUE_A
    #VALUE_B

    constructor(a,b=4){
        this.#VALUE_A = a,
        this.#VALUE_B = b
    }

    add(){
        console.log(this.#VALUE_A + this.#VALUE_B)
    }

    minus(){
        return this.#VALUE_A - this.#VALUE_B
    }

    divide(){
        return this.#VALUE_A / this.#VALUE_B
    }

    multiplication(){
        return this.#VALUE_A * this.#VALUE_B
    }
}



function main(){
    const cal = new Calculator(5,)
    cal.add()
}

main()