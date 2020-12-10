import {
  assertEquals,
} from "https://deno.land/std/testing/asserts.ts";

import {
  partOne,
  partTwo
} from './solution.ts'

// Process test data
const testInput1: number[] = (await Deno.readTextFile("./test_input_1.txt")).split("\n").map(num => parseInt(num));
const testInput2: number[] = (await Deno.readTextFile("./test_input_2.txt")).split("\n").map(num => parseInt(num));

// Part 1 Asserts

Deno.test("Day 1, Part 1 test 1", () => {
  //1745 * 275 = 479875
  assertEquals(partOne(testInput1), 479875)
})

Deno.test("Day 1, Part 1 test 2", () => {
  //1721 * 299 = 514579
  assertEquals(partOne(testInput2), 514579)
})

// Part 2 Asserts:

Deno.test("Day 1, Part 2 test 1", () => {
  //1999 * 15 * 6 = 179910
  assertEquals(partTwo(testInput1), 179910)
})

Deno.test("Day 1, Part 2 test 1", () => {
  //979 * 366 * 675 = 241861950
  assertEquals(partTwo(testInput2), 241861950)
})