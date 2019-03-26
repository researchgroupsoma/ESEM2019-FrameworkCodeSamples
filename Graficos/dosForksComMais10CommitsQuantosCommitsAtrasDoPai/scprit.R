library(effsize)
library(ggplot2)
library(devtools)
library(easyGgplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/ic/Graficos/dosForksComMais10CommitsQuantosCommitsAtrasDoPai/dados.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$sample, levels = c("Android","Spring")), all$behind_by + 1)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10() +
  geom_boxplot(width=0.6,alpha=0.6) + ggtitle("Number of behind commits") + xlab("Ahead Samples") + ylab("Number of behind commits (log scale)") + 
  annotate("text", x = 1, y = 5.7, label = "6", size = 6) + annotate("text", x = 2, y = 15.0, label = "18", size = 6) +
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

  #mediana do android 6
  #mediana do  spring 18

p1

ggsave("/home/gabriel/Documentos/ic/Graficos/dosForksComMais10CommitsQuantosCommitsAtrasDoPai/numberOfBehindParent.pdf", width = 4.5, height = 4.5)


subtipos = rep(c("Android", "Spring"), each=4)

anos <- rep( c("0", "1-10", "11-50", ">50") , 2)



values <-c(0.238805970149254*100,0.358208955223881*100,0.223880597014925*100,0.17910447761194*100,0.056179775280899*100,0.224719101123595*100,0.606741573033708*100,0.112359550561798*100)


df2 <- data.frame(supp=subtipos,
                  dose=anos,
                  len=values)
head(df2)


p <- ggplot(data=df2, aes(x=dose, y=len, fill=supp)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Relative projects by behind commits", x="Number of Commits", y = "Projects") +
  scale_fill_manual("", values = c("Android" = "#87CEFA", "Spring" = "#4682b4"))+
  theme(plot.title=element_text(size=15, face = "bold"), axis.title=element_text(size=16),axis.text=element_text(size=18), legend.position = c(0.2, 0.80))

p

ggsave("/home/gabriel/Documentos/ic/Graficos/dosForksComMais10CommitsQuantosCommitsAtrasDoPai/numberOfBehindParentMoreThen10CommitsAhead.pdf", width = 4.5, height = 4.5)
