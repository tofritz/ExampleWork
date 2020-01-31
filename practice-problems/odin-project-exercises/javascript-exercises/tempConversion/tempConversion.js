const ftoc = function(numFarenheight) {
  numCelsius = (numFarenheight - 32) * (5 / 9);
  return Math.round(numCelsius * 10) / 10;
};

const ctof = function(numCelsius) {
  numFarenheight = numCelsius * (9 / 5) + 32;
  return Math.round(numFarenheight * 10) / 10;
};

module.exports = {
  ftoc,
  ctof
};
