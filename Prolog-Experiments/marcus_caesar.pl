% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).
tried_to_assassinate(marcus, caesar).

% Rules
roman(X) :-
    pompeian(X).

person(X) :-
    man(X).

% Marcus hates Caesar because he tried to assassinate him
hate(X, Y) :-
    tried_to_assassinate(X, Y).

% A person is loyal only if they do not hate
loyal(X, Y) :-
    person(X),
    \+ hate(X, Y).

% Loyal people love Caesar
love(X, caesar) :-
    loyal(X, caesar).