using System;

// --- STATIC KEYWORD ---
// static = belongs to the CLASS itself, not to any object instance
//
// Use static when:
//  - The data/method is shared across ALL instances
//  - You don't need an object to use it (utility/helper)

// Static UTILITY class — you never create an object of this
static class MathHelper
{
    // static method: call via MathHelper.Square(5)
    public static double Square(double n) => n * n;

    public static double Cube(double n) => n * n * n;

    public static bool IsEven(int n) => n % 2 == 0;

    public static int Clamp(int value, int min, int max)
    {
        if (value < min) return min;
        if (value > max) return max;
        return value;
    }
}

// Static FIELD: shared across all instances of the class
class Player
{
    // Static: shared by ALL Player objects
    private static int _totalPlayers = 0;

    // Instance: each Player has their own
    public string Name { get; }
    public int Score { get; private set; }

    public Player(string name)
    {
        Name = name;
        Score = 0;
        _totalPlayers++;  // updates the shared counter
    }

    public void AddScore(int points)
    {
        Score += points;
    }

    // Static method to get shared data
    public static int GetTotalPlayers() => _totalPlayers;

    public override string ToString() => $"{Name}: {Score} pts";
}

// --- STATIC CONSTRUCTOR ---
// Runs ONCE when the class is first used, to initialize static members
class Config
{
    public static string AppName { get; }
    public static string Version { get; }
    public static DateTime LaunchTime { get; }

    // Static constructor — no parameters, runs automatically once
    static Config()
    {
        AppName = "MyApp";
        Version = "1.0.0";
        LaunchTime = DateTime.Now;
        Console.WriteLine("  [Config static constructor ran]");
    }
}

class StaticKeyword
{
    public static void Run()
    {
        Console.WriteLine("=== STATIC KEYWORD ===");
        Console.WriteLine();

        // Static utility class — no 'new' needed
        Console.WriteLine("-- MathHelper (static utility class) --");
        Console.WriteLine($"Square of 7:   {MathHelper.Square(7)}");
        Console.WriteLine($"Cube of 3:     {MathHelper.Cube(3)}");
        Console.WriteLine($"Is 8 even?     {MathHelper.IsEven(8)}");
        Console.WriteLine($"Clamp(150, 0, 100): {MathHelper.Clamp(150, 0, 100)}");

        Console.WriteLine();

        // Static field: shared across all instances
        Console.WriteLine("-- Static Field (shared counter) --");
        Player p1 = new Player("Khanishk");
        Player p2 = new Player("Aarav");
        Player p3 = new Player("Maya");

        p1.AddScore(50);
        p2.AddScore(80);
        p3.AddScore(65);

        Console.WriteLine(p1);
        Console.WriteLine(p2);
        Console.WriteLine(p3);
        Console.WriteLine($"Total players created: {Player.GetTotalPlayers()}");  // shared!

        Console.WriteLine();

        // Static constructor
        Console.WriteLine("-- Static Constructor --");
        Console.WriteLine($"App: {Config.AppName} v{Config.Version}");
        Console.WriteLine($"Launched at: {Config.LaunchTime:HH:mm:ss}");
    }
}
