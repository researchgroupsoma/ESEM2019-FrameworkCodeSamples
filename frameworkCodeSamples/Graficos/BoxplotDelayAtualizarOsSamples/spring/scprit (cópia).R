library(effsize)
library(ggplot2)
library(devtools)
library(easyGgplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/Graficos/BoxplotDelayAtualizarOsSamples/spring/apenasOsDados.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$type, levels = c("General","ByYear")), all$delay)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10() +
  geom_boxplot(width=0.6,alpha=0.6) + ggtitle("Spring's samples delay to update") + xlab("") + ylab("Delay in days (log scale)") +
  annotate("text", x = 1, y = 0.14, label = "0", size = 6) + annotate("text", x = 2, y = 2.9, label = "2.3", size = 6) +
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

#mediana do general 0
#mediana do byYear 2,3

p1

ggsave("/home/gabriel/Documentos/Graficos/BoxplotDelayAtualizarOsSamples/spring/delay_spring.pdf", width = 4.5, height = 4.5)


