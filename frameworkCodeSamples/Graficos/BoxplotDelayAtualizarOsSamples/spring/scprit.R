library(effsize)
library(ggplot2)
library(devtools)
library(easyGgplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/ic/Graficos/BoxplotDelayAtualizarOsSamples/spring/apenasOsDados.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$type, levels = c("Spring")), all$delay)) + 
  geom_violin(width=1, trim=TRUE,fill="#87CEFA") +
  scale_y_log10() +
  geom_boxplot(width=0.6,alpha=0.6) + ggtitle("Spring's samples delay to update") + xlab("") + ylab("Delay in days (log scale)") +
  annotate("text", x = 1, y = 0.14, label = "0", size = 6) +
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

#mediana do general 0
#mediana do byYear 2,3

p1

ggsave("/home/gabriel/Documentos/ic/Graficos/BoxplotDelayAtualizarOsSamples/spring/delay_spring.pdf", width = 4.5, height = 4.5)



#subtipos = rep(c("TargetSdk", "MinSdk"), each=9)

anos <- rep( c("2014", "2015", "2016", "2017", "2018"))



values <-c(0.35, 8, 0.6, 3.6, 2.3)

df2 <- data.frame(dose=anos,
                  len=values)
head(df2)


p <- ggplot(data=df2, aes(x=dose, y=len)) +
  geom_bar(stat="identity", position=position_dodge(), fill = "#87CEFA") +
  labs(title="Spring Samples", x="Year", y = "Days to update") +
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18), legend.position = c(0.2, 0.80))

p

ggsave("/home/gabriel/Documentos/ic/Graficos/BoxplotDelayAtualizarOsSamples/spring/delay_years_spring.pdf", width = 4.5, height = 4.5)


