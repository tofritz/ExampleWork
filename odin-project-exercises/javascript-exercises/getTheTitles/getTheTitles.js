const getTheTitles = function(array) {
  const titles = array.map(book => book.title);
  return titles;
};

module.exports = getTheTitles;
