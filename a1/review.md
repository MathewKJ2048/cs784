# Word Acquisition in Neural Language Models - Review

## Summary

- The paper aims to compare the rate aquisition of words between human children and LSTMs, BERT and GPT-2.

- The age of aquisition is defined as "production of word by child, as reported by parent, with mean time when 50% of children produce a word" for children and "point where surprisal is midway between baseline and minimum surprisal" for language models. Alternate definitions were considered and rejected on various grounds.

- Log frequency, MLU, n-chars, concreteness and lexical class were used as predictors for age of acquisition. When correlations were computed, no predictor had a VIF over 5. Moderate correlations between log-frequencies and concreteness were observed, which are consistent with existing literature on child-directed speech.

- Children were affected negatively by word length (which didn't affect LMs), log-frequency was a better predictor for LMs than for children, children performed better than LMs at learning short words with high polysemy (possibly because of ease of pronunciation), and children were biased in favour of nouns compared to LMs (possibly due to the presence of sensorimotor cues).

- When analysing unigram frequencies, an initial period of overfitting to raw token frequencies was observed, before the LMs diverged away from the unigram distribution. This was tested by computing the KL divergence between the unigram distribution and the distribution of model predictions at various stages of the model's training.

- When analysing bigram frequencies via the same method, it was observed that the KL divergence decreased as the models converged on the bigram distribution, even after the point of diverging from the unigram distribution. This was observed even in models with no architectural reasons to overfit to bigram distributions (like BERT and GPT-2).

- The paper discusses relevant literature in distributional learning among people, distributional models and non-distributional learning, and concludes that multi-modal and non-distibutional models could exhibit learning more similar to humans than distributional models.

## Strengths

- The paper is able to link its results to existing literature in both human language research and LM research, which suggests that it is good interdisciplinary work.

- The five selected predictors may not have been independent of each other (for instance, MLU and n-chars are heavily correlated to each other, with n-chars moderately corelated with log-frequency). The paper addressed this concern by using the VIF.

- The review of alternative definitions of age of acquisition and the substantial reasons for rejecting them make the methodology of the paper seem more robust, since the authors pre-empted obvious lines of criticism by readers.


## Weaknesses

- Since the distribution of word inputs given to human children are different from the general distribution of words in the language (for instance, a motivated parent may use words such as "mommy" or "daddy" at disproprtionately high rates with their child), an apples-to-apples comparison between child word acquisition and LM word acquisition would need the distribution of words fed into the LM to match that of those fed to the children.

- The comparison of learning processes between LMs and children is confounded by the fact that the LM is given input passively, while a (good) parent tailors the interactions they have with their children depending on the words the child has already said. The presence of feedback loops in such interactions could change the way children learn, compared to LMs.

- The reliance on parental reporting for word acquisition could bias the results, since parents are more likely to recognize common words as valid when uttered. 

- Furthermore, parents have specific motivations in making the child learn particular words, since, having knowledge of the language's grammar and semantics, the parents recognize that usage of certain words requires the knowledge of other words (for instance, using a conjunction usually requires at least the usage of two nouns, such as "A and B").

## Comments, Suggestions and Questions

- To account for the different distributions in the training data, a possible solution would be to use the parent section of the CHILDE dataset as the training corpus for the LMs. This could remove the effect of different distributions affecting learning rates for different words.

- The paper compares number of steps for the LM with the time taken by the human child. This is a comparison of two quantities of different dimensions. How was the time measurement for children normalized to make it a quantity comparable to the number of steps taken by the LM? Does it make assumptions about collinearlity between the time taken with children and the number of steps?

- As an addendum to the earlier question, the rate of input of words is constant at each step for LMs, but not so with children - presumably, children who talk more tend to be talked at more. What would the results look like if they were compared on the basis of number of words input rather than time?

- The speculation at the end of section 5 about unigram and bigram learning being a natural consequence of distributional learning could benefit from further work, if no such work exists. If such work exists, the paper could benefit from linking to the aforementioned work.

- When discussing the failure of the alternate method for determining acquisition age, the paper can benefit from making stringer claims about specific cases of failure. For instanc, it can show the approximate percentage of words where the asymptotes fail to approximate surprisal values accurately.