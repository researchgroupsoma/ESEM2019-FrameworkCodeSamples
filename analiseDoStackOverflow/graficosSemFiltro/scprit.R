library(effsize)
library(ggplot2)
library(forcats)

all=read.csv("QueryResultsNoFilter - QueryResults.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$creationYear)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Creation Year") + xlab("Code Samples") + ylab("Date") + 
  annotate("text", x = 1, y = 2016.5, label = "2017", size = 6) + 
  annotate("text", x = 2, y = 2016.5, label = "2016", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("creationDate.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$Score + 0.1)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Post score") + xlab("Code Samples") + ylab("Score") + 
  annotate("text", x = 1, y = 0.8, label = "1", size = 6) + 
  annotate("text", x = 2, y = 0.8, label = "1", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("score.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$ViewCount)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of views") + xlab("Code Samples") + ylab("Views") + 
  annotate("text", x = 1, y = 200, label = "347", size = 6) + 
  annotate("text", x = 2, y = 500, label = "623", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

#mediana 347
#mediana 623

p1

ggsave("views.pdf", width = 4.5, height = 4.5)



p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$CommentCount + 0.1)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of Comments") + xlab("Code Samples") + ylab("Comments") + 
  annotate("text", x = 1, y = 0.2, label = "1", size = 6) + 
  annotate("text", x = 2, y = 0.2, label = "1", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("comments.pdf", width = 4.5, height = 4.5)
