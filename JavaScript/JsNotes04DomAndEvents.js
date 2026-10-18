// ============================================================
//  JavaScript Notes — 04: DOM & Events
//============================================================

// 💡 DOM = Document Object Model
//    The browser turns your HTML into a tree of objects (nodes)
//    JS lets you read and modify that tree — changing the page live!

// ─────────────────────────────────────────────
//  1. SELECTING ELEMENTS
// ─────────────────────────────────────────────

// By ID — returns single element
const title = document.getElementById("title");

// By CSS selector — returns FIRST match
const btn = document.querySelector(".btn"); // class
const header = document.querySelector("#header"); // id
const para = document.querySelector("p"); // tag

// By CSS selector — returns ALL matches (NodeList)
const allBtns = document.querySelectorAll(".btn");
const allParas = document.querySelectorAll("p");

// Iterating over NodeList
allBtns.forEach((btn) => console.log(btn.textContent));

// 💡 querySelector/querySelectorAll are the modern standard — use these!
// 💡 NodeList is like an array but not exactly — use forEach or spread [...allBtns]

// ─────────────────────────────────────────────
//  2. READING & CHANGING CONTENT
// ─────────────────────────────────────────────

const heading = document.querySelector("h1");

// Read content
console.log(heading.textContent); // plain text (no HTML tags)
console.log(heading.innerHTML); // includes HTML tags inside

// Change content
heading.textContent = "New Title!"; // sets plain text
heading.innerHTML = "<span>Bold Title</span>"; // ⚠️ parses HTML — careful with user input!

// 💡 Prefer textContent for plain text — innerHTML can cause security issues (XSS)

// ─────────────────────────────────────────────
//  3. READING & CHANGING STYLES
// ─────────────────────────────────────────────

const box = document.querySelector(".box");

// Inline styles
box.style.color = "#3b82f6";
box.style.backgroundColor = "#1e293b";
box.style.fontSize = "18px";
box.style.display = "none"; // hide element

// ✅ Better approach — toggle CSS classes
box.classList.add("active"); // add class
box.classList.remove("active"); // remove class
box.classList.toggle("hidden"); // add if absent, remove if present
box.classList.contains("active"); // check if class exists → true/false

// 💡 Keep styles in CSS, control them via classes in JS — cleaner separation!

// ─────────────────────────────────────────────
//  4. READING & CHANGING ATTRIBUTES
// ─────────────────────────────────────────────

const img = document.querySelector("img");
const input = document.querySelector("input");

// Get/set attributes
console.log(img.getAttribute("src"));
img.setAttribute("src", "new-image.png");
img.setAttribute("alt", "A new image");

// Direct property access (cleaner for common attributes)
console.log(input.value); // current input value
console.log(input.placeholder); // placeholder text
console.log(input.disabled); // true/false
input.disabled = true; // disable input

// ─────────────────────────────────────────────
//  5. CREATING & INSERTING ELEMENTS
// ─────────────────────────────────────────────

// Create a new element
const newPara = document.createElement("p");
newPara.textContent = "I was created by JS!";
newPara.classList.add("dynamic-text");

// Insert into DOM
const container = document.querySelector(".container");
container.appendChild(newPara); // add at end
container.prepend(newPara); // add at start
container.insertBefore(newPara, btn); // add before specific element

// Modern insertAdjacentHTML (flexible positioning)
container.insertAdjacentHTML("beforeend", "<p>Added!</p>");
// positions: "beforebegin", "afterbegin", "beforeend", "afterend"

// Remove an element
newPara.remove(); // removes itself from DOM

// ─────────────────────────────────────────────
//  6. EVENTS — Reacting to User Actions
// ─────────────────────────────────────────────

const button = document.querySelector("#myBtn");

// addEventListener — the modern way ✅
button.addEventListener("click", function (event) {
  console.log("Button clicked!");
  console.log(event); // event object — has lots of info
});

