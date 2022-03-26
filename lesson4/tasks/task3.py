print("find dividents of 20 or 21")
if __name__=="__main__":
    print([i for i in range(20, 240) if i % 20 == 0 or i % 21 ==0])