
### 2. `ab_test_calculator.py`

Your updated Python script.

```python
import scipy.stats as stats

def calculate_performance_metrics(a_success, a_total, b_success, b_total):
    # Calculate success rates
    a_success_rate = a_success / a_total
    b_success_rate = b_success / b_total

    # Calculate p-value for A/B test using Chi-Square test
    success = [a_success, b_success]
    total = [a_total, b_total]
    chi2, p = stats.chisquare(success, f_exp=total)

    return p, a_success_rate, b_success_rate, b_success_rate - a_success_rate

def main():
    print("A/B Test Significance Calculator")
    
    # Hypotheses
    print("\nHypotheses:")
    print("Null Hypothesis (H0): There is no significant difference between the success rates of A and B.")
    print("Alternative Hypothesis (H1): There is a significant difference between the success rates of A and B.")
    
    # Input values
    a_success = int(input("Enter A Success: "))
    a_total = int(input("Enter A Total: "))
    b_success = int(input("Enter B Success: "))
    b_total = int(input("Enter B Total: "))
    
    # Input alpha value
    alpha = float(input("Enter the significance level (alpha, e.g., 0.05): "))
    
    # Calculate metrics
    p, a_success_rate, b_success_rate, diff = calculate_performance_metrics(a_success, a_total, b_success, b_total)
    
    # Print results
    print(f"\nP-value: {p:.4f}")
    print(f"Success Rate A: {a_success_rate:.4f}")
    print(f"Success Rate B: {b_success_rate:.4f}")
    print(f"Difference in Success Rates: {diff:.4f}")
    
    if p < alpha:
        print(f"Result: Significant difference between A and B (p < {alpha}).")
    else:
        print(f"Result: No significant difference between A and B (p >= {alpha}).")
    
    input("\nPress Enter to exit...")  # Wait for user input before closing

if __name__ == "__main__":
    main()
