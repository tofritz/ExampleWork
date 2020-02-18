const palindromes = function(string) {
  editedString = string.toLowerCase().replace(/[^\w]/g, "");
  reversedString = editedString
    .split("")
    .reverse()
    .join("");
  return editedString == reversedString ? true : false;
};

module.exports = palindromes;
