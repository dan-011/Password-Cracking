//
//  ECPolynomial.h
//  
//
//  Created by Yufeng Wu on 9/17/22.
//

#ifndef ECPolynomial_h
#define ECPolynomial_h

#include <vector>

// *****************************************************************
// Represent a polynomial of a single variable, x, and
// support common operations on polynomial: add, scaling, multiple
// and (long) division, etc

class ECPolynomial
{
public:
    // Feel free to add more interface or implementation functions
    ECPolynomial();
    
    // Construct a polynomial with coefficients, where the first position is the constant term and [i] is the coefficient of x^i
    // Example: given [1, 3, 0, 2], polynomial = 1 + 3x + 2x^3
    // We assume listCoeffsIn is not empty
    // Note: the last term in listCoeffsIn should not be zero (unless its length is 1). For example, if given [1, 3, 0], we should simply it to [1,3]. Since coefficient is a double, we consider a value is practically zero if its absolute value is sufficiently small (say less than 1e^(-10)
    ECPolynomial(const std::vector<double> &listCoeffsIn);
    
    // Copy constructor
    ECPolynomial(const ECPolynomial &rhs);

    ECPolynomial(int degree);
    
    // Get the degree. Example: if polynomial=1+x+3x^3, degree=3
    int GetDegree() const;

    // Get the coefficients. Example: if polynomial=1+x+3x^3, coefficients(0)=1, coefficients(1)=3, coefficients(2)=0, coefficients(3)=2
    double GetCoeff(int d) const;    
    
    // Scale by a constant and return the resulting polynomial. For example, if polynomial is 1+3x, and
    // factor = 2, the result is 2+6x
    ECPolynomial Scale(double factor);
    
    // Add a polynomial to the current polynomial (and return the result). Example: (1+2x) + (2x+3x^2) = 1+4x+3x^2
    ECPolynomial operator+(const ECPolynomial &rhs) const{
        ECPolynomial res = AddPolynomial(rhs);
        return res;
    }
    
    // Multiply a polynomial by another polynomail and return the result. Example: (1+2x)*(1-x^2) = 1 + 2x - x^2 -2x^3
    ECPolynomial operator*(const ECPolynomial &rhs) const{
        ECPolynomial res = MultiplyPolynomial(rhs);
        return res;
    }
    
    // Divide a polynomial by another, and return the quotient (and save the remainder to the passed in parameter called remainder)
    // Example: if we divide x^3-2x^2-4 by x-3, then quotient = x^2+x+3 and remainder is 5
    // For now, assume rhs (denominator) is zero
    ECPolynomial DivideBy(const ECPolynomial &rhs, ECPolynomial &remainder) const;

    ECPolynomial& operator=(const ECPolynomial& pol){
        CopyPolynomial(pol);
        return *this;
    }

    ECPolynomial operator-(const ECPolynomial &rhs) const{
        ECPolynomial res(rhs.coeffs);
        res.Scale(-1.0);
        res = *this + res;
        return res;
    }
    
    // This is for testing only. It can be useful to dump out the polynomial (in some format) to the terminal for debugging
    void Dump() const;
    
    
private:
    std::vector<double> coeffs;
    void CopyPolynomial(const ECPolynomial& pol);
    ECPolynomial AddPolynomial(const ECPolynomial& pol) const;
    ECPolynomial MultiplyPolynomial(const ECPolynomial& pol) const;
    void ClearTrailingZeroes();
};

#endif /* ECPolynomial_h */
