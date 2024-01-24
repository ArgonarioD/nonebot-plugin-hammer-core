from nonebot.adapters.onebot.v11 import Bot, ActionFailed


async def get_qq_nickname_with_group(
        bot: Bot,
        user_id: int,
        current_group_id: int,
        target_group_id: int = None,
        pattern: str = '{nickname}{qq_id}{target_group}',
        qq_id_pattern: str = '({id})',
        target_group_pattern: str = '@{target_group_name}'
) -> str:
    if target_group_id is None:
        target_group_id = current_group_id

    try:
        info = await bot.get_group_member_info(group_id=current_group_id, user_id=user_id)
        # if the same group
        if len(info['card'].strip()) == 0:
            nickname = info['nickname']
        else:
            nickname = info['card'].strip()
        return (pattern.replace('{target_group}', '')
                .replace('{nickname}', nickname)
                .replace('{qq_id}', qq_id_pattern.replace('{id}', str(user_id))))
    except ActionFailed:
        # if not the same group
        nickname = '未知用户'
        group_name = '未知群组'
        try:
            stranger_info = await bot.get_stranger_info(user_id=user_id)
            nickname = stranger_info['nickname']
        except ActionFailed:
            pass
        try:
            group_info = await bot.get_group_info(group_id=target_group_id)
            group_name = group_info['group_name']
        except ActionFailed:
            pass

        return pattern.replace('{nickname}', nickname) \
            .replace('{qq_id}', '') \
            .replace('{target_group}', target_group_pattern.replace('{target_group_name}', group_name))
