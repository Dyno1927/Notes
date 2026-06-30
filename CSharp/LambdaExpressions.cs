using System;
using System.Collections.Generic;

// --- LAMBDA EXPRESSIONS ---
// A lambda is a SHORT, unnamed (anonymous) function
//
// Syntax:
//   (parameters) => expression
//   (parameters) => { statements; }
//
// Used with: delegates, Func<>, Action<>, LINQ, events

class LambdaExpressions
{
    public static void Run()
    {
        Console.WriteLine("=== LAMBDA EXPRESSIONS ===");
        Console.WriteLine();

        // --- Basic lambdas with Func and Action ---
        // Func<input, output>: a function that RETURNS something
        // Action<input>:       a function that returns NOTHING (void)

        Console.WriteLine("-- Basic Lambdas --");

        Func<int, int> square = x => x * x;
        Func<int, int, int> add = (a, b) => a + b;
        Func<string, bool> isLong = s => s.Length > 5;

        Console.WriteLine($"Square of 6:         {square(6)}");
        Console.WriteLine($"Add 3 + 4:           {add(3, 4)}");
        Console.WriteLine($"Is 'Khanishk' long?  {isLong("Khanishk")}");

        Console.WriteLine();

        // Action: no return value
        Action<string> greet = name => Console.WriteLine($"Hello, {name}!");
        Action<string, int> describe = (name, age) =>
        {
            Console.WriteLine($"{name} is {age} years old.");
        };

        greet("Khanishk");
        describe("Maya", 18);

        Console.WriteLine();

        // --- Multi-line lambda ---
        Console.WriteLine("-- Multi-line Lambda --");

        Func<int, string> grade = score =>
        {
            if (score >= 90) return "A";
            if (score >= 80) return "B";
            if (score >= 70) return "C";
            return "F";
        };

        int[] scores = { 95, 82, 71, 58, 88 };
        foreach (int s in scores)
            Console.WriteLine($"Score {s} → Grade {grade(s)}");

        Console.WriteLine();

        // --- Passing lambdas to methods ---
        Console.WriteLine("-- Passing Lambdas to Methods --");

        List<int> numbers = new List<int> { 3, 8, 1, 15, 7, 20, 4, 11 };

        Console.WriteLine("Original: " + string.Join(", ", numbers));

        // Sort using lambda
        numbers.Sort((a, b) => a.CompareTo(b));
        Console.WriteLine("Sorted:   " + string.Join(", ", numbers));

        // FindAll using lambda
        List<int> evens = numbers.FindAll(n => n % 2 == 0);
        Console.WriteLine("Evens:    " + string.Join(", ", evens));

        Console.WriteLine();

        // --- Storing lambdas as variables and reusing ---
        Console.WriteLine("-- Reusable Lambda Variables --");

        Func<double, double> celsiusToF = c => c * 9 / 5 + 32;
        Func<double, double> fToCelsius = f => (f - 32) * 5 / 9;

        double[] temps = { 0, 25, 37, 100 };
        foreach (double t in temps)
            Console.WriteLine($"{t}°C = {celsiusToF(t):0.0}°F");

        Console.WriteLine();

        // --- Using lambdas with custom method that accepts Func ---
        Console.WriteLine("-- Lambda as Parameter --");
        ApplyToAll(new int[] { 2, 4, 6, 8 }, n => n * n, "Squared");
        ApplyToAll(new int[] { 2, 4, 6, 8 }, n => n + 10, "Plus 10");
    }

    // Method that takes a Func lambda as parameter
    static void ApplyToAll(int[] values, Func<int, int> transform, string label)
    {
        Console.Write($"{label}: ");
        foreach (int v in values)
            Console.Write($"{transform(v)} ");
        Console.WriteLine();
    }
}
