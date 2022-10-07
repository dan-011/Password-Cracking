//
//  ECPolynomial.cpp
//  
//
//  Created by Yufeng Wu on 9/17/22.
//

#include "ECPolynomial.h"
#include <iostream>
using namespace std;
    
ECPolynomial::ECPolynomial(){}
ECPolynomial::ECPolynomial(int degree){
    for(int i = 0; i <= degree; i++){
        coeffs.push_back(0);
    }
}
ECPolynomial::ECPolynomial(const vector<double> &listCoeefsIn){
    coeffs = listCoeefsIn;
    //ClearTrailingZeroes();
}
ECPolynomial::ECPolynomial(const ECPolynomial &rhs){
    coeffs = rhs.coeffs;
    //ClearTrailingZeroes();
}
int ECPolynomial::GetDegree() const{
    if(coeffs.size() == 0) return 0;
    else{
        ECPolynomial copy(coeffs);
        copy.ClearTrailingZeroes();
        return copy.coeffs.size() - 1;
    }
}
double ECPolynomial::GetCoeff(int d) const{
    if(coeffs.size() == 0 || GetDegree() < d) return 0;
    else{
        return coeffs[d];
    }
}
ECPolynomial ECPolynomial::Scale(double factor){ // this might not want to change the object calling it
    //ClearTrailingZeroes();
    for(int i = 0; i <= GetDegree(); i++){
        coeffs[i] = coeffs[i] * factor;
    }
    return *this;
}
void ECPolynomial::CopyPolynomial(const ECPolynomial& pol){
    coeffs = pol.coeffs;
    //ClearTrailingZeroes();
}
ECPolynomial ECPolynomial::AddPolynomial(const ECPolynomial& pol) const{
    ECPolynomial res;
    unsigned int n1 = coeffs.size();
    unsigned int n2 = pol.coeffs.size();
    unsigned int i = 0;
    while(i < n1 && i < n2){
        res.coeffs.push_back(coeffs[i] + pol.coeffs[i]);
        i++;
    }
    while(i < n1){
        res.coeffs.push_back(coeffs[i]);
        i++;
    }
    while(i < n2){
        res.coeffs.push_back(pol.coeffs[i]);
        i++;
    }
    //res.ClearTrailingZeroes();
    return res;
}

void ECPolynomial::ClearTrailingZeroes(){
    if(coeffs.size() > 0 && (coeffs[coeffs.size() - 1] == 0 || (coeffs[coeffs.size() - 1] < 0.0000000001 && coeffs[coeffs.size() - 1] > 0))){
        int i = coeffs.size() - 1;
        while(i >= 0 && (coeffs[i] == 0 || coeffs[i] < 0.0000000001)){
            coeffs.pop_back();
            i--;
        }
    }
}

void ECPolynomial::Dump() const{
    /*for(unsigned int i = 0; i < coeffs.size(); i++){
        if(i == 0){
            cout << coeffs[i];
        }
        else{
            double val = coeffs[i];
            if(val == 0) continue;
            if(val < 0){
                cout << "-";
                val = val * -1;
            }
            else{
                cout << "+";
            }
            if(val != 1){
                cout << val;
            }
            cout << "x";
            if(i > 1){
                cout << "^" << i;
            }
        }
    }*/
    // Deg: 1:  -3 1 \n
    cout << "Deg: " << GetDegree() << ":  ";
    ECPolynomial copy(coeffs);
    copy.ClearTrailingZeroes();
    for(double d : copy.coeffs){
        cout << d << ' ';
    }
    cout << endl;
}

ECPolynomial ECPolynomial::MultiplyPolynomial(const ECPolynomial& rhs) const{
    int max_coeff = GetDegree() + rhs.GetDegree() + 1;
    vector<double> vec;
    for(int i = 0; i < max_coeff; i++){
        vec.push_back(0.0);
    }
    for(int i = 0; i <= GetDegree(); i++){
        for(int j = 0; j <= rhs.GetDegree(); j++){
            vec[i+j] += coeffs[i]*rhs.coeffs[j];
        }
    }
    ECPolynomial res(vec);
    return res;
}

ECPolynomial ECPolynomial::DivideBy(const ECPolynomial &rhs, ECPolynomial &remainder) const{
    int max_coeff = GetDegree() - rhs.GetDegree() + 1;
    ECPolynomial dividend(coeffs);
    //ECPolynomial divisor(rhs.coeffs);
    vector<double> res_vec;
    for(int i = 0; i < max_coeff; i++){
        res_vec.push_back(0);
    }
    int n1 = GetDegree();
    int n2 = rhs.GetDegree();
    for(int i = n1; i >= 0; i--){ // going through the coefficients in reverse order
        if(i < n2) break; // we can no longer divide when the remainder is smaller than the divisor
        double _dividend = dividend.coeffs[i];
        double _divisor = rhs.GetCoeff(n2);
        double _quotient = _dividend/_divisor;
        int quot_index = i - n2;
        res_vec[quot_index] = _quotient;
        ECPolynomial subtract;
        for(int c = 0; c <= dividend.GetDegree(); c++){
            subtract.coeffs.push_back(0);
        }
        for(int j = n2; j >= 0; j--){ // for each of the divisor's values
            double rVal = _quotient*rhs.GetCoeff(j);
            int rIndex =  quot_index + j;
            subtract.coeffs[rIndex] = rVal;
        }
        dividend = dividend - subtract; // change to Polynomials and implement a push back method
    }
    remainder = dividend;
    ECPolynomial res(res_vec);
    return res;
}
/* These are ordered largest degree first
        _
[1 -3] [1 -2 0 -4] [0 0 0 0] [0 0 0]
1/1(3-1) [1 0 0]
1*1(1+2) 1*-3(0+2) [1 -3 0 0] mult div with res num to get subtract val
[1 -2 0 -4] - [1 -3 0 0]
          _
[1 -3] [0 1 0 -4] [0 0 0 0] [1 0 0]
1/1(2-1)1*1(1+1) 1*-3(0+1) [0 1 -3 0] [1 1 0]
[0 1 0 -4] - [0 1 -3 0]
            _
[1 -3] [0 0 3 -4] [0 0 0 0] [1 1 0]
3/1(1-1) 1*3(1+0) -3*3(0+0) [0 0 3 -9] [1 1 3]
[0 0 3 -4] - [0 0 3 -9]
              _
[1 -3] [0 0 0 5] [0 0 0 0] [1 1 3]
degree of [1, -3] is larger than the degree of [0 0 0 5] so stop
res: [1 1 3] rem: [0 0 0 5]
*/