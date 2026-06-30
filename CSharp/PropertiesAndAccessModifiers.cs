using System;

// --- ACCESS MODIFIERS ---
// Controls WHO can see/use a member
//
// public    → anyone can access
// private   → only THIS class can access
// protected → this class + subclasses
// internal  → only within same project/assembly

class BankAccount
{
    // private: only this class can touch these
    private string _owner;
    private double _balance;

    // --- PROPERTIES ---
    // Properties are like smart variables with get/set logic

    // Full property with validation in setter
    public string Owner
    {
        get { return _owner; }
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new ArgumentException("Owner name cannot be empty.");
            _owner = value;
        }
    }

    // Read-only property (no setter)
    public double Balance
    {
        get { return _balance; }
    }

    // Auto-property (C# handles the private field for you)
    public string AccountNumber { get; private set; }  // external: read only, internal: can set

    // Computed property (no field, calculates on the fly)
    public bool IsOverdrawn => _balance < 0;

    // Constructor
    public BankAccount(string owner, string accountNumber, double initialBalance = 0)
    {
        Owner = owner;                 // uses the property setter (with validation)
        AccountNumber = accountNumber;
        _balance = initialBalance;
    }

    // public method: anyone can call this
    public void Deposit(double amount)
    {
        if (amount <= 0)
        {
            Console.WriteLine("Deposit amount must be positive.");
            return;
        }

        _balance += amount;
        LogTransaction("Deposit", amount);
    }

    public bool Withdraw(double amount)
    {
        if (amount <= 0)
        {
            Console.WriteLine("Withdrawal amount must be positive.");
            return false;
        }

        if (amount > _balance)
        {
            Console.WriteLine("Insufficient funds.");
            return false;
        }

        _balance -= amount;
        LogTransaction("Withdrawal", amount);
        return true;
    }

    // private: only this class uses this internally
    private void LogTransaction(string type, double amount)
    {
        Console.WriteLine($"  [{type}] ₹{amount:0.00} | New balance: ₹{_balance:0.00}");
    }

    public override string ToString()
    {
        return $"Account [{AccountNumber}] | Owner: {Owner} | Balance: ₹{_balance:0.00}";
    }
}

// --- PROTECTED demo ---
class Animal
{
    public string Name { get; set; }

    protected int Age;  // subclass can access, but outsiders can't

    public Animal(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

class Tiger : Animal
{
    public Tiger(string name, int age) : base(name, age) { }

    public void ShowInfo()
    {
        // Can access 'Age' because it's protected and we're a subclass
        Console.WriteLine($"{Name} is {Age} years old.");
    }
}

class PropertiesAndAccessModifiers
{
    public static void Run()
    {
        Console.WriteLine("=== PROPERTIES & ACCESS MODIFIERS ===");
        Console.WriteLine();

        BankAccount account = new BankAccount("Khanishk", "ACC-001", 1000);
        Console.WriteLine(account);
        Console.WriteLine();

        Console.WriteLine("Depositing ₹500:");
        account.Deposit(500);

        Console.WriteLine("Withdrawing ₹200:");
        account.Withdraw(200);

        Console.WriteLine("Withdrawing ₹5000 (should fail):");
        account.Withdraw(5000);

        Console.WriteLine();
        Console.WriteLine($"Is overdrawn? {account.IsOverdrawn}");
        Console.WriteLine($"Owner: {account.Owner}");
        Console.WriteLine($"Account Number: {account.AccountNumber}");

        Console.WriteLine();

        // Protected demo
        Console.WriteLine("-- Protected Modifier Demo --");
        Tiger tiger = new Tiger("Shera", 5);
        tiger.ShowInfo();
        // tiger.Age  ← this would cause a compile ERROR (protected)
    }
}
