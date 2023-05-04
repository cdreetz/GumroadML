# GumroadML
-----------------------

GumroadML is a Recommendation system that considers customer purchase history, search history, and various personal attributes to be able to 
predict what product a user is most likely going to purchase next.  Allowing Gumroad to provide recommendations either on a users Discover page 
or product pages that they view.  It is based off of Youtube's Recommendation system just altered to apply for Gumroad's case.

1. Generate Candidates (candidates.py) out of total corpus 
2. Rank the candidates (rank.py)





------------------------
## Files:

Candidates.py is the model that generates candidate recommendations, prior to ranking.  This step is necessary in the context of the Youtube 
recommendation becauseof the extremely large number of possible videos to recommend on Youtube.  Similarly for Gumroad, instead of trying to 
rank the recommendation of every single available product to users, we generate good candidates and then rank those.  This step embeds a users 
purchase history, search history, and various persoanal data variables specific to each user, location, gender, age, etc.

Rank.py is the model that ranks the candidate products in order of most likely for a user to purchase next.  This uses a larger set of parameters 
than the Candidates model but does so on a smaller set of products per user.

Layers.py defines the masked embedding layer and the L2 norm layer to be used
