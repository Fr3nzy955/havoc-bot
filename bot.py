import discord
from discord.ext import commands
from discord import app_commands

# ⚠️ ВСТАВЬТЕ СЮДА ВАШ НОВЫЙ ТОКЕН (старый скомпрометирован!)
TOKEN = os.environ.get('TOKEN')

# Настройка интентов
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


# ===== ID КАНАЛОВ И РОЛЕЙ (ЗАМЕНИТЕ НА СВОИ!) =====
LOG_CHANNEL_ID = 1556989855505055774  # ID канала для логов модерации
WELCOME_CHANNEL_ID = 1557035682965225553  # ID канала #приветствие
TARGET_ROLE_ID = 1556675373842833529  # ID роли "Игрок проекта"

ALLOWED_CHANNELS = [
    1556989660981493932  # Каналы, где ссылки разрешены (белый список)
]


# ===== СОБЫТИЕ ЗАПУСКА БОТА =====
@bot.event
async def on_ready():
    """Бот запустился"""
    print(f'✅ Бот {bot.user} успешно подключился!')
    print(f'ID бота: {bot.user.id}')
    
    try:
        synced = await bot.tree.sync()
        print(f' Синхронизировано {len(synced)} команд')
    except Exception as e:
        print(f'❌ Ошибка синхронизации: {e}')


# ===== КОМАНДЫ БОТА =====

@bot.tree.command(name='правила', description='Отправить полные правила сервера HAVOC DM')
async def rules_command(interaction: discord.Interaction):
    embed1 = discord.Embed(
        title="📋 Правила использования Discord-сервера HAVOC DM",
        description=(
            "На соблюдение нижеописанных правил Вы даете согласие при подключении к Discord-серверу. "
            "**Незнание данных Правил не освобождает от ответственности.**\n\n"
            "📌 **Условия использования Discord**\n"
            "Соблюдайте все [условия использования Discord](https://discord.com/terms). "
            "Нарушение этих условий ведет за собой перманентную блокировку.\n\n"
            "📌 **Правила проекта**\n"
            "Несоблюдение правил проекта при общении также повлечет за собой наказание."
        ),
        color=0xFFA500,
        timestamp=interaction.created_at
    )
    
    embed1.add_field(name="⛔ ВО ВСЕХ КАНАЛАХ СЕРВЕРА ЗАПРЕЩАЕТСЯ:", value="\u200b", inline=False)
    
    rules_left = [
        "**1. Высказывания** (в том числе лозунги, приветствия и изречения), никнеймы, статусы, аватарки расистского, фашистского, националистского характера, а также другие формы унижения человеческого достоинства.",
        "**2. Оскорбление других Пользователей**, в том числе и без использования ненормативной лексики, а также провокации на оскорбление.",
        "**3. Flood, offtop, CAPS, Zalgo, троллинг**, препятствие общению, в том числе посредством \"реакций\" к сообщениям.",
        "**4. Угрозы расправы в реальной жизни**, а также угрозы причинения какого-либо ущерба.",
        "**5. Обсуждение, предложения, спрос о продаже услуг и любого игрового имущества за реальные (неигровые) ценности или услуги.**",
        "**6. Попытки выдачи себя за представителя администрации.**",
        "**7. Реклама любых промокодов во всех чатах.**"
    ]
    
    rules_right = [
        "**8. Деструктивные действия по отношению к проекту:** неконструктивная критика, призывы покинуть проект, распространение заведомо ложной информации.",
        "**9. Провокация или подталкивание к нарушению** действующих правил проекта, любого из игровых серверов, а также данных правил Discord-сервера.",
        "**10. Вымогательство или попрошайничество** во всех возможных проявлениях.",
        "**11. Обсуждение действий и дискредитация модераторов, хелперов и администраторов** в любом возможном виде.",
        "**12. Распространение рекламы**, ссылок и файлов никак не относящихся к проекту, а также распространение вредоносных программ.",
        "**13. Все перечисленные правила применимы и к голосовым каналам. Будьте особо внимательны!**",
        "**14. Реклама любых видео/стримов во всех чатах. Исключение: канал #медиа-стримы.**"
    ]
    
    for left, right in zip(rules_left, rules_right):
        embed1.add_field(name="\u200b", value=left, inline=True)
        embed1.add_field(name="\u200b", value=right, inline=True)
    
    embed1.add_field(name="🤖 Использование self-ботов", value="Использование self-ботов для автоматизации профиля/отправки сообщений **строго запрещено**.", inline=False)
    embed1.set_footer(text="HAVOC DM • Часть 1 из 2", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)
    
    embed2 = discord.Embed(
        title=" Правила HAVOC DM (продолжение)",
        description="Остальные случаи, наказания и прочие условия.",
        color=0xFF4500,
        timestamp=interaction.created_at
    )
    
    embed2.add_field(name="⚠️ ОСТАЛЬНЫЕ СЛУЧАИ:", value="В остальных случаях, не затронутых в вышеописанных Правилах, когда действие так или иначе наносит ущерб проекту, решение по наложению наказания определяется администрацией.\n\nБудьте внимательны, для некоторых каналов сервера могут быть установлены дополнительные правила поведения.", inline=False)
    
    embed2.add_field(name="🔨 ВЫДАВАЕМЫЕ НАКАЗАНИЯ:", value="1) временное ограничение на возможность оставлять сообщения (Mute);\n2) временный или постоянный бан аккаунта;\n3) разовое принудительное исключение с сервера;\n4) черный список проекта.", inline=False)
    
    embed2.add_field(name="📝 ПРОЧИЕ УСЛОВИЯ:", value="Администрация не несет ответственности за любые высказывания иного участника, опубликованные на официальном сервере Discord HAVOC DM.", inline=False)
    embed2.set_footer(text="HAVOC DM • Администрация проекта", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)
    
    await interaction.response.send_message(embed=embed1)
    await interaction.followup.send(embed=embed2)


