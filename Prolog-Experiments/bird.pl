% Birds
bird(parrot).
bird(sparrow).
bird(peacock).
bird(penguin).
bird(ostrich).

% Birds that cannot fly
cannot_fly(penguin).
cannot_fly(ostrich).

% Rule: A bird can fly if it is a bird and cannot_fly is false
can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).