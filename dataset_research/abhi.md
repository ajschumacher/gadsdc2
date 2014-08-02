Analyzing Ironman (Triathlon) Data
---
An Ironman Triathlon is one of a series of long-distance triathlon races organized by the World Triathlon Corporation (WTC) consisting of a 2.4-mile swim, a 112-mile bicycle ride and a marathon 26.2-mile run, raced in that order and without a break. It is widely considered one of the most difficult one-day sporting events in the world.

About Dataset
---
[Athlinks.com](http://athlinks.com) is worlds largest race database with over 150,378,596 race results. My analysis for now is centered around Ironman triathlon data which I was able to scrape/clean and persist in a structured database.

Challenges
* No data API
* Not 100% sure about data authenticity
* Flaky website
* Parsing and scraping large dataset
* Gathering race factors like humidity, elevation, temperature

Analysis
---
Dataset I'm playing around consists of athletes with more than 10 ironman races.Each ironman race has race factors associated with it e.g High/low temperature, starting/gross elevation and high/low humidity. In my initial analysis I'm hoping to find co-relation between race factors and athlete's final race time. In other words how race factors affect athlete's performance.If I'm able to find a model that can fit this then I can flip the problem and use the model to predict race timings given certain race factors. This can help athlete know analytically how they will perform in a race given various race factors.

Sample data is hosted on [S3](https://s3.amazonaws.com/datathletics/ironman_40_49_10_plus_races.csv).

    race_results <- read.csv("/Users/akapatkar/Desktop/ironman_40_49_10_plus_races.csv")

    names(race_results)
    [1] "id"   "race_id"              "qualifier_id"        "name"
    [5] "year"                 "age"                  "athlete_id"           "final_time"
    [9] "high_temp"            "low_temp"             "high_humidity"        "low_humidity"
    [13] "starting_elevation"   "gross_elevation_gain"

    summary(race_results$final_time) (in secs)
    Min.    1st Qu.  Median   Mean   3rd Qu.  Max.
    33530   35880    38540   39760   42250   57760