@bot.tree.command(name='привет', description='Проверочная команда')
async def hello_command(interaction: discord.Interaction):
    embed = discord.Embed(title=" Привет!", description=f"Бот HAVOC DM работает! Привет, {interaction.user.mention}!", color=0x00FF00)
    embed.set_footer(text="HAVOC DM Bot")
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='помощь', description='Список всех команд бота')
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="📚 Список команд HAVOC Bot", description="Используйте слэш-команды для взаимодействия с ботом:", color=0xFFA500)
    embed.add_field(name="/правила", value="Отправить полные правила сервера (2 части)", inline=False)
    embed.add_field(name="/привет", value="Проверочная команда", inline=False)
    embed.add_field(name="/помощь", value="Показать этот список", inline=False)
    embed.set_footer(text="HAVOC DM • Все права защищены")
    await interaction.response.send_message(embed=embed)


# ===== АВТОМОДЕРАЦИЯ ССЫЛОК НА ДРУГИЕ DISCORD-СЕРВЕРЫ =====

@bot.event
async def on_message(message):
    # 1. Игнорируем самого себя
    if message.author == bot.user:
        return
    
    # 2. Игнорируем ВЛАДЕЛЬЦА СЕРВЕРА (он может кидать любые ссылки)
    if message.author == message.guild.owner:
        return
    
    # 3. Игнорируем каналы из белого списка
    if message.channel.id in ALLOWED_CHANNELS:
        return
    
    discord_invite_patterns = [
        'discord.gg/',
        'discord.com/invite/',
        'discordapp.com/invite/',
        'dis.gd/'
    ]
    
    message_content = message.content.lower()
    
    for pattern in discord_invite_patterns:
        if pattern in message_content:
            # Удаляем сообщение в любом случае
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            
            # Проверяем, является ли нарушитель ботом
            if message.author.bot:
                try:
                    await message.author.kick(reason='Публикация сторонних Discord-ссылок')
                    result_msg = "🤖 Бот был кикнут с сервера."
                except discord.Forbidden:
                    result_msg = "⚠️ Не удалось кикнуть бота (мой бот находится ниже его в иерархии ролей или нет прав)."
                except Exception as e:
                    result_msg = f"❌ Ошибка при кике бота: {e}"
            else:
                try:
                    await message.author.kick(reason=f'Реклама стороннего Discord-сервера: {message.content[:50]}')
                    result_msg = "👢 Пользователь был кикнут с сервера."
                except discord.Forbidden:
                    result_msg = "️ Не удалось кикнуть пользователя (недостаточно прав)."
                except Exception as e:
                    result_msg = f"❌ Ошибка при кике: {e}"
            
            # Отправляем лог в канал модерации
            log_channel = bot.get_channel(LOG_CHANNEL_ID)
            if log_channel:
                author_name = f"{message.author} [БОТ 🤖]" if message.author.bot else f"{message.author}"
                
                embed = discord.Embed(
                    title="🛡️ Автомодерация: Обнаружена реклама",
                    description=f"**{author_name}** (`{message.author.id}`) попытался опубликовать ссылку на другой Discord-сервер.\n\n**Результат:** {result_msg}",
                    color=0xFF0000,
                    timestamp=message.created_at
                )
                embed.add_field(name="Канал", value=message.channel.mention, inline=True)
                embed.add_field(name="Сообщение", value=f"```\n{message.content[:1000]}\n```", inline=False)
                embed.set_thumbnail(url=message.author.avatar.url if message.author.avatar else message.author.default_avatar.url)
                embed.set_footer(text=f"ID: {message.author.id}")
                
                await log_channel.send(embed=embed)
            
            break
    
    # ВАЖНО: Обязательно вызываем обработку других команд
    await bot.process_commands(message)


