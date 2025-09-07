const fs = require('fs')

//you can read a file using fs

function read(fileName){
   try{
    const data = fs.readFileSync(fileName, 'utf-8')
    return data
   }catch(err){
    console.log(err)
   }
}

function main(){
    const file = "file.txt"

    lines = read(file)
    console.log(lines)
}

main()