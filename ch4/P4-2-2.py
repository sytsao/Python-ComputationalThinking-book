# P4-2-2功能: 簡化版個人綜合所得稅試算。
income=int(input('請輸入年所得淨額: '))
if income<=540000: #條件1
    tax=income*0.05
elif income<=1210000: #條件2
    tax= (income*0.12)-37800
elif income<= 2420000: #條件3
    tax= (income*0.2)-134600
elif income<=4530000: #條件4
    tax= (income*0.3)-376600
elif income<=10310000: #條件5
    tax= (income*0.4)-829600
else: #條件6
    tax= (income*0.45)-1345100    
print('應繳稅額 = ', tax)
