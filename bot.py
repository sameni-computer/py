from config import *
bot = telebot.TeleBot(TOKEN)


global tedad_salavat
tedad_salavat = 0

@bot.message_handler(commands=['start'])

def send(message):
    global tedad_salavat
    tedad_salavat = 0

    

    dokme_box= telebot.types.InlineKeyboardMarkup(row_width=1)
    dokme1 = telebot.types.InlineKeyboardButton(text="احراز هویت " , callback_data="password" )
    dokme_box.add(dokme1)

    global welcome
    welcome = bot.send_message(message.chat.id , reply_markup= dokme_box ,
text= f"""سلام و عرض ادب
                                    
به ربات صلوات *دارالقرآن مسجد جامع* خوش آمدید
                                    
احراز هویت : تایید نشده❌""")

@bot.message_handler(func= lambda m : True)
def welcome(message):
    if message.text == "edit":
        time.sleep(1)
        bot.delete_message(chat_id=message.chat.id , message_id=message.message_id)
        msg_text =message.reply_to_message.text
        bot.edit_message_text(chat_id=message.chat.id , message_id=message.reply_to_message.id , text=msg_text)
    if message.text == "delet":
        time.sleep(1)
        bot.delete_message(chat_id=message.chat.id , message_id=message.reply_to_message.id)
        bot.delete_message(chat_id=message.chat.id , message_id=message.message_id)



@bot.callback_query_handler(func=lambda call : True)

def check_pass(call):
    global tedad_salavat
    global channel_message

    if call.data == "D5":
        inDokme = 5
        jadid = inDokme + tedad_salavat
        tedad_salavat = jadid

        bot.edit_message_text(chat_id=call.message.chat.id , message_id=channel_message.message_id , reply_markup=salavat_box ,
                              text= f"{salavat_text} \n \n🌹مجموع صلوات ختم شده : {tedad_salavat}")
        
    if call.data == "D14":
        inDokme = 14
        jadid = inDokme + tedad_salavat
        tedad_salavat = jadid


        bot.edit_message_text(chat_id=call.message.chat.id , message_id=channel_message.message_id , reply_markup=salavat_box ,
                              text= f"{salavat_text}\n \n🌹مجموع صلوات ختم شده : {tedad_salavat}")

    if call.data == "D110":
        inDokme = 110
        jadid = inDokme + tedad_salavat
        tedad_salavat = jadid

        bot.edit_message_text(chat_id=call.message.chat.id , message_id=channel_message.message_id , reply_markup=salavat_box ,
                              text= f"{salavat_text} \n \n🌹مجموع صلوات ختم شده : {tedad_salavat}")

    if call.data == "D313":
        inDokme = 313
        jadid = inDokme + tedad_salavat
        tedad_salavat = jadid

        bot.edit_message_text(chat_id=call.message.chat.id , message_id=channel_message.message_id , reply_markup=salavat_box ,
                              text= f"{salavat_text} \n \n🌹مجموع صلوات ختم شده : {tedad_salavat}")
        
    if call.data == "password":
        if call.message.chat.id == 715921910:
            dokme_box= telebot.types.InlineKeyboardMarkup(row_width=1)
            dokme3 = telebot.types.InlineKeyboardButton(text="وارد کردن متن" , callback_data="enterText")
            dokme_box.add(dokme3)
            bot.edit_message_text(chat_id=welcome.chat.id ,
                              message_id= welcome.message_id, reply_markup=dokme_box ,
text= f"""سلام و عرض ادب
                                    
به ربات صلوات *دارالقرآن مسجد جامع* خوش آمدید
                                    
احراز هویت : تایید شده✅

""" )
        
        else:
            bot.send_message(call.message.chat.id , "شما دسترسی لازم برای استفاده از این ربات را ندارید") 




    if call.data == "preview":
        final_text = f"{salavat_text} \n🌹مجموع صلوات ختم شده : {tedad_salavat}"

        m1 = bot.send_message(chat_id= call.message.chat.id , text=final_text )
        m2 = bot.send_message(chat_id= call.message.chat.id , text="پیش نمایش تا 20 ثانیه دیگر حذف می شود")

        time.sleep(3)
        bot.delete_message(chat_id= m1.chat.id , message_id= m1.message_id)
        bot.delete_message(chat_id= m2.chat.id , message_id= m2.message_id)


    if call.data == "sendToChannel":
        final_text = f"{salavat_text} \n \n🌹مجموع صلوات ختم شده : {tedad_salavat}"

        channel_message = bot.send_message(chat_id= "@alborzqqq" , text=final_text , reply_markup=salavat_box)
        deletBTN= telebot.types.InlineKeyboardMarkup(row_width=1)
        delet = telebot.types.InlineKeyboardButton(text="❌ حذف پیام از کانال ❌" , callback_data="deletFromChannel")
        deletBTN.add(delet)

        bot.edit_message_text(chat_id=welcome.chat.id , message_id= welcome.message_id, reply_markup=deletBTN ,
text= f"""سلام و عرض ادب
                                    
به ربات صلوات *دارالقرآن مسجد جامع* خوش آمدید
                                    
* ✅پیام مورد نظر در کانال ارسال شد ✅*

""")
        
    if call.data == "deletFromChannel":
        Nooo= telebot.types.InlineKeyboardMarkup()
        Nooo.add()

        final_text =  f"{salavat_text} \n \n🌹مجموع صلوات ختم شده : {tedad_salavat}"
        bot.edit_message_text(chat_id= "@alborzqqq", message_id= channel_message.message_id ,
                              reply_markup = Nooo , text= final_text) 


        bot.edit_message_text(chat_id=welcome.chat.id , message_id=welcome.message_id , 
text= f"""
* ✅پیام مورد نظر از کانال حذف شد ✅*

جهت شروع مجدد از /start  استفاده کنید
""")



    if call.data == "enterText":
            global msg
            msg = bot.send_message(call.message.chat.id, "متن مورد نظر را وارد کنید: ")
            bot.register_next_step_handler(msg , name)

def name(message):
    if message:
        global salavat_text 
        salavat_text = message.text

        bot.delete_message(chat_id= message.chat.id , message_id=msg.message_id)
        bot.delete_message(chat_id= message.chat.id , message_id=message.message_id)

        ThreeBTN= telebot.types.InlineKeyboardMarkup(row_width=1)
        dokme6 = telebot.types.InlineKeyboardButton(text="ویرایش متن"       , callback_data="enterText")
        dokme7 = telebot.types.InlineKeyboardButton(text="پیش نمایش"        , callback_data="preview")
        dokme8 = telebot.types.InlineKeyboardButton(text="ارسال در کانال"   , callback_data="sendToChannel")
        ThreeBTN.add(dokme6 , dokme7 , dokme8)

        bot.edit_message_text(chat_id=welcome.chat.id , message_id= welcome.message_id, reply_markup=ThreeBTN ,
text= f"""سلام و عرض ادب
                                    
به ربات صلوات *دارالقرآن مسجد جامع* خوش آمدید
                                    
وضعیت متن : ذریافت شده✅

""" )

bot.infinity_polling()
print("Bot is running.......")