using System;
using System.Text;

// --- STRING INTERPOLATION & FORMATTING ---
// You've used $"..." already — there's a lot more to it!

class StringFormattingDemo
{
    public static void Run()
    {
        Console.WriteLine("=== STRING FORMATTING ===");
        Console.WriteLine();

        // --- Number formatting specifiers ---
        Console.WriteLine("-- Number Format Specifiers --");

        double price = 1499.9;
        int count = 42000;
        double pi = Math.PI;
        double percent = 0.756;

        Console.WriteLine($"Currency:    {price:C}");         // ₹ or $ depending on system locale
        Console.WriteLine($"Fixed 2 dp:  {price:F2}");        // 1499.90
        Console.WriteLine($"Fixed 0 dp:  {price:F0}");        // 1500
        Console.WriteLine($"Thousands:   {count:N0}");         // 42,000
        Console.WriteLine($"Percent:     {percent:P1}");       // 75.6%
        Console.WriteLine($"Exponential: {pi:E2}");            // 3.14E+000
        Console.WriteLine($"Custom:      {price:0,000.00}");   // 1,499.90

        Console.WriteLine();

        // --- Padding & alignment ---
        Console.WriteLine("-- Padding & Alignment --");

        // Positive number = right align, negative = left align
        Console.WriteLine($"|{"Name",10}|{"Score",8}|");       // right aligned
        Console.WriteLine($"|{"Khanishk",-10}|{95,8}|");
        Console.WriteLine($"|{"Aarav",-10}|{82,8}|");
        Console.WriteLine($"|{"Maya",-10}|{91,8}|");

        Console.WriteLine();

        // --- String.Format (older but still useful) ---
        Console.WriteLine("-- String.Format --");

        string result = String.Format("Name: {0,-10} | Score: {1:F1} | Grade: {2}", "Khanishk", 88.5, "A");
        Console.WriteLine(result);

        Console.WriteLine();

        // --- String methods you might not know ---
        Console.WriteLine("-- Useful String Methods --");

        string text = "  Hello, C# World!  ";

        Console.WriteLine($"Original:    '{text}'");
        Console.WriteLine($"Trim:        '{text.Trim()}'");
        Console.WriteLine($"TrimStart:   '{text.TrimStart()}'");
        Console.WriteLine($"Replace:     '{text.Trim().Replace("C#", "Python")}'");
        Console.WriteLine($"Contains:    {text.Contains("World")}");
        Console.WriteLine($"StartsWith:  {text.Trim().StartsWith("Hello")}");
        Console.WriteLine($"IndexOf '#': {text.IndexOf('#')}");
        Console.WriteLine($"Split by ' ': {string.Join("|", text.Trim().Split(' '))}");

        Console.WriteLine();

        // --- Verbatim strings: @"..." ---
        // No need to escape backslashes
        Console.WriteLine("-- Verbatim Strings (@) --");

        string path1 = "C:\\Users\\Khanishk\\Documents";    // needs \\
        string path2 = @"C:\Users\Khanishk\Documents";       // cleaner!

        Console.WriteLine(path1);
        Console.WriteLine(path2);

        Console.WriteLine();

        // --- StringBuilder: for building large strings efficiently ---
        // Repeated string += creates many string objects (slow)
        // StringBuilder modifies in place (fast)
        Console.WriteLine("-- StringBuilder (efficient string building) --");

        StringBuilder sb = new StringBuilder();
        sb.Append("Hello");
        sb.Append(", ");
        sb.Append("C#");
        sb.AppendLine("!");
        sb.AppendLine("This is efficient string building.");
        sb.Insert(0, "[START] ");   // insert at position 0
        sb.Replace("C#", "C# programming");

        Console.WriteLine(sb.ToString());
        Console.WriteLine($"StringBuilder length: {sb.Length}");
    }
}
