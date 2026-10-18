// ============================================================
//  JavaScript Notes — 03: Arrays & Objects
//============================================================

// ════════════════════════════════════════════
//  PART A — ARRAYS
// ════════════════════════════════════════════

// ─────────────────────────────────────────────
//  1. CREATING ARRAYS
// ─────────────────────────────────────────────

const nums = [1, 2, 3, 4, 5];
const mixed = [1, "hello", true, null]; // JS arrays can hold any type
const empty = [];
const matrix = [
  [1, 2],
  [3, 4],
]; // nested arrays (2D)

// 💡 Like Python lists — dynamic size, mixed types allowed
// 💡 Like C# List<T> but without type restrictions

// ─────────────────────────────────────────────
//  2. ACCESSING & MODIFYING
// ─────────────────────────────────────────────

const fruits = ["apple", "banana", "cherry"];

console.log(fruits[0]); // "apple" — zero indexed
console.log(fruits.at(-1)); // "cherry" — last element (ES2022)
console.log(fruits.length); // 3

fruits[1] = "mango"; // modify element
console.log(fruits); // ["apple", "mango", "cherry"]

// ─────────────────────────────────────────────
//  3. ADDING & REMOVING ELEMENTS
// ─────────────────────────────────────────────

const arr = [1, 2, 3];

// Add/remove at END
arr.push(4); // [1, 2, 3, 4]  — add to end
arr.pop(); // [1, 2, 3]     — remove from end

// Add/remove at START
arr.unshift(0); // [0, 1, 2, 3]  — add to start
arr.shift(); // [1, 2, 3]     — remove from start

// splice — add/remove at any position
arr.splice(1, 1); // remove 1 element at index 1 → [1, 3]
arr.splice(1, 0, 99, 100); // insert 99,100 at index 1 → [1, 99, 100, 3]

// ─────────────────────────────────────────────
//  4. POWERFUL ARRAY METHODS (The Big 3) 🔥
// ─────────────────────────────────────────────

const numbers = [1, 2, 3, 4, 5];

