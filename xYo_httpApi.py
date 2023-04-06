# -*- coding: UTF-8 -*-
import os
import time
import json
import requests


# *************************插件接口*****************************
def output_log(log_type: str, msg: str):
    """
    向框架输出一份日志
    :param log_type:日志类型，建议 【1/调试】【2/提示】【3/警告】也可以是其他任意文本内容
    :param msg:日志内容
    :return:结果
    """

    if log_type == '1' or log_type == '调试':
        colour = 'ffc125'
        log_type = '调试'
    elif log_type == '3' or log_type == '警告':
        colour = 'ff0000'
        log_type = '警告'
    elif log_type == '2' or log_type == '提示':
        colour = '00FC00'
        log_type = '提示'
    else:
        colour = '00BFFF'

    payload = json.dumps({
        "type": log_type,
        "content": msg,
        "colour": colour,
        "token": token,
        "api": "OutPut"
    })
    return requests.request("POST", url, data=payload)


def get_ver():
    """
    获取框架版本号
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetVer",
    })
    return requests.request("POST", url, data=payload)


def restart_framework():
    """
    重启框架
    注意，这是重启框架不是重启http模块请谨慎使用
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "RestartFramework",
    })
    return requests.request("POST", url, data=payload)

def get_runtime():
    """
    获取框架运行时长
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetRuntime",
    })
    return requests.request("POST", url, data=payload)

def get_wxlogintime(bot_id:str):
    """
    获取微信登录时长
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetWxidLogintime",
        "robot_wxid":bot_id
    })
    return requests.request("POST", url, data=payload)


def get_wxrecmsgnum(bot_id:str):
    """
    获取微信收信数量
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetWxidRecmsgNum",
        "robot_wxid":bot_id
    })
    return requests.request("POST", url, data=payload)

def get_wxsendmsgnum(bot_id:str):
    """
    获取微信发信数量
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetWxidSendmsgNum",
        "robot_wxid":bot_id
    })
    return requests.request("POST", url, data=payload)
def get_robotlist():
    """
    获取登录账号列表
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetRobotList",
    })
    return requests.request("POST", url, data=payload)



def exit_wechat(bot_id:str):
    """
    退出指定微信
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "ExitWeChat",
        "robot_wxid": bot_id
    })
    return requests.request("POST", url, data=payload)


def get_localapiver():
    """
    取 httpApi 当前使用版本
    【非本模块】
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetHttpApiCurrentVer",

    })
    return requests.request("POST", url, data=payload)

def get_webapiver():
    """
    取 httpApi 最新使用版本
    【非本模块】
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetHttpApiNewestVer",

    })
    return requests.request("POST", url, data=payload)






# *************************个人微信*****************************


def send_textmsg(bot_id: str, to_id: str, msg: str):
    """
    发送普通文本消息
    :param bot_id:机器人微信id
    :param to_id:目标用户微信id
    :param msg:文本内容
    :return:
    """
    payload = json.dumps({
        "api": "SendTextMsg",
        "msg": msg,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,

    })
    return requests.request("POST", url, data=payload)


def send_groupmsg_at(bot_id: str, to_id: str, msg: str, at_list: list):
    """
    群里艾特并发送一段内容
    例如（@a这是消息内容）多人（@a@b内容）
    :param bot_id: 机器人id
    :param to_id: 接收的群
    :param at_list: 需要艾特的用户列表
    :param msg: 发送的文本
    :return:
    """
    if type(at_list) != list:
        return 'at_name type not is list'

    if len(at_list) == 0:
        return 'at_name cannot be empty'

    member_wxid = ''
    for i in at_list:
        member_wxid += i + ','
    member_wxid = member_wxid[:-1]

    payload = json.dumps({
        "member_wxid": member_wxid,
        "member_name": "",
        "msg": msg,
        "token": token,
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "api": "SendGroupMsgAndAt"
    })

    return requests.request("POST", url, data=payload)


def send_image(bot_id: str, to_id: str, path: str):
    """
    发送图片
    :param bot_id:机器人id
    :param to_id: 接收id
    :param path: 图片地址
    :return:
    """
    payload = json.dumps({
        "path": path,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "SendImageMsg"
    })

    return requests.request("POST", url, data=payload)


