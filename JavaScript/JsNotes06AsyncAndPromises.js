// ============================================================
//  JavaScript Notes — 06: Async & Promises
//============================================================

// 💡 JS runs on a SINGLE thread — it can't pause and wait for slow operations
//    (like fetching data from an API or reading a file)
//    Async features let it START a task, move on, and come back when it's done

// ─────────────────────────────────────────────
//  1. THE PROBLEM — WHY ASYNC EXISTS
// ─────────────────────────────────────────────

// Imagine fetching data from a server takes 2 seconds
// If JS waited (blocked), the entire page would freeze! ❌

// Instead, JS says:
// "Start the fetch, I'll handle it when it's ready, keep running other code" ✅

// ─────────────────────────────────────────────
//  2. CALLBACKS — The Old Way (you'll see this in older code)
// ─────────────────────────────────────────────

function fetchData(callback) {
  setTimeout(() => {
    // setTimeout simulates a delay
    callback("Data received!");
  }, 2000);
}

fetchData((data) => {
  console.log(data); // "Data received!" — after 2 seconds
});

console.log("This runs FIRST!"); // runs immediately, doesn't wait!

// ⚠️ Callback Hell — chaining multiple callbacks gets ugly fast:
fetchData((data) => {
  processData(data, (processed) => {
    saveData(processed, (saved) => {
      notifyUser(saved, (done) => {
        // 😵 this goes very deep very fast
      });
    });
  });
});

// ─────────────────────────────────────────────
//  3. PROMISES — The Better Way
// ─────────────────────────────────────────────

// A Promise represents a value that will be available in the future
// It's in one of 3 states:
//   ⏳ pending   — still working
//   ✅ fulfilled — done successfully
//   ❌ rejected  — something went wrong

// Creating a Promise
const myPromise = new Promise((resolve, reject) => {
  const success = true; // simulate success/failure

  if (success) {
    resolve("✅ Data loaded!"); // call when done
  } else {
    reject("❌ Something went wrong!"); // call when failed
  }
});

// Using a Promise with .then() and .catch()
myPromise
  .then((data) => {
    console.log(data); // "✅ Data loaded!"
    return data + " (processed)"; // chain to next .then()
  })
  .then((processed) => {
    console.log(processed); // "✅ Data loaded! (processed)"
  })
  .catch((error) => {
    console.error(error); // only runs if rejected
  })
  .finally(() => {
    console.log("Always runs — cleanup here!"); // like try/finally
  });

// 💡 .then() chains cleanly — way better than nested callbacks!
// 💡 Like Task<T> in C#!

// ─────────────────────────────────────────────
//  4. ASYNC / AWAIT — The Modern Way ✅ (use this!)
// ─────────────────────────────────────────────

// async/await is syntactic sugar over Promises — reads like normal code!

