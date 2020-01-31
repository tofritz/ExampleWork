const reverseString = function(string) {
  let array = string.split("");
  let output = array.reverse();
  return output.join("");
};

module.exports = reverseString;
