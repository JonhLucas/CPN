#include <stdio.h>
#include <string.h>
#include <math.h>
void segment_tree(int a[], int size)
{

}
int build_tree(int a[], int index, int left, int right, int st[])
{
	if (left == right)
	{
		st[index] = a[left];
		//printf("folha: %d %d\n", a[left], index);
		return a[left];
	}
	int middle = (left+right)/2;
	//printf("%d %d %d meio: %d\n", left, right, index, middle);
	int se = build_tree(a, 2*index + 1, left, middle, st),
	 sd = build_tree(a, 2*(index+1), middle+1, right, st);
	 if (se > sd)
	 {
	 	st[index] = se;
	 }
	 else
	 {
	 	st[index] = sd;
	 }
	 return st[index];
}
int main(int argc, char const *argv[])
{
	int size;
	scanf("%d", &size);
	int height[size], i, tree[size*4];
	double h = (double) size, k = 17.5;
	for ( i = 0; i < size; i++)
	{
		scanf("%d", &height[i]);
	}
	build_tree(height, 0, 0, size-1, tree);
	tree[3*size-1] = 1000000;
	for (i = 0; i < 3*size; i++)
	{
		printf("%d-%d ", tree[i], i);
	}
	printf("\n");
	k = log(56);
	printf("%2f\n", k);
	return 0;
}