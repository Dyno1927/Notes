using System;

// --- NULLABLE TYPES ---
// By default, value types (int, bool, double) CANNOT be null
// Nullable types let you represent "no value" with the ? syntax
//
//   int  x = null;   ← ERROR!
//   int? x = null;   ← OK!
//
// Useful for: optional data, database fields, user input that might be missing

class NullableTypes
{
    public static void Run()
    {
        Console.WriteLine("=== NULLABLE TYPES ===");
        Console.WriteLine();

        // --- Nullable value types ---
        Console.WriteLine("-- Nullable Value Types (int?, bool?, double?) --");

        int? age = null;
        Console.WriteLine($"Age has value? {age.HasValue}");
        Console.WriteLine($"Age: {age}");  // prints empty

        age = 16;
        Console.WriteLine($"Age has value? {age.HasValue}");
        Console.WriteLine($"Age value: {age.Value}");

        Console.WriteLine();

        // --- Null coalescing operator: ?? ---
        // "Give me the value, OR if null, use this default instead"
        Console.WriteLine("-- ?? (Null Coalescing Operator) --");

        int? score = null;
        int displayScore = score ?? 0;   // if score is null, use 0
        Console.WriteLine($"Score: {displayScore}");

        string? nickname = null;
        string name = nickname ?? "Unknown";
        Console.WriteLine($"Name: {name}");

        nickname = "Khanishk";
        name = nickname ?? "Unknown";
        Console.WriteLine($"Name: {name}");

        Console.WriteLine();

        // --- ??= (Null coalescing assignment) ---
        // Assign a value ONLY if the variable is currently null
        Console.WriteLine("-- ??= (Assign if null) --");

        string? city = null;
        city ??= "Aligarh";  // city is null, so assign "Aligarh"
        Console.WriteLine($"City: {city}");

        city ??= "Delhi";    // city is NOT null, so keep "Aligarh"
        Console.WriteLine($"City: {city}");

        Console.WriteLine();

        // --- Null conditional operator: ?. ---
        // Safely access a member of an object that might be null
        Console.WriteLine("-- ?. (Null Conditional Operator) --");

        string? word = null;
        Console.WriteLine($"Length (safe): {word?.Length}");   // prints nothing (null), no crash

        word = "Hello";
        Console.WriteLine($"Length (safe): {word?.Length}");   // prints 5

        Console.WriteLine();

        // Chaining ?.  with ??
        string? input = null;
        int length = input?.Length ?? 0;
        Console.WriteLine($"Length of null string: {length}");

        Console.WriteLine();

        // --- Practical example: optional user profile ---
        Console.WriteLine("-- Practical: Optional Profile Fields --");
        ShowProfile("Khanishk", age: 16, phone: null, score: null);
        ShowProfile("Aarav", age: 17, phone: "9876543210", score: 88.5);
    }

    static void ShowProfile(string name, int? age, string? phone, double? score)
    {
        Console.WriteLine($"Name:  {name}");
        Console.WriteLine($"Age:   {age?.ToString() ?? "Not provided"}");
        Console.WriteLine($"Phone: {phone ?? "Not provided"}");
        Console.WriteLine($"Score: {(score.HasValue ? score.Value.ToString("0.0") : "Not available")}");
        Console.WriteLine();
    }
}
