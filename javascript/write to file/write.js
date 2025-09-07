import { writeFileSync} from 'fs'

function write(filename){
    const data = `This is huge and i hope a lot of good come out of this`
    writeFileSync(filename, data, { flag :'a'})
    console.log('Writting was successfull')
}

function main(){
    const filename = 'file.txt'
    write(filename)
}

main()