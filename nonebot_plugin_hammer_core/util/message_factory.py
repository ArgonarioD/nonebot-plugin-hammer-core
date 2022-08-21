from nonebot.adapters.onebot.v11 import MessageSegment, Message, MessageEvent


def reply_text(text: str, event: MessageEvent, message_id: int = None) -> Message:
    if message_id is not None:
        return Message([
            MessageSegment(type='reply', data={'id': message_id}),
            MessageSegment(type='text', data={'text': text})
        ])
    return Message([
        MessageSegment(type='reply', data={'id': event.message_id}),
        MessageSegment(type='text', data={'text': text})
    ])


def reply(data, event: MessageEvent) -> Message:
    datalist = [MessageSegment(type='reply', data={'id': event.message_id})]
    return Message(datalist + data)
