using System;

// --- INTERFACES ---
// An interface is like a CONTRACT
// Any class that "implements" it MUST have those methods

interface IAnimal
{
    string Name { get; }     // property contract
    void Speak();            // method contract
    string GetInfo();
}

interface ITrainable
{
    void Train(string trick);
}

// Dog implements BOTH interfaces
class Dog : IAnimal, ITrainable
{
    public string Name { get; }

    public Dog(string name)
    {
        Name = name;
    }

    public void Speak() => Console.WriteLine($"{Name} says: Woof!");

    public string GetInfo() => $"Dog named {Name}";

    public void Train(string trick) => Console.WriteLine($"{Name} learned: {trick}!");
}

// Cat implements only IAnimal
class Cat : IAnimal
{
    public string Name { get; }

    public Cat(string name)
    {
        Name = name;
    }

    public void Speak() => Console.WriteLine($"{Name} says: Meow!");

    public string GetInfo() => $"Cat named {Name}";
}

// --- DEPENDENCY INJECTION ---
// Instead of a class CREATING its own dependencies,
// we PASS them in from outside. This makes code flexible and testable.

interface ILogger
{
    void Log(string message);
}

class ConsoleLogger : ILogger
{
    public void Log(string message) =>
        Console.WriteLine($"[LOG] {message}");
}

class FileLogger : ILogger
{
    public void Log(string message) =>
        Console.WriteLine($"[FILE] Would write: {message}");
}

// UserService DEPENDS on ILogger — injected via constructor
class UserService
{
    private readonly ILogger _logger;  // depends on the interface, not a specific class

    // Dependency is INJECTED here
    public UserService(ILogger logger)
    {
        _logger = logger;
    }

    public void CreateUser(string username)
    {
        _logger.Log($"Creating user: {username}");
        Console.WriteLine($"User '{username}' created successfully.");
    }

    public void DeleteUser(string username)
    {
        _logger.Log($"Deleting user: {username}");
        Console.WriteLine($"User '{username}' deleted.");
    }
}

class InterfacesAndDI
{
    public static void Run()
    {
        Console.WriteLine("=== INTERFACES & DEPENDENCY INJECTION ===");
        Console.WriteLine();

        // --- Interface demo ---
        Console.WriteLine("-- Interface Demo --");

        // We can store both Dog and Cat in IAnimal variables!
        IAnimal[] animals = { new Dog("Rex"), new Cat("Whiskers"), new Dog("Buddy") };

        foreach (IAnimal animal in animals)
        {
            animal.Speak();
            Console.WriteLine(animal.GetInfo());
        }

        Console.WriteLine();

        // ITrainable — only Dog has this
        Dog myDog = new Dog("Max");
        myDog.Train("sit");
        myDog.Train("roll over");

        Console.WriteLine();

        // --- Dependency Injection demo ---
        Console.WriteLine("-- Dependency Injection Demo --");

        // Swap the logger without changing UserService at all!
        ILogger consoleLogger = new ConsoleLogger();
        ILogger fileLogger = new FileLogger();

        Console.WriteLine("Using ConsoleLogger:");
        UserService service1 = new UserService(consoleLogger);
        service1.CreateUser("Khanishk");

        Console.WriteLine();

        Console.WriteLine("Using FileLogger (same UserService, different logger):");
        UserService service2 = new UserService(fileLogger);
        service2.CreateUser("Aarav");
        service2.DeleteUser("Khanishk");
    }
}
