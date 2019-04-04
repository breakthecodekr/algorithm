#include <iostream>

using namespace std;

int main() {
	int test, M, N, max, tmp;
	int arr[16][16] = {0};
	cin >> test;
	for(int i = 1; i <= test; i ++)
	{
		cin >> N >> M;
		
		max = 0, tmp = 0;
		
		for(int j = 0; j < N; j++)
		{
			fill_n(arr[j], N, 0);
		}
		
		for(int j = 0; j < N; j++)
		{
			for(int k = 0; k < N; k++)
				cin >> arr[j][k];
		}
		
		for(int j = 0; j < N-M+1; j++)
		{
			for(int cnt = 0; cnt < N-M+1; cnt++)
			{
				for(int k = j; k < j+M; k++)
				{
					for(int l = cnt; l < cnt+M; l++)
					{
						tmp += arr[k][l];
					}
				}
				if(max < tmp)
					max = tmp;
				tmp = 0;
			}
		}
		cout << "#" << i << " " << max << endl;
	}
	return 0;
}
