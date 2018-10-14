:- discontiguous male/1, female/1, parent/2.
male(sagar).
male(raaj).
male(harsh).
male(vishal).
male(murli).
female(laxmi).
female(durga).
female(monica).
female(aarushi).
female(aditi).
male(aman).
male(god).
female(god).

parent(vishal,raaj).
parent(vishal,harsh).
parent(vishal,laxmi).
parent(durga,raaj).
parent(durga,harsh).
parent(durga,laxmi).
parent(murli,vishal).
parent(aarushi,vishal).
parent(monica,durga).
parent(monica,sagar).
parent(aditi,monica).
parent(raaj,aman).

male(mishall).
male(abid).
parent(mishallsr,mishall).
parent(mishallsr,abid).

american(laxmi).
american(X) :-  ancestor(X,laxmi).
american(X) :- ancestor(laxmi,X).
relation(X,Y) :- ancestor(A,X), ancestor(A,Y).

father(X,Y) :- male(X),parent(X,Y).
mother(X,Y) :- female(X),parent(X,Y).
son(X,Y) :- male(X),parent(Y,X).
daughter(X,Y) :- female(X),parent(Y,X).
grandfather(X,Y) :- male(X),parent(X,Somebody),parent(Somebody,Y).
sister(X,Y) :- female(X),parent(Par,X),parent(Par,Y), X \= Y.
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Somebody),ancestor(Somebody,Y).
brother(X,Y) :-  male(X),parent(Somebody,X),parent(Somebody,Y), X \= Y.
