

def num_2_word(num: int) -> str:
    """
    Description
    """

    if not isinstance(num,int):
        raise TypeError("Error")


    if num == 0:
        return "صفر"

    def convert_3_digit(num: int) -> str:

        #region DEFINE
        zero_nineteen = {
            "0":"",
            "1":"یک",
            "2":"دو",
            "3":"سه",
            "4":"چهار",
            "5":"پنج",
            "6":"شش",
            "7":"هفت",
            "8":"هشت",
            "9":"نه",
            "10":"ده",
            "11":"یازده",
            "12":"دوازده",
            "13":"سیزده",
            "14":"چهارده",
            "15":"پانزده",
            "16":"شانزده",
            "17":"هفده",
            "18":"هجده",
            "19":"نوزده"
        }

        twenty_ninety={
            "0":"",
            "1":"",
            "2":"بیست",
            "3":"سی",
            "4":"چهل",
            "5":"پنجاه",
            "6":"شصت",
            "7":"هفتاد",
            "8":"هشتاد",
            "9":"نود"
        }

        onehundred_ninehundred={
            "0":"",
            "1":"یک صد",
            "2":"دویست",
            "3":"سیصد",
            "4":"چهارصد",
            "5":"پانصد",
            "6":"ششصد",
            "7":"هفتصد",
            "8":"هشتصد",
            "9":"نهصد"
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
            res = f"{twenty_ninety[middle_digit]}{' و ' if last_digit!='0' else ''}{zero_nineteen[last_digit]}"

        if first_digit!="0":
            res = f"{onehundred_ninehundred[first_digit]}{' و ' if two_digit!='00' else ''}{res}"

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
        1:"هزار",
        2:"میلیون",
        3:"میلیارد",
        4:"بیلیون",
        5:"بیلیارد",
        6:"تریلیون",
        7:"تریلیارد",
        8:"کوآدریلیون",
        9:"کادریلیارد",
        10:"کوینتیلیون",
        11:"کوانتینیارد",
        12:"سکستیلیون",
        13:"سکستیلیارد",
        14:"سپتیلیون",
        15:"سپتیلیارد",
        16:"اکتیلیون",
        17:"اکتیلیارد",
        18:"نانیلیون",
        19:"نانیلیارد",
        20:"دسیلیون",
        21:"دسیلیارد",
        22:"آندسیلیون",
        23:"آندسیلیارد",
        24:"دودسیلیون",
        25:"دودسیلیارد",
        26:"تریدسیلیون",
        27:"تریدسیلیارد",
        28:"کوادردسیلیون",
        29:"کوادردسیلیارد",
        30:"کویندسیلیون",
        31:"کویندسیلیارد",
        32:"سیدسیلیون",
        33:"سیدسیلیارد"
    }
    #endregion

    num_list = sep_3_digit(num)
    num_list.reverse()

    res = []

    for index, num_part in enumerate(num_list):
        if num_part!=0:
            res.insert(0, f"{convert_3_digit(num_part)} {unit[index]}" )


    return f"{'منفی ' if is_negative else ''}{' و '.join(res)}"





