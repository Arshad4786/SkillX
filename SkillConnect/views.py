from django.shortcuts import render

def factorial(n):
    """Recursive function to calculate factorial."""
    if n == 0:
        return 1
    elif n < 0:
        return None  # Factorial is not defined for negative numbers
    else:
        return n * factorial(n - 1)

def home(request):
    number = 5  # Example number
    fact = factorial(number)
    context = {'number': number, 'factorial': fact}
    return render(request, 'SkillConnect/base.html', context)