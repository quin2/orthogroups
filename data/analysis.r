# 1 line per gene
dat.g.r <- read.table("black_rockcod_genecount.tab", header=T,sep="\t")
dat.g.s <- read.table("stickleback_genecount.tab", header=T, sep="\t")

# 1 line per repeat
dat.r <- read.table("black_rockcod_seqlength.tab", header=T,sep="\t")
dat.s <- read.table("stickleback_seqlength.tab",header=T,sep="\t")


# takes the data of 1 line per repeat as the argument
# For each gene, select the longest repeats
# The returned result has 1 line per gene
maxRepPerGene <- function (dat) {
    allGenes <- levels(dat$record);

    result <- dat[0,]  # remove all contents and keeps the column names
    for(i in 1:length(allGenes)) {
        records <- subset(dat, record==allGenes[i])

        # find the first instance of the maximum length, and append to the bottom of result
        result <- rbind(result, records[which(records$segment_length == max(records$segment_length))[[1]],])
    }
    return (result)
}

dat.s.max <- maxRepPerGene(dat.s)
dat.r.max <- maxRepPerGene(dat.r)

# histogram
comb<-hist(c(dat.r.max$segment_length, dat.s.max$segment_length), breaks=40)
p1 <- hist(dat.r.max$segment_length,breaks=comb$breaks, freq=F)
p2 <- hist(dat.s.max$segment_length,breaks=comb$breaks,freq=F)

# converting to relative frequency
p1$counts <- p1$counts/sum(p1$counts)
p2$counts <- p2$counts/sum(p2$counts)

plot(p1, col=rgb(0,0,1,1/4), xlim=c(5,55), ylim=c(0,0.15))
plot(p2, col=rgb(1,0,0,1/4), xlim=c(5,55),add=T)

# I'm subtracting 5 from the length, and considering it to have a geometric distribution
# Then fitting this distribution to the data to get the maximum likelihood estimate
# of the parameter
library(fitdistrplus)
fitg.s <- fitdist(dat.s.max$segment_length - 5, "geom")
fitg.r <- fitdist(dat.r.max$segment_length - 5, "geom")

summary(fitg.s)
## Fitting of the distribution ' geom ' by maximum likelihood 
## Parameters : 
##       estimate  Std. Error
## prob 0.5127869 0.009050577
## Loglikelihood:  -2113.101   AIC:  4228.203   BIC:  4233.558 
summary(fitg.r)
## Fitting of the distribution ' geom ' by maximum likelihood 
## Parameters : 
##       estimate  Std. Error
## prob 0.2905125 0.004460156
## Loglikelihood:  -6243.641   AIC:  12489.28   BIC:  12495.29 
