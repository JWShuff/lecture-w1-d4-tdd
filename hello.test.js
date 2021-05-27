// const { expect } = require("@jest/globals");
var h = require("./hello.js")

test("test that 1 + 3 + 5 == 9", 
  () => {
    expect(h.sum(1,3,5)).toBe(9)
  }
)

test("test that 1 * 3 * 5 == 15", 
  () => {
    expect(h.multiply(1,3,5)).toBe(15)
  }
)