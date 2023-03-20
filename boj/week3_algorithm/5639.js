const stack = [];
const input = [];
const result = [];

const readline = require("readline").createInterface(
  process.stdin,
  process.stdout
);

readline
  .on("line", function (line) {
    input.push(Number(line.trim()));
  })
  .on("close", function () {
    postorder(0, input.length - 1);
  });

function postorder(first, end) {
  if (first > end) {
    return;
  }
  let mid;
  for (i = first + 1; i <= end + 1; i++) {
    let flag = 1;
    if (input[first] < input[i]) {
      mid = i;
      flag = 0;
      break;
    }
  }
  if (flag === 1) {
    mid = end + 1;
  }
  postorder(first + 1, mid - 1);
  postorder(mid, end);
  console.log(input[first]);
}
