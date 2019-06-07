library(effsize)
library(ggplot2)
library(forcats)

all=read.csv("/home/gabriel/Documentos/ic/Graficos/BoxplotRazaoDosMantenedoresEmComum/comGitLog/dados.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$framework,levels = c("android","spring")), 1 + (all$common.contributors/all$framework.contributors) * 100)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative number of frameworks \ncontributors in code samples and \nthe total of springboot contributors") + xlab("Code Samples") + ylab("") + 
  annotate("text", x = 2, y = 2, label = "1.12", size = 6) + annotate("text", x = 1, y = 1.05, label = "0", size = 6) +
  theme(plot.title=element_text(size=16,face="bold") ,axis.title=element_text(size=16),axis.text=element_text(size=16))

p1

ggsave("springbootContributors.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("android","spring")), 1 + (all$common.contributors/all$sample.contributors) * 100)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative number of frameworks \ncontributors in code samples and \nnumber of contributors of the own \ncode sample") + xlab("Code Samples") + ylab("") + 
  annotate("text", x = 2, y = 8, label = "5.43", size = 6) + annotate("text", x = 1, y = 1.3, label = "0", size = 6) + 
  theme(plot.title=element_text(size=16,face="bold") ,axis.title=element_text(size=16),axis.text=element_text(size=16))

p1

ggsave("codeSampleContributors.pdf", width = 4.5, height = 4.5)
