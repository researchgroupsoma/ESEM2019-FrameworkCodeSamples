library(ggplot2)


subtipos = rep(c("Android", "Spring"), each=4)

apiLevel <- rep( c("1", "2-3", "4-10", "> 10"), 2 )



values <-c(0.46*100,0.29*100,0.16*100,0.07*100,0.47*100,0.26*100,0.16*100,0.09*100)





df2 <- data.frame(supp=subtipos,
                  dose=apiLevel,
                  len=values)
head(df2)



p <- ggplot(data=df2, aes(x=dose, y=len, fill=supp)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Relative projects ahead by commits", x="Number of commits", y = "Number of projects") +
  scale_fill_manual("", values = c("Android" = "#87CEFA", "Spring" = "#4682b4"))+
  geom_text(aes(label=len), vjust=0, color="black",position = position_dodge(0.9), size=5)+
  theme(plot.title=element_text(size=16, face = "bold"), axis.title=element_text(size=16),axis.text=element_text(size=16), legend.position = c(0.87, 0.80))

p

ggsave("/home/gabriel/Documentos/ic/Graficos/metrificandoOsForksAheadPorGrupoDeNumeroDeCommits/relative_projects_by_commits.pdf", width = 4.5, height = 4.5) 
