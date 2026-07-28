disease(fever,viral_fever).
disease(cough,cold).
disease(headache,migraine).
disease(chest_pain,heart_problem).

diagnose(Symptom,Disease):-
    disease(Symptom,Disease).