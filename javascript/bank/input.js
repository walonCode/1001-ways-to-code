const readline = require("readline/promises");
const { stdin: inputStream, stdout: outputStream } = require("node:process");

const rl = readline.createInterface({
  input: inputStream,
  output: outputStream,
});

async function input(question) {
  const answer = await rl.question(question);
  rl.close();   // this will now run
  return answer;
}

module.exports = input;
