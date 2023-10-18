

def num_2_word(num: int) -> str:
    """
    Description
    """

    if not isinstance(num,int):
        raise TypeError("Error")


    if num == 0:
        return "zero"

    def convert_3_digit(num: int) -> str:

        #region DEFINE
        zero_nineteen = {
            "0":"", 
            "1":"One", 
            "2":"Two", 
            "3":"Three", 
            "4":"Four", 
            "5":"Five", 
            "6":"Six", 
            "7":"Seven", 
            "8":"Eight", 
            "9":"Nine",
            "10":"Ten", 
            "11":"Eleven", 
            "12":"Twelve", 
            "13":"Thirteen", 
            "14":"Fourteen", 
            "15":"Fifteen", 
            "16":"Sixteen", 
            "17":"Seventeen", 
            "18":"Eighteen", 
            "19":"Nineteen"
        }

        twenty_ninety={
            "0":"", 
            "1":"",
            "2":"Twenty", 
            "3":"Thirty", 
            "4":"Forty", 
            "5":"Fifty", 
            "6":"Sixty", 
            "7":"Seventy", 
            "8":"Eighty", 
            "9":"Ninety"
        }

        onehundred_ninehundred={
            "1":"one hundred", 
            "2":"Two hundred", 
            "3":"Three hundred", 
            "4":"Four hundred", 
            "5":"Five hundred", 
            "6":"Six hundred", 
            "7":"Seven hundred", 
            "8":"Eight hundred", 
            "9":"Nine hundred"
        }
        #endregion

        str_num = str(num).zfill(3) 

        two_digit =  str_num[1:] 
        first_digit = str_num[0] 
        middle_digit = str_num[1] 
        last_digit = str_num[2] 

        res = "" 

        if int(two_digit) in range(1,20):
            res = zero_nineteen[str(int(two_digit))]
        else:
            res = f"{twenty_ninety[middle_digit]}{' ' if last_digit!='0' else ''}{zero_nineteen[last_digit]}"

        if first_digit!="0":
            res = f"{onehundred_ninehundred[first_digit]}{' ' if two_digit!='00' else ''}{res}"

        return res

    def sep_3_digit(num:int) -> list:
        res = []

        while num!=0:
            res.insert(0, num%1000)
            num//=1000

        return res


    is_negative = False

    if num<0:
        is_negative = True
        num *= -1


    #region DEFINE
    unit = {
        0:"",
        1:"Thousand",
        2:"Million",
        3:"Billion",
        4:"Trillion",
        5:"Quadrillion",
        6:"Quintillion",
        7:"Sextillion",
        8:"Septillion",
        9:"Octillion",
        10:"Nonillion",
        11:"Decillion",
        12:"Undecillion",
        13:"Duodecillion",
        14:"Tredecillion",
        15:"Quattuordecillion",
        16:"Quindecillion",
        17:"Sedecillion",
        18:"Septendecillion",
        19:"Octodecillion",
        20:"Novendecillion",
        21:"Vigintillion",
        22:"Unvigintillion",
        23:"Duovigintillion",
        24:"Tresvigintillion",
        25:"Quattuor­vigint­illion",
        26:"Quinvigintillion",
        27:"Sesvigintillion",
        28:"Septemvigintillion",
        29:"Octovigintillion",
        30:"Novemvigintillion",
        31:"Trigintillion",
        32:"Untrigintillion",
        33:"Duotrigintillion"
    }
    #endregion

    num_list = sep_3_digit(num)
    num_list.reverse()

    res = []

    for index, num_part in enumerate(num_list):
        if num_part!=0:
            res.insert(0, f"{convert_3_digit(num_part)} {unit[index]}" )


    return f"{'Minus ' if is_negative else ''}{' '.join(res)}"





