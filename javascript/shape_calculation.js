class Shape {
    #length
    #breadth
    #width

    constructor(l, b, w){
        this.#breadth = b;
        this.#length = l;
        this.#width = w
    }

    area(){
        if(this.#length === 0 || this.#breadth === 0){
            return
        }

        console.log(`The area is: ${this.#length * this.#breadth}`)
    }

    volume(){
       if(this.#length === 0 || this.#breadth === 0 || this.#width === 0){
            return
        }

        console.log(`The volume is: ${this.#length * this.#breadth  * this.#width}`) 
    }

    perimeter(){
        if(this.#length === 0 || this.#breadth === 0){
            return
        }

        console.log(`The perimeter is: ${2 * (this.#length + this.#breadth)}`)
    }
}


function main(){
    const shape = new Shape(10, 10, 6)

    shape.area()
    shape.perimeter()
    shape.volume()
}

main()