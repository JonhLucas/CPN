#include <stdio.h>
#include <stdlib.h>
void build_tree(int a[], int max[], int left, int right, int index)
{
	if ((right - left) < 2)
	{
		max[index] = left;
		return;
	}
	int middle = (left+right)/2;
	build_tree(a, max, left, middle, index*2);
	build_tree(a, max, middle, right, index*2 + 1);
	if (a[max[index * 2]] >= a[max[index * 2 + 1]])
	{
		max[index] = max[index * 2];
	}
	else
	{
		max[index] = max[index * 2 + 1];
	}
}

int get_max(int left, int right, int begin, int end, int index, int max[], int a[])
{
	if (left <= begin && right >= end)
	{
		return max[index];
	}
	if (end <= left || begin >= right)
	{
		return -1;
	}
	int middle = (begin + end) / 2, i1, i2;
	i1 = get_max(left, right, begin, middle, index * 2, max, a);
	i2 = get_max(left, right, middle, end, index * 2 + 1, max, a);
	if (i1 == -1)
	{
		return i2;
	}
	else if (i2 == -1)
	{
		return i1;
	}
	else
	{
		if (a[i1] >= a[i2])
		{
			return i1;
		}
		else
		{
			return i2;
		}
	}
}

int main(int argc, char const *argv[])
{
	int x, y, i, j, k, m, n;
	scanf("%d%d", &x, &y);
	while(x != 0 && y != 0)
	{
		j = 1;
		k = 0;
		int a[x + 1];
		int tree[x * 4 + 1];
		for (i = 0; i < x * 4 + 1; i++)
		{
			tree[i] = 0;
		}
		char b[x + 1];
		getchar();
		scanf("%s", b);
		for (i = 0; i < x; i++)
		{
			a[i+1] = b[i] - 48;		
		}
		build_tree(a, tree, 1, x + 1, 1);
		for (k = 0, n = 0; k < x-y; k++)
		{
			m = get_max(j, y+2+n, 1, x + 1, 1, tree, a);
			printf("%d %d %d %d\n", a[m], m, j, y+2+n);
			j = m + 1;
			if (x-y+2+n <= x)
			{
				n++;
			}
			else
			{
				while(k < x-y-1)
				{
					printf("%d\n", a[j]);
					k++;
					j++;
				}
				k = x-y;
			}
		}
		printf("\n");
		scanf("%d%d", &x, &y);
	}
	return 0;
}
