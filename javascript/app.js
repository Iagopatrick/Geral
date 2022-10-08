var name = 'Iago Patrick'
var age = 19
var weight = 61.6
var alive = false
var food = null
var time //undefined
var fruits = ['banana', 23, 23.5, false, null] // Pode ter qualquer tipo dentro do array
var person = {
    name: 'Iago Patrick', 
    age: 21,
    alive: true,
    height: 1.78
} //Objeto funciona quase como um struct em C, armazena varias propriedades referentes a uma entidade

// console.log(person.height) --> como acessar as propriedades dentro do objeto

var product = 'Camisa'
var price = 10

console.log('o preço da ' + product + ' é R$' + price + ' e pertece ao ' + person.name)

function action(number1, number2){
    return number1 + number2
}

console.log(action(10, 20))

var isActive = true
var message = ''

if (isActive){
    message = 'Está ativo'
} else {
    message = 'Não está ativo'
}


switch (isActive){
    case 'verde':
        message = 'Tá verde'
        break
    case 'vermelho':
        message = 'Tá vermelho'
        break
    default:
        message = 'Inválido'
        
}