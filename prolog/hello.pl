boy(kaushal).
boy(utsav).
girl(simran).
lovesHackathon(X) :-
    girl(X).

loves(vincent,mia).
loves(marsellus,mia).
loves(pumpkin,honey_bunny).
loves(honey_bunny,pumpkin).

jealous(X,Y):- loves(X,Z), loves(Y,Z).
