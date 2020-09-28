library(ggplot2)

subtipos = rep(c("TargetSdk", "MinSdk"), each=9)

apiLevel <- rep( c("19", "21", "22", "23", "24", "25", 
               "26", "27", "28"), 2 )




values <-c(1,8,7,13,15,19,46,177,25, 1,62,0,22,18,5,6,1,1)





df2 <- data.frame(supp=subtipos,
                  dose=apiLevel,
                  len=values)
head(df2)



p <- ggplot(data=df2, aes(x=dose, y=len, fill=supp)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Android Versions", x="Versions of Code Samples", y = "Number of Projects / Subprojects") +
  scale_fill_manual("", values = c("MinSdk" = "#87CEFA", "TargetSdk" = "#4682b4"))+
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18), legend.position = c(0.2, 0.80))

p


ggsave("C:\\Users\\dudur\\Documents\\gabrielsmenezes\\ic\\frameworkCodeSamples\\Graficos\\ultimasVersoes\\android\\androidAPILevel.pdf", width = 4.5, height = 4.5) 



all=read.csv("/home/gabriel/Documentos/ic/Graficos/ultimasVersoes/android/android.csv", sep=",",header=T)





subtipos = rep(c("TargetSdk", "MinSdk"), each=9)

apiLevel <- rep( c("19", "21", "22", "23", "24", "25", 
                   "26", "27", "28"), 2 )



values <-c(0.003215434083601*100, 0.02572347266881*100, 0.022508038585209*100, 0.041800643086817*100, 0.048231511254019*100, 0.061093247588425*100,0.147909967845659*100, 0.569131832797428*100, 0.080385852090032*100, 0.008620689655172*100, 0.53448275862069*100, 0, 0.189655172413793*100, 0.155172413793103*100, 0.043103448275862*100, 0.051724137931035*100, 0.008620689655172*100, 0.008620689655172*100)





df2 <- data.frame(supp=subtipos,
                  dose=apiLevel,
                  len=values)
head(df2)



p <- ggplot(data=df2, aes(x=dose, y=len, fill=supp)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Android Samples", x="API Level", y = "Number of Projects / Subprojects") +
  scale_fill_manual("", values = c("MinSdk" = "#87CEFA", "TargetSdk" = "#4682b4"))+
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18), legend.position = c(0.2, 0.80)) +
  ggsave("/home/gabriel/Documentos/ic/Graficos/ultimasVersoes/android/androidAPILevelRelative.pdf", width = 4.5, height = 4.5) 

p

