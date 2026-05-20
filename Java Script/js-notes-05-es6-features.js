// ============================================================
//  JavaScript Notes — 05: ES6+ Features
//============================================================

// 💡 ES6 (2015) was a massive update to JS — most modern JS uses these features
//    Everything here is stuff you'll see constantly in real code!

// ─────────────────────────────────────────────
//  1. let & const (covered in variables — quick recap)
// ─────────────────────────────────────────────

let mutable = "can change";
const fixed = "cannot change";

// ─────────────────────────────────────────────
//  2. TEMPLATE LITERALS
// ─────────────────────────────────────────────

const name = "Khanishk";
const score = 95;

// Old way
const msg1 = "Hello " + name + ", your score is " + score;

// ES6 Template Literal ✅
const msg2 = `Hello ${name}, your score is ${score}`;

// Expressions inside ${}
const msg3 = `${name} ${score >= 90 ? "passed with distinction" : "passed"}!`;

// Multi-line
const html = `
  <div class="card">
    <h2>${name}</h2>
    <p>Score: ${score}</p>
  </div>
`;

// 💡 Like Python f-strings!

// ─────────────────────────────────────────────
//  3. DESTRUCTURING (Arrays & Objects)
// ─────────────────────────────────────────────

// Array destructuring
const [a, b, c] = [1, 2, 3];
const [first, , third] = [10, 20, 30]; // skip middle

// Object destructuring
const { brand, model, year = 2020 } = { brand: "Toyota", model: "Corolla" };

// Rename on destructure
const { brand: carBrand } = { brand: "Honda" };
console.log(carBrand); // "Honda"

// In function parameters — very common!
function displayUser({ name, age, role = "user" }) {
  console.log(`${name}, ${age}, ${role}`);
}
displayUser({ name: "Khanishk", age: 18 });

// Swap variables (cool trick!)
let x = 1,
  y = 2;
[x, y] = [y, x];
console.log(x, y); // 2 1

// ─────────────────────────────────────────────
//  4. SPREAD OPERATOR (...)
// ─────────────────────────────────────────────

// Spread arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]
const copy = [...arr1]; // shallow copy

// Spread objects
const defaults = { theme: "dark", lang: "en" };
const settings = { ...defaults, lang: "ur", fontSize: 14 }; // lang overwritten
console.log(settings); // { theme: "dark", lang: "ur", fontSize: 14 }

// Spread into function args
function sum(a, b, c) {
  return a + b + c;
}
const nums = [1, 2, 3];
console.log(sum(...nums)); // 6

// 💡 Like Python's *args unpacking!

// ─────────────────────────────────────────────
//  5. REST PARAMETERS (...)
// ─────────────────────────────────────────────

// Collect remaining items
function logAll(first, second, ...rest) {
  console.log(first); // first item
  console.log(second); // second item
  console.log(rest); // array of everything else
}
logAll(1, 2, 3, 4, 5);

// Rest in destructuring
const [head, ...tail] = [10, 20, 30, 40];
console.log(head); // 10
console.log(tail); // [20, 30, 40]

// ─────────────────────────────────────────────
//  6. ARROW FUNCTIONS (covered in functions — key differences recap)
// ─────────────────────────────────────────────

// Arrow functions don't have their own `this`
// This matters when using them inside classes/objects — covered in OOP notes
const greet = (name) => `Hello, ${name}!`;

// ─────────────────────────────────────────────
//  7. SHORT CIRCUIT & NULLISH OPERATORS
// ─────────────────────────────────────────────

// || (OR) — returns first truthy value or last value
const username = "" || "Guest"; // "Guest" — empty string is falsy
const val = null || "default"; // "default"

// && (AND) — returns first falsy value or last value
const isLoggedIn = true;
const welcome = isLoggedIn && "Welcome back!"; // "Welcome back!"

// ?? (Nullish Coalescing) — only falls back on null/undefined (not 0 or "")
const count = 0 ?? 10; // 0  — 0 is NOT null/undefined
const count2 = null ?? 10; // 10 — null triggers fallback