// Mark function as async
async function loadData() {
  try {
    const data = await myPromise; // wait for promise to resolve
    console.log(data); // "✅ Data loaded!"
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
}

loadData();

// 💡 await can ONLY be used inside an async function
// 💡 Like C#'s async/await — almost identical!
// 💡 try/catch works just like normal error handling

// ─────────────────────────────────────────────
//  5. FETCHING DATA FROM AN API — Real World! 🌐
// ─────────────────────────────────────────────

// fetch() is built into browsers — returns a Promise
// Used to get data from APIs (like REST APIs)

// Using .then() chaining
fetch("https://jsonplaceholder.typicode.com/users/1")
  .then((response) => response.json()) // parse response body as JSON
  .then((data) => console.log(data)) // use the data
  .catch((error) => console.error(error));

// ✅ Using async/await — cleaner!
async function getUser(id) {
  try {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/users/${id}`,
    );

    if (!response.ok) {
      // check for HTTP errors (404, 500, etc.)
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const user = await response.json(); // parse JSON
    console.log(user.name); // use data
    return user;
  } catch (error) {
    console.error("Failed to fetch user:", error);
  }
}

getUser(1);

// 💡 response.json() is itself async — needs await!
// 💡 Always check response.ok for HTTP errors — fetch() doesn't throw on 404!

// ─────────────────────────────────────────────
//  6. POSTING DATA (Sending to API)
// ─────────────────────────────────────────────

async function createPost(postData) {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST", // HTTP method
      headers: {
        "Content-Type": "application/json", // tell server we're sending JSON
      },
      body: JSON.stringify(postData), // convert object to JSON string
    });

    const result = await response.json();
    console.log("Created:", result);
    return result;
  } catch (error) {
    console.error("Failed:", error);
  }
}

createPost({ title: "My Post", body: "Hello World", userId: 1 });

// ─────────────────────────────────────────────
//  7. PROMISE UTILITIES — Running Multiple at Once
// ─────────────────────────────────────────────

const p1 = fetch("https://jsonplaceholder.typicode.com/users/1").then((r) =>
  r.json(),
);
const p2 = fetch("https://jsonplaceholder.typicode.com/users/2").then((r) =>
  r.json(),
);
const p3 = fetch("https://jsonplaceholder.typicode.com/users/3").then((r) =>
  r.json(),
);

// --- Promise.all() — run ALL in parallel, wait for ALL ✅ ---
async function getAllUsers() {
  try {
    const [user1, user2, user3] = await Promise.all([p1, p2, p3]);
    console.log(user1.name, user2.name, user3.name);
  } catch (error) {
    console.error(error); // fails if ANY promise fails
  }
}

// --- Promise.allSettled() — run all, get ALL results (even failures) ---
async function tryAll() {
  const results = await Promise.allSettled([p1, p2, p3]);
  results.forEach((result) => {
    if (result.status === "fulfilled") {
      console.log("✅", result.value.name);
    } else {
      console.log("❌", result.reason);
    }
  });
}

// --- Promise.race() — returns FIRST settled (success or fail) ---
async function fastest() {
  const first = await Promise.race([p1, p2, p3]);
  console.log("Fastest:", first.name);
}

// --- Promise.any() — returns FIRST successful ---
async function anySuccess() {
  const first = await Promise.any([p1, p2, p3]);
  console.log("First success:", first.name);
}

// 💡 Promise.all() is most commonly used — great for fetching multiple things at once!

// ─────────────────────────────────────────────
//  8. SETTIMEOUT & SETINTERVAL — Timed Execution
// ─────────────────────────────────────────────

// Run ONCE after delay (ms)
const timeoutId = setTimeout(() => {
  console.log("Runs after 2 seconds!");
}, 2000);

// Cancel before it runs
clearTimeout(timeoutId);

// Run REPEATEDLY every interval
const intervalId = setInterval(() => {
  console.log("Runs every 1 second!");
}, 1000);

// Stop after 5 seconds
setTimeout(() => clearInterval(intervalId), 5000);

// 💡 Common use: quiz timers, countdowns, polling for updates

// ─────────────────────────────────────────────
//  9. ASYNC PATTERNS — Practical Examples
// ─────────────────────────────────────────────

// Loading quiz questions from an API (relevant to your Web Quiz Game!)
async function loadQuizQuestions() {
  const loadingEl = document.querySelector("#loading");
  const quizEl = document.querySelector("#quiz");

  try {
    loadingEl.style.display = "block"; // show loading spinner

    const response = await fetch(
      "https://opentdb.com/api.php?amount=5&type=multiple",
    );
    const data = await response.json();
    const questions = data.results;

    loadingEl.style.display = "none"; // hide spinner
    quizEl.style.display = "block"; // show quiz

    questions.forEach((q) => {
      console.log(q.question); // render questions
    });
  } catch (error) {
    loadingEl.textContent = "Failed to load questions. Try again.";
    console.error(error);
  }
}

// ─────────────────────────────────────────────
//  10. QUICK REFERENCE
// ─────────────────────────────────────────────

// Callback        → function passed to run later (old, messy)
// Promise         → object representing future value (.then/.catch)
// async/await     → clean syntax for Promises (USE THIS)
// fetch()         → built-in API for HTTP requests
// Promise.all()   → run multiple promises in parallel
// setTimeout()    → run once after delay
// setInterval()   → run repeatedly

// The golden rule:
// async function name() {
//   try {
//     const result = await somePromise();
//   } catch (err) {
//     // handle error
//   }
// }
