# getgit
Python script using git api to search through git repos

Maximum results is 100.  Sorts decending by number of stars by default.    

Usage: python3 getgit.py [switches]  

Available switches:

-l or --language : list the language specified for the repo.  Example: -l python  
-u or --user     : specify the username of the owner of the repo.  Example -u secnonsense  
-s or --stars    : only show repos with this number of stars or greater.  Example -s 1000  
-q or --query    : list keywords to search by. Separate multiple keywords with +.  Example -q population+genetics  



