% Facts: Different types of food
food(pizza).
food(burger).
food(rice).
food(fruits).

% Rule: John likes all kinds of food
likes(john, X) :- food(X).