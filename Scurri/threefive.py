class ThreeFiveManager:

    def get(self,start, end):
        result=list()

        #return empty for invalid range
        if start>end :
            return result;
        end=end+1
        for i in range(start, end):
            isThree=i % 3==0
            isFive=i % 5 ==0
            if isThree and isFive:
                result.append("ThreeFive")
            elif isThree:
                result.append("Three")
            elif isFive:
                result.append("Five")
            else:
                result.append(i)

        return result

if __name__ == '__main__':
    three=ThreeFiveManager()
    result=three.get(1,100)
    for each in result:
        print(each)