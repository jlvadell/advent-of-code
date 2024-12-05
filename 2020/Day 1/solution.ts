const GOAL = 2020;

// Part One


export function partOne(input: number[]) {
  const inputMap: Record<number, boolean> = {};

  for (const num of input) {
    inputMap[num] = true;
    const toFind = 2020-num;
    if (inputMap[toFind]) {
      return toFind * num;
    }
  }
}

// Part Two



export function partTwo(input:number[]): number {
  for (const numA of input) {
    for (const numB of input) {
      for (const numC of input) {
        if (numA + numB + numC === GOAL) {
          return numA * numB * numC;
        }
      }
    }
  }
  return 0;
}


Deno.readTextFile("./input.txt").then((rawInput) => {
  const input: number[] = rawInput.split("\n").map(num => parseInt(num));
  console.log("Day One, Part One Solution:", partOne(input));
  console.log("Day One, Part Two Solution:", partTwo(input));
})