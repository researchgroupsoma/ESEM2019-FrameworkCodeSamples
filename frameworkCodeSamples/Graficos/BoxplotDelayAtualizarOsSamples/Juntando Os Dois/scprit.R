library(effsize)
library(ggplot2)
library(devtools)
library(easyGgplot2)
library(forcats)

setwd("C:\\Users\\dudur\\Documents\\gabrielsmenezes\\ic\\frameworkCodeSamples\\Graficos\\BoxplotDelayAtualizarOsSamples\\Juntando Os Dois")

all=read.csv("apenasOsDados.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$type, levels = c("Android", "Spring")), all$delay)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Delay to Update") + xlab("Code Samples") + ylab("Delay in days (log scale)") +
  annotate("text", x = 1, y = 48, label = "56", size = 8) + annotate("text", x = 2, y = 0.14, label = "0", size = 8) +
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

#mediana do general 56

p1

ggsave("delay_samples.pdf", width = 4.5, height = 4.5)





subtipos = rep(c("Android", "Spring"), each=5)

anos <- rep( c("2014", "2015", "2016", "2017", "2018") , 2)



values <-c(94, 31, 41, 89, 65, 0.35, 8, 0.6, 3.6, 2.3)





df2 <- data.frame(supp=subtipos,
                  dose=anos,
                  len=values)
head(df2)


p <- ggplot(data=df2, aes(x=dose, y=len, fill=supp)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Delay by year", x="Year", y = "Delay in days") +
  scale_fill_manual("", values = c("Android" = "#87CEFA", "Spring" = "#4682b4"))+
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18), legend.position = c(0.2, 0.80))

p

ggsave("/home/gabriel/Documentos/ic/Graficos/BoxplotDelayAtualizarOsSamples/Juntando Os Dois/delay_years.pdf", width = 4.5, height = 4.5)