// Arrow function version
button.addEventListener("click", (e) => {
  console.log("Clicked!", e.target); // e.target = the element that was clicked
});

// 💡 event (or e) is automatically passed — it contains details about what happened
// 💡 e.target = the element that triggered the event

// ─────────────────────────────────────────────
//  7. COMMON EVENT TYPES
// ─────────────────────────────────────────────

const input2 = document.querySelector("#myInput");

// Mouse events
button.addEventListener("click", (e) => console.log("click"));
button.addEventListener("dblclick", (e) => console.log("double click"));
button.addEventListener("mouseenter", (e) => console.log("mouse entered"));
button.addEventListener("mouseleave", (e) => console.log("mouse left"));

// Keyboard events
input2.addEventListener("keydown", (e) => console.log("Key down:", e.key));
input2.addEventListener("keyup", (e) => console.log("Key up:", e.key));
input2.addEventListener("keypress", (e) => console.log("Key pressed:", e.key)); // deprecated but seen in older code

// Form / Input events
input2.addEventListener("input", (e) => console.log("Value:", e.target.value)); // fires on every change
input2.addEventListener("change", (e) =>
  console.log("Changed:", e.target.value),
); // fires when focus leaves
input2.addEventListener("focus", (e) => console.log("Focused!"));
input2.addEventListener("blur", (e) => console.log("Lost focus!"));

// Page/Window events
window.addEventListener("load", () => console.log("Page fully loaded"));
document.addEventListener("DOMContentLoaded", () => console.log("DOM ready")); // fires earlier than load
window.addEventListener("resize", () => console.log("Window resized"));
window.addEventListener("scroll", () => console.log("User scrolled"));

// ─────────────────────────────────────────────
//  8. EVENT OBJECT — Key Properties
// ─────────────────────────────────────────────

button.addEventListener("click", (e) => {
  e.target; // element that was clicked
  e.currentTarget; // element the listener is on
  e.type; // "click"
  e.key; // key name (for keyboard events)
  e.clientX; // mouse X position
  e.clientY; // mouse Y position
  e.preventDefault(); // stop default behavior (e.g. form submit, link navigation)
  e.stopPropagation(); // stop event bubbling up to parent elements
});

// Prevent form from submitting to server:
const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault(); // very common!
  const val = document.querySelector("#nameInput").value;
  console.log("Submitted:", val);
});

// ─────────────────────────────────────────────
//  9. EVENT DELEGATION — Smart Pattern 🔥
// ─────────────────────────────────────────────

// ❌ Adding listener to each button (inefficient for dynamic lists)
// allBtns.forEach(btn => btn.addEventListener("click", handler));

// ✅ Add ONE listener to the parent — check which child was clicked
const list = document.querySelector("#myList");

list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    // only react to li clicks
    console.log("Clicked item:", e.target.textContent);
    e.target.classList.toggle("selected");
  }
});

// 💡 Works even for dynamically added elements! Very useful in your Quiz Game!

// ─────────────────────────────────────────────
//  10. PRACTICAL MINI EXAMPLE — Quiz-style Interaction
// ─────────────────────────────────────────────

/*
HTML structure assumed:
  <div id="quiz">
    <p id="question">What is 2 + 2?</p>
    <div id="options">
      <button class="option">3</button>
      <button class="option">4</button>
      <button class="option">5</button>
    </div>
    <p id="feedback"></p>
  </div>
*/

const correctAnswer = "4";

document.querySelectorAll(".option").forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const selected = e.target.textContent;
    const feedback = document.querySelector("#feedback");

    if (selected === correctAnswer) {
      feedback.textContent = "✅ Correct!";
      feedback.style.color = "#22c55e";
    } else {
      feedback.textContent = "❌ Wrong!";
      feedback.style.color = "#ef4444";
    }
  });
});

// 💡 This is basically the core logic of your Web Quiz Game!
