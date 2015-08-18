require("ggplot2")
df <- read.csv(file="quarterly_stock_data.csv",head=TRUE,sep=",")
ggplot(df, aes(x=df$ProjectedGrowth, y=df$ActualGrowth)) + geom_point(shape=1,size=.6,color="steelblue") + 
  ylim(-1,2) + xlim(-1,2) +
  xlab("Projected") + ylab("Actual") + theme(
    panel.background = element_rect(fill = "transparent",colour = NA), 
    panel.grid.minor = element_blank(), 
    panel.grid.major = element_blank(),
    plot.background = element_rect(fill = "transparent",colour = NA)
  )
