library('ggplot2')
df_used_cars <- read.csv('/Users/lindazhong/Documents/Data science 365/Data Visualization/car_brand.csv')

horizontal_bar <- ggplot(df_used_cars,aes(x = Brand, y = Cars.Listings))+
                        geom_bar(stat = "identity", width = 0.8)+
                        ggtitle('Car Lising by Brand')+
                        theme_classic()+
                        labs(x = NULL,
                             y = 'Number of Car Listing')+
                        coord_flip()

horizontal_bar