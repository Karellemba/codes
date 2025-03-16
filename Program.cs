Console.WriteLine("Sisesta esimene arv:");
double arv1 = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Sisesta tehe (+, -, *, /):");
char tehe = Convert.ToChar(Console.ReadLine());

Console.WriteLine("Sisesta teine arv:");
double arv2 = Convert.ToDouble(Console.ReadLine());

double tulemus = 0;

if (tehe == '+')
{
    tulemus = arv1 + arv2;
}
else if (tehe == '-')
{
    tulemus = arv1 - arv2;
}
else if (tehe == '*')
{
    tulemus = arv1 * arv2;
}
else if (tehe == '/')
{
    if (arv2 != 0)
    {
        tulemus = arv1 / arv2;
    }
    else
    {
        Console.WriteLine("Nulliga jagamine pole lubatud.");
        return;
    }
}
else
{
    Console.WriteLine("Vigane tehe.");
    return;
}

Console.WriteLine("Tulemus: " + tulemus);


