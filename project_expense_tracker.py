#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class expense_tracker:
    def __init__(self):
        self.revenue=0
        self.loan=0
        self.grocery=0
        self.medical=0
        self.monthlybill=0
        self.balance=0
        self.depo_bal=0
    def user_entery(self):
        self.revenue=int(input("enter your revenue :"))
        self.loan=int(input("enter your loan amount :"))
        self.grocery=int(input("enter your grocery expense :"))
        self.medical=int(input("enter your medical expense :"))
        self.monthlybill=int(input("enter your monthlybill expense :"))
    def monthly_revenue(self):
        print("monthly revenue:",self.revenue)
    def balance1(self):
        if self.revenue>0:
            self.balance=self.revenue-self.loan-self.grocery-self.medical-self.monthlybill
            print("balance:",self.balance)
    def expense_limiter(self):
        limit=int(input("enter expense limit % :"))
        print("reached the limit:",(self.revenue*limit/100))
        if self.balance>self.revenue*20/100:
            print("you have saved ",self.balance-self.revenue*20/100,"above the limit")
    def additional_exp(self):
        global exp
        exp=int(input("enter additional expense amount :"))
        self.balance=self.revenue-self.loan-self.grocery-self.medical-self.monthlybill-exp
        print("balance after additional expense",self.balance)
    def deposit(self):
        if self.balance>0:
            self.depo_bal=self.depo_bal+self.balance
            print("your deposit balance:",self.depo_bal)
        else:
            print('unavailable balance')
    def catagory_with_more_exp(self):
        if self.grocery>self.medical and self.grocery>self.monthlybill:
            print("grocery cause more expense")
        elif self.medical>self.grocery and self.medical>self.monthlybill:
            print("medical cause more expense")
        else:
            print("monthlybill cause more expense")
e=expense_tracker()
while True:
    print("1.enter details \n 2.expense_limiter \n 3.balance \n 4.additional_exp \n 5.deposit \n 6.catagory_with_more_exp ")
    ch=int(input("enter your choice :"))
    if ch==1:
        e.user_entery()
    elif ch ==2:
            e.expense_limiter()
        
    elif ch==3:
        if e.balance<=0:
            print("no balance ")
        else:
            print(e.balnce)
    
            
    elif ch==4:
        if e.balance<=0:
            print("there is no balance for additional expense ")
        else:
            e.additional_exp()
        
    elif ch==5:
        if e.depo_bal <=0:
            print('invalid deosit balance')
        else:
            e.deposit()
        
    elif ch==6:
        if e.loan or e.medical or e.grocery or e. monthlybill ==0:
            print("first enter expense")
        else:
            e.catagory_with_more_exp()
        
    else:
        print("invalid")
    print("if you want to continue type YES otherwise NO")
    g=input("enter here")
    if g=='YES' :
        continue
    else:
        break


# In[ ]:


e.balance1()


# In[ ]:




