# Jamie's Dataset Research


Answers to the questions listed in the GADSDC [readme file](https://github.com/ajschumacher/gadsdc/tree/master/dataset_research) can be found below.



**What are the structure and contents of your dataset? (Number of records, columns, missing values, etc.)** 



The data that I'll be using comes from a project from work that examines whether the percentile rank of grants during peer review actually predicts for grant productivity and impact. Each row represents a de novo grant from the National Institite of Mental Health (NIMH). For each grant, we have an impact score, which tells us how well a particular grant performed during peer review. These impact scores are then converted to percentiles to help correct for differences in scoring behavior across the study sections that reviewed grants. We linked the grants to the publications they produced. 



- Rows: 1757
- Columns: 37

- Missing values: None



**What is the history of your dataset (How was it created?)**



The data was created using administrative databases internal to NIH and Pubmed. 



**Has your dataset been written about? What have others used it for?**

The dataset was created to reproduce a study conducted by the National Heart, Lung, and Blood Institute (NHLBI), but using NIMH data. We are preparing a publication based on an analysis of these data. 



**How do you acquire and load the dataset into  R ? (Include code.)**



```
final_nimh<- read.csv(C:/Users/doylejm/final_nimh.csv)

```

**What are some simple statistics describing the dataset?**



- Mean percentile rank: 11.67

- Mean number of citations: 231

- Human studies: 1043 (59%) 

**Other information**
- What is an "impact score": An impact score is intended to measure, "...the likelihood for the project to exert a sustained, powerful influence on the research field(s) involved." It's based on 5 
individual criteria and on reviews from 3 reviewers. The individual institutes and centers (ICs) do not assign percentiles--instead, much of the peer review system is managed by a third party 
within NIH called the Center for Scientific Review (CSR). The method they use to assign percentiles is not published, but generally they say, that.. "A percentile is the approximate percentage 
of applications that received a better overall impact/priority score from the study section during the past year." 

- More on percentiles: The percentiles are given within study sections. Study sections tend to specialize in certain scientific areas, so grant applications are not randomly assigned. 
The issue here is, since humans are making the determination of what grants go where, it's not entirely clear whether they're actually doing a good job and whether they assign things consistently. 
This is a huge problem since we rely on peer review to help select the most promising science. 

-I'm actually working with NHLBI on a [publication] (http://circres.ahajournals.org/content/early/2014/01/09/CIRCRESAHA.114.302656) (which basically reproduces their study using our data), so I have their code. Thankfully they also use R.
 

