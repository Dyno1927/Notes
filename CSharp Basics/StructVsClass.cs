using System;

// --- STRUCT vs CLASS ---
//
// Both can have fields, properties, constructors, and methods.
// The BIG difference is HOW they are stored in memory:
//
// CLASS  → Reference type: variable stores a REFERENCE (pointer) to data
//           Stored on the HEAP
//           When you copy a class variable, both point to the SAME object
//
// STRUCT → Value type: variable stores the ACTUAL data
//           Stored on the STACK
//           When you copy a struct variable, you get a SEPARATE copy
//
// When to use STRUCT:
//   - Small, simple data (Point, Color, Temperature)
//   - Doesn't need inheritance
//   - Frequently created/destroyed (performance matters)

// STRUCT: value type
struct Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public double DistanceTo(Point other)
    {
        int dx = X - other.X;
        int dy = Y - other.Y;
        return Math.Sqrt(dx * dx + dy * dy);
    }

    public override string ToString() => $"({X}, {Y})";
}

// STRUCT: another practical example
struct Temperature
{
    public double Celsius { get; }
    public double Fahrenheit => Celsius * 9 / 5 + 32;

    public Temperature(double celsius)
    {
        Celsius = celsius;
    }

    public override string ToString() => $"{Celsius}°C / {Fahrenheit:0.0}°F";
}

// CLASS: reference type (for comparison)
class PersonRef
{
    public string Name;
    public int Age;

    public PersonRef(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public override string ToString() => $"{Name}, {Age}";
}

class StructVsClass
{
    public static void Run()
    {
        Console.WriteLine("=== STRUCT vs CLASS ===");
        Console.WriteLine();

        // --- Struct: value copy behavior ---
        Console.WriteLine("-- STRUCT: Value Copy (independent copies) --");

        Point p1 = new Point(3, 4);
        Point p2 = p1;   // COPY: p2 gets its own separate data

        p2.X = 99;       // change p2 — does NOT affect p1

        Console.WriteLine($"p1 = {p1}");   // still (3, 4)
        Console.WriteLine($"p2 = {p2}");   // (99, 4)
        Console.WriteLine("Changing p2.X did NOT change p1 (they are separate copies)");

        Console.WriteLine();

        // --- Class: reference copy behavior ---
        Console.WriteLine("-- CLASS: Reference Copy (same object) --");

        PersonRef person1 = new PersonRef("Khanishk", 16);
        PersonRef person2 = person1;   // REFERENCE: both point to SAME object

        person2.Name = "Aarav";         // change through person2...
        Console.WriteLine($"person1 = {person1}");  // ...also changes person1!
        Console.WriteLine($"person2 = {person2}");
        Console.WriteLine("Changing person2.Name ALSO changed person1 (same object in memory)");

        Console.WriteLine();

        // --- Struct methods ---
        Console.WriteLine("-- Struct methods --");
        Point a = new Point(0, 0);
        Point b = new Point(3, 4);
        Console.WriteLine($"Distance from {a} to {b}: {a.DistanceTo(b)}");

        Console.WriteLine();

        // --- Temperature struct ---
        Console.WriteLine("-- Temperature struct --");
        Temperature[] temps = { new Temperature(0), new Temperature(25), new Temperature(100) };
        foreach (var t in temps)
            Console.WriteLine(t);

        Console.WriteLine();

        // --- Summary ---
        Console.WriteLine("-- Summary --");
        Console.WriteLine($"{"Feature",-20} {"struct",-20} {"class"}");
        Console.WriteLine(new string('-', 55));
        Console.WriteLine($"{"Memory",-20} {"Stack",-20} {"Heap"}");
        Console.WriteLine($"{"Copy behavior",-20} {"Independent copy",-20} {"Same reference"}");
        Console.WriteLine($"{"Inheritance",-20} {"No",-20} {"Yes"}");
        Console.WriteLine($"{"Best for",-20} {"Small simple data",-20} {"Complex objects"}");
        Console.WriteLine($"{"Default null?",-20} {"No",-20} {"Yes"}");
    }
}
