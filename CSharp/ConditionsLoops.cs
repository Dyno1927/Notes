using System;

class ConditionsLoops
{
    public static void Run()
    {
        Console.WriteLine("=== CONDITIONS & LOOPS ===");
        Console.WriteLine();

        // if / else
        Console.Write("Enter your age: ");
        string? ageInput = Console.ReadLine();

        if (int.TryParse(ageInput, out int age))
        {
            if (age >= 18)
            {
                Console.WriteLine("You are an adult.");
            }
            else if (age >= 13)
            {
                Console.WriteLine("You are a teenager.");
            }
            else
            {
                Console.WriteLine("You are a child.");
            }
        }
        else
        {
            Console.WriteLine("Invalid age.");
        }

        Console.WriteLine();

        // switch
        Console.Write("Enter a day number (1-7): ");
        string? dayInput = Console.ReadLine();

        switch (dayInput)
        {
            case "1":
                Console.WriteLine("Monday");
                break;
            case "2":
                Console.WriteLine("Tuesday");
                break;
            case "3":
                Console.WriteLine("Wednesday");
                break;
            case "4":
                Console.WriteLine("Thursday");
                break;
            case "5":
                Console.WriteLine("Friday");
                break;
            case "6":
                Console.WriteLine("Saturday");
                break;
            case "7":
                Console.WriteLine("Sunday");
                break;
            default:
                Console.WriteLine("Invalid day number.");
                break;
        }

        Console.WriteLine();

        // for loop
        Console.WriteLine("For loop:");
        for (int i = 1; i <= 5; i++)
        {
            Console.WriteLine($"Count: {i}");
        }

        Console.WriteLine();

        // while loop
        Console.WriteLine("While loop:");
        int counter = 3;
        while (counter > 0)
        {
            Console.WriteLine(counter);
            counter--;
        }

        Console.WriteLine();

        // do-while loop
        Console.WriteLine("Do-while loop:");
        int x = 1;
        do
        {
            Console.WriteLine($"x = {x}");
            x++;
        }
        while (x <= 3);

        Console.WriteLine();

        // break / continue
        Console.WriteLine("Break and continue:");
        for (int i = 1; i <= 10; i++)
        {
            if (i == 5)
            {
                continue; // skip 5
            }

            if (i == 8)
            {
                break; // stop the loop at 8
            }

            Console.WriteLine(i);
        }
    }
}
