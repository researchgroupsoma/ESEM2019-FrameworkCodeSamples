library(effsize)
library(ggplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/ic/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/numeroDeImports.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$framework,levels = c("android","spring")), all$todos.nao.distintos)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Non-distinct imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 7.5, label = "8.6", size = 6) + 
  annotate("text", x = 2, y = 5, label = "5.7", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("/home/gabriel/Documentos/ic/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/totalImportsNonDistinct.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("android","spring")), all$todos.distintos)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Distinct imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 42, label = "34.5", size = 6) + 
  annotate("text", x = 2, y = 28, label = "19", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("/home/gabriel/Documentos/ic/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/totalImportsDistinct.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("android","spring")), all$apenas.do.framework.nao.distintos)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Non-distinct \nframework imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 50, label = "39", size = 6) + 
  annotate("text", x = 2, y = 5.5, label = "4", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("/home/gabriel/Documentos/ic/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/frameworkImportsNonDistinct.pdf", width = 4.5, height = 4.5)



p1 <- ggplot(all, aes(factor(all$framework,levels = c("android","spring")), all$apenas.do.framework.distinto)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Distinct framework imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 33, label = "26.5", size = 6) + 
  annotate("text", x = 2, y = 4.5, label = "4", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("/home/gabriel/Documentos/ic/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/frameworkImportsDistinct.pdf", width = 4.5, height = 4.5)