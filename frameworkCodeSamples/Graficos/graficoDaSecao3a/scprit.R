library(effsize)
library(ggplot2)
library(forcats)

all=read.csv("planilha.csv", sep=",",header=T)

#stars

p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android", "Spring")), all$stargazers)) + 
  scale_y_log10() +
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of Stars") + xlab("Code Samples") + ylab("Number of Stars (log scale)") + 
  annotate("text", x = 1, y = 120, label = "95", size = 8) + annotate("text", x = 2, y = 30, label = "45", size = 8) +
  theme(plot.title=element_text(size=24,face="bold") ,axis.title=element_text(size=20),axis.text=element_text(size=18))

p1

ggsave("stars.pdf", width = 4.5, height = 4.5)

#Commits


p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android", "Spring")), all$commits)) + 
  scale_y_log10() +
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of Commits") + xlab("Code Samples") + ylab("Number of Commits (log scale)") + 
  annotate("text", x = 1, y = 20, label = "24", size = 8) + annotate("text", x = 2, y = 160, label = "137", size = 8) +
  theme(plot.title=element_text(size=24,face="bold") ,axis.title=element_text(size=20),axis.text=element_text(size=18))

p1

ggsave("commits.pdf", width = 4.5, height = 4.5)


#Files

p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android", "Spring")), all$files)) + 
  scale_y_log10() +
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of Files") + xlab("Code Samples") + ylab("Number of Files (log scale)") + 
  annotate("text", x = 1, y = 60, label = "47", size = 8) + annotate("text", x = 2, y = 30, label = "27", size = 8) +
  theme(plot.title=element_text(size=24,face="bold") ,axis.title=element_text(size=20),axis.text=element_text(size=18))

p1

ggsave("files.pdf", width = 4.5, height = 4.5)

