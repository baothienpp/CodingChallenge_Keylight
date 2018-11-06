# CodingChallenge_Keylight

The API will fetch a list of github repositories in the last 7 days and sum all the stars in the list. It has following end points:
```
/size/<int> : define the maximum size of analyzed repositories
E.g : 0.0.0.0:80/size/50 will return a list with maximum 50 repository

/star/<int> : define the minimum star for a repository
E.g : 0.0.0.0:80/star/100 will return respositories with minimum 100 stars

Combination:
/size/<int>/star/<int> 
```
