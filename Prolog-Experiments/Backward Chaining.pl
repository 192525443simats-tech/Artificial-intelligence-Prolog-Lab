parent(ram,rahul).
parent(rahul,anu).

ancestor(X,Y):-
    parent(X,Y).

ancestor(X,Y):-
    parent(X,Z),
    ancestor(Z,Y).