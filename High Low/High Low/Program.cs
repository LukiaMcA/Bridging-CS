using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace High_Low
{
    class Program
    {
        static void Main(string[] args)
        {
            //welcome message
            Console.WriteLine("Welcome to my high low picolo cool game");
            //number generator
            Random rng = new Random();
            // generates number between 1 and 11
            int number = rng.Next(1, 11);
            int Tries = new int();
            Tries = 0;
            while (true)
            {
     
                //enter users guess
                Console.Write("Enter guess: ");
                int guess = Convert.ToInt32(Console.ReadLine());
                //compares guess to number
                if (guess < number)
                {
                    Console.WriteLine("Too Low, Go Higher!");
                    Tries = Tries + 1;
                }
                else if (guess > number)
                {
                    Console.WriteLine("Too High, Go Lower!");
                    Tries = Tries + 1;
                }
                else
                {
                    Console.WriteLine("Correct Guess!");
                    Tries = Tries + 1;
                    Console.WriteLine("You took " + Tries + " Tries");
                    break;
                }
                

            }
            Console.ReadKey();
        }
    }
}
