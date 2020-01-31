const repeatString = function(string, number) {
  if (number < 0) return "ERROR";
  let output = "";
  for (i = 0; i < number; i++) {
    output += string;
  }
  return output;
};

module.exports = repeatString;
