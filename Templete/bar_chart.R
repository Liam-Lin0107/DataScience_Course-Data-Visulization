library('ggplot2')

df_used_cars <- read.csv("/Users/lindazhong/Documents/Data science 365/Data Visualization/car_brand.csv")

bar_chart <- ggplot(df_used_cars,
                    aes(x = Brand, y = Cars.Listings))+
                    geom_bar(stat = 'identity', width = 0.8,color = 'navy', fill = 'navy')+
                    ggtitle("Car Listings by Brand")+
                    theme_classic()+
                    theme(axis.text.x = element_text(angle = 45, hjust = 1))+
                    labs(x = NULL,
                         y = "Number of Listings")
                  
bar_chart