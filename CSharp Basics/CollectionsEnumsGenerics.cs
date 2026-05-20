using System;
using System.Collections.Generic;

enum Difficulty
{
    Easy,
    Medium,
    Hard
}

class CollectionsEnumsGenerics
{
    public static void Run()
    {
        Console.WriteLine("=== LISTS, ENUMS & GENERICS ===");
        Console.WriteLine();

        // List
        List<string> topics = new List<string>
        {
            "Basics",
            "Conditions",
            "Loops",
            "Arrays",
            "OOP"
        };

        topics.Add("Lists");
        topics.Remove("Conditions");

        Console.WriteLine("Topics in list:");
        foreach (string topic in topics)
        {
            Console.WriteLine(topic);
        }

        Console.WriteLine();

        // Dictionary
        Dictionary<string, int> scores = new Dictionary<string, int>
        {
            { "Quiz 1", 8 },
            { "Quiz 2", 10 },
            { "Quiz 3", 9 }
        };

        Console.WriteLine("Quiz scores:");
        foreach (KeyValuePair<string, int> item in scores)
        {
            Console.WriteLine($"{item.Key} = {item.Value}");
        }

        Console.WriteLine();

        // Enum
        Difficulty currentLevel = Difficulty.Medium;
        Console.WriteLine($"Current difficulty: {currentLevel}");

        Console.WriteLine();

        // Generic method
        ShowValue("Hello");
        ShowValue(123);
        ShowValue(45.67);

        Console.WriteLine();

        // Generic swap
        int a = 10;
        int b = 20;

        Console.WriteLine($"Before swap: a={a}, b={b}");
        Swap(ref a, ref b);
        Console.WriteLine($"After swap:  a={a}, b={b}");
    }

    static void ShowValue<T>(T value)
    {
        Console.WriteLine($"Value: {value}");
    }

    static void Swap<T>(ref T first, ref T second)
    {
        T temp = first;
        first = second;
        second = temp;
    }
}
