# getgit
Python script using git api to search through git repos

Maximum results is 100.  Sorts decending by number of stars by default.    

Usage: python3 getgit.py [switches]  

Available switches:

|Switch|Usage|
|:--|:--|
|-l --language |List the language specified for the repo.  Example: -l python|
|-u  --user |Specify the username of the owner of the repo.  Example -u secnonsense| 
|-s  --stars|Only show repos with this number of stars or greater.  Example -s 1000|
|-q  --query|List keywords to search by. Separate multiple keywords with +.  Example -q population+genetics|
|-p  --pushed|Look for repos which have been updated since the listed date format YYYY-MM-DD. Example -p 2020-01-01 |