// ?. (Optional Chaining) — safely access nested properties
const user = { profile: { name: "Ali" } };
console.log(user?.profile?.name); // "Ali"
console.log(user?.address?.city); // undefined — no crash!
console.log(user?.greet?.()); // undefined — safely calls method if exists

// 💡 ?. is incredibly useful for avoiding "Cannot read property of undefined" errors!
// 💡 ?? is better than || when 0 or "" are valid values

// ─────────────────────────────────────────────
//  8. ENHANCED OBJECT LITERALS
// ─────────────────────────────────────────────

const playerName = "Khanishk";
const playerScore = 100;

// Old way
const player1 = { playerName: playerName, playerScore: playerScore };

// ES6 shorthand — if key and variable name match
const player2 = { playerName, playerScore }; // same result ✅

// Computed property names
const key = "level";
const player3 = {
  [key]: 5, // becomes { level: 5 }
  [`${key}Name`]: "Intermediate", // { levelName: "Intermediate" }
};

// Method shorthand
const player4 = {
  name: "Ali",
  greet() {
    // instead of greet: function() {}
    return `Hi, I'm ${this.name}`;
  },
};

// ─────────────────────────────────────────────
//  9. MODULES (import / export)
// ─────────────────────────────────────────────

// --- math.js (exporting) ---
export const PI = 3.14159;
export function add(a, b) {
  return a + b;
}
export default function multiply(a, b) {
  return a * b;
} // default export

// --- main.js (importing) ---
import multiply, * as Math from "./math.js"; // default + named

console.log(Math.PI); // 3.14159
console.log(Math.add(2, 3)); // 5
console.log(multiply(3, 4)); // 12

// 💡 Like Python's import system!
// 💡 In browser: <script type="module" src="main.js">
// 💡 Named exports: export { x }  →  import { x }
// 💡 Default export: export default x  →  import anyName from "..."
// 💡 Only ONE default export per file, but unlimited named exports

// ─────────────────────────────────────────────
//  10. CLASSES (ES6)
// ─────────────────────────────────────────────

class Animal {
  #sound; // private field (ES2022)

  constructor(name, sound) {
    this.name = name; // public
    this.#sound = sound; // private
  }

  // Method
  speak() {
    return `${this.name} says ${this.#sound}!`;
  }

  // Getter
  get info() {
    return `${this.name} (${this.#sound})`;
  }

  // Static method — called on class, not instance
  static create(name, sound) {
    return new Animal(name, sound);
  }
}

// Inheritance
class Dog extends Animal {
  constructor(name) {
    super(name, "Woof"); // call parent constructor
  }

  fetch() {
    return `${this.name} fetches the ball!`;
  }
}

const dog = new Dog("Rex");
console.log(dog.speak()); // Rex says Woof!
console.log(dog.fetch()); // Rex fetches the ball!
console.log(dog.info); // Rex (Woof)

// 💡 Very similar to C# classes!
// 💡 # prefix = private (like private in C#)
// 💡 static works the same as C#
// 💡 extends + super = inheritance

// ─────────────────────────────────────────────
//  11. USEFUL NEWER FEATURES (ES2020+)
// ─────────────────────────────────────────────

// Array.at() — negative indexing
const arr = [1, 2, 3, 4, 5];
console.log(arr.at(-1)); // 5 — last element
console.log(arr.at(-2)); // 4

// Object.fromEntries() — convert entries back to object
const entries = [
  ["name", "Ali"],
  ["age", 20],
];
const obj = Object.fromEntries(entries);
console.log(obj); // { name: "Ali", age: 20 }

// Array.flat() & flatMap()
const nested = [
  [1, 2],
  [3, [4, 5]],
];
console.log(nested.flat()); // [1, 2, 3, [4, 5]] — 1 level deep
console.log(nested.flat(2)); // [1, 2, 3, 4, 5]   — 2 levels deep

// Logical assignment operators (ES2021)
let a2 = null;
a2 ??= "default"; // assign only if null/undefined → "default"

let b2 = "";
b2 ||= "fallback"; // assign if falsy → "fallback"

let c2 = 5;
c2 &&= c2 * 2; // assign if truthy → 10
