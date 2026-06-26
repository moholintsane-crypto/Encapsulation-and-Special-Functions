def calculate_simple_interest(principal, rate, time):
    """Calculates simple interest."""
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return interest, total_amount

def calculate_compound_interest(principal, rate, time, n):
    """Calculates compound interest."""
    # Formula: A = P(1 + r/n)^(nt)
    amount = principal * (1 + (rate / 100) / n) ** (n * time)
    interest = amount - principal
    return interest, amount

def main():
    print("=== Python Interest Calculator ===")
    
    try:
        # Get user inputs
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (in years): "))
        
        # Calculate Simple Interest
        si_interest, si_total = calculate_simple_interest(principal, rate, time)
        print("\n--- Simple Interest ---")
        print(f"Interest: ${si_interest:.2f}")
        print(f"Total Amount: ${si_total:.2f}")
        
        # Calculate Compound Interest (Compounded Annually, n = 1)
        ci_interest, ci_total = calculate_compound_interest(principal, rate, time, n=1)
        print("\n--- Compound Interest (Annually) ---")
        print(f"Interest: ${ci_interest:.2f}")
        print(f"Total Amount: ${ci_total:.2f}")

    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
