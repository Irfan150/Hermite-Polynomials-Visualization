import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite

def plot_hermite_polynomials(n_max=5):
    """
    Generates and plots the first few Hermite polynomials.

    Args:
        n_max (int): The maximum order of the polynomial to plot.
    """
    # Create a range of x values for the plot
    x = np.linspace(-3, 3, 400)
    
    plt.figure(figsize=(10, 7))
    
    # Loop from n=0 to n_max
    for n in range(n_max + 1):
        # SciPy's hermite(n) returns a polynomial object
        # This is based on the "physicists'" Hermite polynomials, which match
        # the generating function from your presentation: exp(2xt - t^2) 
        Hn = hermite(n)
        
        # Evaluate the polynomial H_n(x) at all x points
        y = Hn(x)
        
        # Plot the polynomial with a label
        plt.plot(x, y, label=f'$H_{n}(x)$')
        
    # Add plot details for a professional look
    plt.title(f'Hermite Polynomials $H_n(x)$ for n=0 to {n_max}')
    plt.xlabel('x')
    plt.ylabel('$H_n(x)$')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5) # x-axis line
    plt.ylim(-50, 50) # Set a reasonable y-axis limit
    
    # Save the plot as a file
    plt.savefig("hermite_polynomials.png")
    
    # Show the plot
    plt.show()

# --- Run the visualization ---
if __name__ == "__main__":
    plot_hermite_polynomials(n_max=5)