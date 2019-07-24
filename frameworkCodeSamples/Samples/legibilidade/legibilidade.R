library(ggplot2)
library(scales)

##############NLegibilidade dos samples

all=read.csv("/home/gabriel/Documentos/ic/frameworkCodeSamples/Samples/legibilidade/legibilidade_samples.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$framework, levels = c("Android","Spring")), all$readability+ 0.00000001)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10(breaks = c(0.001,0.01,1)) +
  geom_boxplot(width=0.6,alpha=0.6) + ggtitle("Readability") + xlab("Code Samples") + ylab("Readability value") + 
  annotate("text", x = 1, y = 0.006, label = "0.0107", size = 6) + annotate("text", x = 2, y = 0.13, label = "0.2129", size = 6) +
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("/home/gabriel/Documentos/ic/frameworkCodeSamples/Samples/legibilidade/readeability.pdf", width = 4.5, height = 4.5)
