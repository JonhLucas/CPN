#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<stdbool.h>
double search(double peso, double d[], double p[], int n, double value, double previous)
{
	//printf("%.16lf\n", value);
	int i;
	double np = peso + value;
	for (i = 0; i < n; ++i)
	{
		np -= np / d[i];
	}
	for (i = 0; i < n; ++i)
	{
		np -= np / p[i];
	}
	double delta = (previous-value)/2;
	if (delta < 0.000000001)
	{
		return value;
	}
	if (np > peso)
	{
		return search(peso, d, p, n, value-delta, value);
	}
	else if (np < peso)
	{
		if (value+delta >= 1000000000)
		{
			return 0;
		}
		return search(peso, d, p, n, value + delta, previous);
	}
	else
	{
		return value;
	}
}
int main() {
	int n, i, j = 100;
	double  peso;
	scanf("%d%lf", &n, &peso);
	double decolagem[n], pouso[n], max = 500000000, resultado;
	bool calculo = 1;
	for (i = 0; i < n; ++i)
	{
		scanf("%lf", &decolagem[i]);
		if (decolagem[i] == 1)
		{
			calculo = 0;
		}
	}
	for (i = 0; i < n; ++i)
	{
		scanf("%lf", &pouso[i]);
		if (pouso[i] == 1)
		{
			calculo = 0;
		}
	}
	if (calculo)
	{
		resultado = search(peso, decolagem, pouso, n, max, 2*max);
		if (resultado)
		{
			printf("%.2lf\n", resultado);
		}
		else
		{
			printf("-1\n");
		}
		
	}
	else
	{
		printf("-1\n");
	}
	return 0;
}