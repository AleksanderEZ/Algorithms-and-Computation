int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

%Escribir el código a partir de aquí
array[1..n] of var 0..1: taken;

constraint sum(i in ITEMS)(weight[i] * taken[i]) <= capacity;

solve maximize sum(i in ITEMS)(taken[i]*value[i]);
output [show(taken), "\n"];
output [show(sum(i in ITEMS)(taken[i]*value[i])), "\n"];