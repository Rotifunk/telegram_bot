import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from apscheduler.schedulers.background import BackgroundScheduler
from RecognizeVoice import speech_to_text
from Crawling import get_weather, get_news



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# /start 커맨드 핸들러
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 해당 업데이트에 대한 user정보
    user = update.effective_user
    await update.message.reply_text(
        f"안녕하세요  {user.name}!\n글로벌 도시들의 날씨가 궁금하시다면\n'도시이름'날씨 알려줘 라고 말해보세요"
    )

# /help 커맨드 핸들러
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("마이크 버튼을 꾹 누르고\n'도시이름'날씨 알려줘 라고 말해보세요")

# 에코 핸들러
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('도움이 필요하시면 /help를 입력해주세요.')

# voice 핸들러
async def send_weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # voice파일 다운로드
    new_file = await update.message.effective_attachment.get_file()
    await new_file.download_to_drive('test_audio.ogg')
    # STT
    voice_message = speech_to_text('./test_audio.ogg', './test_audio.wav')
    weather = get_weather(voice_message)
    await update.message.reply_text(weather)

# 워드클라우드 전송
async def wordcloud(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo('./test.jpg')
    await update.message.reply_text('오늘의 IT뉴스 키워드입니다.')


def main() -> None:
    application = Application.builder().token("7163371922:AAFYwFkicVApPc9MnC9pErj3zdh_7VyVOmY").build()

    # 스케줄링
    sched = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
    sched.add_job(get_news, 'cron', hour='16',minute='23', id='get_news')
    sched.start()

    # 명령어 핸들러
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("wordcloud", wordcloud))
    # 메시지 핸들러
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # 음성 핸들러
    application.add_handler(MessageHandler(filters.VOICE, send_weather))
    # 폴링
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()