# Telegram-Bot
Бот в Телеграме для транслитерации ФИО

# Инструкция

1. В Telegram необходимо найти @BotFather

2. Вводим команду `/newbot` и далее, следуя указаниям @BotFather, присваиваем своему будущему боту name и username

3. После этого @BotFather пришлет ссылку на созданного бота, а также Токен для доступа к HTTP API.

4. Открываем в текстовом редакторе папку myBot_GitHub и в файле *dockerfile* * указываем токен от @BotFather (ENV TOKEN='*здесь необходимо указать свой TOKEN*')

* *Dockerfile — это текстовый файл с инструкциями, необходимыми для создания образа контейнера. Эти инструкции включают идентификацию существующего образа, используемого в качестве основы, команды, выполняемые в процессе создания образа, и команду, которая будет выполняться при развертывании новых экземпляров этого образа контейнера*.


5. В файле *dockerfile* открываем терминал и прописываем команду для запуска процесса создания образа (image): 
`docker build .`
	
6. После того как образ успешно сгенерируется, мы сможем найти его ID в последней строке: 
>> Successfully built **85bc6bef4ece**
где комбинация цифр и букв и есть ID образа.

7. Для запуска вводим команду с указанием ID образа:
	 `docker run -d -p 80:80 **85bc6bef4ece**`
(вместо последнего аргуента в коде указывайте свод ID образа)

8. В Telegram переходим по ссылке от @BotFather (см. п.3) и можем начинать взаимодействовать с нашим ботом.
