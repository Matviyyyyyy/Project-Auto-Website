from SQLAgent import*

sql_agent = SQLAgent("logo-cars-table.db")
sql_agent_brand = SQLAgent("brand_cars_table.db")
sql_agent_news = SQLAgent("news_table.db")


#sql_agent.add_logo("Maserati", "maserati.ua", "https://www.maserati.com/ua/uk", "maserati-logo.png")
#sql_agent_brand.add_brand_car("Mercedes-Benz", "EQA", 1786893, "mercedes-benz_eqa.png")
#sql_agent_news.add_new("УкрАВТО починає продаж автомобілів KG MOBILITY (SSANGYONG) в Україні", "17.10", "news-im-12.jpg")


#sql_agent_brand.add_brand_car("Geely", "COOLRAY", "846 400", "geely_coolray.png", "Geely COOLRAY – довгоочікувана новинка для широкого кола споживачів в Україні: як для поціновувачів вдалого поєднання автомобільної естетики і виняткового комфорту в автомобілі, так і для тих, хто перш за все цінує нові технології безпеки або потребує відмінних динамічних характеристик свого нового авто. У перекладі з англійської Cool - крутий, кльовий, а Ray - промінь. І ці слова повністю відповідають сутності нового COOLRAY — яскравий, крутий, динамічний кросовер, який вирізняється не лише своєю зовнішністю, а й преміальними технологіями, що дозволяють водієві насолоджуватися керуванням автомобіля так само вільно, як промінь світла переміщається у просторі. Geely COOLRAY - НЕСКІНЧЕННІСТЬ ЕМОЦІЙ!", "Xетчбек", 1499, "Бензиновий з турбонаддувом", "174 / 5500", "290 (2000 - 3500)", "Автоматична", "Передній", "Незалежна типу MacPherson", "Торсіона балка", 195, "7.6", "7.2", "5.5","6.1", 45, 1357, 1732, 4380, 1810, 1615, 2600, 170, 330, "geely_coolray_up.jpg", 2022, "im-gel-1-geely-colray.jfif", "im-gel-2-geely-colray.jfif", "im-gel-3-geely-colray.jfif", "geely_coolray_cool_8_1000-768x432-1.jpg")
sql_agent_brand.add_brand_car("KIA", "Sportage", "1 069 340 ", "kia-sportage.png","Новий Kia Sportage  –  міський кросовер та яскравий послідовник свого попередника-лідера вподобань українців, який об'єднує практичність традиційних SUV з сучасним екстер'єром, інтер’єром та керованістю. Покупцям буде запропоновано не тільки яскраву самобутню «зовнішність», але і просторий інтер'єр, неймовірну кількість сучасних комунікаційних технологій і систем безпеки. Новий Sportage має продуманий внутрішній простір, що поєднує практичність, функціональність і універсальність, підкріплюється компактною колісною базою 2680 мм, шириною 1865 мм, довжиною 4515 мм і висотою 1645 мм. В основі нового європейського Sportage лежать ефективність, потужність і продуктивність.", "Джип", 2359, "G4KD серії Theta II", "156 / 6200", "265 (1500-4500)", "Автомат", "Повний", "Незалежна, типу MacPherson", "Незалежна, багатоважільна (Мульти Лінк)", 181, "11,4", "10,9", "6,5", "8,1", 58, 1687, 2175, 4515, 1865, 1645, 2680, 170, 591, "kia_sportage_up.jpeg", 2021, "im-gel-1-kia-sportage.jpg", "im-gel-2-kia-sportage.jfif", "im-gel-3-kia-sportage.jpg", "im-gel-4-kia-sportage.webp")
