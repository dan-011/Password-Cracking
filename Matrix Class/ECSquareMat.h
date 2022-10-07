#ifndef EC_SQUARE_MAT
#define EC_SQUARE_MAT

#include <vector>
#include <ostream>

// square matrix
class ECSquareMat
{
public:
    ECSquareMat(int nDim);     // nDim: dimension of matrix (number of rows or columns)
    ECSquareMat(const ECSquareMat &rhs);
    ~ECSquareMat();
    
    ECSquareMat &operator=(const ECSquareMat &rhs){
        CopyMatrix(rhs);
        return *this;
    }
    
    int GetDimension() const;
    void SetValAt(int nRow, int nCol, int val);
    int GetValAt(int nRow, int nCol) const;
    ECSquareMat operator+(const ECSquareMat &rhs){
        ECSquareMat res = Add(rhs);
        return res;
    }
    ECSquareMat operator*(const ECSquareMat &rhs){
        ECSquareMat res = Multiply(rhs);
        return res;
    }
    friend std::ostream& operator<<(std::ostream& os, ECSquareMat& a){
        a.Print(os);
        return os;
    }
    
private:
    std::vector<std::vector<int> > listMatEntries;
    void CopyMatrix(const ECSquareMat &rhs);
    void Print(std::ostream& os) const;
    ECSquareMat Add(const ECSquareMat &rhs);
    ECSquareMat Multiply(const ECSquareMat &rhs);
};


#endif

