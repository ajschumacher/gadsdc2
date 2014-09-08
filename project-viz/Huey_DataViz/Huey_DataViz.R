######## GETTING ERRORS ON SOME LINES, BUT OUTPUT OF IMAGES DOESN'T SEEM TO BE AFFECTED. WILL REVISIT ERRORS. ########

#############
# LearnZillion Survey Analysis
############

#todo:
# for all data, for each bucket of teaching XP, for each subject area:
# InitialReason: most popular initial reasons.  Scatterplot these
# ContinueReason: most popular continue reasons; scatterplot these
# ImportanceOf: most important; scatterplot these
# SatisfactionWith: summary stats (average, 25/75, SD)
# OtherSites: summary stats on level of satisfaction
# capture the self-populated data: "other" explanations, "very unsatisfied" explanation, goals for other sites, other sites used, general info

##########
# Setup
#########
rm(list=ls())

library(ggplot2)

datapath <- "/Users/huey/downloads/Data_All_131209 (xls+)/CSV"
dataframe <- read.csv(paste(datapath,"Sheet_1.csv",sep="/"))

colnames(dataframe)<-c("RespondentID","CollectorID","StartDate","EndDate","IPAddress","EmailAddress","FirstName","LastName","CustomData","Subject","Grade","YearsTeaching","VisitsPerWeek","InitialReason.LearnMore","InitialReason.PlanLesson","InitialReason.FindVideo","InitialReason.FindResource","InitialReason.Other","InitialReason.OtherExplanation","ContinueReason.LearnMore","ContinueReason.PlanLesson","ContinueReason.FindVideo","ContinueReason.FindResource","ContinueReason.Other","ContinueReason.OtherExplanation","ImportanceOf.LessonVideos","ImportanceOf.LessonSlides","ImportanceOf.InteractiveAssessments","ImportanceOf.PrintableAssessments","ImportanceOf.OnlinePractice","ImportanceOf.PracticeWorksheets","ImportanceOf.OtherResourcesForStandards","SatisfactionWith.LessonVideos","SatisfactionWith.LessonSlides","SatisfactionWith.InteractiveAssessments","SatisfactionWith.PrintableAssessments","SatisfactionWith.PracticeSheets","SatisfactionWith.OnlinePractice","SatisfactionWith.OtherResourcesForStandards","VeryUnsatisfiedOrUnsatisfiedExplanation","OtherSites.BetterLesson.Goal","OtherSites.BetterLesson.Satisfaction","OtherSItes.ShareMyLesson.Goal","OtherSites.BrainPOP.Satisfaction","OtherSites.IXL.Goal","OtherSites.IXL.Satisfaction","OtherSites.KhanAcademy.Goals","OtherSites.KhanAcademy.Satisfaction","OtherSItes.ShareMyLesson.Goal","OtherSites.ShareMyLesson.Satisfaction","OtherSites.StudyJams.Goal","OtherSites.StudyJams.Satisfaction","OtherSites.TeachingChannel.Goal","OtherChannel.TeachingChannel.Satisfaction","OtherSites.YouTube.Goal","OtherSites.YouTube.Satisfaction","OtherSites.OpenEnded","AnythingElse.OpenEnded")

#########
# Data Manipulation
########

# define a function to identify the top InitialReason, ContinueReason, ImportanceOf for each observation
defineTops <- function(i){
  InitialReasonTop <- gsub("(.*\\.)","",colnames(dataframe)[grepl("InitialReason.*", colnames(dataframe))][which.min(as.numeric(dataframe[i,colnames(dataframe)[grepl("InitialReason.*", colnames(dataframe))]]))])
  ContinueReasonTop <- gsub("(.*\\.)","",colnames(dataframe)[grepl("ContinueReason.*", colnames(dataframe))][which.min(as.numeric(dataframe[i,colnames(dataframe)[grepl("ContinueReason.*", colnames(dataframe))]]))])
  ImportanceOfTop <- gsub("(.*\\.)","",colnames(dataframe)[grepl("ImportanceOf.*", colnames(dataframe))][which.min(as.numeric(dataframe[i,colnames(dataframe)[grepl("ImportanceOf.*", colnames(dataframe))]]))])
  Tops <- c("InitialReasonTop"=InitialReasonTop,"ContinueReasonTop"=ContinueReasonTop,"ImportanceOfTop"=ImportanceOfTop)
  return(Tops)
}

