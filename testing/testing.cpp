#include <iostream>

using namespace std;

int main(){
	int x = 0;
	cin >> x;
	cout << x << endl;
	if(x == 4){
		cout << "Success!" << endl;
		return 0;
	}
	else{
		cout << "Failure" << endl;
		return 1;
	}	
}
