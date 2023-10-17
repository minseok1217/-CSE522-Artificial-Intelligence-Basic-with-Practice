import numpy as np
import matplotlib.pyplot as plt

DELTA_X = 1e-5

def func(x):
    return x**4 - 7*x**3 + 9*x**2 + 30

def fun_c(x):
    return x**3 + 3 * x**2

def derivative(f, a, h=DELTA_X):
    y_prime = (f(a+h)-f(a))/h
    return y_prime

def double_d(f, a, h = DELTA_X):
    f_prime_a = derivative(f, a, h)
    f_prime_a_plus_h = derivative(f, a + h, h)
    
    # 2계 도함수 계산
    y_double_prime = (f_prime_a_plus_h - f_prime_a) / h
    return y_double_prime

def show_first_derivative(f, interval) :
    plt.figure(figsize=(12, 10), dpi=150)
    x = np.linspace(*interval, 10000)
    y = f(x)

    # plot the origin function
    plt.subplot(3, 1, 1)
    plt.plot(x, y, label = 'Function', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('origin Function')
    plt.axhline(0, color='gray', linestyle= 'dashed')
    plt.axvline(0, color='gray', linestyle= 'dashed')
    plt.legend()

    # plot the first derivative of function (plot code를 완성하시오)
    plt.subplot(3, 1, 2)
    y_prime = derivative(f, x)
    plt.title('First Derivative of Function')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.plot(x, y_prime, label = 'First Derivative', linewidth=2)
    plt.axhline(0, color='gray', linestyle='dashed')
    plt.axvline(0, color='gray', linestyle='dashed')
    plt.legend()

    # Show the plots
    plt.tight_layout()
    plt.show()
    


def main():
    # show_first_derivative(f=func, interval=(0, 5)) # 수정 x
    print(double_d(fun_c, 2))
    
if __name__ == "__main__":
    main()