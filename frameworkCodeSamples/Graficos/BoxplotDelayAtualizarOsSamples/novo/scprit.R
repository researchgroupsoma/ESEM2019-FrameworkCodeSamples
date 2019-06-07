library(effsize)
library(ggplot2)
library(devtools)
library(easyGgplot2)
library(forcats)

all=read.csv("versoes.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$framework, levels = c("Android", "Spring")), all$delay+0.1)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10() +
  geom_boxplot(width=0.6,alpha=0.6) + ggtitle("Samples delay to update") + xlab("") + ylab("Delay in days (log scale)") +
  annotate("text", x = 1, y = 45, label = "50", size = 4) + annotate("text", x = 2, y = 0.14, label = "0", size = 4) +
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

#mediana do android 50
#mediana do spring 0

p1

ggsave("delay_samples2.pdf", width = 4.5, height = 4.5)
