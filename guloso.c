#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<stdbool.h>
int min(int a,int b)
{
	return a < b? a : b;
}
void build(int a[], int min_tree[], int left, int right, int index)
{
	if ((right - left) < 2)
	{
		min_tree[index] = left;
		return;
	}
	int middle = (left+right)/2;
	build(a, min_tree, left, middle, index*2);
	build(a, min_tree, middle, right, index*2 + 1);
	if (a[min_tree[index*2]] < a[min_tree[index*2+1]])
	{
		min_tree[index] = min_tree[index*2];
	}
	else
	{
		min_tree[index] = min_tree[index*2+1];
	}
}
int get_min(int left, int right, int begin, int end, int index, int minn[])
{
	if (left <= begin && right >= end)
	{
		return minn[index];
	}
	if (end <= left || begin >= right)
	{
		return 100000;
	}
	int middle = (begin+end)/2;
	int o = get_min(left, right, begin, middle, index*2, minn);
	int p = get_min(left, right, middle, end, index*2+1, minn);
	return min(o, p);

}
void update(int index, int minn[])
{
	int parent = index/2;
	minn[parent] = min(minn[parent*2], minn[parent*2 + 1]);
	if (parent > 0)
	{
		update(parent, minn);
	}
}
void modify(int pos, int value, int index, int left, int right, int minn[], int a[])
{
	minn[index] = min(value, minn[index]);
	if ((right - left) < 2)
	{
		minn[index] = value;
		update(index, minn);
		a[pos] = value;
		return;
	}
	int middle = (left+right)/2;
	if (pos < middle)
	{
		modify(pos, value, index * 2, left, middle, minn, a);
	}
	else
	{
		modify(pos, value, index * 2 + 1, middle, right, minn, a);
	}
}
int main(int argc, char const *argv[])
{
	int size, i;
	scanf("%d", &size);
	int begin[size+1], end[size];
	int tree[4*size], e_tree[4*size];
	for (i = 1; i <= size; i++)
	{
		scanf("%d%d", &begin[i], &end[i]);
	}
	for (i = 1; i <= size; i++)
	{
		printf("%d %d\n", begin[i], end[i]);
	}
	for (i = 1; i <= 4*size ; ++i)
	{
		tree[i] = 0;
		e_tree[i] = 0;
	}
	build(begin, tree, 1, size+1, 1);
	for (i = 1; i <= 4*size ; ++i)
	{
		printf("%d ", tree[i]);
	}
	printf("\n");
	printf("%d\n", get_min(5+1, size + 1, 1, size + 1, 1, tree));
	return 0;
}