# create a df of the top InitialReason, ContinueReason, ImportanceOf reason for all observations
AllTops <- NULL
for(i in 1:nrow(dataframe)){
  temp <- defineTops(i)
  AllTops <- rbind(AllTops, temp)
  row.names(AllTops)<-c(1:nrow(AllTops))
}

# bind it back onto the initial dataframe
dataframe<-cbind(dataframe,AllTops)

# Reshape some vars wide to Long.  
dataframelong <- reshape(dataframe,
                    varying = colnames(dataframe)[grepl("((InitialReason\\.)|(ContinueReason\\.))(?!OtherExplanation)",colnames(dataframe),ignore.case=TRUE,perl=TRUE)],
                    timevar = "Initial.Continue.Reason.Resource",
                    direction = "long"); rownames(dataframelong)<-1:nrow(dataframelong); dataframelong<-subset(dataframe,select=-id)

dataframelong <- reshape(dataframelong,
                    varying = colnames(dataframelong)[grepl("ImportanceOf\\.",colnames(dataframelong),ignore.case=TRUE,perl=TRUE)],
                    timevar = "ImportanceOf.Resource",
                    direction = "long"); rownames(dataframelong)<-1:nrow(dataframelong); dataframelong<-subset(dataframelong,select=-id)

# fix the ordering of some factors
dataframelong$YearsTeaching <- ordered(dataframelong$YearsTeaching, levels=c("0-5 years","6-10 years","11+ years"))

################
# GGPLOT section
################
########
# style
########

scale_x_ImportanceOf <- scale_x_continuous(breaks=c(1:7), minor_breaks=NULL, limits=c(1,8), name="Ranking of Importance (1=highest)")
scale_y_ImportanceOf <- scale_y_continuous(labels=NULL, name="Portion of Respondents")
theme_ImportanceOf <- theme(
  panel.grid.minor.x = NULL,
  axis.text.x = element_text(hjust=-4),
  axis.ticks = element_line(size=0)
)

scale_x_Initial.Continue.Reason <- scale_x_continuous(breaks=c(1:5), limits=c(1,6), name="Ranking of Importance (1=highest)")
scale_y_Initial.Continue.Reason <- scale_y_continuous(labels=NULL, name="Portion of Respondents")
theme_Initial.Continue.Reason <- theme(
  panel.grid.minor.x = NULL,
  axis.text.x = element_text(hjust=-5),
  axis.ticks = element_line(size=0)
)

scale_x_whisker_ImportanceOf <-	scale_x_discrete(name="Resource")
scale_y_whisker_ImportanceOf <-	scale_y_continuous(expand=c(0.001,0.001), breaks=c(1,2,3,4,5,6,7), limits = c(0.5,7.5), name="Ranking of Importance (1=highest)")
theme_whisker_ImportanceOf <- theme(
  panel.grid.major=element_line(size=0),
  panel.grid.minor=element_line(size=2, colour="white"),
  axis.text.x = element_text(angle=15, hjust=1)
)


scale_x_whisker_Initial.Continue.Reason <-	scale_x_discrete(name="Reason")
scale_y_whisker_Initial.Continue.Reason <-	scale_y_continuous(expand=c(0.01,0.01), name="Ranking of Importance (1=highest)")
theme_whisker_Initial.Continue.Reason <- theme(
  panel.grid.major=element_line(size=0),
  panel.grid.minor=element_line(size=2, colour="white")
)



#################
# Relative Quants
#################


