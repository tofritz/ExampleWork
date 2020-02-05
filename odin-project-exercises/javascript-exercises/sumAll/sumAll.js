const sumAll = function(from, to) {
  sum = 0;
  if (typeof from == "number" && from > 0) {
    if (typeof to == "number" && to > 0) {
      if (from < to) {
        for (i = from; i < to + 1; i++) {
          sum += i;
        }
      } else {
        for (i = to; i < from + 1; i++) {
          sum += i;
        }
      }
    } else {
      return "ERROR";
    }
  } else {
    return "ERROR";
  }
  return sum;
};

module.exports = sumAll;
