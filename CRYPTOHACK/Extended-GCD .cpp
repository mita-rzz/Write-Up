#include <bits/stdc++.h>
using namespace std;
signed main(){
  
  for (int i =1; i <1000000;i++){
    if ( ((32321*i)+1 )%26513==0){
    cout << i <<  ' ' << ((32321*i)+1 )/26513 << '\n';
      break;
    }
  }
}
