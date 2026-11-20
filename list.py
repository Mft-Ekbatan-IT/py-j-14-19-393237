



#list1=["narin","maede","fariborz"]
#print(list1[1])
#list1.append("milad")
#name=input("add your name:")
#list1.remove("narin")

#print(list1)
#delete=int(input("kodum hazf:"))
#list1.pop(delete-1)
#print(list1)


#property

#seq
#iterable
#i=iterator

#my_list=["fariborz","narin","jafar","goli","farnaz","sara"]
#print(my_list[::-2])

#my_list2=list()
#print(len(my_list))
#for i in my_list:
#    print(i)


#my_list[2]="tina"
#print(my_list)

#my_list=[1,2,3,4]
#a=12
#print(id(a))
#print("-"*20)
#b=5
#print(id(b))
#print("-"*20)
#c="f"
#print(id(c))
#print("-"*20)


#from sys import getrefcount
#
#data=512
#
#print(getrefcount(data))
#del(data)
#print(getrefcount(data))

#my_list=[1,2,3,"ali",5,6,7,"ali"]
#my_list2=my_list.copy()
#my_list.append("fariborz")
#my_list.clear()
#res=my_list.index("lili",5)
#my_list[1]="fariborz"
#my_list.insert(2,"yasi")
#res=my_list.pop(2)
#my_list.reverse()
#my_list.remove(5)
#my_list.remove("ali")
#res=my_list.pop(3)
#print(my_list)
#print(res)
#
#print(my_list2)
#print(my_list)


#my_list=["a","Z","q","A","a","Z"]
#
##my_list.sort()
#my_list2=[1,2,3,4,5,6,7,8,9,10,11]
#my_list.extend(my_list2)
#print(my_list)


#my_lis=[1,2,20,10,80]
#print(sum(my_lis))







#from math import ceil

#resid=[]
#while True:
#    menu=input("1.cafe  2.restooran  3.exit:")
#    while True:
#        match menu:
#            case"1":
#                menu_cafe=input("1.espersoo 150  2.late 350 3.exit:")
#                match menu_cafe:
#                    case"1":
#                        tedad_espersoo=int(input("tedad:"))
#                        mablagh=tedad_espersoo*150*1.1
#                        mablagh_rond=ceil(mablagh)
#                        resid.append(mablagh_rond)
#                        print(resid)
#                        break
#                    case"2":
#                        tedad_late=int(input("tedad:"))
#                        mablagh_late=tedad_late*350*1.1
#                        mablagh_rond_late=ceil(mablagh_late)
#                        resid.append(mablagh_rond_late)
#                        print(resid)
#                        break
#                    case _:
#                        print(sum(resid))
#                        break
#            
#            case"2":
#                menu_restooran=input("1.soltani  1200    2.jooje  750   3.exit:")
#
#                match menu_restooran:
#                    case"1":
#                        tedad_soltani=int(input("tedad:"))
#                        mablagh_soltani=tedad_soltani*1200*1.1
#                        mablagh_rond_soltani=ceil(mablagh_soltani)
#                        resid.append(mablagh_rond_soltani)
#                        print(resid)
#                        break
#                    
#                    
#                    case"2":
#
#                        tedad_jooj=int(input("tedad:"))
#                        mablagh_jooj=tedad_jooj*750*1.1
#                        mablagh_rond_jooj=ceil(mablagh_jooj)
#                        resid.append(mablagh_rond_jooj)
#                        print(resid)
#                        break
#
#                    case _:
#                        print(sum(resid))
#                        break
#            
#            case _:
#                print(sum(resid))
#                break
#
#
#
#
#            
#                    

            
#ist1=[]
#ist1.append(-10)
#rint(sum(list1))



emtiaz=[]

while True:
    print("be mosabeghe khosh amadi .")

    while True:
        menu_mosabeghe=input("1.tarikh 2.exit:")

        match menu_mosabeghe:
            case"1":
                tarikh_s=input("1.akharin padeshe iran  2.paytakhte iran dar zaman nader shah afshar 3.exit:")
                match tarikh_s:
                    case"1":
                        j1=input("(1.mohamad reza shah 2.nader shah )")
                        match j1:
                            case"1":
                                print("javab ok")
                                emtiaz.append(10)
                                print(sum(emtiaz))
                                break
                            case _:
                                print("eshtebah")
                                emtiaz.append(-10)
                                print(sum(emtiaz))
                                break
                        
                

