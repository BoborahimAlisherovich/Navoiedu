import requests
from core.settings import BOT_TOKEN,CHAT_ID

def send_message(murojat_kimga,murojat_turi,familiya,ismi,otasining_ismi,kompaniyaning_nomi,pochta_manzil,mirojat_matni,tel_raqam,create_date,id):
    text = f"{id}-sonli Yangi murojat kelib tushdi \n\n\nMurojat kimga :{murojat_kimga}\nMurojat turi: {murojat_turi}\nIsm: {ismi}\nEmail: {familiya}\nOtasining ismi: {otasining_ismi}\nKompaniyaning nomi: { kompaniyaning_nomi}\nEmail: {pochta_manzil}\nTelephone_number: {tel_raqam}\n\nmurojat matni: {mirojat_matni}\n\n\nyaratilgan sana: {create_date}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/SendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)