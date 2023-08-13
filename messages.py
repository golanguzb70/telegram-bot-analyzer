welcome="""
    Assalomu alaykum botga xo'sh kelibsiz. Bu bot orqali siz telegram guruhingizni analyze qila olasiz.
"""


def GetAnalyticsMessage(data:object) -> str:
    res = f"""👥 Guruh nomi: {data['name']} 
📝 Active a'zolar soni: {len(data['members'])}
📝 Jami yozilgan xabarlar: {sum(len(item['messages']) for item in data['members'])}
"""
    mems = []
    for m in data['members']:
        mems.append(AnalyticOfEachMember(m))
    res = res + "\n".join(mems)    
    return res

def AnalyticOfEachMember(member:object) -> str:
    topWords = []
    for i in range(len(member['top_words'])):
       if i == 3:
           break
       
       e = member['top_words'][i]
       topWords.append(f"🔸 {e['word']} {e['count']} marta ")
    joined = "\n".join(topWords)
    
    return f"""\n   📸 @{member["username"]} \nYozgan xabarlari soni {len(member['messages'])}ta\nIshlatgan so'zlar soni {len(member['top_words'])} ta
Eng ko'p ishlatgan so'zlari max 3 ta 
{joined}
"""