// --- map() — transform each element, returns NEW array ---
const doubled = numbers.map((n) => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// --- filter() — keep elements that pass a test, returns NEW array ---
const evens = numbers.filter((n) => n % 2 === 0);
console.log(evens); // [2, 4]

// --- reduce() — reduce array to a single value ---
const sum = numbers.reduce((total, n) => total + n, 0);
console.log(sum); // 15

// 💡 These never modify the original array — they return new ones!
// 💡 Chain them together:
const result = numbers
  .filter((n) => n > 2) // [3, 4, 5]
  .map((n) => n * 10); // [30, 40, 50]
console.log(result);

// ─────────────────────────────────────────────
//  5. MORE USEFUL ARRAY METHODS
// ─────────────────────────────────────────────

const items = [3, 1, 4, 1, 5, 9, 2, 6];

// Searching
console.log(items.includes(5)); // true
console.log(items.indexOf(1)); // 1 — first occurrence
console.log(items.find((n) => n > 4)); // 5 — first match
console.log(items.findIndex((n) => n > 4)); // 4 — index of first match
console.log(items.some((n) => n > 8)); // true — at least one matches
console.log(items.every((n) => n > 0)); // true — all match

// Sorting
const sorted = [...items].sort((a, b) => a - b); // ascending
console.log(sorted); // [1, 1, 2, 3, 4, 5, 6, 9]

// Slicing (non-destructive)
console.log(items.slice(1, 4)); // [1, 4, 1] — elements from index 1 to 3

// Joining
console.log(items.join(", ")); // "3, 1, 4, 1, 5, 9, 2, 6"

// Flattening nested arrays
const nested = [[1, 2], [3, 4], [5]];
console.log(nested.flat()); // [1, 2, 3, 4, 5]

// Spread — copy or merge arrays
const copy = [...items];
const merged = [...[1, 2], ...[3, 4]]; // [1, 2, 3, 4]

// 💡 [...arr] is like Python's arr.copy() or list(arr)

// ─────────────────────────────────────────────
//  6. DESTRUCTURING ARRAYS
// ─────────────────────────────────────────────

const [first, second, ...rest] = [10, 20, 30, 40, 50];
console.log(first); // 10
console.log(second); // 20
console.log(rest); // [30, 40, 50]

// Skip elements
const [, , third] = [1, 2, 3];
console.log(third); // 3

// ════════════════════════════════════════════
//  PART B — OBJECTS
// ════════════════════════════════════════════

// ─────────────────────────────────────────────
//  7. CREATING OBJECTS
// ─────────────────────────────────────────────

// Object literal — most common way
const person = {
  name: "Khanishk",
  age: 18,
  isStudent: true,
  greet() {
    // method shorthand
    return `Hi, I'm ${this.name}!`;
  },
};

// 💡 Like a Dictionary in C# or a dict in Python — but with methods too!

// ─────────────────────────────────────────────
//  8. ACCESSING PROPERTIES
// ─────────────────────────────────────────────

console.log(person.name); // "Khanishk" — dot notation
console.log(person["age"]); // 18 — bracket notation
console.log(person.greet()); // "Hi, I'm Khanishk!"

// Bracket notation is useful when key is dynamic:
const key = "name";
console.log(person[key]); // "Khanishk"

// ─────────────────────────────────────────────
//  9. MODIFYING OBJECTS
// ─────────────────────────────────────────────

person.email = "k@example.com"; // add new property
person.age = 19; // modify existing
delete person.isStudent; // remove property

console.log(person);

// ─────────────────────────────────────────────
//  10. OBJECT DESTRUCTURING
// ─────────────────────────────────────────────

const { name, age } = person;
console.log(name); // "Khanishk"
console.log(age); // 19

// Rename while destructuring
const { name: fullName } = person;
console.log(fullName); // "Khanishk"

// Default value
const { country = "India" } = person;
console.log(country); // "India" — not in object, uses default

// ─────────────────────────────────────────────
//  11. SPREAD & REST WITH OBJECTS
// ─────────────────────────────────────────────

// Spread — copy or merge objects
const base = { a: 1, b: 2 };
const extended = { ...base, c: 3 };
console.log(extended); // { a: 1, b: 2, c: 3 }

// Overwrite with spread
const updated = { ...person, age: 25 };
console.log(updated.age); // 25 — overwritten

// Rest in destructuring
const { name: n, ...others } = person;
console.log(others); // everything except name

// ─────────────────────────────────────────────
//  12. USEFUL OBJECT METHODS
// ─────────────────────────────────────────────

const car = { brand: "Toyota", model: "Corolla", year: 2022 };

console.log(Object.keys(car)); // ["brand", "model", "year"]
console.log(Object.values(car)); // ["Toyota", "Corolla", 2022]
console.log(Object.entries(car)); // [["brand","Toyota"], ["model","Corolla"], ["year",2022]]

// Iterate over object
Object.entries(car).forEach(([key, value]) => {
  console.log(`${key}: ${value}`);
});

// Check if property exists
console.log("brand" in car); // true

// ─────────────────────────────────────────────
//  13. ARRAYS OF OBJECTS — Common Real-World Pattern
// ─────────────────────────────────────────────

const students = [
  { id: 1, name: "Ali", grade: 85 },
  { id: 2, name: "Sara", grade: 92 },
  { id: 3, name: "Khanishk", grade: 78 },
];

// Get names only
const names = students.map((s) => s.name);
console.log(names); // ["Ali", "Sara", "Khanishk"]

// Filter passing students (grade > 80)
const passing = students.filter((s) => s.grade > 80);
console.log(passing);

// Find a specific student
const found = students.find((s) => s.name === "Khanishk");
console.log(found); // { id: 3, name: "Khanishk", grade: 78 }

// Sort by grade descending
const ranked = [...students].sort((a, b) => b.grade - a.grade);
console.log(ranked);

// 💡 This pattern (array of objects + map/filter/find) is used EVERYWHERE in real JS apps!
