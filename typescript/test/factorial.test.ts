import { fact } from "../src/factorial";
import { it, describe, expect } from "vitest";

describe("factorial function", () => {
    it("test the function", () => {
        expect(fact(10)).toBe(3628800);
    })
})