# relative quantities of Importance of Various Resources
x <- "Importance of LearnZillion Resources"
png(filename=paste(x,".png",sep=""))
ggplot(dataframelong, aes(x=ImportanceOf,fill=ImportanceOf.Resource)) +
  geom_bar(stat="bin", binwidth=1) +
  scale_x_ImportanceOf +
  scale_y_ImportanceOf +
  theme_ImportanceOf + 
  ggtitle(x) +
  scale_fill_discrete(name="Resource")
dev.off()

#relative quantities of Initial Reason
x <- "Initial Reason for using LearnZillion"
png(filename=paste(x,".png",sep=""))
ggplot(dataframelong, aes(x=InitialReason,fill=Initial.Continue.Reason.Resource)) +
  geom_bar(stat="bin", binwidth=1) +
  scale_x_Initial.Continue.Reason +
  scale_y_Initial.Continue.Reason +
  theme_Initial.Continue.Reason +
  ggtitle(x) +
  scale_fill_discrete(name="Resource")
dev.off()

#relative quantities of Continue Reason
x <- "Reason for Continuing to use LearnZillion"
png(filename=paste(x,".png",sep=""))
ggplot(dataframelong, aes(x=ContinueReason,fill=Initial.Continue.Reason.Resource)) +
  geom_bar(stat="bin", binwidth=1) +
  scale_x_Initial.Continue.Reason +
  scale_y_Initial.Continue.Reason +
  theme_Initial.Continue.Reason +
  ggtitle(x) +
  scale_fill_discrete(name="Resource")
dev.off()



##########
# Density
##########

#densityplot for Importance Of
x <- "Density Plot: Importance of LearnZillion Resources, by Subject and Years of Teaching Experience"
png(filename=paste(x,".png",sep=""), width=1200, height=800)
ggplot(dataframelong, aes(x=ImportanceOf.Resource,y=ImportanceOf,colour=Subject)) +
  geom_jitter(alpha=.5) +
  scale_x_whisker_ImportanceOf +
  scale_y_whisker_ImportanceOf +
  theme_whisker_ImportanceOf +
  ggtitle(x) +
  facet_wrap("YearsTeaching") +
  theme(legend.position='top')
dev.off()

#densityplot for Inition Reason
x <- "Density Plot: Initial Reason for using Learnzillion"
png(filename=paste(x,".png",sep=""))
ggplot(dataframelong, aes(x=Initial.Continue.Reason.Resource,y=InitialReason)) +
  geom_jitter(alpha=.4) +
  scale_x_whisker_Initial.Continue.Reason +
  scale_y_whisker_Initial.Continue.Reason +
  theme_whisker_Initial.Continue.Reason +
  ggtitle(x)	
dev.off()


#densityplot for Continue Reason
x <- "Density Plot: Reason for Continuing to use LearnZillion"
png(filename=paste(x,".png",sep=""))
ggplot(dataframelong, aes(x=Initial.Continue.Reason.Resource,y=ContinueReason)) +
  geom_jitter(alpha=.4) +
  scale_x_whisker_Initial.Continue.Reason +
  scale_y_whisker_Initial.Continue.Reason +
  theme_whisker_Initial.Continue.Reason +
  ggtitle(x)	
dev.off()




#######
# Old plots: These do NOT use GGPlot2.  They use R's built-in graphics.
############


# graph
png(filename="InitialReasonTop.png")
barplot(sort(table(dataframe$InitialReasonTop), decreasing=TRUE))
title(main="Top Reasons for Initially Coming to LearnZillion")
dev.off()

png(filename="ContinueReasonTop.png")
barplot(sort(table(dataframe$ContinueReasonTop), decreasing=TRUE))
title(main="Top Reasons for Continuing to Return to LearnZillion")
dev.off()

png(filename="ImportanceOfTop.png")
test <- barplot(sort(table(dataframe$ImportanceOfTop), decreasing=TRUE), axisnames=FALSE)
text(test, par("usr")[3],labels=names(sort(table(dataframe$ImportanceOfTop), decreasing=TRUE)),srt=20, adj=c(1,1),xpd=TRUE, cex=.9)
title(main="Top LearnZillion Resources by Importance to Users")
dev.off()

