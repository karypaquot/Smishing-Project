#include <iostream>
#include <string>
#include <cmath>

using namespace std;



string BinaryReversal(string str) {
  int num = stoi(str);
  string binary = "";

  // Convert to binary
  while (num > 0) {
    binary = to_string(num % 2) + binary;
    num /= 2;
  }

  // Pad with zeroes to the nearest N*8 bits
  int len = binary.length();
  int pad = (len % 8 == 0) ? 0 : 8 - len % 8;
  for (int i = 0; i < pad; i++) {
    binary = "0" + binary;
  }

  // Reverse the binary string
  int left = 0, right = binary.length() - 1;
  while (left < right) {
    swap(binary[left], binary[right]);
    left++;
    right--;
  }

  // Convert back to decimal
  int decimal = 0;
  for (int i = 0; i < binary.length(); i++) {
    if (binary[i] == '1') {
      decimal += pow(2, i);
    }
  }

  return to_string(decimal);
}

int main(void) { 
  cout << BinaryReversal("4567") << endl;
  cout << BinaryReversal("213") << endl;
  return 0;
}
