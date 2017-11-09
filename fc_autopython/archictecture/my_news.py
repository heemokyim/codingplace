class News:
    news=[]

    def find_news(self,kwd):
        for each in range(10):
            self.news.append('\''+str(each)+' news: '+kwd+'\'')
            print('Completed !')
            return self.news
