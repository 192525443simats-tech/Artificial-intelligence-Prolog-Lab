% Student Database
student(varshi).
student(rahul).
student(ananya).

% Teacher Database
teacher(ramesh).
teacher(priya).
teacher(suresh).

% Subject Codes
subject(cs101).
subject(cs102).
subject(cs103).

% Teacher teaches Subject
teaches(ramesh, cs101).
teaches(priya, cs102).
teaches(suresh, cs103).

% Student studies Subject
studies(varshi, cs101).
studies(rahul, cs102).
studies(ananya, cs103).

% Rule to find a student's teacher
student_teacher(Student, Teacher) :-
    studies(Student, Subject),
    teaches(Teacher, Subject).