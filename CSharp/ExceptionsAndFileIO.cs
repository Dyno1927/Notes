using System;
using System.IO;

class ExceptionsAndFileIO
{
    public static void Run()
    {
        Console.WriteLine("=== EXCEPTIONS & FILE I/O ===");
        Console.WriteLine();

        // Exception handling
        try
        {
            Console.Write("Enter a number to divide 100 by: ");
            string? input = Console.ReadLine();

            int number = int.Parse(input!);

            int result = 100 / number;
            Console.WriteLine($"100 / {number} = {result}");
        }
        catch (FormatException)
        {
            Console.WriteLine("You must enter a valid whole number.");
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("You cannot divide by zero.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Something unexpected happened: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Finished exception demo.");
        }

        Console.WriteLine();
        Console.WriteLine("File I/O demo:");

        string filePath = Path.Combine(AppContext.BaseDirectory, "practice_notes.txt");
        string note = $"Saved on: {DateTime.Now}\nThis is a practice note.\n\n";

        try
        {
            File.AppendAllText(filePath, note);

            Console.WriteLine($"Note saved to: {filePath}");
            Console.WriteLine();
            Console.WriteLine("Current file content:");
            Console.WriteLine(File.ReadAllText(filePath));
        }
        catch (Exception ex)
        {
            Console.WriteLine($"File error: {ex.Message}");
        }
    }
}
