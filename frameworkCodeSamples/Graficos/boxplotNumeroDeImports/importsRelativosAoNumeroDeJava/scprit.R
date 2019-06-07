library(effsize)
library(ggplot2)
library(forcats)

all=read.csv("numeroDeImports.csv", sep=",",header=T)

p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$todos.nao.distintos)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative non-distinct imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 7.5, label = "8.6", size = 6) + 
  annotate("text", x = 2, y = 5, label = "5.6", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("totalImportsNonDistinct.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$todos.distintos)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative distinct imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 5.5, label = "4.5", size = 6) + 
  annotate("text", x = 2, y = 5, label = "4.3", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("totalImportsDistinct.pdf", width = 4.5, height = 4.5)


p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$apenas.do.framework.nao.distintos)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative non-distinct \nframework imports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 7, label = "5.6", size = 6) + 
  annotate("text", x = 2, y = 1.2, label = "1", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("frameworkImportsNonDistinct.pdf", width = 4.5, height = 4.5)



p1 <- ggplot(all, aes(factor(all$framework,levels = c("Android","Spring")), all$apenas.do.framework.distinto)) + 
  geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
  scale_y_log10() +
  geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative distinct framework\nimports") + xlab("Code Samples") + ylab("Imports") + 
  annotate("text", x = 1, y = 4, label = "3.7", size = 6) + 
  annotate("text", x = 2, y = 0.89, label = "1", size = 6) +
  theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("frameworkImportsDistinct.pdf", width = 4.5, height = 4.5)
