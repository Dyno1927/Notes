using System;
using System.Collections.Generic;

class ArraysMethods
{
    public static void Run()
    {
        Console.WriteLine("=== ARRAYS & METHODS ===");
        Console.WriteLine();

        int[] marks = { 78, 91, 66, 84, 95 };

        Console.WriteLine("Marks in array:");
        PrintArray(marks);

        Console.WriteLine();
        Console.WriteLine($"Total marks: {Sum(marks)}");
        Console.WriteLine($"Average marks: {Average(marks):0.00}");
        Console.WriteLine($"Highest mark: {Highest(marks)}");

        Console.WriteLine();
        Console.Write("Enter 3 numbers separated by commas: ");
        string? input = Console.ReadLine();

        int[] customNumbers = ParseNumbers(input);

        Console.WriteLine();
        Console.WriteLine("Your numbers:");
        PrintArray(customNumbers);

        Console.WriteLine();
        Console.WriteLine($"Sum of your numbers: {Sum(customNumbers)}");
    }

    static void PrintArray(int[] values)
    {
        if (values.Length == 0)
        {
            Console.WriteLine("Array is empty.");
            return;
        }

        foreach (int value in values)
        {
            Console.WriteLine(value);
        }
    }

    static int Sum(int[] values)
    {
        int total = 0;

        foreach (int value in values)
        {
            total += value;
        }

        return total;
    }

    static double Average(int[] values)
    {
        if (values.Length == 0)
        {
            return 0;
        }

        return (double)Sum(values) / values.Length;
    }

    static int Highest(int[] values)
    {
        int highest = values[0];

        for (int i = 1; i < values.Length; i++)
        {
            if (values[i] > highest)
            {
                highest = values[i];
            }
        }

        return highest;
    }

    static int[] ParseNumbers(string? input)
    {
        if (string.IsNullOrWhiteSpace(input))
        {
            return Array.Empty<int>();
        }

        string[] parts = input.Split(',');
        List<int> numbers = new List<int>();

        foreach (string part in parts)
        {
            if (int.TryParse(part.Trim(), out int number))
            {
                numbers.Add(number);
            }
        }

        return numbers.ToArray();
    }
}
