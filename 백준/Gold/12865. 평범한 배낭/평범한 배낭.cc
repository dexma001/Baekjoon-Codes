#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int find(const pair<int, int> item[], int N, int K)
{
	int bag[100'001] = { 0 };

	for (int i = 0; i < N; i++)
	{
		for (int j = K; j > 0; j--)
		{
			if (bag[j] and j + item[i].first <= K)
			{
				bag[j + item[i].first] = max(bag[j] + item[i].second, bag[j + item[i].first]);
			}
		}

		bag[item[i].first] = max(bag[item[i].first], item[i].second);
	}
	int maxVal = 0;
	for (int p = 1; p <= K; p++)
	{
		if (bag[p] > maxVal) {
			maxVal = bag[p];
		}
	}

	return maxVal;
}

int main()
{
	int N, K;
	cin >> N >> K;
	pair<int, int> item[101];

	for (int i = 0; i < N; i++)
	{
		cin >> item[i].first >> item[i].second;
	}

	sort(item, item+N);

	cout << find(item, N, K);

	return 0;
}