## PUI2016_tw1574
## HW5
For this homework (and class) I was out of town, so could not work with anyone in-person. I referenced the work of Dana Karwas (dlk253@nyu.edu), Bailey Griswold (bg1672@nyu.edu), Christian O Rosado (cor215@nyu.edu), and Jonathan A Toy (jt2276@nyu.edu) for Assignments 1 & 2. For Assignment 3, I referenced the work of Dana Karwas (dlk253@nyu.edu).


### Assignment 1: 

```
Test whether a gaussian model N($\mu$, $\sigma$) for the age distribution of citibike drivers is a sensible model, or if you can find a better fit with another distribution.

Use 2 tests: KS, AD, KL, chisq (even though we have not talked about it in detail yet) to do this.

Test at the Normal and a least one other distributions (e.g. Poisson, or Binomial, or Chisq, Lognormal.......)

No skeleton: you are on your own!

Extra credit: Divide your sample geographically: by Borrow + split Manhattan in an Uptown and a Downtown sample (use your discretion to do so, but ZIP code is a good idea) and see if you notice any differences in how the age distribution can be modeled.
```

### Assignment 2: 

```
You may know that it is estimated that women earn about 78% of men in the same job position. You will test if it is true on real income data, and turn your model into a prediction: if you get hired at a certain stipend as a men, what should you expect to make as a woman? Follow the skeleton notebook

Your notebook must:

have all celled filled in as indicated

properly organize the data

plot the scatter matrix

plot the data (female vs male income) as directed

do and plot a linear regression to the data, only Total Median Income and median income by category

compare the linear regressions

have predictions at the end of a salaty for a female, given the corresponding male salary
```

### Assignment 3: 

```
Formulate the Null hypothesis in words and in formulae for the 4 experiments below:

Do diets help lose more fat than the exercise?
Experimental setup: you have a test and a control sample.

Do American trust the president?
POLL RESULTS: On May 16, 1994, Newsweek reported the results of a public opinion poll that asked: “From everything you know about Bill Clinton, does he have the honesty and integrity you expect in a president?” (p. 23). Poll surveyed 518 adults and 233, or 0.45 of them answered yes.

Effectiveness of nicotine patches to quit smoking.
Experimental setup: measure cessation rates for smokers randomly assigned to use a nicotine patch versus a placebo patch.

Quantify the danger of smoking for pregnant women.
Experimemtal setup: measure IQ of children at ages 1, 2, 3, and 4 years of age.
```
#
### Do diets help lose more fat than the exercise? Experimental setup: you have a test and a control sample.
#
#### Null Hypothesis: The % of fat lost in adults who dieted during the study period is lower than those who exercised during the same period
#
#### Control sample = % of fat lost by exercise over study period (%fat_exercise)
#
#### Test sample = % of fat lost by dieting over study period (%fat_diet)
#
#### H0 = %fat_diet < %fat_exercise
#
#### Ha = %fat_diet >= %fat_exercise
# 
# 
### Do American trust the president? POLL RESULTS: On May 16, 1994, Newsweek reported the results of a public opinion poll that asked: “From everything you know about Bill Clinton, does he have the honesty and integrity you expect in a president?” (p. 23). Poll surveyed 518 adults and 233, or 0.45 of them answered yes.
#
#### Null Hypothesis: The percentage of 'yes' responses is less than or equal to 'no' response, within a significance of 5%.
#
#### H0 = %yes <= %no
#
#### Ha = %yes > %no
#
#
### Effectiveness of nicotine patches to quit smoking. Experimental setup: measure cessation rates for smokers randomly assigned to use a nicotine patch versus a placebo patch.
#
#### Null Hypothesis: The percentage of cessation rates of former smokers that used the nicotine patch to quit smoking is the same or lower for candidates who participated in the placebo patch program as for the control group.
#
#### Control sample = % of cessation for people using placebo patch (%CR_placebo)
#
#### Test sample = % of cessation for people using nicotine patch (%CR_nicotine)
#
#### H0: CR_nicotine <= CR_placebo
#
#### Ha: CR_nicotine > CR_placebo
# 
#
### Quantify the danger of smoking for pregnant women. Experimemtal setup: measure IQ of children at ages 1, 2, 3, and 4 years of age.
#
#### Null Hypothesis: The IQ of children measured at ages 1, 2, 3, and 4 years is the same or higher than the IQ of children who had mothers that smoked during pregnancy as for the control group.
#
#### Control sample 1 = IQ of children age 1 who had mothers who smoked (IQ_smoke_1)
#### Control sample 2 = IQ of children age 2 who had mothers who smoked (IQ_smoke_2)
#### Control sample 3 = IQ of children age 3 who had mothers who smoked (IQ_smoke_3)
#### Control sample 4 = IQ of children age 4 who had mothers who smoked (IQ_smoke_4)
#
#### Test sample 1 = IQ of children age 1 who had mothers who did not smoke (IQ_non_1)
#### Test sample 2 = IQ of children age 2 who had mothers who did not smoke (IQ_non_2)
#### Test sample 3 = IQ of children age 3 who had mothers who did not smoke (IQ_non_3)
#### Test sample 4 = IQ of children age 4 who had mothers who did not smoke (IQ_non_4)
#
#### H0_1: IQ_non_1 >= IQ_smoke_1 
#### H0_2: IQ_non_2 >= IQ_smoke_2
#### H0_3: IQ_non_3 >= IQ_smoke_3
#### H0_4: IQ_non_4 >= IQ_smoke_4 
#
#
#### Ha_1: IQ_non_1 < IQ_smoke_1 
#### Ha_2: IQ_non_2 < IQ_smoke_2
#### Ha_3: IQ_non_3 < IQ_smoke_3
#### Ha_4: IQ_non_4 < IQ_smoke_4 
