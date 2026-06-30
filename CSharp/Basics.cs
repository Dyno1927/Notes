using System;

class Basics
{
    public static void Run()
    {
        Console.WriteLine("=== BASICS ===");
        Console.WriteLine();

        // Variables
        string name = "Khanishk";
        int age = 16;
        double height = 5.8;
        bool isStudent = true;

        // Constant
        const double PI = 3.14159;

        Console.WriteLine($"Name: {name}");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"Height: {height}");
        Console.WriteLine($"Student: {isStudent}");
        Console.WriteLine($"PI: {PI}");
        Console.WriteLine();

        // User input
        Console.Write("Enter your favorite number: ");
        string? input = Console.ReadLine();

        if (int.TryParse(input, out int favoriteNumber))
        {
            Console.WriteLine($"Your number is: {favoriteNumber}");
            Console.WriteLine($"Your number + 10 = {favoriteNumber + 10}");
            Console.WriteLine($"Your number squared = {favoriteNumber * favoriteNumber}");
        }
        else
        {
            Console.WriteLine("That was not a valid number.");
        }

        Console.WriteLine();

        // Math
        double price = 499.99;
        double tax = price * 0.18;
        double total = price + tax;

        Console.WriteLine($"Price: {price}");
        Console.WriteLine($"Tax: {tax}");
        Console.WriteLine($"Total: {total}");

        Console.WriteLine($"Rounded total: {Math.Round(total)}");
        Console.WriteLine($"Square root of 64: {Math.Sqrt(64)}");
        Console.WriteLine();

        // Random
        Random random = new Random();
        int randomNumber = random.Next(1, 101);
        Console.WriteLine($"Random number from 1 to 100: {randomNumber}");

        Console.WriteLine();

        // Strings
        string message = "Hello C#";
        Console.WriteLine($"Message: {message}");
        Console.WriteLine($"Length: {message.Length}");
        Console.WriteLine($"Uppercase: {message.ToUpper()}");
        Console.WriteLine($"Lowercase: {message.ToLower()}");
        Console.WriteLine($"First 5 letters: {message.Substring(0, 5)}");
    }
}
