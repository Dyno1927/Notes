// ============================================================
//  JavaScript Notes — 01: Variables & Data Types
//============================================================

// ─────────────────────────────────────────────
//  1. DECLARING VARIABLES
// ─────────────────────────────────────────────

// JS has 3 ways to declare variables:

var oldWay = "avoid this"; // ❌ outdated, has weird scoping issues
let age = 18; // ✅ use for values that CHANGE
const name = "Khanishk"; // ✅ use for values that DON'T change

// 💡 Coming from C#: think of const like `readonly`, let like a normal variable
// 💡 Coming from Python: JS needs let/const — no naked assignment like x = 5

// ─────────────────────────────────────────────
//  2. DATA TYPES
// ─────────────────────────────────────────────

// --- Primitive Types ---
let myString = "Hello"; // String
let myNumber = 42; // Number (JS has ONE number type — no int/float split!)
let myFloat = 3.14; // also Number
let myBool = true; // Boolean
let nothing = null; // intentional empty value
let notDefined; // undefined — declared but no value assigned yet
let unique = Symbol("id"); // Symbol — unique identifier (advanced, rarely needed early on)
let bigNum = 9007199254740991n; // BigInt — for very large numbers

// 💡 Biggest difference from C#: no int, float, double — everything is just "number"
// 💡 null vs undefined: null = "intentionally empty", undefined = "not set yet"

// --- Reference Types ---
let arr = [1, 2, 3]; // Array
let obj = { name: "Ali", age: 20 }; // Object
let fn = function () {}; // Function (yes, functions are values in JS!)

// ─────────────────────────────────────────────
//  3. typeof OPERATOR
// ─────────────────────────────────────────────

console.log(typeof "hello"); // "string"
console.log(typeof 42); // "number"
console.log(typeof true); // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null); // "object" ← ⚠️ famous JS bug, null is NOT an object!
console.log(typeof []); // "object" ← arrays are objects in JS
console.log(typeof {}); // "object"
console.log(typeof function () {}); // "function"

// ─────────────────────────────────────────────
//  4. TYPE COERCION — JS's Quirky Behavior
// ─────────────────────────────────────────────

// JS automatically converts types — this can surprise you!

console.log("5" + 3); // "53"  ← + with string = concatenation
console.log("5" - 3); // 2     ← - forces number conversion
console.log("5" * "2"); // 10    ← works!
console.log(true + 1); // 2     ← true = 1
console.log(false + 1); // 1     ← false = 0
console.log(null + 1); // 1     ← null = 0

// 💡 This is called "implicit coercion" — JS tries to "help" but can cause bugs
// Always use === (strict equality) to avoid coercion surprises (more in comparisons)

// ─────────────────────────────────────────────
//  5. == vs === (VERY IMPORTANT)
// ─────────────────────────────────────────────

console.log(5 == "5"); // true  ← ⚠️ converts types before comparing
console.log(5 === "5"); // false ← ✅ checks value AND type — always use this!
console.log(null == undefined); // true  ← they're "loosely equal"
console.log(null === undefined); // false ← strict: different types

// 💡 Rule of thumb: ALWAYS use === unless you have a specific reason not to

// ─────────────────────────────────────────────
//  6. STRING FEATURES
// ─────────────────────────────────────────────

let firstName = "Khanishk";
let lang = "JavaScript";

// Concatenation (old way)
let msg1 = "Hello, " + firstName + "!";

// Template Literals (modern, ES6+) ← use this!
let msg2 = `Hello, ${firstName}! Welcome to ${lang}.`;
console.log(msg2); // Hello, Khanishk! Welcome to JavaScript.

// Multi-line strings
let multiLine = `
  Line 1
  Line 2
  Line 3
`;

// Common string methods
let str = "  Hello World  ";
console.log(str.trim()); // "Hello World" — removes whitespace
console.log(str.toLowerCase()); // "  hello world  "
console.log(str.toUpperCase()); // "  HELLO WORLD  "
console.log(str.includes("World")); // true
console.log(str.replace("World", "JS")); // "  Hello JS  "
console.log(str.split(" ")); // splits into array by space

// 💡 Template literals = Python's f-strings!  `Hello ${name}` == f"Hello {name}"

// ─────────────────────────────────────────────
//  7. TYPE CONVERSION (Manual)
// ─────────────────────────────────────────────

// To Number
let num1 = Number("42"); // 42
let num2 = Number("abc"); // NaN (Not a Number)
let num3 = parseInt("42px"); // 42 — parses until it hits a non-number
let num4 = parseFloat("3.14abc"); // 3.14

// To String
let str1 = String(42); // "42"
let str2 = (42).toString(); // "42"

// To Boolean
let b1 = Boolean(0); // false
let b2 = Boolean(""); // false
let b3 = Boolean(null); // false
let b4 = Boolean(undefined); // false
let b5 = Boolean("hello"); // true
let b6 = Boolean(1); // true

// 💡 Falsy values in JS: 0, "", null, undefined, NaN, false
// Everything else is truthy!

// ─────────────────────────────────────────────
//  8. QUICK REFERENCE — VARIABLE RULES
// ─────────────────────────────────────────────

// ✅ DO:
const PI = 3.14; // constant values
let counter = 0; // changing values
let userName = "ali"; // camelCase naming (JS standard)

// ❌ AVOID:
// var anything                // outdated
// let x = 5; x = "hello"     // changing types mid-code (confusing)
// starting names with numbers // invalid
