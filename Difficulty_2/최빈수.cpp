#include <iostream>
#include <vector>

using namespace std;

int main() {
	int test, cnt, tmp, max_num, max_cnt;
	int arr[1001];
	
	cin >> test;
	for(int i = 1; i <= test; i++)
	{
		cin >> cnt;
		cout << "#" << cnt << " ";
		fill_n(arr, 1001, 0);
		max_num = 0, max_cnt= 0;
		
		for(int j = 1; j <= 1000; j++)
		{
			cin >> tmp;
			arr[tmp] += 1;
		}
		
		for(int j = 1; j <= 1000; j++)
		{
			if(max_cnt <= arr[j])
			{
				max_cnt = arr[j];
				if(max_num < j)
					max_num = j;
			}
			
		}
		cout << max_num << endl;
	}
	return 0;
}
