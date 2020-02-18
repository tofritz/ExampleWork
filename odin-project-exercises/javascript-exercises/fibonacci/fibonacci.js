const fibonacci = function(number) {
  array = [];
  if (number < 0) return "OOPS";
  for (let i = 0; i < number; i++) {
    if (i == 0 || i == 1) array.push(1);
    else {
      array.push(array[i - 1] + array[i - 2]);
    }
  }
  return array.pop();
};

module.exports = fibonacci;
