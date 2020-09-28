library(effsize)
library(ggplot2)
library(forcats)

setwd("C:\\Users\\dudur\\Documents\\gabrielsmenezes\\ic\\frameworkCodeSamples\\Graficos\\graficosDaCarol")


all=read.csv("all.csv", sep=",",header=T)

# Star, Forks

p1 <- ggplot(all, aes(factor(all$ecosystem, levels = c("Android","Spring")), all$forks))
p1 <- p1 + geom_violin(width=1, trim=TRUE,fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of forks") + xlab("Code Samples") + ylab("Number of forks (log scale)")
#[3,]  47.0   71
p1 <- p1 + annotate("text", x = 1, y = 65, label = "47", size = 8) + annotate("text", x = 2, y = 100, label = "71", size = 8) 
p1 + theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("forks.pdf", width = 4.5, height = 4.5)

# -------- Size
p1 <- ggplot(all, aes(factor(all$ecosystem, levels = c("Android","Spring")), all$numberofFilesJava)) + 
geom_violin(width=1, trim=TRUE,fill="#87CEFA") + scale_y_log10()+
geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Number of Java Files") + xlab("Code Samples") + ylab("Number of files (log scale)") +
#[3,]    9    4 
annotate("text", x = 1, y = 11, label = "9", size = 8) + annotate("text", x = 2.3, y = 8, label = "4", size = 8) + 
theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18))

p1

ggsave("files.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), (all$CountDeclMethodPublic)+1 ))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Public methods") + xlab("Code Samples") + ylab("Number of public methods (log scale)")
#[3,]   53    9
p1 <- p1 + annotate("text", x = 1, y = 40, label = "53", size = 6) + annotate("text", x = 2, y = 11, label = "9", size = 6) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/NPM.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$RelativeMethodPublic*100))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative public methods") + xlab("Code Samples") + ylab("Percent of public methods (log scale)")
#[3,]  75.0  100
p1 <- p1 + annotate("text", x = 1, y = 80, label = "75", size = 6) + annotate("text", x = 2, y = 109, label = "100", size = 6) 
p1 + theme(plot.title=element_text(size=17.4, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/RPM.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$CountLineCode))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Lines of code") + xlab("Code Samples") + ylab("Lines of code (log scale)")
#[3,]  497   95
p1 <- p1 + annotate("text", x = 1, y = 650, label = "497", size = 6) + annotate("text", x = 2, y = 110, label = "95", size = 6) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("LOC.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$CountLineCode/all$numberofFilesJava ))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Lines of Code per Java File") + xlab("Code Samples") + ylab("Lines of code (log scale)")
#[3,]  70.23387 25.00000
p1 <- p1 + annotate("text", x = 1, y = 85, label = "70.23", size = 8) + annotate("text", x = 2, y = 28, label = "25", size = 8) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("RLOC_files.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), (all$RelativeLineCode)*100))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative lines of code") + xlab("Code Samples") + ylab("Percent of lines (log scale)")
#[3,]   56   70
p1 <- p1 + annotate("text", x = 1, y = 58, label = "56", size = 6) + annotate("text", x = 2, y = 72, label = "70", size = 6) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/RLOC.pdf", width = 4.5, height = 4.5)

