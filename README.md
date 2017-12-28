# Amazon Reviews: Linguistics Analysis
Using a psycholinguistics database, this program scores over two million Amazon reviews based on several psycholinguistics factors. The program requires an MRC psycholinguistics database and a CSV file containing all of the reviews. 

## How it works
The given reviews contain many common words that we do not want to analyze -- known as stop words -- so we must first remove those before proceeding. 

Once the stop words have been dealt with, I moved onto the MRC database. One key insight is that the database largely consists of lemmas of words (e.g., believe is the lemma for believing). Because of this limitation, I also lemmatize each word in the review. The result of these two steps is a list containing all lemmatized words, excluding all stop words. 

With this reduced review, we can now look up each word in the database to retrieve its scores and add them to the review's total scores. To reduce lookup times, I count the frequencies of each word in the reduced review and multiply the score for word by its frequency. 

Finally, I append the review's scores to the row in the output CSV. 

## Resources
Information regarding the database can be found [here](http://websites.psychology.uwa.edu.au/school/MRCDatabase/uwa_mrc.htm).

## Tests
The test directory contains unit tests for small examples (e.g., a small MRC-esque database with a small sample size of reviews). Run these in the terminal to verify the desired behavior.

To determine the expected behavior, I manually stepped through the different processes (e.g., importing the MRC database correctly, scoring a review, etc) and recorded the results.

# Contact
landon.baxter@colorado.edu

