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
  labs(title="Spring Boot Versions", x="Versions of Code Samples", y = "Number of Projects / Subprojects") +
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))
  

p

ggsave("C:\\Users\\dudur\\Documents\\gabrielsmenezes\\ic\\frameworkCodeSamples\\Graficos\\ultimasVersoes\\spring\\springVersions.pdf", width = 4.5, height = 4.5) 
