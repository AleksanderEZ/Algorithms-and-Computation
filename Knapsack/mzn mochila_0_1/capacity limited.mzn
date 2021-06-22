int:n; %numero maximo de items
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

int:m; %numero maximo de items a elegir dentro del conjuto limitation
set of ITEMS: limitation;

%Escribir el código a partir de aquí

var set of ITEMS: taken;

constraint sum(i in taken)(weight[i]) <= capacity;

constraint card(taken intersect limitation) <= m;

solve maximize sum(i in taken)(value[i]);

output [show(taken),"\n",show(sum(i in taken)(value[i]))];
