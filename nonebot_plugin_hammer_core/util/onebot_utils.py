import traceback

from nonebot.adapters.onebot.v11 import Bot, ActionFailed


async def get_qq_nickname_with_group(
        bot: Bot,
        user_id: int,
        current_group_id: int,
        target_group_id: int = None,
        pattern: str = '{nickname}{qq_id}{target_group}',
        target_group_pattern: str = '(来自群“{target_group_name}”)'
) -> str:
    if target_group_id is None:
        target_group_id = current_group_id
    if target_group_id != current_group_id: # if not the same group
        info = await bot.get_stranger_info(user_id=user_id)
        return await __stranger_convert(bot, info['nickname'], user_id, target_group_id, pattern, target_group_pattern)

    try:
        info = await bot.get_group_member_info(group_id=current_group_id, user_id=user_id)
        # if the same group
        if len(info['card'].strip()) == 0:
            nickname = info['nickname']
        else:
            nickname = info['card']
        return pattern.replace('{target_group}','').replace('{nickname}', nickname).replace('{qq_id}', f'({user_id})')
    except ActionFailed as exc:
        if exc.info['retcode'] == 100:
            # if not the same group
            info = await bot.get_stranger_info(user_id=user_id)
            return await __stranger_convert(bot, info['nickname'], user_id, target_group_id, pattern, target_group_pattern)
        else:
            traceback.print_exc()


async def __stranger_convert(bot: Bot, nickname: str, user_id: int, target_group_id: int, pattern: str, target_group_pattern: str) -> str:
    group_info = await bot.get_group_info(group_id=target_group_id)
    return pattern.replace('{nickname}', nickname) \
        .replace('{qq_id}', '') \
        .replace('{target_group}', target_group_pattern.replace('{target_group_name}', group_info['group_name']))
