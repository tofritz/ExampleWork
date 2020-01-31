const removeFromArray = function(array, ...toRemove) {
  for (item of toRemove) {
    if (array.includes(item)) {
      array.splice(array.indexOf(item), 1);
    }
  }
  return array;
};
module.exports = removeFromArray;
