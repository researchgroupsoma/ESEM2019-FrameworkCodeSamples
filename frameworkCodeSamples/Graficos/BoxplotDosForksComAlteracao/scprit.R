library(effsize)
library(ggplot2)
library(devtools)
library(easyGgplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/Graficos/BoxplotDosForksComAlteracao/metricas.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$ecosystem, levels = c("Android","Spring")), all$forksAhead)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10() +
  geom_boxplot(width=0.6,alpha=0.6) + ggtitle("Number of forks ahead of parent") + xlab("Code Samples") + ylab("Number of forks ahead (log scale)") + 
  annotate("text", x = 1, y = 4, label = "1", size = 6) + annotate("text", x = 2, y = 10, label = "7", size = 6) +
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

  #mediana do spring 7
  #mediana do android 1

p1

ggsave("/home/gabriel/Documentos/Graficos/BoxplotDosForksComAlteracao/forks_ahead.pdf", width = 4.5, height = 4.5)