# ===== СИСТЕМА ПРИВЕТСТВИЯ И ОПРОСНИК ДЛЯ НОВИЧКОВ =====

@bot.event
async def on_member_join(member):
    print(f"🚨 Зашел пользователь: {member.name} ({member.id})")
    
    if member.bot:
        print(" Это бот, игнорируем его.")
        return
    
    # Проверяем права бота на создание каналов
    if not member.guild.me.guild_permissions.manage_channels:
        print("❌ У бота НЕТ права 'Управление каналами'! Проверьте роль бота.")
        return
    
    # Находим или создаём категорию для регистраций
    category_name = "🔒 РЕГИСТРАЦИЯ"
    category = discord.utils.get(member.guild.categories, name=category_name)
    
    if not category:
        try:
            # Создаём категорию с правами: никто не видит, кроме бота
            overwrites = {
                member.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member.guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True, send_messages=True)
            }
            category = await member.guild.create_category(name=category_name, overwrites=overwrites)
            print(f"✅ Создана категория: {category.name}")
        except Exception as e:
            print(f"❌ Ошибка создания категории: {e}")
            return
    
    # Создаём приватный канал для новичка
    channel_name = f"регистрация-{member.name.lower().replace(' ', '-')}"
    
    # Настройка прав канала
    overwrites = {
        # Все по умолчанию — не видят канал
        member.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        # Новичок — видит и пишет
        member: discord.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True),
        # Бот — видит, пишет и управляет каналом
        member.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True, manage_channels=True)
    }
    
    try:
        channel = await category.create_text_channel(
            name=channel_name,
            overwrites=overwrites
        )
        print(f"✅ Создан канал: {channel.name} (ID: {channel.id})")
    except Exception as e:
        print(f"❌ Ошибка создания канала: {e}")
        return
    
    # Небольшая задержка, чтобы Discord успел применить права
    import asyncio
    await asyncio.sleep(1)
    
    # Проверяем, что бот действительно видит канал
    channel_check = bot.get_channel(channel.id)
    if not channel_check:
        print(f"⚠️ Канал создан, но бот его не видит. Пробуем отправить напрямую...")
        channel_check = channel
    
    # Отправляем опросник
    view = WelcomeView(target_user_id=member.id, temp_channel_id=channel.id)
    
    embed = discord.Embed(
        title=f" Добро пожаловать на HAVOC DM, {member.name}!",
        description=(
            "Чтобы получить доступ ко всем каналам сервера, пожалуйста, пройди короткий опрос.\n"
            "Это займет всего 10 секунд!"
        ),
        color=0x00FF00,
        timestamp=discord.utils.utcnow()
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.set_footer(text="HAVOC DM • Администрация проекта")
    
    try:
        await channel_check.send(content=member.mention, embed=embed, view=view)
        print(f"✅ Сообщение отправлено в канал {channel.name}")
    except discord.Forbidden as e:
        print(f" НЕТ ПРАВ на отправку в канал {channel.name}: {e}")
        print(f"💡 Проверьте: роль бота должна быть ВЫШЕ роли новичка в настройках сервера!")
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}")


