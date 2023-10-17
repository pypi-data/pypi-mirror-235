# Notify 
用于分发消息到IM软件上

# 配置说明
仅支持*.toml

```
# 飞书配置
[lark]
bot_url = "https://open.feishu.cn/open-apis/bot/v2/hook/20fc3aab-e539-427e-a708-314fcefd0fbf"

# 企业微信
[weixin]
bot_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx"

# 钉钉
[dingtalk]
bot_url = "https://oapi.dingtalk.com/robot/send?access_token=xxx"
secret = "yyy"

# telegram
[telegram]
token = "xxx:AAFgkJ--yyy"
chat_id = 1
```