YYY Election Audit
The Coloroda Board of Elections is running an audit of one of its Congressional districts.  The firm selected ran this project as a pilot attempt at automating election tabulation.  Presented with a data file with rows listing the candidate selected and the county in which each ballot cast was cast, we wrote a python script that tallied the votes, sorted them by candidate and evaluated those results.  The same script also performed the actions to see how the votes were distributed across counties. 

Election-Audit Results: 
- There were 369,711 votes cast in the election.
- Denver county had the largest number of votes, with 306,605.
- Jefferson county had 38,855 votes and Arapahoe county had 24801.
- The three candidates received the following votes respectively:
  - Charles Casper Stockham: 85,213 (23.1%)
  - Diana DeGette': 272,892 (73.8%)
  - Raymon Anthony Doane: 11,606 (3.1%)
- Diane DeGetter ran away with the contest, receiving 272,892 votes, almost 74%.

Summary: 
Automating verifies results more quickly than hand counting!  It is also lesss prone to error, assuming the data file presented is correct.  Should the Commission wish, the script presented here could easily be used for any Congressional district for which the data are available.  In addition it could easily be adapted to additional purposes (to "add functionality").  It could, for example, be augmented to provide vote counts by candidate in each county, or, conversely, the results in each county for each candidate.  With additional data, for example census figures on population, one could develop a routine for determining what percent of eligible voters turned out in the election.  Looking at data from previous elections could also provide a sense of how turnout is trending and how it is effected by other electoral variables (e.g., whether there is a Presidential election in the same year).
