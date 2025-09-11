import { fibo } from "../src/fibonacci";
import { describe, it, expect } from "vitest";


describe("fibo function", () => {
    it("testing the fibo function", () => {
        expect(fibo(10)).toBe(55)
    })
})