# getgit
Python script using git api to search through git repos

Maximum results is 100.  Sorts decending by number of stars by default.    

Usage: python3 getgit.py [switches]  

Available switches:

<table>
<tr>
<th>-l or --language 
<th>list the language specified for the repo.  Example: -l python
</tr>
<th>-u or --user     
<th>specify the username of the owner of the repo.  Example -u secnonsense 
</tr>
<th>-s or --stars
<th>only show repos with this number of stars or greater.  Example -s 1000
</tr>
<th>-q or --query
<th>list keywords to search by. Separate multiple keywords with +.  Example -q population+genetics
</tr>
<th>-p or --pushed
<th>look for repos which have been updated since the listed date format YYYY-MM-DD. Example -p 2020-01-01 
</tr>
</table>


