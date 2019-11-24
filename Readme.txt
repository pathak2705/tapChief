An implementation of Elastic Search kind of application where paragraphs are indexed accordingly and in case of a word query, list of paragraphs containing that particular word would appear.

Application : -
 
 Instead of manually searching for a query word in each paragraphs, we index each paragraph in the document like 0,1 and so on and we store indexes of each paragraph along with each word. So, next time whenever we need to search for a word in a paragraph, we would just search for the index associated with that word and fetch those paragraphs.

Functions : -
 
 1) clear() - clears the indexed document.

 2) index() - indexes each paragraph in the document and makes a dictionary where each word is mapped along with the paragraph index in which it appears.

 3) search() - takes an input word and fetches top 10 paragraphs containing that word.
  
** I have added frequency of the word in the list too so that the paragraphs which have most appearances of the word in them are fetched first.

How to use : -

-> index Button - It will index all the paragraphs so that words can be searched now (would take some time to build).
 
-> search Button - Would open up a window where you have to select one word to be searched from a list of all words appearing in the document. Submitting that word would open up a window containing top 10 paragraphs containing that particular word in it.

  