def send_cardmsg(bot_id: str, to_id: str, card_id: str):
    """
    发送名片
    :param bot_id: 机器人id
    :param to_id: 目标id
    :param card_id: 名片id
    :return:
    """
    payload = json.dumps({
        "content": card_id,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "SendCardMsg"
    })

    return requests.request("POST", url, data=payload)


def send_sharelinkmsg(bot_id: str, to_id: str, title: str, desc: str, img_url: str, html_url: str):
    """
    发送普通分享链接
    :param bot_id:机器人id
    :param to_id:目标id
    :param title:标题
    :param desc:内容
    :param img_url:图片地址
    :param html_url:跳转地址
    :return:
    """
    payload = json.dumps({
        "title": title,
        "desc": desc,
        "image_url": img_url,
        "url": html_url,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "SendShareLinkMsg"
    })

    return requests.request("POST", url, data=payload)


def send_musiclinkmsg(bot_id: str, to_id: str, title: str, desc: str, img_url: str, html_url: str, audio: str):
    """
    发送一条可播放的歌曲链接
    :param bot_id:机器人id
    :param to_id:目标id
    :param title:标题
    :param desc:正文
    :param img_url:图片地址
    :param html_url:跳转地址
    :param audio:媒体地址
    :return:
    """
    payload = json.dumps({
        "title": title,
        "desc": desc,
        "thumburl": img_url,
        "dataurl": audio,
        "url": html_url,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "SendMusicLinkMsg"
    })

    return requests.request("POST", url, data=payload)


def send_filemsg(bot_id: str, to_id: str, path: str):
    """
    发送文件消息
    :param bot_id:机器人id
    :param to_id: 目标id
    :param path: 文件路径
    :return:
    """
    payload = json.dumps({
        "path": path,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "SendFileMsg"
    })
    return requests.request("POST", url, data=payload)


def send_videomsg(bot_id: str, to_id: str, path: str):
    """
    发送视频消息
    :param bot_id:机器人id
    :param to_id: 目标id
    :param path: 视频地址
    :return:
    """
    payload = json.dumps({
        "path": path,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "SendVideoMsg"
    })
    return requests.request("POST", url, data=payload)


def modify_nameremark(bot_id: str, to_id: str, name: str):
    """
    修改好友备注
    :param bot_id:机器人id
    :param to_id: 目标id
    :param path: 表情地址
    :return:
    """
    payload = json.dumps({
        "note": name,
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "ModifyFriendNote"
    })
    return requests.request("POST", url, data=payload)


def delete_friend(bot_id: str, to_id: str):
    """
    删除好友
    :param bot_id:机器人id
    :param to_id: 目标id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "api": "DeleteFriend"
    })
    return requests.request("POST", url, data=payload)


def agree_friendverify(bot_id: str, type: int, v1: str, v2: str):
    """
    同意好友请求
    :param bot_id:机器人id
    :param to_id: 目标id
    :param v1: v1的值
    :param v2: v2的值
    :return:
    """
    payload = json.dumps({
        "token": token,
        "robot_wxid": bot_id,
        "type": type,
        "v1": v1,
        "v2": v2,
        "api": "AgreeFriendVerify"
    })
    return requests.request("POST", url, data=payload)


def quit_group(bot_id: str, to_id: str):
    """
    退出群聊
    :param bot_id: 机器人id
    :param to_id: 要退的群id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "api": "QuitGroup"
    })
    return requests.request("POST", url, data=payload)


def accepte_transfer(bot_id: str, from_id: str, money: str, payer_id: str, receiver_id: str, pay_type: int):
    """
    同意转帐
    :param bot_id:机器人id
    :param from_id: 发送者id
    :param money: 金额
    :param payer_id:付款id
    :param receiver_id:收款id
    :param pay_type:付款类型
    :return:
    """
    payload = json.dumps({
        "token": token,
        "robot_wxid": bot_id,
        "api": "AccepteTransfer",
        "from_wxid": from_id,
        "money": money,
        "payer_pay_id": payer_id,
        "receiver_pay_id": receiver_id,
        "paysubtype": pay_type
    })
    return requests.request("POST", url, data=payload)