# -------- Complexity

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$SumCyclomaticStrict))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Total CC") + xlab("Code Samples") + ylab("Nº of Decisions Points (log scale)")
#[3,]  81.5   10
p1 <- p1 + annotate("text", x = 1, y = 105, label = "81.5", size = 8) + annotate("text", x = 2, y = 12, label = "10", size = 8) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/SCC.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$CyclomaticPerMethod ))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Cyclomatic Complexity per\nMethod in Java File") + xlab("Code Samples") + ylab("N� of Decisions Points (log scale)")
#[3,] 1.480 1.00
p1 <- p1 + annotate("text", x = 1, y = 1.6, label = "1.48", size = 8) + annotate("text", x = 2, y = 1.1, label = "1", size = 8) 
p1 + theme(plot.title=element_text(size=18, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("ACC.pdf", width = 4.5, height = 4.5)

# -------- Documentation

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$CountLineComment))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Comment lines") + xlab("Code Samples") + ylab("Nº of lines (log scale)")
#[3,]  385   15
p1 <- p1 + annotate("text", x = 1, y = 250 , label = "385", size = 6) + annotate("text", x = 2, y = 10, label = "15", size = 6) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/NCL.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), (all$RelativeLineComment)*100))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative Comment Lines in\nJava File") + xlab("Code Samples") + ylab("Percent of lines (log scale)")
#[3,]   32    7
p1 <- p1 + annotate("text", x = 1, y = 27.5, label = "32", size = 8) + annotate("text", x = 2, y = 6.8, label = "7", size = 8) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("RCL.pdf", width = 4.5, height = 4.5)

#----------  RQ2

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$Lifetime))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Lifetime") + xlab("Code Samples") + ylab("Days (log scale)")
#[3,] 1474 1924
p1 <- p1 + annotate("text", x = 1, y = 2000, label = "1474", size = 8) + annotate("text", x = 2, y = 2500, label = "1924", size = 8) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("lifetime.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$Commit))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Commits") + xlab("Code Samples") + ylab("Nº of commits (log scale)")
#[3,]   24  117
p1 <- p1 + annotate("text", x = 1, y = 18, label = "24", size = 6) + annotate("text", x = 2, y = 145, label = "117", size = 6) 
p1 + theme(plot.title=element_text(size=20, face = "bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/commits.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$LifetimePerCommit))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Lifetime per Commit") + xlab("Code Samples") + ylab("Frequency of commits (log scale)")
#[3,]   63   15
p1 <- p1 + annotate("text", x = 1.5, y = 90, label = "63", size = 8) + annotate("text", x = 2.45, y = 18, label = "15", size = 8) 
p1 + theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("lifetime_commits.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$Contributor))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Contributors") + xlab("Code Samples") + ylab("Nº of contributors (log scale)")
#[3,]    1    9
p1 <- p1 + annotate("text", x = 1, y = 1.2, label = "1", size = 6) + annotate("text", x = 2, y = 10, label = "9", size = 6) 
p1 + theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/contributors.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$LifetimePerCont))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Code Sample Lifetime per\nContributor") + xlab("Code Samples") + ylab("Frequency of contributors (log scale)")
#[3,] 1027  201
p1 <- p1 + annotate("text", x = 1, y = 1170, label = "1027", size = 6) + annotate("text", x = 2, y = 180, label = "201", size = 6) 
p1 + theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("lifetime_contributors.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$BC+1))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") + scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Breaking Changes") + xlab("Code Samples") + ylab("Breaking Changes (log scale)")
#[3,]    1  180
p1 <- p1 + annotate("text", x = 1, y = 1.5, label = "1", size = 6) + annotate("text", x = 2, y = 260, label = "180", size = 6)
p1 + theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/BC.pdf", width = 4.5, height = 4.5)

p1 <- ggplot(all, aes(factor(all$ecosystem,levels = c("Android","Spring")), all$relativeBC))
p1 <- p1 + geom_violin(width=1, trim=TRUE, fill="#87CEFA") #+ scale_y_log10()
p1 <- p1 + geom_boxplot(width=0.7,alpha=0.7) + ggtitle("Relative Breaking Changes") + xlab("Code Samples") + ylab("Percent of BC (log scale)")
#[3,]  0.00   40
p1 <- p1 + annotate("text", x = 1, y = 4, label = "0", size = 6) + annotate("text", x = 2, y = 44, label = "40", size = 6)
p1 + theme(plot.title=element_text(size=20,face="bold") ,axis.title=element_text(size=18),axis.text=element_text(size=18))
ggsave("/home/facom/Documents/GIT/Samples/figuras/relativeBC.pdf", width = 4.5, height = 4.5)
