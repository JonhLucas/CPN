#include <stdio.h>
#include <math.h>
void merge(int a[], int begin, int middle, int end)
{
	int size1 = middle - begin;
	int size2 = end - middle;
	int a1[size1], a2[size2], i, j, k;
	for (i = 0; i <= size1; i++)
	{
		a1[i] = a[begin+i];
	}
	for (i = 1; i <= size2; i++)
	{
		a2[i] = a[middle + i];
		printf("*%d", a2[i]);
	}
	j = 0;
	k = 0;
	for (i = 1; i <= size2; i++)
	{
		printf("-%d", a2[i]);
	}
	printf("\n");
	for (i = begin; i < end; i++)
	{
		if (a1[j] <= a2[k])
		{
			a[i] = a1[j];
			j = j + 1;
		}
		else
		{
			a[i] = a2[k];
			k = k + 1;
		}
	}
}
void invertion_count(int a[], int begin, int end)
{
	int middle;
	if (begin < end)
	{
		middle = (end+begin)/2;
		invertion_count(a, begin, middle);
		invertion_count(a, middle+1, end);
		merge(a, begin, middle, end);
	}
}
int main(int argc, char const *argv[])
{
	int x;
	int i, size;
	scanf("%d", &size);
	int a[size];
	for ( i = 0; i < size; i++)
	{
		scanf("%d", &a[i]);
	}
	invertion_count(a, 0, size-1);
	for (i = 0; i < size; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}