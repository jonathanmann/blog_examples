require("ggplot2")
dat2 <- read.csv(file="quarterly_sp_data.csv",head=TRUE,sep=",")
ggplot(dat2, aes(x=dat2$Projected, y=dat2$Actual)) + geom_point(shape=1,size=.6,color="steelblue") + 
  ylim(-.5, 1.5) + xlim(-.3,.7) + xlab("Projected") + ylab("Actual") + theme(
    panel.background = element_rect(fill = "transparent",colour = NA), # or theme_blank()
    panel.grid.minor = element_blank(), 
    panel.grid.major = element_blank(),
    plot.background = element_rect(fill = "transparent",colour = NA)
  )

