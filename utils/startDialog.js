const inquirer = require("inquirer")

async function startDialog(question, { type, defaultAnswer, options, validator, transformer, filter}) {
  const enterSpotifyLinkQuestion = {
    type: type || (options ? "list" : "input"),
    name: "answer",
    message: question,
    choices: options,
    default: defaultAnswer,
    validate: validator,
    transformer,
    filter,
  }

  const { answer } = await inquirer.prompt([enterSpotifyLinkQuestion])
  return answer
}

module.exports = startDialog
