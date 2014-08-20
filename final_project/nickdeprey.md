## Elevator Pitch - Nick DePrey
With NPR One, we are looking for ways to personalize the experience for every listener.  Users give us signals as to what their preferences are by "rating" individual audio stories.  Ratings include only "complete" "skip" "mark interesting" "share" "start" (which ironically means you ended your listening session on that piece).  

I want to prove or disprove the ability to predict what rating a user will assign to individual audio stories. 

1) Develop a series of algorithms that predict a rating for a user based on previous listening history for that individual user, how others have rated the same audio piece, and other audio metadata.  
2) Test algorithms on a training set to optimize and tune.  
3) With a tuned algorithm, determine which types of audio stories are most likely to be predictable by the machine
4) Apply the best algorithm to a test set of (still historical) data but blinded to the actual rating, measure the accuracy.  
5) Intuit the value we would provide to listeners by implementing this algorithm. If we could swap out a piece of audio that we predict you won't like with something we predict to you, what effect would this have on total listening time and user retention?
6) Develop a proposed implementation method and make the case to the product owner (Jeremy) for why we should implement.