class WelcomeView(discord.ui.View):
    def __init__(self, target_user_id: int, temp_channel_id: int):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.temp_channel_id = temp_channel_id

    @discord.ui.button(label="📝 Пройти опрос и получить роль", style=discord.ButtonStyle.primary, emoji="📝")
    async def start_survey(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.target_user_id:
            await interaction.response.send_message(
                "⛔ Этот опросник не для тебя!",
                ephemeral=True
            )
            return
        
        modal = SurveyModal(temp_channel_id=self.temp_channel_id)
        await interaction.response.send_modal(modal)


class SurveyModal(discord.ui.Modal, title="Опрос новичка HAVOC DM"):
    def __init__(self, temp_channel_id: int):
        super().__init__()
        self.temp_channel_id = temp_channel_id
    
    nickname_input = discord.ui.TextInput(
        label="Ваш никнейм на сервере",
        placeholder="Например: Alex_Pro или Nik_Name",
        required=True,
        min_length=3,
        max_length=32
    )
    
    age_input = discord.ui.TextInput(
        label="Как узнали о нас",
        placeholder="",
        required=True,
        style=discord.TextStyle.short,
        min_length=1,
        max_length=50
    )

    async def on_submit(self, interaction: discord.Interaction):
        member = interaction.user
        guild = interaction.guild
        
        # Меняем никнейм
        try:
            await member.edit(nick=self.nickname_input.value)
            nick_status = "✅ Никнейм успешно изменен."
        except discord.Forbidden:
            nick_status = "⚠️ У бота нет прав на изменение никнейма."
        
        # Выдаем роль
        role = guild.get_role(TARGET_ROLE_ID)
        if role:
            try:
                await member.add_roles(role)
                role_status = f"✅ Роль **{role.name}** выдана!"
            except discord.Forbidden:
                role_status = "❌ У бота нет прав на выдачу роли."
        else:
            role_status = "❌ Роль не найдена."
        
        # Сообщение об успехе
        success_embed = discord.Embed(
            title="🎉 Регистрация завершена!",
            description=f"Спасибо, **{self.nickname_input.value}**!\n\n{nick_status}\n{role_status}\n\nЭтот канал будет удален через 5 секунд.",
            color=0x00FF00
        )
        await interaction.response.send_message(embed=success_embed)
        
        # Лог для администрации
        log_channel = bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            log_embed = discord.Embed(
                title="✅ Новый участник прошел опрос",
                description=f"**{member}** (`{member.id}`) зарегистрировался.\nНик: `{self.nickname_input.value}`\nКак узнали о нас: `{self.age_input.value}`",
                color=0x00FF00,
                timestamp=discord.utils.utcnow()
            )
            await log_channel.send(embed=log_embed)
        
        # Удаляем временный канал через 5 секунд
        import asyncio
        await asyncio.sleep(5)
        temp_channel = bot.get_channel(self.temp_channel_id)
        if temp_channel:
            try:
                await temp_channel.delete()
                print(f"️ Удален временный канал: {temp_channel.name}")
            except Exception as e:
                print(f"❌ Ошибка удаления канала: {e}")

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message(
            "❌ Ошибка при обработке данных.",
            ephemeral=True
        )


# ===== ЗАПУСК БОТА (ДОЛЖЕН БЫТЬ В САМОМ КОНЦЕ ФАЙЛА!) =====
bot.run(TOKEN)