def modify_groupname(bot_id: str, to_id: str, name: str):
    """
    修改群名称
    :param bot_id:机器人id
    :param to_id:群id
    :param name:新群名
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "ModifyGroupName",
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "group_name": name

    })
    return requests.request("POST", url, data=payload)


def get_userimg(bot_id: str, to_id: str):
    """
    获取用户、群头像
    :param bot_id:机器人id
    :param to_id: 目标id/群id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetHeadimgByWxid",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
    })
    return requests.request("POST", url, data=payload)


def get_username(bot_id: str, to_id: str):
    """
    通过ID获取好友,群聊,公众号的昵称(缓存获取)
    :param bot_id:机器人id
    :param to_id: 目标id/群id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetNameByWxid",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
    })
    return requests.request("POST", url, data=payload)


def get_usernote(bot_id: str, to_id: str):
    """
    通过ID获取好友,群聊的备注（公众号之类的理论上也可以）
    :param bot_id:机器人id
    :param to_id: 目标id/群id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetNoteByWxid",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
    })
    return requests.request("POST", url, data=payload)


def get_grouplist(bot_id: str, refresh: int):
    """
    获取群列表
    :param bot_id:
    :param refresh: 0：直接从缓存获取，1：刷新缓存再获取
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetGrouplist",
        "robot_wxid": bot_id,
        "is_refresh": refresh,

    })
    return requests.request("POST", url, data=payload)


def get_subscriptionlist(bot_id: str, refresh: int):
    """
    获取关注的公众号列表
    :param bot_id:
    :param refresh: 0：直接从缓存获取，1：刷新缓存再获取
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetSubscriptionlist",
        "robot_wxid": bot_id,
        "is_refresh": refresh,

    })
    return requests.request("POST", url, data=payload)


def search_account(bot_id: str, content: str):
    """
    搜索好友
    :param bot_id:
    :param content:支持手机号、微信号等等搜索
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SearchAccount",
        "robot_wxid": bot_id,
        "content": content,

    })
    return requests.request("POST", url, data=payload)


def get_userdata(bot_id: str, to_id: str):
    """
    wxid查详细信息
    :param bot_id:
    :param to_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetInfoByWxid",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
    })
    return requests.request("POST", url, data=payload)


def get_groupuserdata(bot_id: str, to_id: str, user_id: str):
    """
    获取某个群成员详细
    :param bot_id:
    :param to_id: 群id
    :param user_id:群里成员的id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetGroupMemberDetailInfo",
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "member_wxid": user_id

    })
    return requests.request("POST", url, data=payload)


def get_groupuserlist(bot_id: str, to_id: str, refresh: int):
    """
    获取群成员列表
    :param bot_id:
    :param to_id:
    :param refresh:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetGroupMember",
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "is_refresh": refresh

    })
    return requests.request("POST", url, data=payload)


def get_moments(bot_id: str, num: int, pyq_id=None):
    """
    获取朋友圈
    :param bot_id:
    :param num:数量1-10条，少了报错，多了无效
    :param pyq_id:获取指定id的朋友圈，不填就是最新一条
    :return:
    """
    if num == '':
        num = 1
    elif num < 1:
        num = 1
    elif num > 10:
        num = 10

    payload = json.dumps({
        "token": token,
        "api": "GetMoments",
        "robot_wxid": bot_id,
        "pyq_id": pyq_id,
        "num": num

    })
    return requests.request("POST", url, data=payload)


def get_usermoments(bot_id: str, to_id: str, num: int, pyq_id=None):
    """
    获取好友朋友圈
    :param bot_id:
    :param to_id:
    :param num:数量1-10条，少了报错，多了无效
    :param pyq_id:获取指定id的朋友圈，不填就是最新一条
    :return:
    """

    if num < 1:
        num = 1
    elif num > 10:
        num = 10

    payload = json.dumps({
        "token": token,
        "api": "GetMomentsForFriend",
        "to_wxid": to_id,
        "robot_wxid": bot_id,
        "pyq_id": pyq_id,
        "num": num

    })
    return requests.request("POST", url, data=payload)


