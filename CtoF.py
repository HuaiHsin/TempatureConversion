while True:
    #print("請輸入數字選擇轉換方案\n攝氏轉換華氏，請輸入1\n華氏轉換攝氏，請輸入2")
    num = input("請選擇\n攝氏轉換華氏，輸入1\n華氏轉換攝氏，輸入2\n離開輸入q\n輸入: ")
    if num == "1":
        temper_C = input("請輸入攝氏溫度： ")
        temper_C = int(temper_C)
        temper_F = temper_C * 9 / 5 + 32
        print("華式溫度為：" , temper_F)
    elif num == "2":
        temper_F = input("請輸入華氏溫度： ")
        temper_F = int(temper_F)
        temper_C = (temper_F - 32) * 5 / 9
        print("攝式溫度為：" , temper_C)
    elif num == "q":
    	break
    else:
        print("請輸入正確的數字")
#華氏= 攝氏*(9/5)+32
#攝氏= (華氏-32)*5/9
