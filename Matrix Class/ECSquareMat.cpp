#include "ECSquareMat.h"
#include <iostream>

using namespace std;

ECSquareMat::ECSquareMat(int nDim){
    for(int i = 0; i < nDim; i++){
        vector<int> v;
        listMatEntries.push_back(v);
        for(int j = 0; j < nDim; j++){
            listMatEntries[i].push_back(0);
        }
    }
}
ECSquareMat::ECSquareMat(const ECSquareMat &rhs){
    // do we have to clear listMatEntries potentially?
    for(auto v : rhs.listMatEntries){
        vector<int> v_add;
        for(int i : v){
            v_add.push_back(i);
        }
        listMatEntries.push_back(v_add);
    }
}
ECSquareMat::~ECSquareMat(){}
void ECSquareMat::CopyMatrix(const ECSquareMat &rhs){
    listMatEntries.clear();
    for(auto v : rhs.listMatEntries){
        vector<int> vec;
        for(int i : v){
            vec.push_back(i);
        }
        listMatEntries.push_back(vec);
    }
}

void ECSquareMat::Print(std::ostream& os) const{
    for(auto v : listMatEntries){
        for(int i : v){
            os << i << " ";
        }
        os << endl;
    }
}

int ECSquareMat::GetDimension() const{
    return listMatEntries.size();
}

void ECSquareMat::SetValAt(int nRow, int nCol, int val){
    listMatEntries[nRow][nCol] = val;
}

int ECSquareMat::GetValAt(int nRow, int nCol) const{
    return listMatEntries[nRow][nCol];
}

ECSquareMat ECSquareMat::Add(const ECSquareMat &rhs){
    if(GetDimension() != rhs.GetDimension()){
        throw "Incompatible Matrices";
    }
    ECSquareMat res(GetDimension());
    for(int i = 0; i < GetDimension(); i++){
        for(int j = 0; j < GetDimension(); j++){
            int val = GetValAt(i, j) + rhs.GetValAt(i, j);
            res.SetValAt(i, j, val);
        }
    }
    return res;
}
ECSquareMat ECSquareMat::Multiply(const ECSquareMat &rhs){
    if(GetDimension() != rhs.GetDimension()){
        throw "Incompatible Matrices";
    }
    int n = GetDimension();
    ECSquareMat res(n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int val = res.GetValAt(i, j);
            for(int k = 0; k < n; k++){
                val += GetValAt(i, k) * rhs.GetValAt(k, j);
            }
            res.SetValAt(i, j, val);
        }
    }
    return res;
}