eats(anil, peanuts).
alive(anil).

food(X) :- eats(_, X), alive(_).