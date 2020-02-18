function add(a, b) {
  let sum = a + b;
  return sum;
}

function subtract(a, b) {
  let dif = a - b;
  return dif;
}

function sum(array) {
  let i;
  let sum = 0;
  for (i = 0; i < array.length; i++) sum += array[i];
  return sum;
}

function multiply(array) {
  product = array.reduce((a, b) => a * b);
  return product;
}

function power(a, b) {
  return a ** b;
}

function factorial(number) {
  let fact = 1;
  for (let i = number; i > 0; i--) {
    fact *= i;
  }
  return fact;
}

module.exports = {
  add,
  subtract,
  sum,
  multiply,
  power,
  factorial
};
