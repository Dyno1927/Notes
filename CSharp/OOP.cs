using System;

class OOPDemo
{
    public static void Run()
    {
        Console.WriteLine("=== OOP DEMO ===");
        Console.WriteLine();

        // Object creation
        Student s1 = new Student("Aarav", 17);
        Student s2 = new Student("Maya", 18);

        Console.WriteLine(s1);
        Console.WriteLine(s2);

        s1.Introduce();
        s2.Introduce();

        Console.WriteLine();

        // Inheritance + polymorphism
        Vehicle vehicle = new Vehicle();
        Car car = new Car("Toyota");

        vehicle.Start();
        car.Start();
        car.Honk();

        Console.WriteLine();

        // Abstract class example
        Shape[] shapes =
        {
            new Circle(5),
            new Rectangle(4, 6)
        };

        foreach (Shape shape in shapes)
        {
            Console.WriteLine($"{shape.Name} area = {shape.Area():0.00}");
        }
    }
}

class Student
{
    // Auto-properties
    public string Name { get; set; }
    public int Age { get; set; }

    public Student(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public void Introduce()
    {
        Console.WriteLine($"Hi, I am {Name} and I am {Age} years old.");
    }

    public override string ToString()
    {
        return $"{Name} ({Age} years old)";
    }
}

class Vehicle
{
    public virtual void Start()
    {
        Console.WriteLine("Vehicle is starting.");
    }
}

class Car : Vehicle
{
    public string Brand { get; set; }

    public Car(string brand)
    {
        Brand = brand;
    }

    public override void Start()
    {
        Console.WriteLine($"{Brand} car is starting.");
    }

    public void Honk()
    {
        Console.WriteLine($"{Brand} car says beep beep!");
    }
}

abstract class Shape
{
    public abstract string Name { get; }
    public abstract double Area();
}

class Circle : Shape
{
    public override string Name => "Circle";

    private readonly double _radius;

    public Circle(double radius)
    {
        _radius = radius;
    }

    public override double Area()
    {
        return Math.PI * _radius * _radius;
    }
}

class Rectangle : Shape
{
    public override string Name => "Rectangle";

    private readonly double _width;
    private readonly double _height;

    public Rectangle(double width, double height)
    {
        _width = width;
        _height = height;
    }

    public override double Area()
    {
        return _width * _height;
    }
}
