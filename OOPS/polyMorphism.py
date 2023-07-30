class A:
    
    def showUp(self):
        print("WELCOME")
    
    def showUp(self,firstname=""):
        print("MY FIRST NAME IS",firstname)

    def showUp(self,firstname="",lastname=""):        
        print(f"MY FIRST NAME {firstname} AND LAST NAME IS {lastname}")

obj = A()
obj.showUp("SAIKIRAN","SHET")
obj.showUp("SAIKIRAN")
