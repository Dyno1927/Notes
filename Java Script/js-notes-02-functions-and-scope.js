// ============================================================
//  JavaScript Notes — 02: Functions & Scope
//============================================================

// ─────────────────────────────────────────────
//  1. FUNCTION DECLARATION
// ─────────────────────────────────────────────

// Classic way — works like C# methods / Python def
function greet(name) {
  return `Hello, ${name}!`;
}
console.log(greet("Khanishk")); // Hello, Khanishk!

// 💡 Function declarations are "hoisted" — you can call them BEFORE they're defined
sayHi(); // works fine!
function sayHi() {
  console.log("Hi!");
}

// ─────────────────────────────────────────────
//  2. FUNCTION EXPRESSION
// ─────────────────────────────────────────────

// Storing a function in a variable
const greet2 = function (name) {
  return `Hey, ${name}!`;
};
console.log(greet2("Khanishk"));

// 💡 NOT hoisted — must be defined before use
// 💡 Treat functions as values — you can pass them around like variables!

// ─────────────────────────────────────────────
//  3. ARROW FUNCTIONS (ES6+) ← Modern JS Standard
// ─────────────────────────────────────────────

// Full arrow function
const add = (a, b) => {
  return a + b;
};

// Shorthand — single expression, implicit return
const addShort = (a, b) => a + b;

// Single parameter — no parentheses needed
const double = (n) => n * 2;

// No parameters
const sayHello = () => console.log("Hello!");

console.log(add(3, 4)); // 7
console.log(addShort(3, 4)); // 7
console.log(double(5)); // 10

// 💡 Arrow functions are like Python lambdas but much more powerful
// 💡 They're the most common style in modern JS — get comfortable with them!

// ─────────────────────────────────────────────
//  4. DEFAULT PARAMETERS
// ─────────────────────────────────────────────

function greetUser(name = "Guest", lang = "JS") {
  return `Hello ${name}, welcome to ${lang}!`;
}

console.log(greetUser()); // Hello Guest, welcome to JS!
console.log(greetUser("Khanishk")); // Hello Khanishk, welcome to JS!
console.log(greetUser("Khanishk", "C#")); // Hello Khanishk, welcome to C#!

// 💡 Same as Python default args and C# optional parameters!

// ─────────────────────────────────────────────
//  5. REST PARAMETERS (...args)
// ─────────────────────────────────────────────

// Accept unlimited arguments
function sumAll(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}

console.log(sumAll(1, 2, 3)); // 6
console.log(sumAll(1, 2, 3, 4, 5)); // 15

// 💡 Like *args in Python, or params[] in C#

// ─────────────────────────────────────────────
//  6. SCOPE
// ─────────────────────────────────────────────

// --- Global Scope ---
let globalVar = "I'm global"; // accessible everywhere

// --- Function Scope ---
function myFunc() {
  let localVar = "I'm local"; // only accessible inside myFunc
  console.log(globalVar); // ✅ can access global
  console.log(localVar); // ✅ can access local
}
// console.log(localVar);     // ❌ ReferenceError — not accessible outside

// --- Block Scope (let & const) ---
{
  let blockVar = "block scoped";
  const blockConst = "also block scoped";
  var oldVar = "NOT block scoped"; // ⚠️ var leaks out of blocks!
}
// console.log(blockVar);   // ❌ ReferenceError
console.log(oldVar); // ✅ works — this is why var is bad!

// 💡 let and const are block scoped (like C#)
// 💡 var is function scoped — another reason to avoid it

// ─────────────────────────────────────────────
//  7. CLOSURES — JS Superpower 🔥
// ─────────────────────────────────────────────

// A function that "remembers" variables from its outer scope
function makeCounter() {
  let count = 0; // this stays alive!

  return function () {
    count++;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3

// 💡 count is "closed over" — the inner function remembers it even after makeCounter() is done
// 💡 This is unique to JS — C# has similar concept with delegates/lambdas capturing variables

// ─────────────────────────────────────────────
//  8. HIGHER ORDER FUNCTIONS
// ─────────────────────────────────────────────

// Functions that take other functions as arguments or return them

// Example: passing a function as argument
function applyOperation(a, b, operation) {
  return operation(a, b);
}

const multiply = (x, y) => x * y;
const subtract = (x, y) => x - y;

console.log(applyOperation(5, 3, multiply)); // 15
console.log(applyOperation(5, 3, subtract)); // 2

// 💡 This is the foundation of array methods like map, filter, reduce (covered in Arrays notes)

// ─────────────────────────────────────────────
//  9. IIFE — Immediately Invoked Function Expression
// ─────────────────────────────────────────────

// A function that runs immediately when defined
(function () {
  let secret = "I only exist in here";
  console.log("IIFE ran!");
})();

// Arrow version
(() => {
  console.log("Arrow IIFE ran!");
})();

// 💡 Used to create isolated scopes — common in older JS codebases

// ─────────────────────────────────────────────
//  10. QUICK REFERENCE — FUNCTION TYPES
// ─────────────────────────────────────────────

// Declaration      → function name() {}          hoisted ✅
// Expression       → const name = function() {}  not hoisted
// Arrow            → const name = () => {}       not hoisted, no own `this`
// Default params   → function f(x = 10) {}
// Rest params      → function f(...args) {}
// Higher Order     → function that takes/returns functions
// Closure          → inner function remembers outer scope
