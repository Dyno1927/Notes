using System;

// --- READONLY vs CONST ---
//
// const:
//   - Value set at COMPILE TIME (must be known before running)
//   - Always static (shared, no object needed)
//   - Only works with simple types: int, double, string, bool
//
// readonly:
//   - Value set at RUNTIME (can be calculated when program runs)
//   - Can be different per object (instance readonly)
//   - Works with any type including objects

// Renamed to CircleShape to avoid conflict with Circle in OOP.cs
class CircleShape
{
    // const: known at compile time, never changes, ever
    public const double Pi = 3.14159265358979;

    // readonly: set once in constructor, can't change after
    public readonly double Radius;
    public readonly double Area;
    public readonly string CreatedAt;

    public CircleShape(double radius)
    {
        Radius = radius;
        Area = Pi * radius * radius;    // calculated at runtime
        CreatedAt = DateTime.Now.ToString("HH:mm:ss");
    }

    public override string ToString() =>
        $"Circle | Radius: {Radius} | Area: {Area:0.00} | Created: {CreatedAt}";
}

class AppSettings
{
    // const: same for the whole app, set before compile
    public const string AppName = "QuizMaster";
    public const int MaxRetries = 3;

    // static readonly: calculated once when app starts
    public static readonly string StartupTime = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
    public static readonly string Environment = "Development";

    // instance readonly: each AppSettings object can have a different value
    public readonly string UserId;

    public AppSettings(string userId)
    {
        UserId = userId;
    }
}

class ReadonlyVsConst
{
    public static void Run()
    {
        Console.WriteLine("=== READONLY vs CONST ===");
        Console.WriteLine();

        // const
        Console.WriteLine("-- const --");
        Console.WriteLine($"App name: {AppSettings.AppName}");
        Console.WriteLine($"Max retries: {AppSettings.MaxRetries}");
        Console.WriteLine($"Pi: {CircleShape.Pi}");

        Console.WriteLine();

        // static readonly
        Console.WriteLine("-- static readonly --");
        Console.WriteLine($"Startup time: {AppSettings.StartupTime}");
        Console.WriteLine($"Environment: {AppSettings.Environment}");

        Console.WriteLine();

        // instance readonly (each object has its own value)
        Console.WriteLine("-- instance readonly --");
        CircleShape c1 = new CircleShape(5);
        CircleShape c2 = new CircleShape(10);

        Console.WriteLine(c1);
        Console.WriteLine(c2);

        // c1.Radius = 99;  ← compile ERROR: readonly can't be changed after constructor

        Console.WriteLine();

        Console.WriteLine("-- Summary Table --");
        Console.WriteLine($"{"Feature",-20} {"const",-20} {"readonly"}");
        Console.WriteLine(new string('-', 60));
        Console.WriteLine($"{"When set",-20} {"Compile time",-20} {"Runtime (constructor)"}");
        Console.WriteLine($"{"Can change?",-20} {"Never",-20} {"Only in constructor"}");
        Console.WriteLine($"{"Works with objects?",-20} {"No",-20} {"Yes"}");
        Console.WriteLine($"{"Per-instance?",-20} {"No (always static)",-20} {"Yes"}");
    }
}
 