def momentslike(bot_id: str, pyq_id: str):
    """
    给指定的朋友圈点赞
    :param bot_id:
    :param pyq_id: 朋友圈id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "MomentsLike",
        "robot_wxid": bot_id,
        "pyq_id": pyq_id,

    })
    return requests.request("POST", url, data=payload)


def moments_comment(bot_id: str, pyq_id: str, msg: str):
    """
    朋友圈评论
    :param bot_id:
    :param pyq_id:朋友圈id
    :param msg:评论内容
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "MomentsComment",
        "robot_wxid": bot_id,
        "pyq_id": pyq_id,
        "msg": msg

    })
    return requests.request("POST", url, data=payload)


def save_contact(bot_id: str, to_id: str):
    """
    将群保存到通讯录
    :param bot_id:
    :param to_id:群id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "ContactSave",
        "robot_wxid": bot_id,
        "group_wxid": to_id,

    })
    return requests.request("POST", url, data=payload)


def remove_contact(bot_id: str, to_id: str):
    """
    将群移出到通讯录
    :param bot_id:
    :param to_id:群id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "ContactRemove",
        "robot_wxid": bot_id,
        "group_wxid": to_id,
    })
    return requests.request("POST", url, data=payload)


def get_favoriteslist(bot_id: str):
    """
    获取收藏列表
    :param bot_id:
    :return:
    """

    payload = json.dumps({
        "token": token,
        "api": "FavoritesGetList",
        "robot_wxid": bot_id,
    })
    return requests.request("POST", url, data=payload)


def add_favoritesmsg(bot_id: str, to_id: str):
    """
    收藏消息
    :param bot_id:
    :param to_id:消息id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "FavoritesMsg",
        "robot_wxid": bot_id,
        "msgid": to_id,
    })
    return requests.request("POST", url, data=payload)


def send_favoritesmsg(bot_id: str, to_id: str, local_id: str):
    """
    发送收藏消息
    :param bot_id:
    :param to_id:目标id
    :param local_id:收藏的local_id
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SendFavoritesMsg",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "local_id": local_id,
    })
    return requests.request("POST", url, data=payload)


def on_antiwithdraw(bot_id: str):
    """
    开启防撤回
    注意【开启后，仅拦截pc端的撤回，其他端还是会撤回的】
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "AntiWithdrawON",
        "robot_wxid": bot_id,
    })
    return requests.request("POST", url, data=payload)


def off_antiwithdraw(bot_id: str):
    """
    关闭防撤回
    :param bot_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "AntiWithdrawOFF",
        "robot_wxid": bot_id,
    })
    return requests.request("POST", url, data=payload)


def withdraw_ownmessage(bot_id: str, to_id: str, msg_id: str):
    """
    撤回自身消息
    :param bot_id:
    :param to_id:对象WXID（好友ID/群ID/公众号ID）
    :param msg_id:消息ID
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "WithdrawOwnMessage",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
        "msgid": msg_id
    })
    return requests.request("POST", url, data=payload)


def get_sriendsstatus(bot_id: str, to_id: str):
    """
    获取好友状态
    【正常状态返回0 对方把我拉黑返回1 对方把我删除返回2 其它原因返回3 失败返回-1】
    :param bot_id:
    :param to_id:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "GetFriendsStatus",
        "robot_wxid": bot_id,
        "to_wxid": to_id,
    })
    return requests.request("POST", url, data=payload)


def get_friendlist(bot_id: str, refresh: int):
    """
    获取好友列表
    :param bot_id:
    :param refresh:1为重刷列表再获取，0为取缓存，默认为0
    :return:
    """
    if refresh == 1 or refresh == 0:
        payload = json.dumps({
            "token": token,
            "api": "GetFriendlist",
            "robot_wxid": bot_id,
            "is_refresh": refresh,
        })
        return requests.request("POST", url, data=payload)

