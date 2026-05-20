using System;
using System.Collections.Generic;
using System.Linq;  // needed for LINQ

// --- LINQ (Language Integrated Query) ---
// LINQ lets you query collections (lists, arrays) using readable methods
// Instead of writing long loops, you write short, expressive queries

class Student2
{
    public string Name { get; set; }
    public int Age { get; set; }
    public double Grade { get; set; }
    public string Subject { get; set; }

    public Student2(string name, int age, double grade, string subject)
    {
        Name = name;
        Age = age;
        Grade = grade;
        Subject = subject;
    }

    public override string ToString() =>
        $"{Name,-12} | Age: {Age} | Grade: {Grade:0.0} | {Subject}";
}

class LINQDemo
{
    public static void Run()
    {
        Console.WriteLine("=== LINQ ===");
        Console.WriteLine();

        List<Student2> students = new List<Student2>
        {
            new Student2("Khanishk", 16, 88.5, "Math"),
            new Student2("Aarav",    17, 72.0, "Science"),
            new Student2("Maya",     18, 95.0, "Math"),
            new Student2("Riya",     16, 61.5, "English"),
            new Student2("Dev",      17, 83.0, "Science"),
            new Student2("Priya",    18, 91.5, "Math"),
        };

        // --- WHERE: filter ---
        Console.WriteLine("-- Students with grade > 80 --");
        var topStudents = students.Where(s => s.Grade > 80);
        foreach (var s in topStudents)
            Console.WriteLine(s);

        Console.WriteLine();

        // --- ORDERBY: sort ---
        Console.WriteLine("-- All students sorted by grade (descending) --");
        var sorted = students.OrderByDescending(s => s.Grade);
        foreach (var s in sorted)
            Console.WriteLine(s);

        Console.WriteLine();

        // --- SELECT: transform / project ---
        Console.WriteLine("-- Just student names --");
        var names = students.Select(s => s.Name);
        Console.WriteLine(string.Join(", ", names));

        Console.WriteLine();

        // --- SELECT into new shape ---
        Console.WriteLine("-- Name + Grade only --");
        var summary = students.Select(s => $"{s.Name}: {s.Grade}");
        foreach (var item in summary)
            Console.WriteLine(item);

        Console.WriteLine();

        // --- GROUPBY: group items ---
        Console.WriteLine("-- Students grouped by subject --");
        var grouped = students.GroupBy(s => s.Subject);
        foreach (var group in grouped)
        {
            Console.WriteLine($"{group.Key}:");
            foreach (var s in group)
                Console.WriteLine($"  {s.Name} ({s.Grade})");
        }

        Console.WriteLine();

        // --- Aggregate methods ---
        Console.WriteLine("-- Aggregate LINQ methods --");
        Console.WriteLine($"Count:   {students.Count()}");
        Console.WriteLine($"Average: {students.Average(s => s.Grade):0.00}");
        Console.WriteLine($"Max:     {students.Max(s => s.Grade)}");
        Console.WriteLine($"Min:     {students.Min(s => s.Grade)}");
        Console.WriteLine($"Sum:     {students.Sum(s => s.Grade)}");

        Console.WriteLine();

        // --- Chaining: combine multiple operations ---
        Console.WriteLine("-- Chained: Math students, grade > 85, sorted by name --");
        var mathToppers = students
            .Where(s => s.Subject == "Math")
            .Where(s => s.Grade > 85)
            .OrderBy(s => s.Name);

        foreach (var s in mathToppers)
            Console.WriteLine(s);

        Console.WriteLine();

        // --- FIRST / FIRSTORDEFAULT ---
        Console.WriteLine("-- First student with grade > 90 --");
        var first = students.FirstOrDefault(s => s.Grade > 90);
        Console.WriteLine(first != null ? first.ToString() : "None found");

        // --- ANY / ALL ---
        Console.WriteLine();
        Console.WriteLine($"Any student failed (< 60)?  {students.Any(s => s.Grade < 60)}");
        Console.WriteLine($"All students passed (>= 60)? {students.All(s => s.Grade >= 60)}");
    }
}
