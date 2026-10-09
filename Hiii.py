import discord
from discord.ext import commands

# ----------------------------------------------------
# [SHADOW CONFIGURATION] إعدادات الاتصال والصلاحيات
# ----------------------------------------------------
# ضع توكن البوت الصحيح هنا بين علامتي التنصيص
TOKEN = "تبي احط توكن بوتي وهاههاا"

# إعداد صلاحيات البوت (Intents) المتوافقة مع المنصة
intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # مفعل لقراءة معلومات السيرفرات والأعضاء بدقة

# تهيئة البوت
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("=" * 70)
    print(f" [Nobido SYSTEM] تم تشغيل الأداة بنجاح! متصل بـ: {bot.user}")
    print(f" [Nobdio] جاري استخراج السيرفرات التي يتواجد فيها البوت...")
    print("=" * 70)
    
    count = 0
    for guild in bot.guilds:
        count += 1
        print(f"[{count}] اسم السيرفر: {guild.name}")
        print(f"    - معرف السيرفر (ID): {guild.id}")
        print(f"    - عدد الأعضاء: {guild.member_count}")
        
        # محاولة جلب أو إنشاء رابط دعوة للسيرفر
        invite_link = "غير متاح (تحتاج صلاحية Create Instant Invite)"
        try:
            for channel in guild.text_channels:
                # التحقق مما إذا كان البوت يمتلك صلاحية إنشاء دعوة في هذه القناة
                if channel.permissions_for(guild.me).create_instant_invite:
                    invite = await channel.create_invite(max_age=0, max_uses=0, reason="Shadow Server Hunter")
                    invite_link = str(invite)
                    break
        except Exception as e:
            invite_link = f"خطأ في الصلاحيات: {str(e)}"
            
        print(f"    - رابط الدعوة: {invite_link}")
        print("-" * 60)
    
    print(f"[+] إجمالي السيرفرات المستخرجة: {count}")
    print("=" * 70)
    
    # إغلاق الاتصال بعد الانتهاء من الطباعة في الكونسول
    await bot.close()

# ----------------------------------------------------
# التشغيل الأساسي للنظام
# ----------------------------------------------------
if __name__ == "__main__":
    if TOKEN == "YOUR_BOT_TOKEN_HERE" or not TOKEN.strip():
        print("[-] خطأ فادح: يرجى وضع توكن البوت الحقيقي الخاص بك مكان 'YOUR_BOT_TOKEN_HERE'.")
    else:
        try:
            bot.run(TOKEN)
        except Exception as e:
            print(f"[-] حدث خطأ أثناء تشغيل البوت: {e}")
      
