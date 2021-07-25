# def test():
            #list(x) = i for i in list(locals().keys()) if i != 'self'
            # print(dict(locals()))
            # k = (k for k in locals().keys() if k != 'self')
            # for each in k: 
            #     self.newAttr(each)
            #     print(each)
            #   newAttr(k for k in locals())
            
            # print(locals())
            # x = list(filter(lambda x:x != 'self', locals().keys()))
            # self.x = x for i in list(x)
            # print(x)
            # print(self.__dict__)
            # print(self.__dict__.keys())
            # for i in x:
            #     self.__setattr__(i,self.__dir__)
            # print(self.__dict__)
                # self.__dict__ = i.__dict__.copy()
            # x = ['arcana', 'suit', 'pos']
            # for i in list(itslocals().keys()):
            #     # self.i = i if i != 'self' else print('SELF!!')
            # self.arcana = self.suit = self.pos = index_

# a = cardPls(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1)).getCardPls()
# print(", ".join(f"{key}: {value}" for key, value in a.items()))

# def mainTest():
    # for i in a.items():
    #     print(i)
    # attrs = vars(a)
    # print(attrs)
    # for i in attrs.items():
    #     print(i)
    # print(item for item in attrs.items())
    # print(', '.join("%s: %s" % item for item in attrs.items()))
    # print(dir(a))
    # attributes = [attr for attr in dir(a)
    #               if not attr.startswith('__')]
    # print(attributes)
    # print(cardPls.getCardPls())