import sys

class pyText:
    def createdicts(self,filename,delimiter='chapter'):
        try:
            fs = open(filename,'r')
        except IOError as e:
            print 'file open error:',e
            return
        lc = fs.read()
        fs.close()
        lst = lc.splitlines()
        chapter={}
        for line in lst:
                if 'chapter' in line.lower():
                        ch=line
                        chapter[ch]=line
                chapter[ch]+=line+'\n'
                
        return chapter

class className:
    def hello(self,name):
        print 'Hello %s' % name
    
def main():
    createdicts(sys.argv[1])

if __name__ == '__main__':
    main()
