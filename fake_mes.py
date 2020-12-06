


# 多条消息的分隔符
SPLIT_TEXT = "\n"


def split_mes(mes:str):
    # 把整条消息分割成列表
    mes = mes.replace("[CQ:at,qq=","").replace("]","")
    mes_list = mes.split(SPLIT_TEXT)

    for i in range(len(mes_list)):
        # 按空格分割指令段
        temp_txt = mes_list[i].split(" ")

        # 去除多余的空字符串
        temp_list = [txt for txt in temp_txt if txt != ""]

        mes_list[i] = temp_list

    return mes_list


def produce_fake_mes(mes:str):
    # 生成假消息

    mes_list = split_mes(mes)

    data_list = []

    for mes in mes_list:
        uid,name,message = mes
        data = {
            "type": "node",
            "data": {
                "name": name,
                "uin": uid,
                "content": message
            }
        }
        data_list.append(data)

    return data_list





