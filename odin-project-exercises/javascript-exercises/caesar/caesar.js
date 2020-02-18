const caesar = function(string, number) {
  let alphabet = "abcdefghijklmnopqrstuvwxyz";
  let result = "";
  for (let i = 0; i < string.length; i++) {
    let char = string[i];
    let isUpper = char === char.toUpperCase() ? true : false;

    char = char.toLowerCase();

    if (alphabet.indexOf(char) > -1) {
      let newIndex =
        (((alphabet.indexOf(char) + number) % alphabet.length) +
          alphabet.length) %
        alphabet.length;
      isUpper
        ? (result += alphabet[newIndex].toUpperCase())
        : (result += alphabet[newIndex]);
    } else {
      result += char;
    }
  }
  return result;
};

module.exports = caesar;
