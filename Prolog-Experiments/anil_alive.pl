% Anil eats peanuts
eats(anil, peanuts).

% Harry eats everything that Anil eats
eats(harry, X) :- eats(anil, X).