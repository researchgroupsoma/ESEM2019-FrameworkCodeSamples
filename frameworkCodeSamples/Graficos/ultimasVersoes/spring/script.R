library(ggplot2)

springVersion <- c("2.0.5", "2.0.2", "2.0.1")



values <-c(115,	1, 7)


#2.0.5 RELEASE	115
#2.0.2 RELEASE	1
#2.0.1 RELEASE	7




df2 <- data.frame(dose=springVersion,
                  len=values)
head(df2)



p <- ggplot(data=df2, aes(x=dose, y=len)) +
  geom_bar(stat="identity", position=position_dodge(), fill = "#87CEFA") +
  labs(title="Spring Samples", x="Springboot Version", y = "Number of Projects / Subprojects") +
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18)) +
  ggsave("/home/gabriel/Documentos/Graficos/criandoGraficoDeBarras/spring/springVersions.pdf", width = 4.5, height = 4.5) 

p