def send_moments_text(bot_id: str, text: str):
    """
    发文本朋友圈
    :param bot_id:
    :param text:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SendMoments_Str",
        "robot_wxid": bot_id,
        "content": text,
    })
    return requests.request("POST", url, data=payload)

def send_moments_img(bot_id: str, text: str,img:str):
    """
    发图片朋友圈
    :param bot_id:
    :param text:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SendMoments_Img",
        "robot_wxid": bot_id,
        "content": text,
        "img":img
    })
    return requests.request("POST", url, data=payload)


def send_moments_vid(bot_id: str, text: str, vid:str):
    """
    发视频朋友圈
    【发圈视频 只支持网页视频地址】
    :param bot_id:
    :param text:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SendMoments_Video",
        "robot_wxid": bot_id,
        "content": text,
        "video":vid
    })
    return requests.request("POST", url, data=payload)
def change_groupname(bot_id: str, to_id: str, name:str):
    """
    修改我在群里的昵称
    :param bot_id:
    :param to_id:
    :param name:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SesNicknameInGroup",
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "name":name
    })
    return requests.request("POST", url, data=payload)
def Send_atallmsg(bot_id: str, to_id: str, msg:str):
    """
    @所有人 文本内容
    :param bot_id:
    :param to_id:
    :param msg:
    :return:
    """
    payload = json.dumps({
        "token": token,
        "api": "SendMsgAtAll",
        "robot_wxid": bot_id,
        "group_wxid": to_id,
        "msg":msg
    })
    return requests.request("POST", url, data=payload)



# *************************脚本内部*****************************

url = ''
token = ''
# 版本号
local_version = 1.5


def __import_config():
    r"""
    请勿主动调用
    配置文件处理函数
    """
    global url
    global token

    if os.path.exists('pyxyoconfig.json'):
        # 配置文件存在，读配置
        with open('pyxyoconfig.json', 'r', encoding='utf8') as f:
            data = json.loads(f.read())
            url = data.get('url')
            token = data.get('token')
        if url == '' or token == '':
            print('请在pyxyoconfig.json中完善url和token')
            return
    else:
        # 配置文件不存在，创建
        with open('pyxyoconfig.json', 'w', encoding='utf8') as f:
            dic = {
                "url": "",
                "token": "",
                "uptime": 0,
                "web_version": 0
            }
            json.dump(dic, f)
            print('请在pyxyoconfig.json中填写url和token值')
            return


__import_config()


def __up():
    """
    请勿主动调用
    检测模块是否有更新(每天请求一次web)
    :return:
    """
    # 取本地日期
    local_time = int(time.strftime('%Y%m%d', time.localtime(time.time())))

    # 取配置文件中的日期
    with open('pyxyoconfig.json', 'r', encoding='utf8') as f:
        json_data = json.loads(f.read())

    # 获取本地检查日期
    json_time = json_data.get('uptime')

    # 时间不对，取网页最新版本
    if local_time != json_time:

        # 获取网络版本文本
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'}
        r = requests.get(url='http://xiaoguais.gitee.io/web/Version_updates/pyxyohttpapi.json', headers=headers)

        # 获取网络版本号
        web_version = r.json().get('new').get('version')

        # 网络版本号大于本地版本号
        if web_version > local_version:
            txt = 'pyxyohttpapi模块有更新【检查单位时是日，所以您要是更新了模块还提示请忽略】'
            # 输出一次文本
            print(txt)

            # 输出一次日志
            output_log(log_type='2', msg=txt)

            # 更新一下网络版本号
            json_data['web_version'] = web_version

        # 更新一下检查日期
        json_data['uptime'] = local_time

        # 持久化存储
        with open('pyxyoconfig.json', 'w', encoding='utf8') as f:
            json.dump(json_data, f)
    else:
        # 获取存储的web版本
        json_version = json_data.get('web_version')

        if local_version != json_version:
            txt = 'pyxyohttpapi模块有更新【检查单位时是日，所以您要是更新了模块还提示请忽略】'
            # 输出一次文本
            print(txt)

            # 输出一次日志
            output_log(log_type='2', msg=txt)


__up()


def help():
    """
    帮助
    :return:
    """
    return '可以打开模块看看每个函数都有注解,或者看开发文档'
