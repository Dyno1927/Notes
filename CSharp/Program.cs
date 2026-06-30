using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.Clear();
            Console.WriteLine("=== C# Practice Menu ===");
            Console.WriteLine();
            Console.WriteLine("--- Original Topics ---");
            Console.WriteLine("1. Basics");
            Console.WriteLine("2. Conditions & Loops");
            Console.WriteLine("3. Arrays & Methods");
            Console.WriteLine("4. OOP");
            Console.WriteLine("5. Lists, Enums & Generics");
            Console.WriteLine("6. Exceptions & File I/O");
            Console.WriteLine();
            Console.WriteLine("7.  Interfaces & Dependency Injection");
            Console.WriteLine("8.  Properties & Access Modifiers");
            Console.WriteLine("9.  Static Keyword");
            Console.WriteLine("10. Readonly vs Const");
            Console.WriteLine("11. LINQ");
            Console.WriteLine("12. Lambda Expressions");
            Console.WriteLine("13. Nullable Types");
            Console.WriteLine("14. Struct vs Class");
            Console.WriteLine("15. String Formatting");
            Console.WriteLine();
            Console.WriteLine("0. Exit");
            Console.Write("Choose an option: ");

            string? choice = Console.ReadLine();

            Console.Clear();

            switch (choice)
            {
                case "1":
                    Basics.Run();
                    break;

                case "2":
                    ConditionsLoops.Run();
                    break;

                case "3":
                    ArraysMethods.Run();
                    break;

                case "4":
                    OOPDemo.Run();
                    break;

                case "5":
                    CollectionsEnumsGenerics.Run();
                    break;

                case "6":
                    ExceptionsAndFileIO.Run();
                    break;

                case "7":
                    InterfacesAndDI.Run();
                    break;

                case "8":
                    PropertiesAndAccessModifiers.Run();
                    break;

                case "9":
                    StaticKeyword.Run();
                    break;

                case "10":
                    ReadonlyVsConst.Run();
                    break;

                case "11":
                    LINQDemo.Run();
                    break;

                case "12":
                    LambdaExpressions.Run();
                    break;

                case "13":
                    NullableTypes.Run();
                    break;

                case "14":
                    StructVsClass.Run();
                    break;

                case "15":
                    StringFormattingDemo.Run();
                    break;

                case "0":
                    return;

                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }

            Console.WriteLine();
            Console.WriteLine("Press any key to go back to the menu...");
            Console.ReadKey();
        }
    }
}
