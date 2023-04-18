# GumroadML

Files:

Candidates.py is the model that generates candidate recommendations, prior to ranking.  This step is necessary in the context of the Youtube recommendation because
of the extremely large number of possible videos to recommend on Youtube.  Similarly for Gumroad, instead of trying to rank the recommendation of every single 
available product to users, generate good candidates and then rank those.  This step embeds a users purchase history, search history, and various persoanal data 
variables specific to each user, location, gender, age, etc.

Rank.py is the model that ranks the candidate products in order of most likely for a user to purchase next.  This uses a large set of parameters than the Candidates model
but does so on a smaller set of products per user.
