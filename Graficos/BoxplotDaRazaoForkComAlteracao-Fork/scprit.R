library(effsize)
library(ggplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/Graficos/BoxplotDaRazaoForkComAlteracao-Fork/metricas.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$razao100)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  #scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative Ahead Forks") + xlab("Code Samples") + ylab("Percent of Ahead Forks") + 
  annotate("text", x = 1, y = 3, label = "2", size = 6) + 
  annotate("text", x = 2, y = 13, label = "12", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

#medianaSpring	medianaAndroid
#12	             2


p1

ggsave("/home/gabriel/Documentos/Graficos/BoxplotDaRazaoForkComAlteracao-Fork/razao.pdf", width = 4.5, height = 4.5)
